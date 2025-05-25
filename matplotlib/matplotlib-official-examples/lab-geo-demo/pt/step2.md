# Criar uma figura e subplots

Nesta etapa, criaremos uma figura e quatro subplots para cada uma das projeções que criaremos. Usaremos o método `plt.subplots()` para criar uma figura e subplots.

```python
fig, axs = plt.subplots(nrows=2, ncols=2, subplot_kw={'projection': 'aitoff'})
```
