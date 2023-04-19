# В предыдущем задании вы создали датаклассы,
# которые описывают структуру ответа из VK API (friends.get).
# В этом задании нужно написать функцию get_vk_data,
# которая на вход должна принять ответ из vk (переменная vk_data, содержащая информацию в формате json),
# а на выходе вернуть объект класса VkData (датакласы уже определены в прекоде).
# В случае если передана некорректная структура,
# то нужно вызвать исключение ValueError

# Подсказка:
# Перед функцией, которую Вам предстоит написать есть переменная
# VkDataSchema
# нужно использовать marshmallow_dataclass.
# marshmallow схемы вызывают исключение ValidationError,
# если переданы на вход некорректные данные,
# нужно это исключение перехватить и вызвать ValueError

import marshmallow_dataclass
import marshmallow

from dataclasses import dataclass
from typing import Dict, List


@dataclass
class University:
    chair_name: str
    id: int
    name: str


@dataclass
class Occupation:
    id: int
    type: str


@dataclass
class OnlineInfo:
    visible: bool
    last_seen: int


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

vk_data = {
   "response": {
       "count": 1,
       "items": [{
           "id": 100,
           "first_name": "Иван",
           "last_name": "Иванов",
           "online_info": {
               "visible": True,
               "last_seen": 1639414645
           },
           "occupation": {
               "KTS": {
                   "id": 1,
                   "type": "work"
               }
           },
           "universities": [{
               "chair_name": "Автоматизированные системы обработки информации и управления",
               "id": 250,
               "name": "МГТУ им. Н.Э. Баумана"
           }],
       }]
   }
}

VkDataSchema = marshmallow_dataclass.class_schema(VkData)


def get_vk_data(data) -> VkData:
    try:
        return VkDataSchema().load(data)
    except:
        raise ValueError


if __name__ == "__main__":
    print(get_vk_data(vk_data))
