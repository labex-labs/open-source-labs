# ヒストグラムに垂直線を追加する

しきい値処理の効果をより明確に見るために、ヒストグラムに垂直線を追加して、現在のしきい値を示します。下限と上限のしきい値にそれぞれ2本の線を作成します。

```python
lower_limit_line = axs[1].axvline(slider.val[0], color='k')
upper_limit_line = axs[1].axvline(slider.val[1], color='k')
```
