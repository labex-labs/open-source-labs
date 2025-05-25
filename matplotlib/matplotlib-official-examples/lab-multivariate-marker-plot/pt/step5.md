# Criar Gráfico

Nesta etapa, você criará o gráfico usando os dados aleatórios gerados anteriormente. Especificamente, você plotará cada ponto de dados como um marcador com o símbolo de sucesso determinado pela variável de sucesso, o tamanho determinado pela variável de habilidade (skill), a rotação determinada pela variável ângulo de lançamento (take-off angle) e a cor determinada pela variável impulso (thrust).

```python
fig, ax = plt.subplots()
fig.suptitle("Throwing success", size=14)
for skill, takeoff, thrust, mood, pos in data:
    t = Affine2D().scale(skill).rotate_deg(takeoff)
    m = MarkerStyle(SUCCESS_SYMBOLS[mood], transform=t)
    ax.plot(pos[0], pos[1], marker=m, color=cmap(thrust))
fig.colorbar(plt.cm.ScalarMappable(norm=Normalize(0, 1), cmap=cmap),
             ax=ax, label="Normalized Thrust [a.u.]")
ax.set_xlabel("X position [m]")
ax.set_ylabel("Y position [m]")
```
