# 相関をプロットする

これで、Matplotlib の`cohere`関数を使って 2 つの信号の相関をプロットすることができます。

```python
cxy, f = axs[1].cohere(s1, s2, 256, 1. / dt)
axs[1].set_ylabel('Coherence')
```
