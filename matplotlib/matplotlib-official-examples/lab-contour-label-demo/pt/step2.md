# Criando rótulos de contorno com formatadores de nível personalizados

Agora criaremos rótulos de contorno com formatadores de nível personalizados. Isso nos permitirá formatar os rótulos de uma maneira específica. Neste caso, removeremos zeros à direita e adicionaremos um sinal de porcentagem.

```python
def fmt(x):
    s = f"{x:.1f}"
    if s.endswith("0"):
        s = f"{x:.0f}"
    return rf"{s} \%" if plt.rcParams["text.usetex"] else f"{s} %"

fig, ax = plt.subplots()
CS = ax.contour(X, Y, Z)
ax.clabel(CS, CS.levels, inline=True, fmt=fmt, fontsize=10)
```
