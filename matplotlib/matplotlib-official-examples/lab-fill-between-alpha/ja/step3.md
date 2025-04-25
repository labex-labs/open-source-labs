# `where`を使った特定の領域の強調表示

`where`キーワード引数は、グラフの特定の領域を強調表示する際に非常に便利です。`where`は、x、ymin、および ymax 引数と同じ長さのブールマスクを取り、ブールマスクが True の領域のみを塗りつぶします。以下の例では、単一のランダムウォーカーをシミュレートし、集団位置の解析的な平均と標準偏差を計算します。集団平均は破線で表示され、平均からのプラス/マイナス 1 シグマの偏差は塗りつぶされた領域として表示されます。`X > upper_bound`の where マスクを使用して、ウォーカーが 1 シグマ境界外にある領域を見つけ、その領域を赤色で塗りつぶします。

```python
# Fixing random state for reproducibility
np.random.seed(1)

Nsteps = 500
t = np.arange(Nsteps)

mu = 0.002
sigma = 0.01

# the steps and position
S = mu + sigma*np.random.randn(Nsteps)
X = S.cumsum()

# the 1 sigma upper and lower analytic population bounds
lower_bound = mu*t - sigma*np.sqrt(t)
upper_bound = mu*t + sigma*np.sqrt(t)

fig, ax = plt.subplots(1)
ax.plot(t, X, lw=2, label='walker position')
ax.plot(t, mu*t, lw=1, label='population mean', color='C0', ls='--')
ax.fill_between(t, lower_bound, upper_bound, facecolor='C0', alpha=0.4,
                label='1 sigma range')
ax.legend(loc='upper left')

# here we use the where argument to only fill the region where the
# walker is above the population 1 sigma boundary
ax.fill_between(t, upper_bound, X, where=X > upper_bound, fc='red', alpha=0.4)
ax.fill_between(t, lower_bound, X, where=X < lower_bound, fc='red', alpha=0.4)
ax.set_xlabel('num steps')
ax.set_ylabel('position')
ax.grid()
```

# `where`を使った特定の領域の強調表示

`where`キーワード引数は、グラフの特定の領域を強調表示する際に非常に便利です。`where`は、x、ymin、および ymax 引数と同じ長さのブールマスクを取り、ブールマスクが True の領域のみを塗りつぶします。以下の例では、単一のランダムウォーカーをシミュレートし、集団位置の解析的な平均と標準偏差を計算します。集団平均は破線で表示され、平均からのプラス/マイナス 1 シグマの偏差は塗りつぶされた領域として表示されます。`X > upper_bound`の where マスクを使用して、ウォーカーが 1 シグマ境界外にある領域を見つけ、その領域を赤色で塗りつぶします。

```python
# 再現性のために乱数シードを固定する
np.random.seed(1)

Nsteps = 500
t = np.arange(Nsteps)

mu = 0.002
sigma = 0.01

# ステップと位置
S = mu + sigma*np.random.randn(Nsteps)
X = S.cumsum()

# 1 シグマの解析的な集団の上限と下限
lower_bound = mu*t - sigma*np.sqrt(t)
upper_bound = mu*t + sigma*np.sqrt(t)

fig, ax = plt.subplots(1)
ax.plot(t, X, lw=2, label='ウォーカーの位置')
ax.plot(t, mu*t, lw=1, label='集団平均', color='C0', ls='--')
ax.fill_between(t, lower_bound, upper_bound, facecolor='C0', alpha=0.4,
                label='1 シグマ範囲')
ax.legend(loc='左上')

# ここでは、where 引数を使用して、ウォーカーが集団の 1 シグマ境界を超えている領域のみを塗りつぶします
ax.fill_between(t, upper_bound, X, where=X > upper_bound, fc='red', alpha=0.4)
ax.fill_between(t, lower_bound, X, where=X < lower_bound, fc='red', alpha=0.4)
ax.set_xlabel('ステップ数')
ax.set_ylabel('位置')
ax.grid()
```
