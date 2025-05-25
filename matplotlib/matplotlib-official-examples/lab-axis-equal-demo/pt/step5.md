# Auto-ajustar os limites dos dados para a proporção de aspecto de eixo igual

Também podemos usar a função `set_aspect('equal', 'box')` para auto-ajustar os limites dos dados para a proporção de aspecto de eixo igual.

```python
axs[1, 1].plot(3 * np.cos(an), 3 * np.sin(an))
axs[1, 1].set_aspect('equal', 'box')
axs[1, 1].set_title('still a circle, auto-adjusted data limits', fontsize=10)
```

O gráfico resultante mostrará um círculo que ainda é proporcional e visualmente atraente.
