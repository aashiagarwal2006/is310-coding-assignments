# Web Scraping Assignment: 2023 Movies

## Research Question

What information about movies can I collect from Wikipedia to create a dataset for future research?

I chose to scrape Wikipedia's List of American films of 2023 because I'm working on a larger research project about how movie popularity differs across platforms like Rotten Tomatoes, Letterboxd, and IMDb. I thought this assignment would be a good way to start collecting some basic movie information that I could use later.

## Data Collection

I used Python with the requests and BeautifulSoup libraries to scrape Wikipedia. My code first goes through the list of American films released in 2023 and collects links to individual movie pages. It then visits each movie's page and collects information from the infobox.

I collected data on 70 movies, including their titles, release years, directors, runtimes, budgets, box office earnings, production companies, distributors, countries, and languages. I saved everything in a CSV file called movies_wiki.csv.

Some information was missing for certain movies. For example, I was able to collect director information for all 70 movies, but budget information was only available for 22 and box office information for 37. I also tried collecting genre, but none of the movie infoboxes had that field.

## Scraping Permissions

Before scraping, I checked Wikipedia's robots.txt file and Wikimedia's User-Agent policy.

- Wikipedia robots.txt: https://en.wikipedia.org/robots.txt
- Wikimedia User-Agent policy: https://foundation.wikimedia.org/wiki/Policy:Wikimedia_Foundation_User-Agent_Policy

Wikipedia allows automated access to regular article pages but restricts certain other pages and requests. To follow these guidelines, my code identifies itself as a student project, uses `time.sleep(2)` between requests, and checks the status code before trying to collect information from a page.

## Limitations

One limitation is that Wikipedia doesn't have the same information for every movie. Some movies had missing budgets, box office numbers, or other details. This doesn't necessarily mean the information doesn't exist, just that my code couldn't find it in the infobox.

Another limitation is that I collected the first 70 movies my scraper could access, which ended up being movies released in the US between January and March 2023. Because of this, my dataset doesn't represent the entire year.

Also, even though I collected box office earnings, that doesn't necessarily tell me how popular or well-liked a movie was. A movie could make a lot of money without receiving good reviews, so I would need other information to study actual audience reception.

Overall, this assignment helped me learn how to collect information from multiple webpages and organize it into a dataset. I plan to use this data as a starting point for my larger project and add ratings from other platforms later.