# チャートにラベルとタイトルを追加する

最後のステップは、チャートにラベルとタイトルを追加することです。チャートにタイトル、x 軸のラベル、およびチャートの凡例を追加します。

```python
ax.set_title('Cup height by group and beverage choice')
ax.set_xlabel('Group')
ax.legend()
ax.autoscale_view()
```
