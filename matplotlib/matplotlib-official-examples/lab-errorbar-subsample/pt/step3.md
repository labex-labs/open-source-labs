# Subamostrar a Cada 6ª Barra de Erro

Agora, vamos aplicar a subamostragem de barras de erro para plotar apenas a cada 6ª barra de erro. Podemos fazer isso usando o parâmetro `errorevery` da função `errorbar`.

```python
fig, ax = plt.subplots()

ax.set_title('A Cada 6ª Barra de Erro')
ax.errorbar(x, y1, yerr=y1err, errorevery=6, label='y1')
ax.errorbar(x, y2, yerr=y2err, errorevery=6, label='y2')

ax.legend()
plt.show()
```
