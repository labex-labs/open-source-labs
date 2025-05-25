# Anotar o Gráfico

Agora, anotaremos o gráfico adicionando uma seta apontando para uma coordenada específica. Neste exemplo, adicionaremos uma seta apontando para o máximo local da função cosseno.

```python
ax.annotate('local max', xy=(2, 1), xytext=(3, 1.5),
            arrowprops=dict(facecolor='black', shrink=0.05),
            )
```

A função `ax.annotate()` recebe vários argumentos. O primeiro argumento é o texto que será exibido no gráfico. O argumento `xy` especifica as coordenadas do ponto que queremos anotar. O argumento `xytext` especifica as coordenadas do texto. O argumento `arrowprops` é um dicionário que especifica as propriedades da seta.
