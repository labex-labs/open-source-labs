# EEGデータの読み込みとトレースのプロット

次のステップは、EEGデータを読み込み、トレースをプロットすることです。データをファイルから読み込むには`fromfile()`関数を、トレースをプロットするには`LineCollection()`を使用します。また、y軸の目盛りラベルを電極チャネルに設定します。

```python
# EEGデータを読み込む
n_samples, n_rows = 800, 4
data = np.load('eeg_data.npy')
t = 10 * np.arange(n_samples) / n_samples

# EEGをプロットする
ax2 = fig.add_subplot(2, 1, 2)
ax2.set_xlim(0, 10)
ax2.set_xticks(np.arange(10))
dmin = data.min()
dmax = data.max()
dr = (dmax - dmin) * 0.7  # 少し詰める。
y0 = dmin
y1 = (n_rows - 1) * dr + dmax
ax2.set_ylim(y0, y1)

segs = []
for i in range(n_rows):
    segs.append(np.column_stack((t, data[:, i])))

offsets = np.zeros((n_rows, 2), dtype=float)
offsets[:, 1] = np.arange(n_rows) * dr

lines = LineCollection(segs, offsets=offsets, transOffset=None)
ax2.add_collection(lines)

# y軸において軸座標を使用するようにyticksを設定する
ax2.set_yticks(offsets[:, 1])
ax2.set_yticklabels(['PG3', 'PG5', 'PG7', 'PG9'])
ax2.set_xlabel('Time (s)')
```
