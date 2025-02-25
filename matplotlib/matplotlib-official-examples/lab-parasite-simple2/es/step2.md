# Definir datos

A continuación, necesitamos definir los datos que se graficarán. En este ejemplo, tenemos un conjunto de observaciones con cuatro variables: nombre, movimiento propio angular, error en el movimiento propio angular y distancia. Convertiremos el movimiento propio angular a velocidad lineal y lo graficaremos contra el FWHM (ancho total a la mitad de la máxima amplitud) de las observaciones.

```python
obs = [["01_S1", 3.88, 0.14, 1970, 63],
       ["01_S4", 5.6, 0.82, 1622, 150],
       ["02_S1", 2.4, 0.54, 1570, 40],
       ["03_S1", 4.1, 0.62, 2380, 170]]

# Factor de conversión del movimiento propio angular a velocidad lineal
pm_to_kms = 1./206265.*2300*3.085e18/3.15e7/1.e5
```
