# Usando Valores Ausentes e de Preenchimento

Os argumentos `missing_values` e `filling_values` são usados para lidar com dados ausentes. O argumento `missing_values` é usado para reconhecer dados ausentes, e o argumento `filling_values` é usado para fornecer um valor para as entradas ausentes.

```python
np.genfromtxt(StringIO(data), missing_values="N/A", filling_values=0)
```
