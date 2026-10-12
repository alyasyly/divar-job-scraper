from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "fa-IR,fa;q=0.9,en;q=0.8",
}

def get_soup(url):
    try:
        response = requests.get(url, headers=headers, timeout=15)
        response.raise_for_status()  # Raise an exception for HTTP errors
    except requests.RequestException as e:
        print(f"faild: {e}")
        return None
    else: 
        return BeautifulSoup(response.text, "html.parser")



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
    