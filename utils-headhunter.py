from abstractclasses import API, Saver
import requests


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
        return vacancies_by_keyword


class HeadHunterVacancy:
    """Класс для работы с вакансиями"""

    def __init__(self, keyword: str, salary: int, experience: str, employment: dict):
        self.keyword = keyword
        self.salary = salary
        self.experience = experience
        self.employment = employment

    def get_filtered(self):
        vacancies_by_keyword = HeadHunterAPI(self.keyword)
        vacancies_filtered = []
        for vacancy in vacancies_by_keyword['objects']:



class JSONSaver(Saver):
    """Класс для сохранения вакансий в файл в формате JSON,
    получения вакансий из файла, удаления информации о вакансиях"""

    def add_vacancy(self):
        pass

    def get_vacancy(self):
        pass

    def del_vacancy(self):
        pass
