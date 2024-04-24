from abc import ABC, abstractmethod
from typing import List

from src.vacancy.vacancy import Vacancy


class BaseFileHandler(ABC):
    """Базовый класс для обработки файлов."""

    @abstractmethod
    def get_vacancies(self, parameter: str) -> List[Vacancy]:
        """Получает вакансии из файла по заданному параметру."""

    @abstractmethod
    def add_vacancy(self, vacancy: Vacancy) -> None:
        """Бобавляет вакансию в файл."""
        
        
    @abstractmethod
    def delete_vacancy(self, vacancy: Vacancy) -> None:
        """Удаляет вакансию из файла."""
