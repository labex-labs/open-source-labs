# 各スタイルシートに対するデモ用のグラフをプロットする

最後に、利用可能な各スタイルシートに対してデモ用のグラフをプロットする必要があります。これは、`style_list`をループして各スタイルシートに対して`plot_figure()`関数を呼び出すことで行うことができます。

```python
if __name__ == "__main__":

    # Set up a list of all available styles, in alphabetical order but
    # the `default` and `classic` ones, which will be forced resp. in
    # first and second position.
    # styles with leading underscores are for internal use such as testing
    # and plot types gallery. These are excluded here.
    style_list = ['default', 'classic'] + sorted(
        style for style in plt.style.available
        if style!= 'classic' and not style.startswith('_'))

    # Plot a demonstration figure for every available style sheet.
    for style_label in style_list:
        with plt.rc_context({"figure.max_open_warning": len(style_list)}):
            with plt.style.context(style_label):
                plot_figure(style_label=style_label)

    plt.show()
```
