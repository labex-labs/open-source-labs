# Establecer las unidades x e y para el gráfico de barras

En este paso, estableceremos las unidades x e y para el gráfico de barras utilizando varios parámetros. Utilizaremos los parámetros `xunits` e `yunits` para establecer las unidades x e y en centímetros e pulgadas.

```python
axs[0, 1].bar(cms, cms, bottom=bottom, width=width, xunits=cm, yunits=inch)
```
