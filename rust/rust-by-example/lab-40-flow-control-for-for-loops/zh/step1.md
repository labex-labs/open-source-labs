# `for` 循环

## `for` 与范围

`for in` 结构可用于遍历 `Iterator`。创建迭代器最简单的方法之一是使用范围表示法 `a..b`。这会以步长为一的方式生成从 `a`（包含）到 `b`（不包含）的值。

让我们用 `for` 而不是 `while` 来编写 FizzBuzz。

```rust
fn main() {
    // 在每次迭代中，`n` 将取以下值：1、2、...、100
    for n in 1..101 {
        if n % 15 == 0 {
            println!("fizzbuzz");
        } else if n % 3 == 0 {
            println!("fizz");
        } else if n % 5 == 0 {
            println!("buzz");
        } else {
            println!("{}", n);
        }
    }
}
```

或者，对于两端都包含的范围，可以使用 `a..=b`。上述代码可以写成：

```rust
fn main() {
    // 在每次迭代中，`n` 将取以下值：1、2、...、100
    for n in 1..=100 {
        if n % 15 == 0 {
            println!("fizzbuzz");
        } else if n % 3 == 0 {
            println!("fizz");
        } else if n % 5 == 0 {
            println!("buzz");
        } else {
            println!("{}", n);
        }
    }
}
```

## `for` 与迭代器

`for in` 结构能够以多种方式与 `Iterator` 进行交互。如在迭代器特征部分所讨论的，默认情况下，`for` 循环会对集合应用 `into_iter` 函数。然而，这并不是将集合转换为迭代器的唯一方式。

`into_iter`、`iter` 和 `iter_mut` 都以不同的方式处理将集合转换为迭代器，它们对集合中的数据提供了不同的视图。

- `iter` - 它在每次迭代中借用集合的每个元素。这样在循环结束后，集合保持不变且可重复使用。

```rust
fn main() {
    let names = vec!["Bob", "Frank", "Ferris"];

    for name in names.iter() {
        match name {
            &"Ferris" => println!("There is a rustacean among us!"),
            // TODO ^ 尝试删除 & 并仅匹配 "Ferris"
            _ => println!("Hello {}", name),
        }
    }

    println!("names: {:?}", names);
}
```

- `into_iter` - 它消耗集合，以便在每次迭代中提供确切的数据。一旦集合被消耗，它就不能再重复使用，因为它已在循环中被“移动”。

```rust
fn main() {
    let names = vec!["Bob", "Frank", "Ferris"];

    for name in names.into_iter() {
        match name {
            "Ferris" => println!("There is a rustacean among us!"),
            _ => println!("Hello {}", name),
        }
    }

    println!("names: {:?}", names);
    // FIXME ^ 注释掉这一行
}
```

- `iter_mut` - 它可变地借用集合的每个元素，允许在原地修改集合。

```rust
fn main() {
    let mut names = vec!["Bob", "Frank", "Ferris"];

    for name in names.iter_mut() {
        *name = match name {
            &mut "Ferris" => "There is a rustacean among us!",
            _ => "Hello",
        }
    }

    println!("names: {:?}", names);
}
```

在上述代码片段中，请注意 `match` 分支的类型，这是不同类型迭代的关键区别。类型的差异当然也意味着能够执行不同的操作。
