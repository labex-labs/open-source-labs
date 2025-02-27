# `panic!`

`panic!` マクロは、パニックを発生させ、スタックをアンワインドし始めるために使用できます。アンワインド中、ランタイムは、そのすべてのオブジェクトのデストラクタを呼び出すことによって、スレッドが所有するすべてのリソースを解放することを担当します。

1 つのスレッドのみを持つプログラムを扱っているため、`panic!` はプログラムにパニック メッセージを報告させて終了させます。

```rust
// 整数除算 (/) の再実装
fn division(dividend: i32, divisor: i32) -> i32 {
    if divisor == 0 {
        // ゼロ除算はパニックを引き起こします
        panic!("division by zero");
    } else {
        dividend / divisor
    }
}

// `main` タスク
fn main() {
    // ヒープ上に割り当てられた整数
    let _x = Box::new(0i32);

    // この操作はタスクの失敗を引き起こします
    division(3, 0);

    println!("This point won't be reached!");

    // この時点で `_x` は破棄されるはずです
}
```

`panic!` がメモリ リークを起こさないことを確認しましょう。

```{=html}
<!-- REUSE-IgnoreStart -->
```

```{=html}
<!-- Prevent REUSE from parsing the copyright statement in the sample code -->
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
