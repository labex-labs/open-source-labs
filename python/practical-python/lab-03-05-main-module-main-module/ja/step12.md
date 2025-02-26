# スクリプトのテンプレート

最後に、コマンドラインスクリプトとして実行される Python プログラムの一般的なコードテンプレートを示します。

```python
#!/usr/bin/env python3
#./prog.py

# インポート文（ライブラリ）
import modules

# 関数
def spam():
  ...

def blah():
  ...

# メイン関数
def main(argv):
    # コマンドライン引数、環境などを解析する
  ...

if __name__ == '__main__':
    import sys
    main(sys.argv)
```
