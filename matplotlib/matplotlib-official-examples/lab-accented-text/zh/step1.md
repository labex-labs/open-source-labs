# 使用数学文本

数学文本是 Matplotlib 中的一项功能，它允许你使用 TeX 命令来渲染数学符号和方程式。数学文本也支持带重音符号的字符。

```python
import matplotlib.pyplot as plt

# 数学文本演示
fig, ax = plt.subplots()
ax.plot(range(10))
ax.set_title(r'$\ddot{o}\acute{e}\grave{e}\hat{O}'
             r'\breve{i}\bar{A}\tilde{n}\vec{q}$', fontsize=20)

# 也支持简写形式，花括号是可选的
ax.set_xlabel(r"""$\"o\ddot o \'e\`e\~n\.x\^y$""", fontsize=20)
ax.text(4, 0.5, r"$F=m\ddot{x}$")
fig.tight_layout()
```
