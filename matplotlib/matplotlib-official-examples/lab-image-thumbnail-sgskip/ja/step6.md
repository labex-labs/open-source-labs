# サムネイルを生成する

このステップでは、指定されたディレクトリ内のすべての画像に対してサムネイルを生成します。指定されたディレクトリ内の `.png` 拡張子を持つすべての画像を for ループで反復処理します。各画像に対して、サムネイルを生成して `thumbs` ディレクトリに保存します。

```python
for path in args.imagedir.glob("*.png"):
    outpath = outdir / path.name
    fig = image.thumbnail(path, outpath, scale=0.15)
    print(f"saved thumbnail of {path} to {outpath}")
```
