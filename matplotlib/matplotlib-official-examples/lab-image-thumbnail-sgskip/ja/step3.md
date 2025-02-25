# 引数を解析する

このステップでは、プログラムに渡された引数を解析します。`ArgumentParser` オブジェクトを作成し、`imagedir` という名前の引数を追加する必要があります。この引数は、画像が含まれるディレクトリのパスを指定します。引数のデータ型を指定するために `type` パラメータを使用できます。この場合、引数は `Path` 型でなければなりません。

```python
parser = ArgumentParser(description="Build thumbnails of all images in a directory.")
parser.add_argument("imagedir", type=Path)
args = parser.parse_args()
```
