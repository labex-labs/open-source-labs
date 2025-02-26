# 予期されるエラーを伴う単体テスト

例外をチェックする単体テストを書きたいとしましょう。以下がその方法です。

```python
class TestStock(unittest.TestCase):
  ...
    def test_bad_shares(self):
        s = stock.Stock('GOOG', 100, 490.1)
        with self.assertRaises(TypeError):
             s.shares = '50'
  ...
```

このテストを参考にして、以下の失敗モードに対する単体テストを書きましょう。

- `shares` を文字列に設定すると `TypeError` が発生することをテストする
- `shares` を負の数に設定すると `ValueError` が発生することをテストする
- `price` を文字列に設定すると `TypeError` が発生することをテストする
- `price` を負の数に設定すると `ValueError` が発生することをテストする
- 存在しない属性 `share` を設定すると `AttributeError` が発生することをテストする

完了したときには合計で約一打の単体テストが必要になります。

**重要な注意事項**

このコースの後の使用のために、完全に機能する `stock.py` と `teststock.py` ファイルが必要になります。必要に応じて作業中の内容を保存してくださいが、この時点でまだ問題がある場合は、`Solutions/5_6` からコードをコピーすることを強くお勧めします。

後で `Stock` コードを改善するためのツールとして `teststock.py` ファイルを使用する予定です。新しいコードが古いコードと同じように動作することを確認するために、それを手元に置いておく必要があります。
