# ロギングの設定

ロギングの動作は別途設定されます。

```python
# main.py

...

if __name__ == '__main__':
    import logging
    logging.basicConfig(
        filename  = 'app.log',      # ログ出力ファイル
        level     = logging.INFO,   # 出力レベル
    )
```

通常、これはプログラム起動時の一度だけの設定です。設定は、ロギング呼び出しを行うコードとは別です。
