# `fill_between`を使った折れ線グラフの強化

最初の例では、`fill_between`を使って折れ線グラフをどのように強化するかを示します。Googleの金融データを使って2つのサブプロットを作成します。1つは単純な折れ線グラフで、もう1つは塗りつぶされた折れ線グラフです。

```python
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cbook as cbook

# load up some sample financial data
r = cbook.get_sample_data('goog.npz')['price_data'].view(np.recarray)

# create two subplots with the shared x and y axes
fig, (ax1, ax2) = plt.subplots(1, 2, sharex=True, sharey=True)

pricemin = r.close.min()

ax1.plot(r.date, r.close, lw=2)
ax2.fill_between(r.date, pricemin, r.close, alpha=0.7)

for ax in ax1, ax2:
    ax.grid(True)
    ax.label_outer()

ax1.set_ylabel('price')
fig.suptitle('Google (GOOG) daily closing price')
fig.autofmt_xdate()
```

`fill_between`を使って折れ線グラフを強化する方法の最初の例を示します。Googleの金融データを使って2つのサブプロットを作成します。1つは単純な折れ線グラフで、もう1つは塗りつぶされた折れ線グラフです。

```python
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cbook as cbook

# いくつかのサンプルの金融データを読み込む
r = cbook.get_sample_data('goog.npz')['price_data'].view(np.recarray)

# 共有のx軸とy軸を持つ2つのサブプロットを作成する
fig, (ax1, ax2) = plt.subplots(1, 2, sharex=True, sharey=True)

pricemin = r.close.min()

ax1.plot(r.date, r.close, lw=2)
ax2.fill_between(r.date, pricemin, r.close, alpha=0.7)

for ax in ax1, ax2:
    ax.grid(True)
    ax.label_outer()

ax1.set_ylabel('価格')
fig.suptitle('Google (GOOG)の日次終値')
fig.autofmt_xdate()
```

各サブプロットに対して、グリッドを表示し、外部のラベルを設定します。最初のサブプロットにはy軸のラベルを設定し、グラフ全体のタイトルを設定し、x軸の日付を自動的に整形します。
