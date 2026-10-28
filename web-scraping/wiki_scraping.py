
import requests
import time
import csv
from bs4 import BeautifulSoup
from urllib.parse import urljoin

URL = "https://en.wikipedia.org/wiki/List_of_American_films_of_2023"

HEADERS = {
    "User-Agent": "IS310-MovieScraper/1.0 (student project; aashia3@illinois.edu)"
}

MOVIE_LIMIT = 70
OUTPUT_FILE = "movies_wiki.csv"


# Download a webpage
def get_page(url):
    try:
        response = requests.get(url, headers=HEADERS, timeout=30)
    except requests.RequestException as error:
        print("Request failed:", error)
        return None

    time.sleep(2)

    if response.status_code != 200:
        print("HTTP error:", response.status_code, url)

        if response.status_code in [403, 429]:
            print("Wikipedia refused or limited access. Stopping.")
            raise SystemExit

        return None

    soup = BeautifulSoup(response.text, "html.parser")
    return soup


# Get movie titles and links from the 2023 list
def get_movies(soup):
    movies = []
    seen_links = []

    tables = soup.find_all("table", class_="wikitable")

    for table in tables:
        headings = table.find_all("th")
        heading_text = ""

        for heading in headings:
            heading_text += heading.get_text(" ", strip=True) + " "

        if "Title" in heading_text and "Cast and crew" in heading_text:
            rows = table.find_all("tr")

            for row in rows:
                cells = row.find_all("td", recursive=False)

                if len(cells) >= 4:
                    title_cell = cells[-4]
                    link = title_cell.find("a", href=True)

                    if link is not None:
                        title = link.get_text(" ", strip=True)
                        movie_url = urljoin(URL, link.get("href"))

                        if "/wiki/" in movie_url and movie_url not in seen_links:
                            movies.append({
                                "title": title,
                                "wikipedia_url": movie_url
                            })

                            seen_links.append(movie_url)

    return movies


# Find information from a movie's infobox
def get_info(infobox, field_name):
    rows = infobox.find_all("tr")

    for row in rows:
        heading = row.find("th")
        value = row.find("td")

        if heading is not None and value is not None:
            heading_text = heading.get_text(" ", strip=True)

            if heading_text.lower() == field_name.lower():
                # Remove Wikipedia citation markers
                for reference in value.find_all("sup", class_="reference"):
                    reference.decompose()

                return value.get_text(" ", strip=True)

    return ""


# Visit one movie page and collect its information
def scrape_movie(movie):
    soup = get_page(movie["wikipedia_url"])

    if soup is None:
        return None

    infobox = soup.find("table", class_="infobox")

    if infobox is None:
        print("No infobox found:", movie["title"])
        return None

    record = {
        "title": movie["title"],
        "us_release_year": 2023,
        "release_dates": get_info(infobox, "Release dates"),
        "director": get_info(infobox, "Directed by"),
        "genre": get_info(infobox, "Genre"),
        "runtime": get_info(infobox, "Running time"),
        "budget": get_info(infobox, "Budget"),
        "box_office": get_info(infobox, "Box office"),
        "production_companies": get_info(infobox, "Production companies"),
        "distributor": get_info(infobox, "Distributed by"),
        "country": get_info(infobox, "Country"),
        "language": get_info(infobox, "Language"),
        "wikipedia_url": movie["wikipedia_url"],
        "source_list": URL
    }

    return record


# Save movies to a CSV
def save_csv(movies):
    if len(movies) == 0:
        print("No movies to save.")
        return

    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=movies[0].keys())
        writer.writeheader()
        writer.writerows(movies)


# Run the complete scraper
def main():
    print("Downloading Wikipedia movie list...")

    soup = get_page(URL)

    if soup is None:
        print("Could not download the movie list.")
        return

    movies = get_movies(soup)

    print("Found", len(movies), "movie links.")

    results = []

    for movie in movies:
        if len(results) >= MOVIE_LIMIT:
            break

        print("Processing:", movie["title"])

        record = scrape_movie(movie)

        if record is not None:
            results.append(record)
            print("Saved movie", len(results), "of", MOVIE_LIMIT)

    save_csv(results)

    print("\nFinished!")
    print("Total movies collected:", len(results))
    print("File:", OUTPUT_FILE)


if __name__ == "__main__":
    main()
