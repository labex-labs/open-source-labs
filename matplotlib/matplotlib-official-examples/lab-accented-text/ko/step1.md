# Mathtext 사용하기

Mathtext 는 Matplotlib 의 기능으로, TeX 명령을 사용하여 수학 기호 및 방정식을 렌더링할 수 있게 해줍니다. Mathtext 는 또한 악센트 문자를 지원합니다.

```python
import matplotlib.pyplot as plt

# Mathtext demo
fig, ax = plt.subplots()
ax.plot(range(10))
ax.set_title(r'$\ddot{o}\acute{e}\grave{e}\hat{O}'
             r'\breve{i}\bar{A}\tilde{n}\vec{q}$', fontsize=20)

# Shorthand is also supported and curly braces are optional
ax.set_xlabel(r"""$\"o\ddot o \'e\`e\~n\.x\^y$""", fontsize=20)
ax.text(4, 0.5, r"$F=m\ddot{x}$")
fig.tight_layout()
```
