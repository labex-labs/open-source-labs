# Criar o gráfico

Vamos criar um gráfico de linha simples com alguns rótulos y longos.

```python
fig, ax = plt.subplots()
ax.plot(range(10))
ax.set_yticks([2, 5, 7], labels=['really, really, really', 'long', 'labels'])
```
