# Представьте, что ваш руководитель поручил
# вам внедрить датаклассы в проект. Перепишите
# класс Person на использование датаклассов.
# Обратите внимание на переменную skills,
# после создания объекта Person значение skills будет []

# Подсказка: для решения задачи нужно использовать:
# from dataclasses import field


import datetime
from typing import Optional, List


class Person:
    def __init__(
        self, first_name: str,
        last_name: str,
        birthday: datetime.date,
        middle_name: Optional[str] = None,
        skills: List[str] = None
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.birthday = birthday
        self.middle_name = middle_name
        self.skills = skills or []
