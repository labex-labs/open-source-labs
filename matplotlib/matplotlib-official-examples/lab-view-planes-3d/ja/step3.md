# 一次3Dビュープレーンとその角度を定義する

一次3Dビュープレーンとそれに対応する仰角、方位角、ロール角を定義します。

```python
views = [('XY',   (90, -90, 0)),
         ('XZ',    (0, -90, 0)),
         ('YZ',    (0,   0, 0)),
         ('-XY', (-90,  90, 0)),
         ('-XZ',   (0,  90, 0)),
         ('-YZ',   (0, 180, 0))]
```
