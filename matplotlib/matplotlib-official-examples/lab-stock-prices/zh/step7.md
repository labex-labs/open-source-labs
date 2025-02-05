# 用各自的颜色分别绘制每只股票

```python
for nn, column in enumerate(stocks_ticker):
    # 用各自的颜色分别绘制每条线。
    # 不包括任何包含NaN的数据。
    good = np.nonzero(np.isfinite(stock_data[column]))
    line, = ax.plot(stock_data['Date'][good], stock_data[column][good], lw=2.5)

    # 在每条线的右端添加一个文本标签。下面的大部分代码
    # 是在添加特定的y轴位置偏移量，因为有些标签会重叠。
    y_pos = stock_data[column][-1]

    # 对于任何需要上下微调的文本，使用以点为单位的偏移变换。
    offset = y_offsets[column] / 72
    trans = mtransforms.ScaledTranslation(0, offset, fig.dpi_scale_trans)
    trans = ax.transData + trans

    # 同样，确保所有标签都足够大，以便查看者能够轻松阅读。
    ax.text(np.datetime64('2022-10-01'), y_pos, stocks_name[nn],
            color=line.get_color(), transform=trans)
```
