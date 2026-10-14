from rich.console import Console
from rich.table import Table
import json
from pathlib import Path

console = Console()
movies = [
    {
        "title": "Spider-Man",
        "year": "2002",
        "series": "Raimi Trilogy",
        "format": "Live Action"
    },
    {
        "title": "The Amazing Spider-Man",
        "year": "2012",
        "series": "Amazing Spider-Man",
        "format": "Live Action"
    },
    {
        "title": "Spider-Man: Into the Spider-Verse",
        "year": "2018",
        "series": "Spider-Verse",
        "format": "Animated"
    }
]

table = Table(title="Spider-Man Movie Archive")

table.add_column("Title", style="cyan")
table.add_column("Year", style="green")
table.add_column("Series", style="magenta")
table.add_column("Format", style="yellow")

for movie in movies:
    table.add_row(
        movie["title"],
        movie["year"],
        movie["series"],
        movie["format"]
    )

console.print(table)

console.print("\n[bold cyan]Add your own Spider-Man movies![/bold cyan]")

while True:
    while True:
        title = input("Movie title: ").strip()
        year = input("Release year: ").strip()
        series = input("Series (Raimi Trilogy, Amazing Spider-Man, MCU, Spider-Verse): ").strip()
        movie_format = input("Format (Live Action or Animated): ").strip()

        if not title or not year or not series or not movie_format:
            console.print("[red]All fields are required. Please try again.[/red]")
            continue

        console.print("\n[bold yellow]Review your entry:[/bold yellow]")
        console.print(f"Title: {title}")
        console.print(f"Year: {year}")
        console.print(f"Series: {series}")
        console.print(f"Format: {movie_format}")

        confirm = input("\nIs this information correct? (yes/no): ").strip().lower()

        if confirm == "yes":
            movies.append({
                "title": title,
                "year": year,
                "series": series,
                "format": movie_format
            })
            console.print("[green]Movie added successfully![/green]")
            break
        else:
            console.print("[yellow]Let's re-enter the movie information.[/yellow]")

    another = input("\nWould you like to add another movie? (yes/no): ").strip().lower()

    if another != "yes":
        break

file_path = Path(__file__).parent / "spiderman_movies.json"

with open(file_path, "w", encoding="utf-8") as file:
    json.dump(movies, file, indent=4)

console.print("\n[bold green]Data saved successfully![/bold green]")
console.print(f"File location: {file_path.resolve()}")