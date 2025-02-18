# CSDを計算する

2つの信号の相互スペクトル密度（Cross Spectral Density, CSD）を計算するには、Matplotlibのcsd関数を使用する必要があります。この関数は、2つの信号、FFT（高速フーリエ変換）のポイント数、およびサンプリング周波数を入力として受け取ります。

```python
fig, ax = plt.subplots()
cxy, f = ax.csd(s1, s2, 256, 1. / dt)
ax.set_ylabel('CSD (dB)')
plt.show()
```
