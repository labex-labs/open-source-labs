# Definir a fonte do Matplotlib

Precisamos definir a fonte a ser usada para o texto do Matplotlib. Usaremos a fonte Computer Modern e a definiremos como a fonte padrão para o Matplotlib.

```python
plt.rcParams.update({"mathtext.fontset": "cm", "mathtext.rm": "serif"})
```
