# У вас есть пример ответа от VK API (https://vk.com/dev/friends.get),
# переменная vk_data. Основываясь на словаре vk_data нужно
# описать структуру ответа API с помощью dataclass.
# Нужно дополнить класс User и описать дополнительно
# датаклассы для OnlineInfo, Occupation и University.
# Также датаклассы должны соответствовать структуре представленного json
#
# Замечание: данные не полностью повторяют формат VK API,
# некоторые поля были убраны или изменены для упрощения/дополнения заданий ниже.
# Для успешного прохождения тестов
# при написании аннотаций используйте, пожалуйста, библиотеку typing

from dataclasses import dataclass
from typing import List, Dict, Union

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


# TODO определите классы OnlineInfo, Occupation и University.
@dataclass
class OnlineInfo:
    visible: bool
    last_seen: int


@dataclass
class Occupation:
    id: int
    type: str


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
