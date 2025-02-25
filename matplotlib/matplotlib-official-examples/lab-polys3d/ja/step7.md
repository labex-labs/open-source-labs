# プロットの範囲とラベルを設定する

最後に、`set`関数を使ってプロットの範囲とラベルを設定します。

```python
ax.set(xlim=(0, 10), ylim=(1, 9), zlim=(0, 0.35),
       xlabel='x', ylabel=r'$\lambda$', zlabel='probability')
```
