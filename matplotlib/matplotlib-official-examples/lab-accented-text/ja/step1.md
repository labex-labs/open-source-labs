# Mathtextの使用

Mathtextは、Matplotlibの機能で、TeXコマンドを使って数学記号や方程式をレンダリングできるようにします。Mathtextはアクセント付き文字もサポートしています。

```python
import matplotlib.pyplot as plt

# Mathtextのデモ
fig, ax = plt.subplots()
ax.plot(range(10))
ax.set_title(r'$\ddot{o}\acute{e}\grave{e}\hat{O}'
             r'\breve{i}\bar{A}\tilde{n}\vec{q}$', fontsize=20)

# 省略表記もサポートされ、波括弧は省略可能です
ax.set_xlabel(r"""$\"o\ddot o \'e\`e\~n\.x\^y$""", fontsize=20)
ax.text(4, 0.5, r"$F=m\ddot{x}$")
fig.tight_layout()
```
