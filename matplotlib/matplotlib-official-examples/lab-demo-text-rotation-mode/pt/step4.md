# Criar os subplots

Agora, criaremos os subplots usando a função `subplots`. Criaremos uma grade de subplots com a mesma proporção (aspect ratio), e removeremos os ticks dos eixos x e y. Também adicionaremos uma linha vertical e horizontal no centro de cada subplot para ajudar a visualizar o alinhamento.

```python
axs = fig.subplots(len(va_list), len(ha_list), sharex=True, sharey=True,
                   subplot_kw=dict(aspect=1),
                   gridspec_kw=dict(hspace=0, wspace=0))

for i, va in enumerate(va_list):
    for j, ha in enumerate(ha_list):
        ax = axs[i, j]
        ax.set(xticks=[], yticks=[])
        ax.axvline(0.5, color="skyblue", zorder=0)
        ax.axhline(0.5, color="skyblue", zorder=0)
        ax.plot(0.5, 0.5, color="C0", marker="o", zorder=1)
```
