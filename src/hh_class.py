import requests

from data.const import COUNT_VACANCIES, HH_VACANCIES_URL

from .api_base_classes import BaseAPI


class HeadHunterAPI(BaseAPI):
    """Поиск вакансий на HH.ru."""

    def __init__(self, search_phrase: str) -> None:
        self.__url = HH_VACANCIES_URL
        self.params = {
            "text": search_phrase,
            "per_page": COUNT_VACANCIES,
            "page": 0,
            "archived": False,
        }
        
    def get_vacancies(self):
        """Ищет вакансии согласно запроса."""
        self.vacancies = requests.get(url=self.__url, params=self.params)
        return self.vacancies.json()
