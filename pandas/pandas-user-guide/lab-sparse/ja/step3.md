# SparseDtype の理解

`SparseDtype` は、非疎な値の dtype とスカラーの埋め値を格納します。dtype のみを渡すか、明示的な埋め値も渡すことで構築できます。

```python
# SparseDtype を作成
print(pd.SparseDtype(np.dtype('datetime64[ns]')))

# 明示的な埋め値を持つ SparseDtype を作成
print(pd.SparseDtype(np.dtype('datetime64[ns]'), fill_value=pd.Timestamp('2017-01-01')))
```
