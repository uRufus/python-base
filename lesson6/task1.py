'''
1. Создать класс TrafficLight (светофор) и определить у него один атрибут
color (цвет) и метод running (запуск). Атрибут реализовать как приватный.
В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд,
второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов,
и при его нарушении выводить соответствующее сообщение и завершать скрипт.
'''
from time import sleep


class TrafficLight:
    __current_color = "красный"
    traffic_lights = {"красный": [3, "желтый"], "желтый": [2, "зеленый"], "зеленый": [5, "красный"]}

    def running(self, color):
        if color != self.__current_color:
            return print("Вы ввели не тот знак светофора")
        sleep(self.traffic_lights[color][0])
        self.__current_color = self.traffic_lights[color][1]
        print(f"Цвет светофора сменился на {self.__current_color}")


traffic_light = TrafficLight()
traffic_light.running("красный")
traffic_light.running("желтый")
traffic_light.running("желтый")
traffic_light.running("зеленый")
