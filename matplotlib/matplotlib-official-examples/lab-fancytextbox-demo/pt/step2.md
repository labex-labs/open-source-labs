# Criar uma Caixa de Texto

```python
plt.text(0.6, 0.7, "eggs", size=50, rotation=30.,
         ha="center", va="center",
         bbox=dict(boxstyle="round",
                   ec=(1., 0.5, 0.5),
                   fc=(1., 0.8, 0.8),
                   )
         )
```

Criamos uma caixa de texto contendo a palavra "eggs" usando o método `text()`. O parâmetro `bbox` é usado para estilizar a caixa. O parâmetro `boxstyle` é definido como "round" para criar uma caixa arredondada, enquanto os parâmetros `ec` e `fc` definem as cores da borda e do preenchimento da caixa, respectivamente. O parâmetro `size` define o tamanho da fonte, o parâmetro `rotation` define o ângulo de rotação e os parâmetros `ha` e `va` definem o alinhamento horizontal e vertical do texto na caixa.
