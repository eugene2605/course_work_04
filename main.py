from utilsheadhunter import HeadHunterVacancy, HeadHunterJSONSaver
from utilssuperjob import SuperJobVacancy


def sort_vacancies(vac_filtered):
    """Сортирует отфильтрованные вакансии в порядке возрастания"""
    vac_sorted = sorted(vac_filtered, key=lambda x: x['salary']['from'])
    return vac_sorted


def sort_vacancies_revers(vac_filtered):
    """Сортирует отфильтрованные вакансии в порядке убывания"""
    vac_sorted = sorted(vac_filtered, key=lambda x: x['salary']['from'], reverse=True)
    return vac_sorted


def user_interaction():
    """Функция для взаимодействия с пользователем"""
    while True:
        platform = input('Выберите платформу для поиска работы\n'
                         '(0 - hh.ru; 1 - superjob.ru): ')
        if platform == '0' or platform == '1':
            break
        else:
            print('Ошибка ввода!')
    keyword = input('Введите ключевое слово для поиска вакансии: ')
    salary = int(input('Введите желаемую зарплату: '))
    while True:
        experience = input('Выберите ваш опыт работы\n'
                           '(0 - без опыта; 1 - от 1 года до 3 лет; 2 - от 3 до 6 лет; 3 - более 6 лет): ')
        if experience == '0':
            id_exp_hh, id_exp_sj = 'noExperience', [0, 1]
            break
        elif experience == '1':
            id_exp_hh, id_exp_sj = 'between1And3', [0, 2]
            break
        elif experience == '2':
            id_exp_hh, id_exp_sj = 'between3And6', [0, 3]
            break
        elif experience == '3':
            id_exp_hh, id_exp_sj = 'moreThan6', [0, 4]
            break
        else:
            print('Ошибка ввода!')
    while True:
        employment = input('Выберите желаемую занятость\n'
                           '(0 - полная; 1 - частичная): ')
        if employment == '0':
            id_emp_hh, id_emp_sj = ['full'], [0, 6]
            break
        elif employment == '1':
            id_emp_hh, id_emp_sj = ['part', 'project'], [0, 10, 12, 14]
            break
        else:
            print('Ошибка ввода!')

    if platform == '0':
        vacancy = HeadHunterVacancy(keyword, salary, id_exp_hh, id_emp_hh)
        vacancies_filtered = vacancy.get_filtered()
        print('='*30)
        if len(vacancy) == 0:
        print('По вашему запросу найдено вакансий:', len(vacancy))
        sort_flag = input('Отсортировать найденные вакансии\n'
                          '(0 - нет; 1 - да, в порядке убывания; 2 - да, в порядке возрастания): ')
        if sort_flag == '0':
            vacancies_save = HeadHunterJSONSaver(vacancies_filtered)
        elif sort_flag == '1':
            vacancies_sorted = sort_vacancies_revers(vacancies_filtered)
            vacancies_save = HeadHunterJSONSaver(vacancies_sorted)
        else:
            vacancies_sorted = sort_vacancies(vacancies_filtered)
            vacancies_save = HeadHunterJSONSaver(vacancies_sorted)
        vacancies_save.add_vacancy()
        vacancies_save.get_vacancy()
        while True:
            flag_del_vacancy = input('Удалить найденные вакансии?\n'
                                     '(0 - нет; 1 - да): ')
            if flag_del_vacancy == '0':
                break
            elif flag_del_vacancy == '1':
                vacancies_save.del_vacancy()
                break
            else:
                print('Ошибка ввода!')
    elif platform == '1':
        vacancy = SuperJobVacancy(keyword, salary, id_exp_sj, id_emp_sj)
        vacancies_filtered = vacancy.get_filtered()
        print('=' * 30)
        if len(vacancy) == 0:
            print('По вашему запросу найдено вакансий:', len(vacancy))
        sort_flag = input('Отсортировать найденные вакансии\n'
                          '(0 - нет; 1 - да, в порядке убывания; 2 - да, в порядке возрастания): ')
        if sort_flag == '0':
            vacancies_save = SuperJobJSONSaver(vacancies_filtered)
        elif sort_flag == '1':
            vacancies_sorted = sort_vacancies_revers(vacancies_filtered)
            vacancies_save = SuperJobJSONSaver(vacancies_sorted)
        else:
            vacancies_sorted = sort_vacancies(vacancies_filtered)
            vacancies_save = SuperJobJSONSaver(vacancies_sorted)
        vacancies_save.add_vacancy()
        vacancies_save.get_vacancy()
        while True:
            flag_del_vacancy = input('Удалить найденные вакансии?\n'
                                     '(0 - нет; 1 - да): ')
            if flag_del_vacancy == '0':
                break
            elif flag_del_vacancy == '1':
                vacancies_save.del_vacancy()
                break
            else:
                print('Ошибка ввода!')


if __name__ == "__main__":
    user_interaction()
