# `panic!`

`panic!` 宏可用于引发恐慌并开始展开堆栈。在展开堆栈的过程中，运行时会通过调用线程所有对象的析构函数来释放该线程所 **拥有** 的所有资源。

由于我们处理的是单线程程序，`panic!` 将导致程序报告恐慌消息并退出。

```rust
// 整数除法 (/) 的重新实现
fn division(dividend: i32, divisor: i32) -> i32 {
    if divisor == 0 {
        // 除零操作会触发恐慌
        panic!("division by zero");
    } else {
        dividend / divisor
    }
}

// `main` 任务
fn main() {
    // 在堆上分配的整数
    let _x = Box::new(0i32);

    // 此操作将触发任务失败
    division(3, 0);

    println!("This point won't be reached!");

    // `_x` 此时应被销毁
}
```

让我们检查一下 `panic!` 不会导致内存泄漏。

```{=html}
<!-- REUSE-IgnoreStart -->
```

```{=html}
<!-- 防止 REUSE 解析示例代码中的版权声明 -->
```

```shell
$ rustc panic.rs && valgrind./panic
==4401== Memcheck, a memory error detector
==4401== Copyright (C) 2002-2013, and GNU GPL'd, by Julian Seward et al.
==4401== Using Valgrind-3.10.0.SVN and LibVEX; rerun with -h for copyright info
==4401== Command:./panic
==4401==
thread '<main>' panicked at 'division by zero', panic.rs:5
==4401==
==4401== HEAP SUMMARY:
==4401==     in use at exit: 0 bytes in 0 blocks
==4401==   total heap usage: 18 allocs, 18 frees, 1,648 bytes allocated
==4401==
==4401== All heap blocks were freed -- no leaks are possible
==4401==
==4401== For counts of detected and suppressed errors, rerun with: -v
==4401== ERROR SUMMARY: 0 errors from 0 contexts (suppressed: 0 from 0)
```

```{=html}
<!-- REUSE-IgnoreEnd -->
```
