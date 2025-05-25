# Deslocar a Segunda Série em 3

Em alguns casos, podemos querer aplicar a subamostragem de barras de erro a diferentes partes de nossos dados. Podemos fazer isso especificando uma tupla para o parâmetro `errorevery`. Por exemplo, vamos aplicar a subamostragem de barras de erro à segunda série, mas deslocá-la em 3 pontos de dados.

```python
fig, ax = plt.subplots()

ax.set_title('Segunda Série Deslocada em 3')
ax.errorbar(x, y1, yerr=y1err, label='y1')
ax.errorbar(x, y2, yerr=y2err, errorevery=(3, 6), label='y2')

ax.legend()
plt.show()
```
