
# Astronomy Picture of the Day Generator using Flask and NASA's Open API

This project is a Flask-based web application that fetches Astronomy Pictures of the Day (APOD) using NASA's Open API. Users can explore and view stunning astronomical images along with accompanying descriptions.

## Prerequisites

Before running this application, ensure you have the following:

- Python 3.x
- Flask (`pip install Flask`)
- An API key from [NASA's API Portal](https://api.nasa.gov/)

## Setup

1. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

2. Set your NASA API key:

    - Open `app.py` in a text editor.
    - Replace `'YOUR_API_KEY'` with your actual NASA API key.

## Usage

1. Run the Flask app:

    ```bash
    python app.py
    ```

2. Open a web browser and go to `http://127.0.0.1:5000`.

3. Explore the daily Astronomy Picture of the Day fetched from NASA's API.
   
## Additional Notes

- Each day, a new Astronomy Picture of the Day is displayed.
- Users can view the image along with the description provided by NASA.
- Customize the app's UI, add features like search functionality, save favorites, or share images on social media.
- Ensure a stable internet connection to fetch the latest Astronomy Picture of the Day.

