# Matplotlibにカスタムボックススタイルを登録する

クラスとしてカスタムボックススタイルを実装したら、Matplotlibに登録できます。これにより、ボックススタイルを文字列として指定できます。`bbox=dict(boxstyle="登録名,param=値,...",...)` です。

```python
BoxStyle._style_list["angled"] = MyStyle  # カスタムスタイルを登録します。
```
