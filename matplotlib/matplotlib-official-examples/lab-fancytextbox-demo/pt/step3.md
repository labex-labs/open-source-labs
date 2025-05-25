# Criar Outra Caixa de Texto

```python
plt.text(0.55, 0.6, "spam", size=50, rotation=-25.,
         ha="right", va="top",
         bbox=dict(boxstyle="square",
                   ec=(1., 0.5, 0.5),
                   fc=(1., 0.8, 0.8),
                   )
         )
```

Criamos outra caixa de texto contendo a palavra "spam". Desta vez, definimos o parâmetro `boxstyle` como "square" para criar uma caixa quadrada e definimos os parâmetros `ha` e `va` como "right" e "top" para alinhar o texto à direita e ao topo da caixa.
