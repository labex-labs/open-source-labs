# Analizar los datos de trayectoria SVG

Utilizaremos la función `svg_parse` para analizar los datos de trayectoria SVG en vértices y códigos que pueden ser utilizados por Matplotlib.

```python
def svg_parse(path):
    commands = {'M': (Path.MOVETO,),
                'L': (Path.LINETO,),
                'Q': (Path.CURVE3,)*2,
                'C': (Path.CURVE4,)*3,
                'Z': (Path.CLOSEPOLY,)}
    vertices = []
    codes = []
    cmd_values = re.split("([A-Za-z])", path)[1:]  # Dividir sobre los comandos.
    for cmd, values in zip(cmd_values[::2], cmd_values[1::2]):
        # Los números están separados ya sea por comas, o por signos +/- (pero no al principio de la cadena).
        points = ([*map(float, re.split(",|(?<!^)(?=[+-])", values))] if values
                  else [(0., 0.)])  # Solo para "z/Z" (CLOSEPOLY).
        points = np.reshape(points, (-1, 2))
        if cmd.islower():
            points += vertices[-1][-1]
        codes.extend(commands[cmd.upper()])
        vertices.append(points)
    return np.array(codes), np.concatenate(vertices)

# Analizar los datos de trayectoria del logotipo de Firefox
codes, verts = svg_parse(firefox)
path = Path(verts, codes)
```
