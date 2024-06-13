from typing import List, Dict, Any
from datetime import datetime

import requests
from bs4 import BeautifulSoup

class TheGuardian:
    def __init__(self) -> None:
        self._site_url = None

    @property
    def site_url(self) -> str:
        return self._site_url

    @site_url.setter
    def site_url(self, url: str) -> None:
        self._site_url = url

    def get_response(self) -> requests.Response:
        response = requests.get(url=self._site_url)
        if response.status_code != 200:
            raise Exception(f"HTTP request failed with status code {response.status_code}")
        return response

    def get_soup(self) -> BeautifulSoup:
        return BeautifulSoup(self.get_response().content, "html.parser")

    def get_structured_page_content(self) -> List[Dict[str, Any]]:
        soup = self.get_soup()
        sections = soup.find_all('section')

        page_data = []

        for section in sections:
            title = section.get("id")

            if title:
                list_items = section.find_all('li')

                for li in list_items:
                    h3 = li.find('h3')
                    article = li.find('a')
                    footer = li.find('footer')
                    time_tag = footer.find('time') if footer else None

                    if h3:
                        span = h3.find('span', class_='show-underline dcr-1ay6c8s')
                        div = h3.find('div')

                        content = span.get_text(strip=True).replace('\xa0', ' ') if span else None
                        subtitle = div.get_text(strip=True).replace('\xa0', ' ') if div else None
                        article_url = "https://www.theguardian.com" + article.get("href") if article else None
                        author_name, author_profile_link= self._get_author_data(url=article_url)

                        page = {
                            "article_date": datetime.strptime(time_tag.get("datetime"), "%Y-%m-%dT%H:%M:%S.%fZ").strftime("%Y-%m-%d") if time_tag else None,
                            "title": title,
                            "subtitle": subtitle,
                            "content": content,
                            "article": article_url,
                            "author": author_name,
                            "author_profile_link": author_profile_link
                        }

                        page_data.append(page)

                        print(page)

        return page_data

    def _get_author_data(self, url: str) -> str:

        self._site_url = url

        soup = self.get_soup()
        author_div = soup.find('div', class_='dcr-1cfpnlw')

        # Extract the author name from the <a> tag with rel="author"
        author_tag = author_div.find('a', rel='author') if author_div else None
        author_name = author_tag.text if author_tag else None

        # Extract the author's profile link
        author_profile_link = author_tag['href'] if author_tag else None

        return author_name, author_profile_link

