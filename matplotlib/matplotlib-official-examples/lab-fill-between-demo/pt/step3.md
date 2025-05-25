# Preenchimento Seletivo de Regiões Horizontais

O parâmetro _where_ permite especificar os intervalos de x a serem preenchidos. É uma matriz booleana com o mesmo tamanho de _x_. Apenas os intervalos de x de sequências _True_ contíguas são preenchidos. Como resultado, o intervalo entre valores _True_ e _False_ vizinhos nunca é preenchido. Portanto, é recomendado definir `interpolate=True`, a menos que a distância x dos pontos de dados seja suficientemente fina para que o efeito acima não seja perceptível.

```python
x = np.array([0, 1, 2, 3])
y1 = np.array([0.8, 0.8, 0.2, 0.2])
y2 = np.array([0, 0, 1, 1])

fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)

ax1.set_title('interpolation=False')
ax1.plot(x, y1, 'o--')
ax1.plot(x, y2, 'o--')
ax1.fill_between(x, y1, y2, where=(y1 > y2), color='C0', alpha=0.3)
ax1.fill_between(x, y1, y2, where=(y1 < y2), color='C1', alpha=0.3)

ax2.set_title('interpolation=True')
ax2.plot(x, y1, 'o--')
ax2.plot(x, y2, 'o--')
ax2.fill_between(x, y1, y2, where=(y1 > y2), color='C0', alpha=0.3,
                 interpolate=True)
ax2.fill_between(x, y1, y2, where=(y1 <= y2), color='C1', alpha=0.3,
                 interpolate=True)
fig.tight_layout()
```
