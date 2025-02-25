# Анализируем данные SVG-пути

Мы будем использовать функцию `svg_parse` для анализа данных SVG-пути на вершины и коды, которые могут быть использованы Matplotlib.

```python
def svg_parse(path):
    commands = {'M': (Path.MOVETO,),
                'L': (Path.LINETO,),
                'Q': (Path.CURVE3,)*2,
                'C': (Path.CURVE4,)*3,
                'Z': (Path.CLOSEPOLY,)}
    vertices = []
    codes = []
    cmd_values = re.split("([A-Za-z])", path)[1:]  # Разделяем по командам.
    for cmd, values in zip(cmd_values[::2], cmd_values[1::2]):
        # Числа разделяются либо запятыми, либо знаками +/- (но не в начале строки).
        points = ([*map(float, re.split(",|(?<!^)(?=[+-])", values))] if values
                  else [(0., 0.)])  # Только для "z/Z" (CLOSEPOLY).
        points = np.reshape(points, (-1, 2))
        if cmd.islower():
            points += vertices[-1][-1]
        codes.extend(commands[cmd.upper()])
        vertices.append(points)
    return np.array(codes), np.concatenate(vertices)

# Анализируем данные пути для логотипа Firefox
codes, verts = svg_parse(firefox)
path = Path(verts, codes)
```
