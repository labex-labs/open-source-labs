# Настройка лимитов и добавление подписей

Наконец, мы настроим пределы графика и добавим подписи осей с использованием функций `set_zlim()`, `set_xlabel()`, `set_ylabel()` и `set_zlabel()` библиотеки Matplotlib. Мы также используем LaTeX-режим математики для написания подписей осей.

```python
ax.set_zlim(0, 1)
ax.set_xlabel(r'$\phi_\mathrm{real}$')
ax.set_ylabel(r'$\phi_\mathrm{im}$')
ax.set_zlabel(r'$V(\phi)$')
```
