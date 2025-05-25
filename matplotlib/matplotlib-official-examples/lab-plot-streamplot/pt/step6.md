# Controlando Pontos de Partida

Nesta etapa, criaremos um streamplot com pontos de partida controlados. O parâmetro `start_points` recebe um array 2D que representa os pontos de partida das linhas de fluxo (streamlines).

```python
seed_points = np.array([[-2, -1, 0, 1, 2, -1], [-2, -1, 0, 1, 2, 2]])

strm = plt.streamplot(X, Y, U, V, color=U, linewidth=2,
                      cmap='autumn', start_points=seed_points.T)
plt.colorbar(strm.lines)
plt.title('Controlling Starting Points')
plt.plot(seed_points[0], seed_points[1], 'bo')
plt.xlim(-w, w)
plt.ylim(-w, w)
plt.show()
```
