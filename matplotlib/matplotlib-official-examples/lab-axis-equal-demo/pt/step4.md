# Ajustar os limites do gráfico enquanto mantém a proporção de aspecto de eixo igual

Também podemos ajustar os limites do gráfico enquanto mantemos a proporção de aspecto de eixo igual.

```python
axs[1, 0].plot(3 * np.cos(an), 3 * np.sin(an))
axs[1, 0].axis('equal')
axs[1, 0].set(xlim=(-3, 3), ylim=(-3, 3))
axs[1, 0].set_title('still a circle, even after changing limits', fontsize=10)
```

O gráfico resultante mostrará um círculo que ainda é proporcional, mesmo depois de alterarmos os limites.
