# ディレクトリ

現在の作業ディレクトリに新しいサブディレクトリを作成し、親ディレクトリを含むディレクトリ階層を作成し、ディレクトリのコンテンツを一覧表示し、現在の作業ディレクトリを変更し、再帰的にディレクトリを訪問する Go プログラムを作成します。

## 要件

- 現在の作業ディレクトリに新しいサブディレクトリを作成する。
- 一時ディレクトリを作成する際は、削除処理を`defer`で行うのが良い。`os.RemoveAll`は、コマンドラインの`rm -rf`と同じように、ディレクトリツリー全体を削除する。
- `MkdirAll`を使って、親ディレクトリを含むディレクトリ階層を作成する。これはコマンドラインの`mkdir -p`に似ている。
- `ReadDir`はディレクトリのコンテンツを一覧表示し、`os.DirEntry`オブジェクトのスライスを返す。
- `Chdir`を使って、現在の作業ディレクトリを変更でき、`cd`と同じように動作する。
- 再帰的にディレクトリを訪問し、そのサブディレクトリすべてを含める。`Walk`は、訪問される各ファイルまたはディレクトリを処理するためのコールバック関数を受け取る。

## 例

```sh
$ go run directories.go
Listing subdir/parent
child true
file2 false
file3 false
Listing subdir/parent/child
file4 false
Visiting subdir
subdir true
subdir/file1 false
subdir/parent true
subdir/parent/child true
subdir/parent/child/file4 false
subdir/parent/file2 false
subdir/parent/file3 false
```
