# パラメータの定義

このステップでは、アイリスデータセット上の決定面をプロットするために必要なパラメータを定義します。

```python
# Parameters
n_classes = 3
n_estimators = 30
cmap = plt.cm.RdYlBu
plot_step = 0.02  # fine step width for decision surface contours
plot_step_coarser = 0.5  # step widths for coarse classifier guesses
RANDOM_SEED = 13  # fix the seed on each iteration
```
