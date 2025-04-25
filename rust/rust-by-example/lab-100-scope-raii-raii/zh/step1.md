# RAII

Rust 中的变量不仅仅是在栈中保存数据：它们还“拥有”资源，例如 `Box<T>` 拥有堆中的内存。Rust 强制实施 RAII（资源获取即初始化），所以每当一个对象超出作用域时，它的析构函数就会被调用，其拥有的资源也会被释放。

这种行为可以防止“资源泄漏”错误，所以你再也不必手动释放内存或担心内存泄漏了！下面是一个快速展示：

```rust
// raii.rs
fn create_box() {
    // 在堆上分配一个整数
    let _box1 = Box::new(3i32);

    // `_box1` 在此处被销毁，内存被释放
}

fn main() {
    // 在堆上分配一个整数
    let _box2 = Box::new(5i32);

    // 一个嵌套作用域：
    {
        // 在堆上分配一个整数
        let _box3 = Box::new(4i32);

        // `_box3` 在此处被销毁，内存被释放
    }

    // 只是为了好玩创建很多盒子
    // 无需手动释放内存！
    for _ in 0u32..1_000 {
        create_box();
    }

    // `_box2` 在此处被销毁，内存被释放
}
```

当然，我们可以使用 `valgrind` 来再次检查内存错误：

```shell
$ rustc raii.rs && valgrind./raii
==26873== Memcheck, a memory error detector
==26873== Copyright (C) 2002-2013, and GNU GPL'd, by Julian Seward et al.
==26873== Using Valgrind-3.9.0 and LibVEX; rerun with -h for copyright info
==26873== Command:./raii
==26873==
==26873==
==26873== HEAP SUMMARY:
==26873==     in use at exit: 0 bytes in 0 blocks
==26873==   total heap usage: 1,013 allocs, 1,013 frees, 8,696 bytes allocated
==26873==
==26873== All heap blocks were freed -- no leaks are possible
==26873==
==26873== For counts of detected and suppressed errors, rerun with: -v
==26873== ERROR SUMMARY: 0 errors from 0 contexts (suppressed: 2 from 2)
```

这里没有泄漏！

## 析构函数

Rust 中的析构函数概念是通过 `Drop` 特性提供的。当资源超出作用域时，析构函数会被调用。并非每个类型都需要实现这个特性，只有当你的类型需要自己的析构函数逻辑时才实现它。

运行下面的示例来看看 `Drop` 特性是如何工作的。当 `main` 函数中的变量超出作用域时，自定义析构函数将会被调用。

```rust
struct ToDrop;

impl Drop for ToDrop {
    fn drop(&mut self) {
        println!("ToDrop 正在被销毁");
    }
}

fn main() {
    let x = ToDrop;
    println!("创建了一个 ToDrop！");
}
```
