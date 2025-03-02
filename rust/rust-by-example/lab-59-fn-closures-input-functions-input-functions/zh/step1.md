# 输入函数

由于闭包可用作参数，你可能会想函数是否也能如此。答案是肯定的！如果你声明一个将闭包作为参数的函数，那么任何满足该闭包特征约束的函数都可以作为参数传递。

```rust
// 定义一个接受泛型 `F` 参数的函数
// 该参数受 `Fn` 约束，并调用它
fn call_me<F: Fn()>(f: F) {
    f();
}

// 定义一个满足 `Fn` 约束的包装函数
fn function() {
    println!("我是一个函数！");
}

fn main() {
    // 定义一个满足 `Fn` 约束的闭包
    let closure = || println!("我是一个闭包！");

    call_me(closure);
    call_me(function);
}
```

另外需要注意的是，`Fn`、`FnMut` 和 `FnOnce` 特征决定了闭包如何从封闭作用域中捕获变量。
