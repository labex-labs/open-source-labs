# Gerando um Gráfico Simples

Para começar, vamos gerar um gráfico simples usando a função `plot` em `pyplot`. Neste exemplo, vamos plotar um gráfico de linha com os valores y `[1, 2, 3, 4]`:

```python
import matplotlib.pyplot as plt

plt.plot([1, 2, 3, 4])
plt.ylabel('some numbers')
plt.show()
```

Explicação:

- Importamos o módulo `pyplot` de `matplotlib` e o apelidamos como `plt`.
- A função `plot` é usada para gerar um gráfico de linha. Ao fornecer uma única lista de valores y, os valores x são gerados automaticamente como `[0, 1, 2, 3]`, uma vez que os intervalos do Python começam com 0.
- A função `ylabel` define o rótulo para o eixo y.
- Finalmente, a função `show` exibe o gráfico.
