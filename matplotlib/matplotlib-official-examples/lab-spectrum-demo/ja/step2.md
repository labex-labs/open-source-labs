# 変数を設定する

次に、信号用の変数を設定します。サンプリング間隔を 0.01 に設定し、これによりサンプリング周波数は 100Hz になります。0 秒から 10 秒までの時間配列を 0.01 秒刻みで作成します。また、NumPy の`randn`関数を使ってノイズを生成し、指数減衰関数と畳み込んでノイジーな信号を作成します。

```python
np.random.seed(0)

dt = 0.01  # サンプリング間隔
Fs = 1 / dt  # サンプリング周波数
t = np.arange(0, 10, dt)

# ノイズを生成する：
nse = np.random.randn(len(t))
r = np.exp(-t / 0.05)
cnse = np.convolve(nse, r) * dt
cnse = cnse[:len(t)]

s = 0.1 * np.sin(4 * np.pi * t) + cnse  # 信号
```
