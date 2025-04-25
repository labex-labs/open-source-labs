# サブフィギュアをカスタマイズする

Matplotlib に用意されているさまざまな関数を使って、サブフィギュアをカスタマイズできます。たとえば、`set_title()` と `set_xlabel()` / `set_ylabel()` を使ってタイトルと軸ラベルを設定できます。

```python
ax1.set_title('Subfigure 1')
ax1.set_xlabel('X Label')
ax1.set_ylabel('Y Label')

ax2.set_title('Subfigure 2')
ax2.set_xlabel('X Label')
ax2.set_ylabel('Y Label')
```

これにより、各サブフィギュアのタイトルと軸ラベルが設定されます。
