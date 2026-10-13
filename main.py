from divar import get_soup, extract_job_listings







if __name__ == "__main__":
    url = "https://divar.ir/s/saveh/jobs?map_interaction=search_this_area_disabled"  # Replace with the desired URL
    soup = get_soup(url)
    job_listings = extract_job_listings(soup, limit=10)
    
    for job in job_listings:
        print(f"Title: {job['title']}, Link: {job['link']}")