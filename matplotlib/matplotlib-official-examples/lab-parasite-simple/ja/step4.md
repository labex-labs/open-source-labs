# データの追加

`plot`関数を使ってデータをプロットに追加します。各線を変数に割り当てることで、後で参照できるようにします。

```python
p1, = host.plot([0, 1, 2], [0, 1, 2], label="Density")
p2, = par.plot([0, 1, 2], [0, 3, 2], label="Temperature")
```
