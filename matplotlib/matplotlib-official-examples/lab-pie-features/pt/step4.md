# Adicionando Rótulos às Fatias

Podemos adicionar rótulos às fatias passando uma lista de rótulos para o parâmetro `labels` da função `pie()`.

```python
fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct='%1.1f%%')
```
