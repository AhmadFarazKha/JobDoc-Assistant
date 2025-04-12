# app.py
import streamlit as st
import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
GOOGLE_CSE_ID = os.getenv("GOOGLE_CSE_ID")

def search_google_jobs(query, location=""):
    """Search for jobs using Google Custom Search API"""
    try:
        if not GOOGLE_API_KEY:
            st.error("Google API Key not found in .env file.")
            return None
        if not GOOGLE_CSE_ID:
            st.error("Google Custom Search Engine ID not found in .env file.")
            return None

        base_url = "https://www.googleapis.com/customsearch/v1"
        params = {
            "key": GOOGLE_API_KEY,
            "cx": GOOGLE_CSE_ID,
            "q": f"{query} jobs {location}",
            "num": 10,
            "safe": "active",
            "cr": "countryUS",  # You had US in the error URL
            "lr": "lang_en"
        }

        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise an exception for HTTP errors (4xx or 5xx)
        results = response.json()

        return results.get("items", [])

    except requests.exceptions.RequestException as e:
        st.error(f"API Request Error: {str(e)}")
        return None
    except ValueError:
        st.error("Error decoding JSON response from API.")
        return None
    except Exception as e:
        st.error(f"Search error: {str(e)}")
        return None

def create_mock_jobs():
    """Fallback mock job data"""
    return [{
        "title": "Senior Software Engineer (Sample)",
        "link": "https://example.com/jobs/123",
        "snippet": "Looking for experienced software engineers. This is a sample description.",
        "pagemap": {
            "metatags": [{
                "og:company_name": "Tech Corp Inc.",
                "og:location": "Remote"
            }]
        }
    },
    {
        "title": "Frontend Developer (Sample)",
        "link": "https://example.com/jobs/456",
        "snippet": "Seeking a talented frontend developer to join our team. Another example job.",
        "pagemap": {
            "metatags": [{
                "og:company_name": "Web Solutions Ltd.",
                "og:location": "London, UK"
            }]
        }
    }]

def main():
    st.set_page_config(
        page_title="Global Job Finder",
        page_icon="🔍",
        layout="wide"
    )

    st.title("Global Job Finder")
    st.markdown("Search job listings across the web using Google's search technology")

    # Search form
    with st.form("job_search"):
        col1, col2 = st.columns(2)
        with col1:
            job_query = st.text_input("Job Title/Role", placeholder="Software Engineer")
        with col2:
            location = st.text_input("Location", placeholder="Country/City/Remote")

        submitted = st.form_submit_button("Search Jobs")

    if submitted and job_query:
        with st.spinner("Searching across job boards and company websites..."):
            # Try Google Search API
            results = search_google_jobs(job_query, location)

            # Fallback to mock data if API fails or no results
            if not results:
                st.warning("Showing sample results - API connection issue detected or no real results found.")
                results = create_mock_jobs()

            if results:
                st.success(f"Found {len(results)} job listings")

                for item in results:
                    company = item.get("pagemap", {}).get("metatags", [{}])[0].get("og:company_name", "Unknown Company")
                    job_location = item.get("pagemap", {}).get("metatags", [{}])[0].get("og:location", "Location not specified")
                    link = item.get("link", "Link not available")
                    description = item.get("snippet", "No description available")
                    title = item.get("title", "No Title")

                    with st.expander(f"{title} - {company}"):
                        st.markdown(f"**📍 Location:** {job_location}")
                        st.markdown(f"**🔗 Source:** {link}")
                        st.markdown("**📝 Description:**")
                        st.write(description)

                        if link:
                            st.markdown(f"[View Full Posting]({link})")
            else:
                st.warning("No jobs found. Try different search terms.")

if __name__ == "__main__":
    main()