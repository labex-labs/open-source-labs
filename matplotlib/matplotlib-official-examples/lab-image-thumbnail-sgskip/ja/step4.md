# ディレクトリを検証する

このステップでは、指定されたディレクトリが存在するかどうかを確認します。ディレクトリが存在しない場合、プログラムを終了してエラーメッセージを表示します。

```python
if not args.imagedir.is_dir():
    sys.exit(f"Could not find input directory {args.imagedir}")
```
