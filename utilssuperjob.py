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
        return vacancies_by_keyword


class SuperJobVacancy:
    """Класс для работы с вакансиями"""

    def __init__(self, keyword: str, salary: int, experience: dict, type_of_work: dict):
        self.keyword = keyword
        self.salary = salary
        self.experience = experience
        self.type_of_work = type_of_work


class JSONSaver(Saver):
    """Класс для сохранения вакансий в файл в формате JSON,
    получения вакансий из файла, удаления информации о вакансиях"""

    def add_vacancy(self):
        pass

    def get_vacancy(self):
        pass

    def del_vacancy(self):
        pass
