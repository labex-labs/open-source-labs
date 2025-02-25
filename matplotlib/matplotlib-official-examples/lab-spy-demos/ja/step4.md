# 疎パターンのプロット

配列の疎パターンをプロットするために`spy`関数を使います。`markersize`や`precision`などのさまざまなパラメータを使ってプロットをカスタマイズします。

```python
ax1.spy(x, markersize=5)
ax2.spy(x, precision=0.1, markersize=5)
ax3.spy(x)
ax4.spy(x, precision=0.1)
```
