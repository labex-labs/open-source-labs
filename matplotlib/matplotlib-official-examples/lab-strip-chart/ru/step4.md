# Создание функции-эмиттера

Функция-эмиттер (`emitter`) генерирует данные, которые будут переданы методу обновления (`update`). В данном случае мы генерируем случайные данные с вероятностью 0.1.

```python
def emitter(p=0.1):
    while True:
        v = np.random.rand()
        if v > p:
            yield 0.
        else:
            yield np.random.rand()
```
