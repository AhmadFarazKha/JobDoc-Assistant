# JobDoc Assistant

A Python application that helps users find job opportunities directly without visiting multiple job platforms. Simply enter a job title and location to get comprehensive job listings with detailed information.

## Features

- Search for jobs by title/keywords and location
- View detailed job information including descriptions, salary, and company details
- Export job listings to PDF, DOCX, or CSV formats
- Clean, user-friendly interface built with Streamlit

## Installation

1. Clone this repository
2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```
4. Create a `.env` file with your API keys:
   ```
   GOOGLE_API_KEY=your_google_api_key_here
   SERPAPI_KEY=your_serpapi_key_here
   ```

## API Keys

This application uses the following APIs:

- SerpAPI for Google Jobs data (alternative to Google Jobs API which requires approval)
- Google API (optional for additional features)

You can get a SerpAPI key by signing up at [serpapi.com](https://serpapi.com/).

## Usage

To run the application:

```
streamlit run app.py
```

Then open your web browser and go to http://localhost:8501

## Project Structure

```
JobDoc-Assistant/
├── .env                # Environment variables (API keys)
├── .gitattributes      # Git attributes file
├── .gitignore          # Git ignore file
├── README.md           # Project documentation
├── app.py              # Main Streamlit application
├── requirements.txt    # Required Python packages
└── venv/               # Virtual environment (not committed)
```

## Dependencies

Main dependencies include:

- streamlit
- PyPDF2
- Pillow
- python-dotenv
- PyMuPDF (fitz)
- pdf2image
- reportlab
- python-docx
