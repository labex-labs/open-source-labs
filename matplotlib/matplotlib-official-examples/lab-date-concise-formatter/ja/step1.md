# デフォルトのフォーマッタ

まずは、デフォルトのフォーマッタとその冗長な出力を見てみましょう。時間の経過に伴うデータをプロットし、デフォルトのフォーマッタが日付と時刻をどのように表示するかを見ます。

```python
import datetime
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates

# create time data
base = datetime.datetime(2005, 2, 1)
dates = [base + datetime.timedelta(hours=(2 * i)) for i in range(732)]
N = len(dates)
np.random.seed(19680801)
y = np.cumsum(np.random.randn(N))

# plot data
fig, axs = plt.subplots(3, 1, layout='constrained', figsize=(6, 6))
lims = [(np.datetime64('2005-02'), np.datetime64('2005-04')),
        (np.datetime64('2005-02-03'), np.datetime64('2005-02-15')),
        (np.datetime64('2005-02-03 11:00'), np.datetime64('2005-02-04 13:20'))]
for nn, ax in enumerate(axs):
    ax.plot(dates, y)
    ax.set_xlim(lims[nn])
    # rotate labels...
    for label in ax.get_xticklabels():
        label.set_rotation(40)
        label.set_horizontalalignment('right')
axs[0].set_title('Default Date Formatter')
plt.show()
```

# デフォルトのフォーマッタ

まずは、デフォルトのフォーマッタとその冗長な出力を見てみましょう。時間の経過に伴うデータをプロットし、デフォルトのフォーマッタが日付と時刻をどのように表示するかを見ます。

```python
import datetime
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates

# 時間データを作成する
base = datetime.datetime(2005, 2, 1)
dates = [base + datetime.timedelta(hours=(2 * i)) for i in range(732)]
N = len(dates)
np.random.seed(19680801)
y = np.cumsum(np.random.randn(N))

# データをプロットする
fig, axs = plt.subplots(3, 1, layout='constrained', figsize=(6, 6))
lims = [(np.datetime64('2005-02'), np.datetime64('2005-04')),
        (np.datetime64('2005-02-03'), np.datetime64('2005-02-15')),
        (np.datetime64('2005-02-03 11:00'), np.datetime64('2005-02-04 13:20'))]
for nn, ax in enumerate(axs):
    ax.plot(dates, y)
    ax.set_xlim(lims[nn])
    # ラベルを回転させる...
    for label in ax.get_xticklabels():
        label.set_rotation(40)
        label.set_horizontalalignment('right')
axs[0].set_title('Default Date Formatter')
plt.show()
```
