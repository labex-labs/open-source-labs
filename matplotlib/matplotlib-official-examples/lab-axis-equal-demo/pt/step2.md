# Plotar um círculo com proporção de aspecto de eixo desigual

Primeiramente, plotaremos um círculo com uma proporção de aspecto de eixo desigual para demonstrar a importância de definir proporções de aspecto de eixo iguais.

```python
an = np.linspace(0, 2 * np.pi, 100)
fig, axs = plt.subplots(2, 2)

axs[0, 0].plot(3 * np.cos(an), 3 * np.sin(an))
axs[0, 0].set_title('not equal, looks like ellipse', fontsize=10)
```

O gráfico resultante mostrará um círculo que parece alongado devido à proporção de aspecto de eixo desigual.
