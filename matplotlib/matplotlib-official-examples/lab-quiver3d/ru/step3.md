# Определение направления стрелок

Теперь мы определим направление стрелок. В этом примере мы будем определять направление стрелок с использованием тригонометрических функций NumPy. Функции `sin` и `cos` используются для создания массивов `u`, `v` и `w`, которые представляют направление стрелок по осям `x`, `y` и `z`.

```python
u = np.sin(np.pi * x) * np.cos(np.pi * y) * np.cos(np.pi * z)
v = -np.cos(np.pi * x) * np.sin(np.pi * y) * np.cos(np.pi * z)
w = (np.sqrt(2.0 / 3.0) * np.cos(np.pi * x) * np.cos(np.pi * y) *
     np.sin(np.pi * z))
```
