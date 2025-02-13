# 派生进程

本挑战要求实现一个 Go 程序，该程序派生外部进程并收集其输出。

## 要求

- 程序应能够派生外部进程。
- 程序应能够收集外部进程的输出。
- 程序应处理外部进程执行期间可能出现的错误。

## 示例

```sh
# 派生的程序返回的输出与我们直接从命令行运行它们时相同。
$ go run spawning-processes.go
> date
2022年5月5日 星期四 晚上10:10:12 太平洋夏令时

# date 没有 `-x` 标志，因此它将以错误消息和非零返回码退出。
命令以 rc = 1 退出
hello > grep
hello grep

-a > ls -l -h
drwxr-xr-x 4 mark 136B 10月3日 16:29.
drwxr-xr-x 91 mark 3.0K 10月3日 12:50..
-rw-r--r-- 1 mark 1.3K 10月3日 16:28 spawning-processes.go
```
