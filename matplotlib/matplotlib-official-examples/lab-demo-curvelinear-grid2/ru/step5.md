# Создать фигуру

Последним шагом является создание фигуры с использованием функции `plt.figure`. Мы установим размер фигуры в (7, 4) и вызовем функцию `curvelinear_test1`, созданную на шагах 2-4.

```python
if __name__ == "__main__":
    fig = plt.figure(figsize=(7, 4))
    curvelinear_test1(fig)
    plt.show()
```
