from divar import get_soup, extract_job_listings
import sys
import requests






if __name__ == "__main__":
    url = "https://divar.ir/s/saveh/jobs?map_interaction=search_this_area_disabled"  # Replace with the desired URL
    try:
        soup = get_soup(url)
    except requests.RequestException as e:
        print(f"Failed to fetch the URL: {e}")
        sys.exit(1)

    
    job_listings = extract_job_listings(soup, limit=10)
    
    if job_listings:
        for job in job_listings:
            print(f"Title: {job['title']}, Link: {job['link']}")
    
