# Определяем функцию обновления

Определяем функцию, которая обновляет график для каждого кадра анимации. Функция принимает три входных параметра: `num` - номер текущего кадра, `walks` - список всех случайных блужданий, и `lines` - список всех линий на графике. Для каждой линии и случайного блуждания мы обновляем данные по координатам x, y и z линии до текущего номера кадра. Мы используем `line.set_data()` и `line.set_3d_properties()` для обновления координат x-y и z соответственно.

```python
def update_lines(num, walks, lines):
    for line, walk in zip(lines, walks):
        # NOTE: there is no.set_data() for 3 dim data...
        line.set_data(walk[:num, :2].T)
        line.set_3d_properties(walk[:num, 2])
    return lines
```
