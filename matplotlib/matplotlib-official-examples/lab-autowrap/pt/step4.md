# Controlando o Posicionamento e Estilo do Texto

Também podemos controlar o posicionamento e o estilo do texto em nosso gráfico Matplotlib. Tente adicionar o seguinte código ao seu script:

```python
plt.text(2, 8, "Top Left", fontsize=12, color='red')
plt.text(8, 8, "Top Right", fontsize=12, color='blue')
plt.text(2, 2, "Bottom Left", fontsize=12, color='green')
plt.text(8, 2, "Bottom Right", fontsize=12, color='purple')
```

Isso adicionará quatro elementos de texto ao nosso gráfico, cada um com uma cor, tamanho de fonte e posição diferentes.
