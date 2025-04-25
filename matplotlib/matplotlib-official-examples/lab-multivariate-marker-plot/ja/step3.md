# ランダムなデータの生成

このステップでは、投手の技術、離陸角度、推力、成功、および位置に関するランダムなデータを生成します。具体的には、位置を除く各変数について 25 個のデータポイントを生成します。位置については、各データポイントに 2 つの座標があります。

```python
N = 25
np.random.seed(42)
skills = np.random.uniform(5, 80, size=N) * 0.1 + 5
takeoff_angles = np.random.normal(0, 90, N)
thrusts = np.random.uniform(size=N)
successful = np.random.randint(0, 3, size=N)
positions = np.random.normal(size=(N, 2)) * 5
data = zip(skills, takeoff_angles, thrusts, successful, positions)
```
