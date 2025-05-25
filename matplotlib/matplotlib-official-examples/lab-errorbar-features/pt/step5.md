# Plotar Variável, Barras de Erro Assimétricas

Em seguida, plotaremos nossos dados com barras de erro variáveis e assimétricas. A função `ax.errorbar()` é usada novamente, mas desta vez o parâmetro `xerr` é usado para especificar os valores de erro assimétricos.

```python
# plot variable, asymmetric error bars
fig, ax = plt.subplots()
ax.errorbar(x, y, xerr=asymmetric_error, fmt='o')
ax.set_title('Variable, Asymmetric Error Bars')
plt.show()
```
