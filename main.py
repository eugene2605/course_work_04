from utilsheadhunter import HeadHunterVacancy, HeadHunterJSONSaver

platform = input('Выберите платформу для поиска работы\n'
                 '(0 - hh.ru, 1 - superjob.ru): ')
keyword = input('Введите ключевое слово для поиска вакансии: ')
salary = int(input('Введите желаемую зарплату: '))
experience = input('Выберите ваш опыт работы\n'
                   '(0 - без опыта, 1 - от 1 года до 3 лет, 2 - от 3 до 6 лет, 3 - более 6 лет): ')
if experience == '0':
    id_exp_hh, id_exp_sj = 'noExperience', [0, 1]
elif experience == '1':
    id_exp_hh, id_exp_sj = 'between1And3', [0, 2]
elif experience == '2':
    id_exp_hh, id_exp_sj = 'between3And6', [0, 3]
else:
    id_exp_hh, id_exp_sj = 'moreThan6', [0, 4]
employment = input('Выберите желаемую занятость\n'
                   '(0 - полная, 1 - частичная): ')
if employment == '0':
    id_emp_hh, id_emp_sj = ['full'], [0, 6]
else:
    id_emp_hh, id_emp_sj = ['part', 'project'], [0, 10, 12, 14]


vacancy = HeadHunterVacancy(keyword, salary, id_exp_hh, id_emp_hh)
vacancies_filtered = vacancy.get_filtered()
print('='*30)
print('По вашему запросу найдено вакансий:', len(vacancy))
# print(vacancies_filtered)
vacancies_save = HeadHunterJSONSaver(vacancies_filtered)
vacancies_save.add_vacancy()
vacancies_save.get_vacancy()
# vacancies_save.del_vacancy()
