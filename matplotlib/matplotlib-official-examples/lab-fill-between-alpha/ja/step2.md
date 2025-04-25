# `alpha`を使って色を柔らかくする

`alpha`引数は、視覚的に魅力的なプロットを作成するために色を柔らかくするためにも使用できます。次の例では、歩幅が抽出される正規分布の平均と標準偏差が異なる 2 つのランダムウォーカーの集団を計算します。集団の平均位置の標準偏差のプラスマイナス 1 をプロットするために塗りつぶされた領域を使用します。

```python
# Fixing random state for reproducibility
np.random.seed(19680801)

Nsteps, Nwalkers = 100, 250
t = np.arange(Nsteps)

# an (Nsteps x Nwalkers) array of random walk steps
S1 = 0.004 + 0.02*np.random.randn(Nsteps, Nwalkers)
S2 = 0.002 + 0.01*np.random.randn(Nsteps, Nwalkers)

# an (Nsteps x Nwalkers) array of random walker positions
X1 = S1.cumsum(axis=0)
X2 = S2.cumsum(axis=0)

# Nsteps length arrays empirical means and standard deviations of both
# populations over time
mu1 = X1.mean(axis=1)
sigma1 = X1.std(axis=1)
mu2 = X2.mean(axis=1)
sigma2 = X2.std(axis=1)

# plot it!
fig, ax = plt.subplots(1)
ax.plot(t, mu1, lw=2, label='mean population 1')
ax.plot(t, mu2, lw=2, label='mean population 2')
ax.fill_between(t, mu1+sigma1, mu1-sigma1, facecolor='C0', alpha=0.4)
ax.fill_between(t, mu2+sigma2, mu2-sigma2, facecolor='C1', alpha=0.4)
ax.set_title(r'random walkers empirical $\mu$ and $\pm \sigma$ interval')
ax.legend(loc='upper left')
ax.set_xlabel('num steps')
ax.set_ylabel('position')
ax.grid()
```

`alpha`引数を使って色を柔らかくすることもできます。次の例では、歩幅が抽出される正規分布の平均と標準偏差が異なる 2 つのランダムウォーカーの集団を計算します。集団の平均位置の標準偏差のプラスマイナス 1 をプロットするために塗りつぶされた領域を使用します。

```python
# 再現性のために乱数シードを固定する
np.random.seed(19680801)

Nsteps, Nwalkers = 100, 250
t = np.arange(Nsteps)

# ランダムウォークの歩幅の (Nsteps x Nwalkers) 配列
S1 = 0.004 + 0.02*np.random.randn(Nsteps, Nwalkers)
S2 = 0.002 + 0.01*np.random.randn(Nsteps, Nwalkers)

# ランダムウォーカーの位置の (Nsteps x Nwalkers) 配列
X1 = S1.cumsum(axis=0)
X2 = S2.cumsum(axis=0)

# 両方の集団の経験的な平均と標準偏差の Nsteps 長さの配列
# 時間経過とともに
mu1 = X1.mean(axis=1)
sigma1 = X1.std(axis=1)
mu2 = X2.mean(axis=1)
sigma2 = X2.std(axis=1)

# プロットする！
fig, ax = plt.subplots(1)
ax.plot(t, mu1, lw=2, label='平均集団 1')
ax.plot(t, mu2, lw=2, label='平均集団 2')
ax.fill_between(t, mu1+sigma1, mu1-sigma1, facecolor='C0', alpha=0.4)
ax.fill_between(t, mu2+sigma2, mu2-sigma2, facecolor='C1', alpha=0.4)
ax.set_title(r'ランダムウォーカーの経験的な$\mu$と$\pm \sigma$区間')
ax.legend(loc='左上')
ax.set_xlabel('ステップ数')
ax.set_ylabel('位置')
ax.grid()
```
