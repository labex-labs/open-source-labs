# Definir la función de densidad de probabilidad (PDF) de la distribución beta

La distribución beta es una distribución de probabilidad continua que a menudo se utiliza para representar la distribución de probabilidades. En la actualización bayesiana, usamos la distribución beta como una distribución a priori para representar nuestras creencias sobre la probabilidad de una hipótesis antes de observar cualquier dato. Luego actualizamos la distribución beta a medida que observamos nuevos datos.

Para simular la actualización bayesiana, necesitamos definir una función que calcule la función de densidad de probabilidad (PDF) de la distribución beta. Podemos usar la función `math.gamma` para calcular la función gamma, que se utiliza en la PDF de la distribución beta.

```python
def beta_pdf(x, a, b):
    return (x**(a-1) * (1-x)**(b-1) * math.gamma(a + b)
            / (math.gamma(a) * math.gamma(b)))
```
