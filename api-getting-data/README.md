## Getting culture across APIs

### Overview

I used the Wikipedia MediaWiki API and also the MusicBrainz API to try to collect information on Taylor Swift. I went with this because I love listening to music!

### API Comparison

The APIs were both free, they didn't have any account or API key needed, and it accepted requests with a descriptive user agent. MusicBrainz limits requests to one per second, and Wikimedia also limits having too many requests. Both returned the JSON output I was hoping for, but Wikimedia had a very detailed biography but MusicBrainz provided much more structured information - birth date, country, aliases, genres, etc. I matched Taylor Swift's name across both the datasets to match them, but I do think this might be harder for less distinctive names. Wikipedia is run by a non profit funded by donations - the Wikimedia Foundation, and MusicBrainz is run by their MusicBrainz Foundation through donations and commercial support, Research could get harder if either of them restricted access. Both need community contributions so also popular artists may be better represented rather than some of the underrepresented artists. This reflects Acker and Kreisberg's and Freelon's arguments about the researchers that depend on APIs that aren't really designed for research.

### Data Files

- wikipedia_artist.json - Wikipedia biography
- musicbrainz_artist.json - MusicBrainz artist metadata

### API Documentation

- https://www.mediawiki.org/wiki/API:Main_page
- https://musicbrainz.org/doc/MusicBrainz_API