# Trazar los datos

En este paso, usaremos la función `plot` de Matplotlib para trazar los tres conjuntos de datos en una sola llamada. Usaremos rayas rojas para el primer conjunto de datos, cuadrados azules para el segundo conjunto de datos y triángulos verdes para el tercer conjunto de datos.

```python
plt.plot(t, t, 'r--', label='linear')
plt.plot(t, t**2, 'bs', label='quadratic')
plt.plot(t, t**3, 'g^', label='cubic')
plt.legend()
plt.show()
```
