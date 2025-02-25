# 出力ディレクトリを作成する

このステップでは、サムネイルが保存される `thumbs` という名前のディレクトリを作成します。ディレクトリが既に存在する場合は、再度作成されません。

```python
outdir = Path("thumbs")
outdir.mkdir(parents=True, exist_ok=True)
```
