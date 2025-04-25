# プロットを作成する

データが用意できたので、プロットを作成しましょう。まず、`matplotlib.pyplot.subplots()`を使って軸オブジェクトを作成します。その後、この軸オブジェクトに最初のセットのデータをプロットし、ラベルの色を赤色に設定します。

```python
fig, ax1 = plt.subplots()

color = 'tab:red'
ax1.set_xlabel('time (s)')
ax1.set_ylabel('exp', color=color)
ax1.plot(t, data1, color=color)
ax1.tick_params(axis='y', labelcolor=color)
```

次に、`ax1.twinx()`メソッドを使って、最初の軸オブジェクトと同じ x 軸を共有する 2 番目の軸オブジェクトをインスタンス化します。その後、この新しい軸オブジェクトに 2 番目のセットのデータをプロットし、ラベルの色を青色に設定します。

```python
ax2 = ax1.twinx()

color = 'tab:blue'
ax2.set_ylabel('sin', color=color)
ax2.plot(t, data2, color=color)
ax2.tick_params(axis='y', labelcolor=color)
```

最後に、`fig.tight_layout()`メソッドを使ってプロットのレイアウトを調整し、`matplotlib.pyplot.show()`を使って表示します。

```python
fig.tight_layout()
plt.show()
```
