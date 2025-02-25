# Tamaño de la figura en centímetros

También podemos especificar el tamaño de la figura en centímetros. Para hacer esto, necesitamos convertir los números basados en centímetros a pulgadas. Esto se puede hacer multiplicando el valor en centímetros por el factor de conversión de cm a pulgadas, que es 1/2.54. Luego podemos utilizar este valor como el parámetro figsize en la función subplots. El código siguiente muestra cómo crear una figura con un tamaño de 15 cm x 5 cm.

```python
cm = 1/2.54  # centímetros en pulgadas
plt.subplots(figsize=(15*cm, 5*cm))
plt.show()
```
