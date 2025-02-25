# 配列のデータ型の取得

配列のデータ型を決定するには、`dtype` 属性にアクセスできます。たとえば：

```python
z.dtype
# 配列 z の dtype を返します。これは uint8 になります
```

`dtype` オブジェクトには、ビット幅やバイトオーダーなど、型に関する情報も含まれています。型のプロパティを照会するために、たとえばそれが整数型であるかどうかを確認するために、`dtype` オブジェクトを使うことができます。たとえば：

```python
d = np.dtype(int)
# int 型用の dtype オブジェクトを作成します

np.issubdtype(d, np.integer)
# d が np.integer のサブタイプであることを示す True を返します

np.issubdtype(d, np.floating)
# d が np.floating のサブタイプでないことを示す False を返します
```
