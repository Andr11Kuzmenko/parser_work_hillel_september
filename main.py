import argparse

from bs4 import BeautifulSoup

import settings

from work_parser.request import RequestEngine
from work_parser.parser import ParserEngine
from work_parser.dto import Vacancy


def main(json_mode: bool, db_mode: bool):
    page = settings.START_PAGE
    result = []

    while True:
        request_engine = RequestEngine()
        response = request_engine.get_response(settings.HOST + settings.ROOT_PATH, {
            'ss': settings.SS,
            'page': page
        })

        parser_engine = ParserEngine(BeautifulSoup(response.text, 'html.parser'))
        cards = parser_engine.find_cards('card card-hover card-search card-visited wordwrap job-link js-job-link-blank js-hot-block')

        if not cards:
            break

        for card in cards:
            name, href, vacancy_id = parser_engine.find_name_and_href(card)
            result.append(Vacancy(vacancy_id, name, href))

        page += 1


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-json', action='store_true', default=False)
    parser.add_argument('-db', action='store_true', default=False)
    parser.add_argument('-dir', type=str)

    args = parser.parse_args()
    main(args.json, args.db)
