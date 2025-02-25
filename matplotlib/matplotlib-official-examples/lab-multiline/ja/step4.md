# 軸ラベルのカスタマイズ

軸ラベルをカスタマイズするには、`set_xlabel`関数と`set_ylabel`関数を使用できます。また、「\n」文字を使って改行も追加できます。

```python
ax0.set_xlabel('this is a xlabel\n(with newlines!)')
ax0.set_ylabel('this is vertical\ntest', multialignment='center')
```
