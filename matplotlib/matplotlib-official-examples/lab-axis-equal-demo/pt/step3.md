# Plotar um círculo com proporção de aspecto de eixo igual

Para definir a proporção de aspecto de eixo igual, podemos usar a função `axis('equal')`.

```python
axs[0, 1].plot(3 * np.cos(an), 3 * np.sin(an))
axs[0, 1].axis('equal')
axs[0, 1].set_title('equal, looks like circle', fontsize=10)
```

O gráfico resultante mostrará um círculo que é proporcional e visualmente atraente.
