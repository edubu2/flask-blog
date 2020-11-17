# Elliot's Website

Big thank you to **Corey Schafer** for his YouTube Flask Tutorial ([link](https://www.youtube.com/watch?v=MwZwr5Tvyxo&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH&ab_channel=CoreySchafer)), which helped me get started with this web app.

My website now contains a [text summarizer](https://www.ewilens.com/summarize-text) that uses NLP (Natural Language Processing) to rank sentences from a piece of long text. The top 3 sentences are returned. Users can use this application to quickly understand long articles or emails without having to read the whole thing! For more information about how this works, checkout my [NLP-Summarize repository](https://github.com/edubu2/NLP-Summarize).

## Steps to Run Locally
- Fork this repository to your computer
- Install necessary Python libraries with `pip3 install -r requirements.txt` in your virtual environment
- create /etc/config.json file to store sensitive information (required for database URI)
  - see config.py for keys to set up
  - email configuration only required for resetting forgotten passwords
  - on Windows machines, place this file anywhere (outside the repository) and change the filename in config.py to the new location
- Execute run.py script from terminal
- Open the app in your browser using the IP address in terminal's stdout

## Tech Stack
- Flask for application framework/jinja2 templating
- Bootstrap for front-end HTML, CSS & JS
- SQLAlchemy ORM for SQLite database
- BCrypt Password Hashing
- Web serving with Nginx and Gunicorn on a Linode VM running Ubuntu 18.04
