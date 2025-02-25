# サブフィギュアにデータをプロットする

サブフィギュアにデータをプロットするには、各サブフィギュア用に `subfig.subplots()` を使ってサブプロットを作成する必要があります。その後、Matplotlibのプロット関数のいずれかを使ってプロットを作成できます。

```python
ax1 = subfigs[0].subplots()
ax1.plot(np.arange(10), np.random.randn(10))

ax2 = subfigs[1].subplots()
ax2.plot(np.arange(10), np.random.randn(10))
```

これにより、それぞれがランダムなデータのプロットを持つ2つのサブフィギュアが作成されます。
