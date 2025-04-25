# SVG パスデータを解析する

SVG パスデータを Matplotlib で使用できる頂点とコードに解析するために、`svg_parse`関数を使用します。

```python
def svg_parse(path):
    commands = {'M': (Path.MOVETO,),
                'L': (Path.LINETO,),
                'Q': (Path.CURVE3,)*2,
                'C': (Path.CURVE4,)*3,
                'Z': (Path.CLOSEPOLY,)}
    vertices = []
    codes = []
    cmd_values = re.split("([A-Za-z])", path)[1:]  # コマンドで分割する。
    for cmd, values in zip(cmd_values[::2], cmd_values[1::2]):
        # 数字はコンマで区切られるか、+/-記号で区切られる（ただし、文字列の先頭ではない）。
        points = ([*map(float, re.split(",|(?<!^)(?=[+-])", values))] if values
                  else [(0., 0.)])  # "z/Z"（CLOSEPOLY）のみ。
        points = np.reshape(points, (-1, 2))
        if cmd.islower():
            points += vertices[-1][-1]
        codes.extend(commands[cmd.upper()])
        vertices.append(points)
    return np.array(codes), np.concatenate(vertices)

# Firefox ロゴのパスデータを解析する
codes, verts = svg_parse(firefox)
path = Path(verts, codes)
```
