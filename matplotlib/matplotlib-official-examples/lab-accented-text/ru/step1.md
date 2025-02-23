# Использование Mathtext

Mathtext - это функция в Matplotlib, которая позволяет использовать команды TeX для отображения математических символов и уравнений. Mathtext также поддерживает символы с ударениями.

```python
import matplotlib.pyplot as plt

# Демонстрация Mathtext
fig, ax = plt.subplots()
ax.plot(range(10))
ax.set_title(r'$\ddot{o}\acute{e}\grave{e}\hat{O}'
             r'\breve{i}\bar{A}\tilde{n}\vec{q}$', fontsize=20)

# Поддерживается также сокращенная запись и фигурные скобки являются необязательными
ax.set_xlabel(r"""$\"o\ddot o \'e\`e\~n\.x\^y$""", fontsize=20)
ax.text(4, 0.5, r"$F=m\ddot{x}$")
fig.tight_layout()
```
