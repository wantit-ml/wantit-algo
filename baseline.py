from db_help import *

class Converter():
    def __init__(self, baseline_techs: list, baseline_lanuages:list):
        self.baseline_techs=baseline_techs
        self.baseline_languages=baseline_lanuages

    def convert(self, data:About) -> int:
        stack_num=['0' for i in range(len(self.baseline_techs))]
        for tech_name in data['stack']:
            stack_num[self.baseline_techs.index(tech_name)]='1'

        lang_num=['0' for i in range(len(self.baseline_languages))]
        for lang_name in data['foreign_languages']:
            lang_num[self.baseline_languages.index(lang_name)]='1'

        return int(''.join(stack_num + lang_num), 2)
    

