# 決定境界を描画する

このステップでは、前のステップで作成した決定境界を描画します。SVMモデルの`coef_`と`intercept_`属性を使って決定境界を描画します。

```python
    for coef, intercept, col in zip(svm.coef_, svm.intercept_, classes):
        line2 = -(line * coef[1] + intercept) / coef[0]
        ax.plot(line2, line, "-", c=colors[col[0]])
        ax.plot(line2, line, "--", c=colors[col[1]])
    ax.set_xlim(xlim)
    ax.set_ylim(ylim)
    ax.set_title(title)
    ax.set_aspect("equal")
```
