# 閾値の定義

```python
x_values = np.arange(0.4, 1.05, 0.05)
x_values = np.append(x_values, 0.99999)
```

0.4 から 1 までの範囲で、0.05 の刻み幅で閾値の配列を定義します。その後、0.99999 という非常に高い閾値を追加して、自己ラベル付きのサンプルが生成されない閾値を含めるようにします。
