# 疑似データを作成する

次に、プロットに使用する疑似データを作成します。0.01から10.0までの値の配列を0.01のステップで作成するために`numpy.arange`を使用します。その後、`numpy.exp`と`numpy.sin`を使用して2セットのデータを作成します。

```python
# Create some mock data
t = np.arange(0.01, 10.0, 0.01)
data1 = np.exp(t)
data2 = np.sin(2 * np.pi * t)
```
