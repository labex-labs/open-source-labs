# 调整界限并添加标签

最后，我们将使用 Matplotlib 的 `set_zlim()` 以及 `set_xlabel()`、`set_ylabel()`、`set_zlabel()` 函数来调整绘图的界限并添加轴标签。我们还将使用 LaTeX 数学模式来书写轴标签。

```python
ax.set_zlim(0, 1)
ax.set_xlabel(r'$\phi_\mathrm{real}$')
ax.set_ylabel(r'$\phi_\mathrm{im}$')
ax.set_zlabel(r'$V(\phi)$')
```
