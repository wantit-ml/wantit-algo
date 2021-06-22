from db_help import *
from typing import Union, List



""" 
converts About or Vacancy class to code num
 
 after declaring 
 converter = Converter(techs_list, languages_list) 
 that should be done once
 
 than for every new or changed application/vacancy you should call 
 converter.convert(object_to_code)
 and add the result of function to "code" field in DB

"""

class Converter():
    def __init__(self, baseline_techs: List[str], baseline_lanuages: List[str]):
        self.baseline_techs = baseline_techs
        self.baseline_languages = baseline_lanuages

    def convert(self, data: Union[About, Vacancy]) -> int:
        stack_code = ['0' for i in range(len(self.baseline_techs))]
        for tech_name in data.stack:
            stack_code[self.baseline_techs.index(tech_name)] = '1'

        lang_code = ['0' for i in range(len(self.baseline_languages))]
        for lang_name in data.foreign_languages:
            lang_code[self.baseline_languages.index(lang_name)] = '1'

        return int(''.join(stack_code + lang_code), 2)


class MatchForHR():
    def __init__(self, baseline_techs: List[str], baseline_lanuages: List[str]):
        self.baseline_techs = baseline_techs
        self.baseline_languages = baseline_lanuages
        self.converter = Converter(baseline_techs, baseline_lanuages)

    def search_users(self, terms: Vacancy, users_list: List[About]) -> List[int]:
        matched_users_ids = []
        vacancy_code = self.converter.convert(terms)
        for candidate in users_list:
            candidate_code = self.converter.convert(candidate)
            if vacancy_code & candidate_code >= vacancy_code:
                matched_users_ids.append(candidate.id)
        return matched_users_ids


class MatchForUser():
    def __init__(self, baseline_techs: List[str], baseline_lanuages: List[str]):
        self.baseline_techs = baseline_techs
        self.baseline_languages = baseline_lanuages
        self.converter = Converter(baseline_techs, baseline_lanuages)

    def search_vacances(self, user_info: About, vacances_list: List[Vacancy]) -> List[int]:
        matched_vacances_ids = []
        user_code = self.converter.convert(user_info)
        for sample_vacancy in vacances_list:
            sample_vacancy_code = self.converter.convert(sample_vacancy)
            if sample_vacancy_code & user_code >= sample_vacancy_code:
                matched_vacances_ids.append(sample_vacancy.id)
        return matched_vacances_ids
