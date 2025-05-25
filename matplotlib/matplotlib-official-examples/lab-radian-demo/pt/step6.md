# Adicionar rótulos e ajustar o layout

Adicione um título e rótulos de eixo aos subplots usando as funções `title`, `xlabel` e `ylabel` de `matplotlib.pyplot`. Ajuste o layout dos subplots usando a função `tight_layout`.

```python
axs[0].set_title('Cosseno com Eixo X em Radianos')
axs[0].set_xlabel('Radianos')
axs[0].set_ylabel('Cosseno')
axs[1].set_title('Cosseno com Eixo X em Graus')
axs[1].set_xlabel('Graus')
axs[1].set_ylabel('Cosseno')
fig.tight_layout()
```
