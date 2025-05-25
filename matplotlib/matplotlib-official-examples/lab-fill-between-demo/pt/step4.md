# Marcação Seletiva de Regiões Horizontais em Todos os Eixos

O mesmo mecanismo de seleção pode ser aplicado para preencher a altura vertical total dos eixos. Para ser independente dos limites de y, adicionamos uma transformação (transform) que interpreta os valores de x em coordenadas de dados e os valores de y em coordenadas de eixos. O exemplo a seguir marca as regiões em que os dados de y estão acima de um determinado limite (threshold).

```python
fig, ax = plt.subplots()
x = np.arange(0, 4 * np.pi, 0.01)
y = np.sin(x)
ax.plot(x, y, color='black')

threshold = 0.75
ax.axhline(threshold, color='green', lw=2, alpha=0.7)
ax.fill_between(x, 0, 1, where=y > threshold,
                color='green', alpha=0.5, transform=ax.get_xaxis_transform())
```
