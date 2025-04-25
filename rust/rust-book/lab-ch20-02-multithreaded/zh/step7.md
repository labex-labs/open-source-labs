# 验证 `new` 函数中线程数量的有效性

我们目前没有对`new`和`execute`函数的参数进行任何处理。让我们按照我们期望的行为来实现这些函数的主体。首先，来考虑一下`new`函数。之前我们为`size`参数选择了无符号类型，因为线程数量为负数的线程池是没有意义的。然而，线程数量为零的线程池同样没有意义，不过零是一个完全有效的`usize`值。我们将添加代码来检查`size`是否大于零，然后在返回`ThreadPool`实例之前，如果接收到零值就让程序恐慌，这可以通过使用`assert!`宏来实现，如清单 20-13 所示。

文件名：`src/lib.rs`

```rust
impl ThreadPool {
    /// 创建一个新的线程池。
    ///
    /// 大小是线程池中线程的数量。
    ///
  1 /// # 恐慌
    ///
    /// 如果大小为零，`new` 函数将恐慌。
    pub fn new(size: usize) -> ThreadPool {
      2 assert!(size > 0);

        ThreadPool
    }

    --snip--
}
```

清单 20-13：实现`ThreadPool::new`，使其在`size`为零时恐慌

我们还使用文档注释为`ThreadPool`添加了一些文档。注意，我们遵循了良好的文档编写规范，添加了一个部分来指出我们的函数可能恐慌的情况\[1\]，正如第 14 章所讨论的那样。尝试运行`cargo doc --open`并点击`ThreadPool`结构体，看看为`new`生成的文档是什么样子的！

我们也可以不像这里这样添加`assert!`宏\[2\]，而是将`new`改为`build`，并像我们在清单 12-9 的 I/O 项目中对`Config::build`所做的那样返回一个`Result`。但在这种情况下，我们决定尝试创建一个没有任何线程的线程池应该是一个不可恢复的错误。如果你有雄心壮志，可以尝试编写一个具有以下签名的名为`build`的函数，与`new`函数进行比较：

```rust
pub fn build(
    size: usize
) -> Result<ThreadPool, PoolCreationError> {
```
