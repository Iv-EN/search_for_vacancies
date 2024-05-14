import os

from src.api.const import PATH_FILE_VACANIES
from src.utils.file_utilities import (
    checks_file_existence,
    delete_vacancies,
    find_by_keyword,
    get_vacancies_from_file,
    print_vacancy,
    write_file,
)
from src.utils.user_utilities import menu


def main():
    """Основная функция программы."""
    os.system("cls" if os.name == "nt" else "clear")
    print("Добро пожаловать!")
    if not checks_file_existence(PATH_FILE_VACANIES):
        print("Похоже праграмма запущена в первый раз")
        write_file()
    vacancies = get_vacancies_from_file()
    while True:
        choise = menu()
        if choise is not None:
            if choise == 0:
                print("Всего хорошего!")
                break
            if choise == 1:
                write_file()
            elif choise == 2:
                print_vacancy(vacancies)
            elif choise == 3:
                number_vacancies = int(
                    input("введите количество вакансий для вывода: ")
                )
                sorted_vacancies = sorted(vacancies, reverse=True)
                vacancies_for_withdrawal = sorted_vacancies[:number_vacancies]
                print_vacancy(vacancies_for_withdrawal)
            elif choise == 4:
                keyword = input("Введите ключевое слово: ")
                vacancies = find_by_keyword(keyword)
                print_vacancy(vacancies)
            elif choise == 5:
                print(
                    """
                    Внимание!
                    Это действие безвозвратно удаляет информацию из файла!
                    """
                )
                confirmation = input("Продолжить? (д/н): ")
                if confirmation.lower() == "д":
                    delete_vacancies()
        else:
            print(
                "Неверный ввод. Попробуйте ввести 1, 3, 4, 5 или 0 для выхода"
            )


if __name__ == "__main__":
    main()
