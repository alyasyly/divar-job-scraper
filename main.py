from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin
import requests_cache
import functools
import time

requests_cache.install_cache('divar_cache', expire_after=1800)  # Cache expires after 30 minutes

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "fa-IR,fa;q=0.9,en;q=0.8",
}


def retry_on_failure(max_retries=3,delay=5):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kwargs):
            for attempt in range(1, max_retries + 1):
                try:
                    return func(*args,**kwargs)
                except requests.RequestException as e:
                    print(f"Attempt {attempt} of {max_retries} failed. Error: {e}")
                    if attempt == max_retries:
                        print("All retry attempts failed.")
                        raise e
                    print(f"Retrying in {delay} seconds...\n")
                    time.sleep(delay)
        return wrapper
    return decorator


@retry_on_failure(max_retries=3, delay=3)
def get_soup(url):
    response = requests.get(url, headers=HEADERS, timeout=10)
    response.raise_for_status()
    return BeautifulSoup(response.content, "html.parser")



def extract_job_listings(soup,limit=10):
    cards = soup.select('.kt-post-card__action')[:limit]
    # job_listings = job_listings[:10:1]
    # print(job_listings)
    # print(len(job_listings))
    jobs = []
    for card in cards:
        href = card.get("href")
        link = urljoin("https://divar.ir", href) if href else "no link"
        title_tag = card.select_one(".kt-post-card__title")
        title = title_tag.get_text(strip=True) if title_tag else "No Title"
        
        jobs.append({'title': title, 'link': link})

        

    print(jobs)

if __name__ == "__main__":
    url = "https://divar.ir/s/saveh/jobs?map_interaction=search_this_area_disabled"  # Replace with the desired URL
    soup = get_soup(url)
    if soup:
        extract_job_listings(soup)
    