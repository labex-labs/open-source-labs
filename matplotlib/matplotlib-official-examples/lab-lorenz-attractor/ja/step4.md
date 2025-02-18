# ローレンツアトラクターの計算

時間を進めながら、前の点とローレンツ関数を使用して次の点を推定することで、ローレンツアトラクターを計算します。

```python
for i in range(num_steps):
    xyzs[i + 1] = xyzs[i] + lorenz(xyzs[i]) * dt
```
