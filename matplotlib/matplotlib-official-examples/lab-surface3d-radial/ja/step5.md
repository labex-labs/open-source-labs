# 表示範囲を調整して軸ラベルを追加する

最後に、Matplotlib の `set_zlim()` と `set_xlabel()`、`set_ylabel()`、`set_zlabel()` 関数を使って、描画の表示範囲を調整して軸ラベルを追加します。また、軸ラベルを記述するために LaTeX の数式モードを使います。

```python
ax.set_zlim(0, 1)
ax.set_xlabel(r'$\phi_\mathrm{real}$')
ax.set_ylabel(r'$\phi_\mathrm{im}$')
ax.set_zlabel(r'$V(\phi)$')
```
