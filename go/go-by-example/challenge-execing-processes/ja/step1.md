# プロセスの実行

問題は、現在の Go プロセスを別のプロセス（たとえば非 Go プロセス）に置き換えることです。

## 要件

- Go プログラミング言語
- Go の `exec` 関数の基本的な知識
- 環境変数に慣れていること

## 例

```sh
# 私たちのプログラムを実行すると、`ls` に置き換えられます。
$ go run execing-processes.go
total 16
drwxr-xr-x 4 mark 136B Oct 3 16:29.
drwxr-xr-x 91 mark 3.0K Oct 3 12:50..
-rw-r--r-- 1 mark 1.3K Oct 3 16:28 execing-processes.go

# 注：Go には古典的な Unix の `fork` 関数はありません。
# 通常は問題になりませんが、goroutine を起動したり、プロセスを生成したり、プロセスを実行したりすることで、
# ほとんどの `fork` のユースケースがカバーされます。
```
