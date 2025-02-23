# 一時ファイルとディレクトリ

このチャレンジでは、Go言語で一時ファイルとディレクトリを作成する必要があります。

## 要件

- `os.CreateTemp` を使用して一時ファイルを作成します。
- `os.MkdirTemp` を使用して一時ディレクトリを作成します。
- `os.RemoveAll` を使用して一時ディレクトリを削除します。
- `os.WriteFile` を使用してファイルにデータを書き込みます。

## 例

```sh
$ go run temporary-files-and-directories.go
Temp file name: /tmp/sample610887201
Temp dir name: /tmp/sampledir898854668
```
