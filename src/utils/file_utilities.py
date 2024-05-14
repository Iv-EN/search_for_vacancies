import json
import os

from src.api.const import PATH_FILE_VACANIES
from src.api.hh_class import HeadHunterAPI
from src.vacancy.vacancy import Vacancy


def checks_file_existence(filename) -> bool:
    """Проверяет наличие файла с вакансиями."""
    return os.path.isfile(filename)


def add_vacancies_to_file(vacancies: list[Vacancy]) -> None:
    """Сохраняет вакансии в файл."""
    with open(PATH_FILE_VACANIES, "w", encoding="utf-8") as file:
        json.dump(vacancies, file, ensure_ascii=False, indent=4)


def create_a_file_with_vacancies(search_phrase: str) -> None:
    """Создаёт файл с данными о вакансиях."""
    hh = HeadHunterAPI()
    vacancies = hh.get_filter_vacancies(search_phrase)
    add_vacancies_to_file(vacancies)
    print(f"Информация о {len(vacancies)} вакансиях сохранена в файл.")


def write_file() -> None:
    """Перезаписывает файл с информацией о вакансиях."""
    search_phrase = input("Bведите фразу для поиска:\n")
    create_a_file_with_vacancies(search_phrase)


def get_info_from_file() -> list:
    """Получает JSON из файла."""
    with open(PATH_FILE_VACANIES, "r", encoding="UTF-8") as file:
        return json.load(file)


def get_vacancies_from_file() -> None:
    """Получает список вакансий из файла"""
    data = get_info_from_file()
    vacancies = []
    for vacancy in data:
        vacancies.append(Vacancy(**vacancy))
    return vacancies


def find_by_keyword(keyword: str) -> list[Vacancy]:
    """Поиск вакансий по ключевому слову."""
    find_vacancies = []
    vacancies = get_vacancies_from_file()
    for vacancy in vacancies:
        if keyword in vacancy.name:
            find_vacancies.append(vacancy)
    return find_vacancies


def print_vacancy(vacancies: list[Vacancy]) -> None:
    """Выводит вакансии из списка на экран."""
    for vacancy in vacancies:
        print(vacancy)
    input("Нажмите 'Enter' для продолжения")


def delete_vacancies() -> None:
    """Удаляет вакансии из файла."""
    keyword = input("Введите ключевое слово: ")
    vacancies = get_info_from_file()
    vacancies_to_save = [
        vacancy
        for vacancy in vacancies
        if keyword.lower() not in vacancy["name"].lower()
    ]
    add_vacancies_to_file(vacancies_to_save)
    print(
        f"Информация о {len(vacancies) - len(vacancies_to_save)} "
        f"вакансиях удалена из файла."
    )
