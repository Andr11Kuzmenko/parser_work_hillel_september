class Vacancy:
    vacancy_id: int
    title: str
    href: str

    def __init__(self, vacancy_id: int, title: str, href: str):
        self.vacancy_id = vacancy_id
        self.title = title
        self.href = href

    def to_list(self):
        return [self.vacancy_id, self.title, self.href]

    def to_dict(self):
        return {
            'vacancy_id': self.vacancy_id,
            'title': self.title,
            'href': self.href
        }