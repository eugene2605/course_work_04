import json

from abstractclasses import API, Saver
import requests


class SuperJobAPI(API):
    """Класс для получения списка словарей вакансий с платформы superjob.ru по ключевому слову"""

    def __init__(self, keyword: str) -> None:
        self.keyword = keyword

    def get_vacancies(self):
        url_sj = '	https://api.superjob.ru/2.0/vacancies'
        superjob_key = 'v3.h.4513713.b998364c6fe2887ae8d78519ca069bf15fb406f8.3a79294d4879328100bc32263d0c3ef57d91a4c7'
        headers = {"X-Api-App-Id": superjob_key}
        params = {
            'keyword': self.keyword,
            'count': 100,
            'not_archive': True,
            'no_agreement': 1
        }
        vacancies_by_keyword = requests.get(url_sj, headers=headers, params=params)
        return vacancies_by_keyword.json()


class SuperJobVacancy:
    """Класс для работы с вакансиями"""

    def __init__(self, keyword: str, salary: int, experience: dict, type_of_work: dict):
        self.keyword = keyword
        self.salary = salary
        self.experience = experience
        self.type_of_work = type_of_work

    def get_filtered(self):
        vacancies_by_api = SuperJobAPI(self.keyword)
        vacancies_by_keyword = vacancies_by_api.get_vacancies()
        vacancies_filtered = []
        for vacancy in vacancies_by_keyword['objects']:
            if type(vacancy['payment_from']) != int:
                continue
            if vacancy['payment_from'] >= self.salary and vacancy['experience']['id'] in self.experience and vacancy['type_of_work']['id'] in self.type_of_work:
                vacancies_filtered.append(vacancy)
        return vacancies_filtered

    def __len__(self):
        return len(self.get_filtered())


class SuperJobJSONSaver(Saver):
    """Класс для сохранения вакансий в файл в формате JSON,
    получения вакансий из файла, удаления информации о вакансиях"""

    def __init__(self, vacancies_filtered: dict):
        self.vacancies_filtered = vacancies_filtered

    def add_vacancy(self):
        with open('vacancies_sj', 'w', encoding='utf-8') as file:
            json.dump(self.vacancies_filtered, file, indent=4, ensure_ascii=False)

    def get_vacancy(self):
        with open('vacancies_sj', 'r', encoding='utf-8') as file:
            vacancies = json.load(file)
        i = 1
        for vacancy in vacancies:
            print('*' * 14, i, '*' * 14)
            print(f'Название вакансии: {vacancy["profession"]}')
            print(f'Место работы: {vacancy["town"]["title"]}')
            print(f'Зарплата: {vacancy["payment_from"]} - {vacancy["payment_to"]} {vacancy["currency"]}')
            print(f'Работодатель: {vacancy["client"]["title"]}')
            print(f'Требования и обязанности: {vacancy["candidat"]}')
            # print(f'Обязанности: {vacancy["snippet"]["responsibility"]}')
            print(f'Ссылка на вакансию: {vacancy["link"]}')
            i += 1

    def del_vacancy(self):
        with open('vacancies_sj', 'w', encoding='utf-8') as file:
            pass
