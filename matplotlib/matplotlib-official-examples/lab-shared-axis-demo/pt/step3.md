# Criar os Subplots

Podemos criar subplots usando o método `plt.subplot()`. Neste exemplo, criaremos três subplots, com o primeiro subplot ocupando a primeira linha e todas as três colunas, e o segundo e terceiro subplots ocupando a segunda e terceira linha, respectivamente, e compartilhando o eixo x com o primeiro subplot.

```python
ax1 = plt.subplot(311)
ax2 = plt.subplot(312, sharex=ax1)
ax3 = plt.subplot(313, sharex=ax1, sharey=ax1)
```
