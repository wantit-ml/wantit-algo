from db_help import *
from typing import Union, List
from cossim import SimCosModel


def count_ones(x):
    result = 0
    while x > 0:
        result += x & 1
        x = x >> 1
    return result


""" 
should be called as 
 users_for_vacancy = await MatchForHR.search_users(vacancy, list_of_about_objects)
"""


class MatchForHR():
    cute_model = SimCosModel()

    @classmethod
    async def search_users(cls, vacancy: Vacancy, users_list: List[About]) -> List[int]:
        matched_users_ids = []
        skills_needed=vacancy.code.count("1")
        for candidate in users_list:
            vacancy_code_len = len(vacancy.code)
            candidate_code_len = len(candidate.code)
            vacancy_code = int(vacancy.code, 2)
            candidate_code = int(candidate.code, 2)

            if vacancy_code_len > candidate_code_len:
                candidate_code <<= (vacancy_code_len - candidate_code_len)
            else:
                vacancy_code <<= (candidate_code_len - vacancy_code_len)

            if count_ones(vacancy_code & candidate_code)/skills_needed >= 0.6:
                matched_users_ids.append(candidate.id)
        return cls.cute_model.rang_candidates(vacancy, matched_users_ids)


""" 
should be called as 
 users_for_vacancy = await MatchForUser.search_users(about_object, list_of_vacancy_objects)
"""


class MatchForUser():
    cute_model = SimCosModel()

    @classmethod
    async def search_vacancies(cls, user_info: About, vacancies_list: List[Vacancy]) -> List[int]:
        matched_vacancies_ids = []

        for sample_vacancy in vacancies_list:
            sample_vacancy_code_len = len(sample_vacancy.code)
            user_info_code_len = len(user_info.code)
            sample_vacancy_code = int(sample_vacancy.code, 2)
            user_info_code = int(user_info.code, 2)

            skills_needed=sample_vacancy.code.count("1")

            if sample_vacancy_code_len > user_info_code_len:
                user_info_code <<= (sample_vacancy_code_len - user_info_code_len)
            else:
                sample_vacancy_code <<= (user_info_code_len - sample_vacancy_code_len)

            if count_ones(sample_vacancy_code & user_info_code)/ skills_needed >= 0.6:
                matched_vacancies_ids.append(sample_vacancy.id)
        return cls.cute_model.rang_candidates(user_info, matched_vacancies_ids)
