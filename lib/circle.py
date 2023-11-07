import math

def area(r):
    """
        Возвращает площадь круга с заданным радиусом.

            Параметры:
                    r (float / int): радиус круга
            Возвращаемое значение:
                    area (float): площадь круга с радиусом r
    """
    return math.pi * r * r

def perimeter(r):
    """
        Возвращает длину окружности с заданным радиусом.

            Параметры:
                    r (float / int): радиус окружности
            Возвращаемое значение:
                    perimeter (float): длина окружности с радиусом r
    """
    return 2.0 * math.pi * r
