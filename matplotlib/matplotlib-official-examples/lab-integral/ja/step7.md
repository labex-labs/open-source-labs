# 軸のラベルと目盛りのラベルを追加する

`figtext`を使って x 軸と y 軸のラベルを追加します。`spines`を使って上と右の目盛り線を非表示にします。`set_xticks`と`set_yticks`を使ってカスタムの目盛りの配置とラベルを設定します。

```python
fig.text(0.9, 0.05, '$x$')
fig.text(0.1, 0.9, '$y$')

ax.spines[['top', 'right']].set_visible(False)
ax.set_xticks([a, b], labels=['$a$', '$b$'])
ax.set_yticks([])
```
