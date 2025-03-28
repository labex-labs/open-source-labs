# Определяем функцию плотности вероятности для бета-распределения

Бета-распределение - это непрерывное распределение вероятностей, которое часто используется для представления распределения вероятностей. В байесовском обновлении мы используем бета-распределение в качестве априорного распределения, чтобы представить наши взгляды на вероятность гипотезы до наблюдения каких-либо данных. Затем мы обновляем бета-распределение при наблюдении новых данных.

Для моделирования байесовского обновления нам нужно определить функцию, которая вычисляет функцию плотности вероятности (PDF) для бета-распределения. Мы можем использовать функцию `math.gamma` для вычисления гамма-функции, которая используется в PDF бета-распределения.

```python
def beta_pdf(x, a, b):
    return (x**(a-1) * (1-x)**(b-1) * math.gamma(a + b)
            / (math.gamma(a) * math.gamma(b)))
```
