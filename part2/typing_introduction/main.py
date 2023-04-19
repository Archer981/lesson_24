# Вам предоставлен код, которые получает топ3 университета среди ваших друзей.
# Друзей, как и в предыдущих заданиях получили с помощью метода VK API.
# Вам нужно провести ревью этого кода и переписать его с использованием типов и dataclass'ов.
# Для удобства мы перенесли переменную vk_data в другой файл,
# Пожалуйста, придерживайтесь нейминга, определенного в условиях задачи.
# Данная задача должна решаться в несколько этапов:
import marshmallow_dataclass

# 1 Этап. Формируем датаклассы для хранения данных.
#    - VkData - Наши сведения
#        - response: содержит класс response
#    - VkResponse - Вложенный словарь response, содержит информацию о количестве друзей и сам список друзей
#        - count
#        - items
#    - User - Класс для хранения данных пользователя
#        - id:
#        - first_name:
#        - last_name:
#        - online_info:
#        - occupation:
#        - universities:
#    - University - информация об университетах
#        - chair_name
#        - id
#        - name
#    - OnlineInfo - информация последнем времени онлайн
#        - visible:
#        - last_seen:
#    - Occupation - информация о роде деятельности
#        - id:
#        - type:
#
# 2 Этап. Создаем переменную VkDataSchema которая будет содержать экземпляр класса marshmallow_dataclass.class_schema
#         и определяем функцию get_vk_data которая загружает данные в VkDataSchema
#
# 3 Этап. Производим рефакторинг функции get_university_pairs.
#
# Первые два этапа проверяются автотестами.
# 3 Этап связан с рефакторингом. Здесь для проверки необходимо ревью
#
# Для успешного прохождения тестов
# при написании аннотаций используйте, пожалуйста, библиотеку typing

from vk_data import vk_data
from dataclasses import dataclass
from typing import Optional, List, Dict, Tuple, Any, Set


@dataclass
class Occupation:
    id: int
    type: str


@dataclass
class OnlineInfo:
    visible: bool
    last_seen: int


@dataclass
class University:
    chair_name: str
    id: int
    name: str


@dataclass
class User:
    id: int
    first_name: str
    last_name: str
    online_info: OnlineInfo
    occupation: Dict[str, Occupation]
    universities: List[University]


@dataclass
class VkResponse:
    count: int
    items: List[User]


@dataclass
class VkData:
    response: VkResponse


VkDataSchema = marshmallow_dataclass.class_schema(VkData)


def get_vk_data(data):
    return VkDataSchema().load(data)


def get_university_pairs(data: VkData) -> List[Tuple[Any, Any]]:
    universities: Dict[int, Dict[str, str | int]] = {}
    for user in data.response.items:
        university_set: Set[int] = set()
        for university in user.universities:
            university_id = university.id
            if university_id not in universities:
                universities[university_id] = {
                    "name": university.name,
                    "count": 0
                }
            if university_id not in university_set:
                # условие нужно для того, чтобы в результате не учитывать 2 раза один и тот же университет,
                # если человек учился, например, в бакалавриате и магистратуре
                universities[university_id]["count"] += 1
                university_set.add(university_id)
    res = sorted(
        map(lambda u: (u["name"], u["count"]), universities.values()),
        reverse=False
    )
    return res[:3]


if __name__ == "__main__":
    print(get_university_pairs(get_vk_data(vk_data)))
