# 解析 SVG 路径数据

我们将使用 `svg_parse` 函数把 SVG 路径数据解析为顶点和代码，以便 Matplotlib 使用。

```python
def svg_parse(path):
    commands = {'M': (Path.MOVETO,),
                'L': (Path.LINETO,),
                'Q': (Path.CURVE3,)*2,
                'C': (Path.CURVE4,)*3,
                'Z': (Path.CLOSEPOLY,)}
    vertices = []
    codes = []
    cmd_values = re.split("([A-Za-z])", path)[1:]  # 按命令分割。
    for cmd, values in zip(cmd_values[::2], cmd_values[1::2]):
        # 数字由逗号或 +/- 符号分隔（但不在字符串开头）。
        points = ([*map(float, re.split(",|(?<!^)(?=[+-])", values))] if values
                  else [(0., 0.)])  # 仅用于 "z/Z"（CLOSEPOLY）。
        points = np.reshape(points, (-1, 2))
        if cmd.islower():
            points += vertices[-1][-1]
        codes.extend(commands[cmd.upper()])
        vertices.append(points)
    return np.array(codes), np.concatenate(vertices)

# 解析 Firefox 标志路径数据
codes, verts = svg_parse(firefox)
path = Path(verts, codes)
```
