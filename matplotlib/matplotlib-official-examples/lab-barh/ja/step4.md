# データを準備する

このステップでは、グラフ用のデータを準備します。人々の名前、彼らのパフォーマンス、およびエラー率のリストを作成します。

```python
people = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim')
y_pos = np.arange(len(people))
performance = 3 + 10 * np.random.rand(len(people))
error = np.random.rand(len(people))
```
