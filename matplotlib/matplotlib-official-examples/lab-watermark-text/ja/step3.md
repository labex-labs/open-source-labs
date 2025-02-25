# テキスト ウォーターマークを追加する

テキスト ウォーターマークを追加するには、`Figure` オブジェクトの `text()` メソッドを使用できます。位置、テキスト、およびフォント サイズ、色、透明度などのその他のプロパティを指定する必要があります。

```python
ax.text(0.5, 0.5, 'created with matplotlib', transform=ax.transAxes,
        fontsize=40, color='gray', alpha=0.5,
        ha='center', va='center', rotation=30)
```
