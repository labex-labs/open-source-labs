# データのプロット

同じプロットに 3 つのデータセット：密度、温度、および速度をプロットします。データをプロットするために`plot()`関数を使用します。

```python
p1, = host.plot([0, 1, 2], [0, 1, 2], label="Density")
p2, = par1.plot([0, 1, 2], [0, 3, 2], label="Temperature")
p3, = par2.plot([0, 1, 2], [50, 30, 15], label="Velocity")
```
