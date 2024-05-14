import requests

from .base_classes import GetVacancies
from .const import COUNT_VACANCIES, HH_VACANCIES_URL


class HeadHunterAPI(GetVacancies):
    """Поиск вакансий на HH.ru."""

    def __init__(self) -> None:
        self.__url = HH_VACANCIES_URL

    def get_response(self, search_phrase: str, per_page: int) -> dict:
        """Получает информацию от HH.ru"""
        params = {"text": search_phrase, "per_page": per_page}
        try:
            response = requests.get(self.__url, params=params)
        except Exception:
            print("Проверьте соединение с интернетом")
        return response

    def get_vacancies(self, search_phrase: str, per_page: int) -> list:
        """Получает информацию о вакансиях в формате JSON."""
        vacancies = self.get_response(search_phrase, per_page).json()["items"]
        return vacancies

    def get_filter_vacancies(
        self, search_phrase: str, per_page: int = COUNT_VACANCIES
    ) -> list:
        """Фильтрует информацию о вакансиях по заданным ключам."""
        filter_vacancies = []
        vacancies = self.get_vacancies(search_phrase, per_page)
        for vacancy in vacancies:
            filter_vacancies.append(
                {
                    "name": vacancy["name"],
                    "salary": vacancy["salary"],
                    "url": vacancy["alternate_url"],
                    "employer": vacancy["employer"]["name"],
                }
            )
        return filter_vacancies
