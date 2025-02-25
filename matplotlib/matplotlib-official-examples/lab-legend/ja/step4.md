# 凡例の追加

グラフに凡例を追加するには、Matplotlibの`legend`関数を使用します。凡例の位置を指定するために`loc`パラメータを渡し、凡例に影の効果を追加するために`shadow`パラメータを渡します。また、凡例のフォントサイズを設定するために`fontsize`パラメータも使用します。

```python
legend = ax.legend(loc='upper center', shadow=True, fontsize='x-large')
```
