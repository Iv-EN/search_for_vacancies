[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

<div align="center">
    <h1>Search for vacancies</h1> 
    <p>
    Это консольное приложение которое умеет получать информацию о вакансиях с платформы hh.ru и сохранять её в файл.
    </p>
</div>

## Описание
При первом запуске программы в папке `data\` создаётся файл `vacancies.json` в который записывается информация о найденых согласно введённого пользователем поискового запроса. Далее выводится информация о количестве сохранённых вакансий (по умолчанию максимум 100, можно изменить в файле `api\const.py` `COUNT_VACANCIES`) и меню пользователя.

## Меню пользователя

### 1: перезезаписать файл с вакансиями
перезапишет файл `vacancies.json` согласно новому поисковому запросу

### Блок вывода вакансий на экран
### 2: все
выведет на экран все вакансии из файла без сортировки. Если в объявлении зарплата указана не врублях, то при выводе на экран она будет сконвектирована в рубли по текущему курсу. При этом будет указано из какой валюты, например `EUR -> RUR`
### 3: с наиболее высокой зарплатой
спросит количество вакансий для вывода и отобразит на экране вакансии с наиболее высокими зарплатами в порядке уменьшения
### 4: выбрать по ключеву слову
выведет на экран вакансии в наименовании которых содержится введёная пользователем ключевая фраза
### 5: удалить вакансию (вакансии)
удаляет из файла вакансии в имени которых содержится введённая пользователем фраза
### 0 - выход из программы
окончание работы программы
___

<div align="center">
    <h3 align="center">
        <p>Использовались языки и инструменты:</p>
        <div>
            <img src="https://github.com/devicons/devicon/blob/master/icons/python/python-original-wordmark.svg" title="Python" alt="Python" width="40" height="40"/>&nbsp;
        </div>
    </h3>
</div>

___

## Локальная установка приложения
1. Склонируйте репозиторий:
```bash
git clone https://github.com/Iv-EN/search_for_vacancies.git
```
2.  Создайте и активируйте виртуальное пространство:
```bash
python3 -m venv venv
```
```bash
sourse venv/bin/activate
```
3. Обновите pip и установите зависимости:
```bash
python3 -m pip install --upgrade pip
```
```bash
pip install -r requirements.txt
```
4. Запустите приложение из корневой папки
```bash
python3 main.py
```
___

<h3 align="center">
    <p><img src="https://media.giphy.com/media/iY8CRBdQXODJSCERIr/giphy.gif" width="30" height="30" style="margin-right: 10px;">Автор: Евгений Иванов. </p>
</h3>
<p align="center">

 <div align="center"  class="icons-social" style="margin-left: 10px;">
        <a href="https://vk.com/engenivanov" target="blank" rel="noopener noreferrer">
      <img src="https://img.shields.io/badge/%D0%92%20%D0%BA%D0%BE%D0%BD%D1%82%D0%B0%D0%BA%D1%82%D0%B5-blue?style=for-the-badge&logo=VK&logoColor=white" alt="В контакте Badge"/>
    </a>
    <a href="https://t.me/IvENauto" target="blank" rel="noopener noreferrer">
    <img src="https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white"/>
    </a>
  </div>
</p>