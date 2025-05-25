# Salvar o gráfico

Finalmente, podemos salvar nosso gráfico no disco. Siga estes passos:

1. Imprima os formatos de arquivo suportados usando `print(fig.canvas.get_supported_filetypes())`.

```python
print(fig.canvas.get_supported_filetypes())
```

2. Salve a figura como um arquivo de imagem usando `fig.savefig(file_path, transparent=False, dpi=80, bbox_inches="tight")`. Descomente esta linha para salvar a figura.

```python
fig.savefig('sales.png', transparent=False, dpi=80, bbox_inches="tight")
```

Você pode abrir o arquivo de imagem salvo usando o explorador de arquivos na barra lateral esquerda.
