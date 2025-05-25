# Plotar a figura de demonstração para cada folha de estilo

Finalmente, você precisa plotar a figura de demonstração para cada folha de estilo disponível. Você pode fazer isso iterando sobre a `style_list` e chamando a função `plot_figure()` para cada folha de estilo.

```python
if __name__ == "__main__":

    # Configura uma lista de todos os estilos disponíveis, em ordem alfabética, mas
    # os estilos `default` e `classic`, que serão forçados, respectivamente, na
    # primeira e segunda posições.
    # estilos com sublinhados no início são para uso interno, como testes
    # e galeria de tipos de plotagem. Estes são excluídos aqui.
    style_list = ['default', 'classic'] + sorted(
        style for style in plt.style.available
        if style != 'classic' and not style.startswith('_'))

    # Plota uma figura de demonstração para cada folha de estilo disponível.
    for style_label in style_list:
        with plt.rc_context({"figure.max_open_warning": len(style_list)}):
            with plt.style.context(style_label):
                plot_figure(style_label=style_label)

    plt.show()
```
