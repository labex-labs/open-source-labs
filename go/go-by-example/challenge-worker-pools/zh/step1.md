# 工作池

实现一个工作池，它通过 `jobs` 通道接收任务，并通过 `results` 通道发送相应的结果。工作池应该有多个并发实例，并且每个工作线程应该为每个任务休眠一秒，以模拟耗时的任务。

## 要求

- 使用 Go 协程和通道来实现工作池。
- 工作池应该有多个并发实例。
- 每个工作线程应该为每个任务休眠一秒，以模拟耗时的任务。
- 工作池应该通过 `jobs` 通道接收任务，并通过 `results` 通道发送相应的结果。

## 示例

```sh
# 我们运行的程序展示了 5 个任务由不同的工作线程执行。尽管总工作量约为 5 秒，但程序仅耗时约 2 秒，因为有 3 个工作线程并发运行。
$ time go run worker-pools.go
worker 1 started job 1
worker 2 started job 2
worker 3 started job 3
worker 1 finished job 1
worker 1 started job 4
worker 2 finished job 2
worker 2 started job 5
worker 3 finished job 3
worker 1 finished job 4
worker 2 finished job 5

real 0m2.358s
```
