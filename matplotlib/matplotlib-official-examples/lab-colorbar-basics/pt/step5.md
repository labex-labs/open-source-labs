# Criar um Gráfico com Dados Positivos e Negativos

Criamos um gráfico com dados positivos e negativos e adicionamos uma colorbar ao gráfico usando a função `colorbar`. Desta vez, especificamos os valores mínimo e máximo para a colorbar usando os parâmetros `vmin` e `vmax`.

```python
# Plot both positive and negative values between +/- 1.2
pos_neg_clipped = plt.imshow(Z, cmap='RdBu', vmin=-1.2, vmax=1.2,
                             interpolation='none')

# Add minorticks on the colorbar to make it easy to read the
# values off the colorbar.
cbar = plt.colorbar(pos_neg_clipped, extend='both')
cbar.minorticks_on()
```
