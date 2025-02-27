# カーネル密度推定器をフィットさせる

次に、`KernelDensity` 推定器のインスタンスを作成して、データにフィットさせます。推定器のカーネルの種類とバンド幅を選ぶことができます。たとえば、ガウスカーネルを使用してバンド幅を0.2に設定することができます。

```python
kde = KernelDensity(kernel='gaussian', bandwidth=0.2).fit(X)
```
