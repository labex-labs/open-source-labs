# Criar o Gráfico

Agora, criaremos o gráfico usando a função `subplots` do Matplotlib. Criaremos dois subplots, um para linhas verticais e outro para linhas horizontais. Definiremos o tamanho da figura como (12, 6) para melhor visibilidade.

```python
# Create the plot
fig, (vax, hax) = plt.subplots(1, 2, figsize=(12, 6))
```
