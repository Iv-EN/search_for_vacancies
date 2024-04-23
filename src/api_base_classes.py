from abc import ABC, abstractmethod


class BaseAPI(ABC):
    """Базовый класс для работы с API."""

    @abstractmethod
    def get_vacancies(self):
        """Получить вакансии."""
