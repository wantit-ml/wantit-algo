from db_help import *

class Converter():
    def __init__(self):
        self.baseline_techs=["C++",
                "C#",
                "Django",
                "Docker"
                "Figma",
                "Git",
                "Go",
                "Java",
                "JavaScript",
                "Keras",
                "Python",
                "Pythorch",
                "SQL",
                "React"
                ]
    def convert(self, data:About) -> int:
        stack_num=['0' for i in range(len(self.baseline_techs))]
        for tech_name in data['stack']:
            stack_num[self.baseline_techs.index(tech_name)]='1'
        return int(''.join(stack_num), 2)


