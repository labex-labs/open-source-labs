# 初期のプロットを作成する

次に、ユーザーの入力に基づいて更新される初期のプロットを作成します。この例では、独立変数として`t`を持つ関数のプロットを作成します。

```python
fig, ax = plt.subplots()
fig.subplots_adjust(bottom=0.2)

t = np.arange(-2.0, 2.0, 0.001)
l, = ax.plot(t, np.zeros_like(t), lw=2)
```
