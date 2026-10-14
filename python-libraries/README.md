## Spider-Man Movie Archive

### Project Overview

For this assignment I wanted to create a Spider-Man movie archive where users can add info on different Spider-Man movies. I record the movie title, release year, series, and live action or animated.

I built two versions - a Python command line interface and an HTML basic webpage. Both will start with 3 movies as a base and allow users to add more and save data as a JSON.

### Files

1. cli_data_entry.py — Python CLI application using the Rich library.

2. index.html — HTML webpage with CSS and JavaScript.

3. spiderman_movies.json — Sample dataset generated using the Python CLI.

4. requirements.txt — Python dependencies.

5. ai-chat-log.md — Documentation of AI assistance.

### How to Run the Python CLI

1. Open the project repository in VS Code.

2. Open terminal in root directory.

3. Create and activate virtual environment:

On macOS:

python3 -m venv .venv
source .venv/bin/activate

4. Install the required packages:

python -m pip install -r requirements.txt

5. Run the application:

python python-libraries/cli_data_entry.py

6. Enter movie information when prompted. Review and confirm each entry. When finished, the data will be saved to python-libraries/spiderman_movies.json.

### How to Run the HTML Application

1. Open the python-libraries folder.

2. Double-click index.html to open it in a browser.

3. Fill in the movie title, release year, series, and format.

4. Click Add Movie and confirm the information.

5. Add movie records.

6. Click Download JSON to download the dataset.

### CLI vs. HTML Comparison

What does each interface make easier or harder?

The CLI is easy to understand because it is one field at a time but entering info takes longer to type. HTML version is easier to use because all the fields are visible at once and the dropdown menus make it easier to fill out.

Did the interfaces lead to different choices about fields, instructions, or validation?

Both interfaces collect the exact same fields. In the CLI version I used text prompts and made sure none of the fields were empty. In HTML I used dropdown menus for the series and format fields and required inputs so there were no incomplete entries.

What did AI contribute, and what did you change or troubleshoot?

I used ChatGPT to help understand every requirement and instruction and give me direction on how to approach the problem. I also used it for help with writing the CLI and HTML applications. I used it for styling as well. I also used it to summarize my prompts and the responses for the AI chat log.

Which interface better fits the cultural material and intended user, and why?

I personally like the HTML version more for this project because it was easier for someone adding movie information as they can see all the fields at once and select values from dropdowns. It is also a very simple application so a simple webpage would be a lot easier than making users run Python in terminal.

AI Usage

I completed the AI-assisted pathway for this assignment. Relevant prompts and responses are documented in ai-chat-log.md.