# waitgroups

このチャレンジで解決する問題は、複数の goroutine を起動し、それぞれに対して WaitGroup のカウンターをインクリメントすることです。その後、起動したすべての goroutine が終了するのを待つ必要があります。

## 要件

- Golang の基本的な知識。
- Golang における並列処理の理解。
- `sync` パッケージに慣れていること。

## 例

```sh
$ go run waitgroups.go
Worker 5 starting
Worker 3 starting
Worker 4 starting
Worker 1 starting
Worker 2 starting
Worker 4 done
Worker 1 done
Worker 2 done
Worker 5 done
Worker 3 done

# 各起動時における worker の起動と終了の順序は
# おそらく異なります。
```
