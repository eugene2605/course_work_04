from abc import ABC, abstractmethod


class API(ABC):
    """Абстрактный класс для работы с API"""

    @abstractmethod
    def get_vacancies(self):
        pass


class Saver(ABC):
    """Абстрактный класс для сохранения вакансий в файл,
    получения вакансий из файла, удаления информации о вакансиях"""

    @abstractmethod
    def add_vacancy(self):
        pass

    @abstractmethod
    def get_vacancy(self):
        pass

    @abstractmethod
    def del_vacancy(self):
        pass
