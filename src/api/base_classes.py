from abc import ABC, abstractmethod
from typing import Any, Dict, List

from src.vacancy.vacancy import Vacancy

# from src.vacancy.vacancy import Vacancy


class GetVacancies(ABC):
    """Базовый класс для получения вакансий от API."""

    @abstractmethod
    def get_response(self, search_phrase: str, per_page: int):
        """Получить данные от API."""

    @abstractmethod
    def get_vacancies(self, search_phrase: str, per_page: int):
        """Получить вакансии."""

    @abstractmethod
    def get_filter_vacancies(self, search_phrase: str, per_page: int):
        """Фильтрация ключей для всех вакансий."""


class BaseFileHandler(ABC):
    """Базовый класс для обработки файлов."""

    @abstractmethod
    def get_vacancies_from_file(self, options: Dict[str, Any]) -> List:
        """Получает вакансии из файла по заданным параметрам."""

    @abstractmethod
    def add_vacancies_to_file(self, vacancy: Vacancy) -> None:
        """Записывает вакансии в файл."""

    @abstractmethod
    def delete_vacancy_from_file(self, vacancy: Vacancy) -> None:
        """Удаляет вакансию из файла."""
