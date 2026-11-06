
import requests
import json

HEADERS = {
    "User-Agent": "is310-course/1.0 (aashia3@illinois.edu)"
}

API_URL = "https://en.wikipedia.org/w/api.php"

params = {
    "action": "query",
    "prop": "extracts",
    "titles": "Taylor Swift",
    "exintro": 1,
    "explaintext": 1,
    "format": "json",
}

try:
    response = requests.get(API_URL, params=params, headers=HEADERS, timeout=15)
    print(response.status_code)

    if response.status_code == 200:
        data = response.json()
        print(data)

        for page in data["query"]["pages"].values():
            if "missing" not in page:
                with open("wikipedia_artist.json", "w") as file:
                    json.dump(page, file, indent=4)
            else:
                print("Wikipedia page not found.")

except Exception as e:
    print("Wikipedia error:", e)

API_URL = "https://musicbrainz.org/ws/2/artist/"

params = {
    "query": "Taylor Swift",
    "fmt": "json",
    "limit": 5,
}

try:
    response = requests.get(API_URL, params=params, headers=HEADERS, timeout=15)
    print(response.status_code)

    if response.status_code == 200:
        data = response.json()
        print(data)

        for artist in data["artists"]:
            if artist["name"] == "Taylor Swift":
                with open("musicbrainz_artist.json", "w") as file:
                    json.dump(artist, file, indent=4)
                break

except Exception as e:
    print("MusicBrainz error:", e)