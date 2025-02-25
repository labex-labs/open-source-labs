# Z軸をカスタマイズする

```python
ax.set_zlim(-1.01, 1.01)
ax.zaxis.set_major_locator(LinearLocator(10))
# A StrMethodFormatter is used automatically
ax.zaxis.set_major_formatter('{x:.02f}')
```

`set_zlim()` 関数を使ってZ軸の範囲を -1.01 から 1.01 に設定することで、Z軸をカスタマイズします。次に、`set_major_locator()` 関数を使って、`LinearLocator(10)` を使ってZ軸の目盛りの数を 10 に設定します。最後に、`set_major_formatter()` 関数を使って、`StrMethodFormatter` を使ってZ軸の目盛りのラベルをフォーマットします。
