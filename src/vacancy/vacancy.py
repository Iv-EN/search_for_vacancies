from functools import total_ordering
from typing import Union


@total_ordering
class Vacancy:
    """Представляет информацию о вакансии."""

    def __init__(self, title: str, link: str, salary: str, date: str) -> None:
        """Инициализация Vacancy.

        title: название вакансии
        link: ссылка на вакансию
        salary: уровень зарплаты
        date: дата публикации вакансии
        """
        self.title = title
        self.link = link
        self.salary = salary
        self.date = date

    def __str__(self) -> str:
        return f"""
            Вакансия: {self.title}\nСсылка: {self.link}\n
            Зарплата: {self.salary}\nДата публикации: {self.date}
        """

    def __repr__(self) -> str:
        return f"""
            Vacancy(title={self.title}, link={self.link},
            salary={self.salary}, date={self.date})
        """

    def __eq__(self, other: "Vacancy") -> bool:
        """Проверка равны ли вакансии по уровню зарплаты."""
        return self.salary == other.salary

    def __lt__(self, other: "Vacancy") -> bool:
        """Определяет сортировку вакансий по уровню зарплаты."""
        return self.salary < other.salary

    @property
    def salary(self) -> int:
        """Возвращает зарплату вакансии."""
        return self.__salary

    @salary.setter
    def salary(self, value: Union[int, float, str]) -> None:
        """Устанавливает зарплату вакансии."""
        self.__salary = int(float(value))

    def validate_salary(self) -> bool:
        """Валидация зарплаты."""
        if isinstance(self.salary, (int, float)):
            return True
        if isinstance(self.salary, str):
            salary_parts = self.salary.split("-")
            if len(salary_parts) == 2:
                from_salary, before_salary = salary_parts
                if from_salary.isdigit() and before_salary.isdigit():
                    return True
        return False

    def validate_all_data(self) -> bool:
        """Проверка валидности всех данных вакансии."""
        if not all([self.title, self.link, self.salary, self.date]):
            return False
        return True
