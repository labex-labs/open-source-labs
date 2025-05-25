# 각 스타일 시트에 대한 데모 그림 플롯

마지막으로, 사용 가능한 각 스타일 시트에 대한 데모 그림을 플롯해야 합니다. `style_list`를 반복하고 각 스타일 시트에 대해 `plot_figure()` 함수를 호출하여 이 작업을 수행할 수 있습니다.

```python
if __name__ == "__main__":

    # Set up a list of all available styles, in alphabetical order but
    # the `default` and `classic` ones, which will be forced resp. in
    # first and second position.
    # styles with leading underscores are for internal use such as testing
    # and plot types gallery. These are excluded here.
    style_list = ['default', 'classic'] + sorted(
        style for style in plt.style.available
        if style != 'classic' and not style.startswith('_'))

    # Plot a demonstration figure for every available style sheet.
    for style_label in style_list:
        with plt.rc_context({"figure.max_open_warning": len(style_list)}):
            with plt.style.context(style_label):
                plot_figure(style_label=style_label)

    plt.show()
```
