# Definir rótulos de marcação para o segundo eixo y

Podemos definir os rótulos de marcação para o segundo eixo y usando a função `set_xticks` e passando as localizações e rótulos de marcação como argumentos.

```python
ax2.set_xticks([0., .5*np.pi, np.pi, 1.5*np.pi, 2*np.pi],
               labels=["$0$", r"$\frac{1}{2}\pi$",
                       r"$\pi$", r"$\frac{3}{2}\pi$", r"$2\pi$"])
```
