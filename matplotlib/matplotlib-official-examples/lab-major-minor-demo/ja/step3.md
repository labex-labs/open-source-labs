# 主目盛りと副目盛りの設定

```python
# Set the major locator
ax.xaxis.set_major_locator(MultipleLocator(20))
# Set the major formatter
ax.xaxis.set_major_formatter('{x:.0f}')
# Set the minor locator
ax.xaxis.set_minor_locator(MultipleLocator(5))
```

ここでは、主目盛りの位置を 20 の倍数で設定し、主目盛りを".0f"形式でラベル付けするための主目盛りのフォーマッタを設定し、副目盛りの位置を 5 の倍数で設定する副目盛りを設定します。
