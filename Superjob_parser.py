import urllib
import requests
import json
from settings import AUTHORIZATION_PARAMETERS
from settings import API_APP_ID
from settings import ACCESS_TOKEN






DATA_FOR_SEARCHING_VACANCIES = {
  'keywords[0][keys]': user_input_job, 
  'keywords[0][srws]': '2',
   'town': user_input_city
   }


def authorize(url):
    authorization = requests.get(url, params = AUTHORIZATION_PARAMETERS)
    return authorization.json()  


def fetch_info_about_vacancies(url):
    info_about_vacancies = requests.get(
        url,
        headers=API_APP_ID,
        params=DATA_FOR_SEARCHING_VACANCIES
    )
    var_for_getting_list = info_about_vacancies.json()['objects']
       
    list_with_major_info_about_vacansies = []
    for list_of_vacancies in var_for_getting_list:
        vacancy = {
            'Название вакансии:': list_of_vacancies['profession'], 
            'Зарплата:': str(list_of_vacancies['payment_to']),
            'Адрес:': str(list_of_vacancies.get('address')),
            'Метро:': str(list_of_vacancies.get('metro')),
            'Требования:': str(list_of_vacancies.get('candidat')),
            'Стаж:': list_of_vacancies['experience'].get('title'),
            'Ссылка на вакансию:': list_of_vacancies['link'],
            'Название компании:': list_of_vacancies['client'].get('title'),
            'Город:': list_of_vacancies['town'].get('title'),
            'Сфера деятельности:': list_of_vacancies['client'].get('description'),
            'Количество вакансий:': str(list_of_vacancies['client'].get('vacancy_count'))
                }

        list_with_major_info_about_vacansies.append(vacancy)
    
    return list_with_major_info_about_vacansies


def requirements_parsing(url):

    vacancy_requirements = fetch_info_about_vacancies(url)
    list_of_requirements = []
    for requirements in vacancy_requirements: 
        parsed_requirements = set(requirements['Требования:'].lower()
                                              .replace('•',' ')
                                              .replace('\n','')
                                              .replace('.','')
                                              .replace('-','')
                                              .replace(',','')
                                              .replace('<','')
                                              .replace('>','')
                                              .replace('?','')
                                              .replace(';','')
                                              .replace('опыт','')
                                              .replace('*','')
                                              .replace('или','')
                                              .replace('хорошие','')
                                              .replace('умение','')
                                              .replace('работы','')
                                              .replace('более','')
                                              .replace(':','')
                                              .replace('лет','')
                                              .replace('знания','')
                                              .replace('хорошее','')
                                              .replace('обязательно','')
                                              .replace('наличие','')
                                              .split(' '))
        list_of_requirements.append(parsed_requirements)


    return list_of_requirements



def clusterise_salaries(salaries_info, min_salary_limit=60000, middle_salary_limit=150000):

    list_of_salaries_unknown = []
    list_of_salaries_low = []
    list_of_salaries_middle = []
    list_of_salaries_high = []

    for salary in salaries_info: 
        value_of_salary = int(salary['Зарплата:'])
        if value_of_salary == 0:  
            list_of_salaries_unknown.append(value_of_salary)

        elif 0 < value_of_salary <= min_salary_limit:
            list_of_salaries_low.append(value_of_salary)

        elif min_salary_limit < value_of_salary <= middle_salary_limit:
            list_of_salaries_middle.append(value_of_salary)

        elif middle_salary_limit < value_of_salary:
            list_of_salaries_high.append(value_of_salary)

    return (
        list_of_salaries_unknown,
        list_of_salaries_low,
        list_of_salaries_middle,
        list_of_salaries_high,
    )


if __name__ == "__main__":
    authorize('https://api.superjob.ru/2.0/oauth2/password/')
    fetch_info_about_vacancies('https://api.superjob.ru/2.0/vacancies/')
    salaries_info = fetch_info_about_vacancies('https://api.superjob.ru/2.0/vacancies/')
    clusterise_salaries(salaries_info)
    test = requirements_parsing('https://api.superjob.ru/2.0/vacancies/')
    print(test)

    