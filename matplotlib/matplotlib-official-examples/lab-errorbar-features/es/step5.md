# Graficar variable con barras de error asimétricas

A continuación, graficaremos nuestros datos con barras de error asimétricas variables. Se utiliza nuevamente la función `ax.errorbar()`, pero esta vez el parámetro `xerr` se utiliza para especificar los valores de error asimétricos.

```python
# plot variable, asymmetric error bars
fig, ax = plt.subplots()
ax.errorbar(x, y, xerr=asymmetric_error, fmt='o')
ax.set_title('Variable, Asymmetric Error Bars')
plt.show()
```
