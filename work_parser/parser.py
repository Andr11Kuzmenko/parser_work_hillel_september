from bs4 import BeautifulSoup, Tag


class ParserEngine:

    def __init__(self, soup: BeautifulSoup):
        self.soup = soup

    def find_name_and_href(self, card: Tag) -> tuple[str, str, int]:
        tag_a = card.find('h2').find('a')
        href = tag_a['href']
        name = tag_a.text
        vacancy_id = href.split('/')[-2]
        return name, href, int(vacancy_id)

    def find_cards(self, class_: str) -> list[Tag]:
        cards = self.soup.find_all('div', class_=class_)
        extended_class = class_ + ' mt-lg'
        first_card = self.soup.find_all('div', class_=extended_class)
        return first_card + cards