# Implementar um estilo de caixa personalizado como uma classe

Estilos de caixa personalizados também podem ser implementados como classes que implementam `__call__`. As classes podem então ser registradas no dicionário `BoxStyle._style_list`, o que permite especificar o estilo da caixa como uma string, `bbox=dict(boxstyle="registered_name,param=value,...", ...)`.

```python
class MyStyle:
    """Uma caixa simples."""

    def __init__(self, pad=0.3):
        """
        Os argumentos devem ser floats e ter valores padrão.

        Parâmetros
        ----------
        pad : float
            Quantidade de preenchimento (padding).
        """
        self.pad = pad
        super().__init__()

    def __call__(self, x0, y0, width, height, mutation_size):
        """
        Dada a localização e o tamanho da caixa, retorna o caminho da caixa
        ao redor dela.

        A rotação é automaticamente tratada.

        Parâmetros
        ----------
        x0, y0, width, height : float
            Localização e tamanho da caixa.
        mutation_size : float
            Escala de referência para a mutação, tipicamente o tamanho da fonte do texto.
        """
        # padding
        pad = mutation_size * self.pad
        # largura e altura com padding adicionado
        width = width + 2.*pad
        height = height + 2.*pad
        # limite da caixa com padding
        x0, y0 = x0 - pad, y0 - pad
        x1, y1 = x0 + width, y0 + height
        # retorna o novo caminho
        return Path([(x0, y0),
                     (x1, y0), (x1, y1), (x0, y1),
                     (x0-pad, (y0+y1)/2.), (x0, y0),
                     (x0, y0)],
                    closed=True)


BoxStyle._style_list["angled"] = MyStyle  # Registrar o estilo personalizado.

fig, ax = plt.subplots(figsize=(3, 3))
ax.text(0.5, 0.5, "Test", size=30, va="center", ha="center", rotation=30,
        bbox=dict(boxstyle="angled,pad=0.5", alpha=0.2))

del BoxStyle._style_list["angled"]  # Remover o registro.

plt.show()
```
