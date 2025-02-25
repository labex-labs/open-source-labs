# 線のプロパティのカスタマイズ

Matplotlib を使えば、線幅、破線スタイル、色など、様々な線のプロパティをカスタマイズできます。線のプロパティを設定するいくつかの方法を示しましょう。

```python
x = np.arange(0, 5, 0.1)
line, = plt.plot(x, np.sin(x), '-')

# Using the Line2D instance's setter method
line.set_linewidth(2.0)  # Set the linewidth property of the line to 2.0

# Using the pyplot.setp function
plt.setp(line, color='r', linewidth=2.0)  # Set the color and linewidth properties using the setp function

plt.show()
```

解説:

- 配列 `x` を作成し、`np.sin` 関数を使って対応する y 値を計算します。
- `plot` 関数を呼び出して線グラフを作成します。
- `Line2D` インスタンスの `set` メソッドを使って、線の線幅プロパティを 2.0 に設定します。
- あるいは、`setp` 関数を使って、キーワード引数を使って線の色や線幅などの複数のプロパティを設定できます。
