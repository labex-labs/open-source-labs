# Подготавливаем данные

Мы подготовим данные для нашей диаграммы SkewT-logP. Мы будем использовать модуль StringIO для чтения данных из строки и NumPy для загрузки их в массивы.

```python
data_txt = '''
        978.0    345    7.8    0.8
        971.0    404    7.2    0.2
        946.7    610    5.2   -1.8
     ...
    '''
sound_data = StringIO(data_txt)
p, h, T, Td = np.loadtxt(sound_data, unpack=True)
```
