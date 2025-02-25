# Определяем функцию для снежинки Коха

Далее мы определим функцию для генерации снежинки Коха. Функция принимает два параметра: глубину рекурсии и коэффициент масштабирования.

```python
def koch_snowflake(order, scale=10):
    """
    Возвращает два списка x, y с координатами точек снежинки Коха.

    Параметры
    ----------
    order : int
        Глубина рекурсии.
    scale : float
        Размер снежинки (длина стороны базового треугольника).
    """
    def _koch_snowflake_complex(order):
        if order == 0:
            # начальный треугольник
            angles = np.array([0, 120, 240]) + 90
            return scale / np.sqrt(3) * np.exp(np.deg2rad(angles) * 1j)
        else:
            ZR = 0.5 - 0.5j * np.sqrt(3) / 3

            p1 = _koch_snowflake_complex(order - 1)  # точки начала
            p2 = np.roll(p1, shift=-1)  # точки конца
            dp = p2 - p1  # векторы соединения

            new_points = np.empty(len(p1) * 4, dtype=np.complex128)
            new_points[::4] = p1
            new_points[1::4] = p1 + dp / 3
            new_points[2::4] = p1 + dp * ZR
            new_points[3::4] = p1 + dp / 3 * 2
            return new_points

    points = _koch_snowflake_complex(order)
    x, y = points.real, points.imag
    return x, y
```
