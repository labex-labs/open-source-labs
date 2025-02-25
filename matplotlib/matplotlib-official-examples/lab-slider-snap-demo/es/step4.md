# Definir los valores permitidos para el deslizador de amplitud

En este paso, definirá los valores permitidos para el deslizador de amplitud. El deslizador de amplitud usará estos valores para ajustarse al valor permitido más cercano.

```python
# define the values to use for snapping
allowed_amplitudes = np.concatenate([np.linspace(.1, 5, 100), [6, 7, 8, 9]])
```
