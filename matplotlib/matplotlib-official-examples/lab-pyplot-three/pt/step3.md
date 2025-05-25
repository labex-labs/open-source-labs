# Plotar os Dados

Nesta etapa, usaremos a função `plot` do Matplotlib para plotar todos os três conjuntos de dados em uma única chamada. Usaremos traços vermelhos para o primeiro conjunto de dados, quadrados azuis para o segundo conjunto de dados e triângulos verdes para o terceiro conjunto de dados.

```python
plt.plot(t, t, 'r--', label='linear')
plt.plot(t, t**2, 'bs', label='quadratic')
plt.plot(t, t**3, 'g^', label='cubic')
plt.legend()
plt.show()
```
