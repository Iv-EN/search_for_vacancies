from src.utils.currency_utilities import get_currency_rates


class Vacancy:
    """Представляет информацию о вакансии."""

    def __init__(
        self, name: str, salary: dict | None, url: str, employer: str
    ) -> None:
        """Инициализация Vacancy.

        name: название вакансии
        url: ссылка на вакансию
        salary: уровень зарплаты
        emploer: работодатель
        """
        self.name = name
        self.url = url
        self.__validate_salary(salary)
        self.currency = self.__get_currency(salary)
        self.employer = employer

    def __str__(self) -> str:
        return f"""
            Вакансия: {self.name}
            Ссылка: {self.url}
            Зарплата: от {self.salary_from} до {self.salary_to} {self.currency} -> RUR
            Работодатель: {self.employer}
        """

    def __repr__(self) -> str:
        return (
            f"Vacancy(title={self.name}, url={self.url}, "
            f"salary={self.salary}), date={self.date}"
        )

    def __eq__(self, other: "Vacancy") -> bool:
        """Проверка равенства вакансий по зарплате."""
        return self.salary == other.salary

    def __lt__(self, other):
        """Определяет сортировку вакансий по уровню зарплаты."""
        return (self.salary_from, self.salary_to) < (
            other.salary_from,
            other.salary_to,
        )

    def __validate_salary(self, salary) -> None:
        """Приводит зарплату к рублю."""
        if salary is None:
            self.salary_from = 0
            self.salary_to = 0
        else:
            currency = self.__get_currency(salary)
            if currency not in ["RUB", "RUR"]:
                currency_rates = get_currency_rates(currency)
                self.salary_from = (
                    int(salary["from"] * currency_rates)
                    if salary["from"]
                    else 0
                )
                self.salary_to = (
                    int(salary["to"] * currency_rates) if salary["to"] else 0
                )
            else:
                self.salary_from = salary["from"] if salary["from"] else 0
                self.salary_to = salary["to"] if salary["to"] else 0

    def __get_currency(self, salary) -> str:
        """Получает обозначение валюты вакансии."""
        if salary is not None:
            return salary["currency"]
        return "Валюта не указана"
