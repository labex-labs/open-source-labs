# Analyser les données de tracé SVG

Nous allons utiliser la fonction `svg_parse` pour analyser les données de tracé SVG en sommets et codes utilisables par Matplotlib.

```python
def svg_parse(path):
    commands = {'M': (Path.MOVETO,),
                'L': (Path.LINETO,),
                'Q': (Path.CURVE3,)*2,
                'C': (Path.CURVE4,)*3,
                'Z': (Path.CLOSEPOLY,)}
    vertices = []
    codes = []
    cmd_values = re.split("([A-Za-z])", path)[1:]  # Diviser en fonction des commandes.
    for cmd, values in zip(cmd_values[::2], cmd_values[1::2]):
        # Les nombres sont séparés soit par des virgules, soit par des signes +/- (mais pas au début de la chaîne).
        points = ([*map(float, re.split(",|(?<!^)(?=[+-])", values))] if values
                  else [(0., 0.)])  # Seulement pour "z/Z" (CLOSEPOLY).
        points = np.reshape(points, (-1, 2))
        if cmd.islower():
            points += vertices[-1][-1]
        codes.extend(commands[cmd.upper()])
        vertices.append(points)
    return np.array(codes), np.concatenate(vertices)

# Analyser les données de tracé du logo de Firefox
codes, verts = svg_parse(firefox)
path = Path(verts, codes)
```
