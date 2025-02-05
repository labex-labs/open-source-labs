# 发散函数

发散函数永远不会返回。它们使用 `!` 进行标记，`!` 是一种空类型。

```rust
fn foo() ->! {
    panic!("This call never returns.");
}
```

与所有其他类型不同，这种类型无法实例化，因为它可能拥有的所有可能值的集合为空。请注意，它与 `()` 类型不同，`()` 类型恰好有一个可能值。

例如，这个函数会像往常一样返回，尽管返回值中没有任何信息。

```rust
fn some_fn() {
    ()
}

fn main() {
    let _a: () = some_fn();
    println!("This function returns and you can see this line.");
}
```

与之相反，这个函数永远不会将控制权返回给调用者。

```rust
#![feature(never_type)]

fn main() {
    let x:! = panic!("This call never returns.");
    println!("You will never see this line!");
}
```

尽管这看起来可能是一个抽象的概念，但实际上它非常有用且常常很方便。这种类型的主要优点是它可以转换为任何其他类型，因此可以在需要精确类型的地方使用，例如在 `match` 分支中。这使我们能够编写如下代码：

```rust
fn main() {
    fn sum_odd_numbers(up_to: u32) -> u32 {
        let mut acc = 0;
        for i in 0..up_to {
            // 注意，由于 "addition" 变量的类型，这个 match 表达式的返回类型必须是 u32
            let addition: u32 = match i%2 == 1 {
                // "i" 变量是 u32 类型，这完全没问题。
                true => i,
                // 另一方面，"continue" 表达式不返回 u32，但仍然没问题，因为它永远不会返回，因此
                // 不会违反 match 表达式的类型要求。
                false => continue,
            };
            acc += addition;
        }
        acc
    }
    println!("Sum of odd numbers up to 9 (excluding): {}", sum_odd_numbers(9));
}
```

它也是永远循环的函数（例如 `loop {}`）（如网络服务器）或终止进程的函数（例如 `exit()`）的返回类型。
