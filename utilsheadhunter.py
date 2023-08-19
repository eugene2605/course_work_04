from abstractclasses import API, Saver
import requests
import json


class HeadHunterAPI(API):
    """Класс для получения списка словарей вакансий с платформы hh.ru по ключевому слову"""

    def __init__(self, keyword: str) -> None:
        self.keyword = keyword

    def get_vacancies(self):
        url_hh = 'https://api.hh.ru/vacancies'
        params = {
            'text': self.keyword,
            'per_page': 100,
            'archived': False,
            'only_with_salary': True
        }
        vacancies_by_keyword = requests.get(url_hh, params=params)
        return vacancies_by_keyword.json()


class HeadHunterVacancy:
    """Класс для работы с вакансиями"""

    def __init__(self, keyword: str, salary: int, experience: str, employment: dict):
        self.keyword = keyword
        self.salary = salary
        self.experience = experience
        self.employment = employment

    def get_filtered(self):
        vacancies_by_api = HeadHunterAPI(self.keyword)
        vacancies_by_keyword = vacancies_by_api.get_vacancies()
        vacancies_filtered = []
        for vacancy in vacancies_by_keyword['items']:
            if type(vacancy['salary']['from']) != int:
                continue
            if vacancy['salary']['from'] >= self.salary and vacancy['experience']['id'] == self.experience and vacancy['employment']['id'] in self.employment:
                vacancies_filtered.append(vacancy)
        return vacancies_filtered

    def __len__(self):
        return len(self.get_filtered())


class HeadHunterJSONSaver(Saver):
    """Класс для сохранения вакансий в файл в формате JSON,
    получения вакансий из файла, удаления информации о вакансиях"""

    def __init__(self, vacancies_filtered: dict):
        self.vacancies_filtered = vacancies_filtered

    def add_vacancy(self):
        with open('vacancies_hh', 'w', encoding='utf-8') as file:
            json.dump(self.vacancies_filtered, file, indent=4, ensure_ascii=False)

    def get_vacancy(self):
        with open('vacancies_hh', 'r', encoding='utf-8') as file:
            vacancies = json.load(file)
        i = 1
        for vacancy in vacancies:
            print('*' * 14, i, '*' * 14)
            print(f'Название вакансии: {vacancy["name"]}')
            print(f'Место работы: {vacancy["area"]["name"]}')
            print(f'Зарплата: {vacancy["salary"]["from"]} - {vacancy["salary"]["to"]} {vacancy["salary"]["currency"]}')
            print(f'Работодатель: {vacancy["employer"]["name"]}')
            print(f'Требования: {vacancy["snippet"]["requirement"]}')
            print(f'Обязанности: {vacancy["snippet"]["responsibility"]}')
            print(f'Ссылка на вакансию: {vacancy["alternate_url"]}')
            i += 1

    def del_vacancy(self):
        with open('vacancies_hh', 'w', encoding='utf-8') as file:
            pass
