# 调整布局并保存图表

最后，你可以分别使用 `fig.tight_layout()` 和 `fig.savefig()` 函数来调整图表的布局并将其保存到文件中。

```python
fig.tight_layout(pad=.5)

fig.savefig("pgf_texsystem.pdf")
fig.savefig("pgf_texsystem.png")
```
