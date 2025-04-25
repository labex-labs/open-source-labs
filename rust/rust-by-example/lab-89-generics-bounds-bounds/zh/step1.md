# 界限

在使用泛型时，类型参数通常必须使用 trait 作为*界限*，以规定类型实现了哪些功能。例如，以下示例使用 trait `Display` 进行打印，因此它要求 `T` 受 `Display` 约束；也就是说，`T` _必须_ 实现 `Display`。

```rust
// 定义一个函数 `printer`，它接受一个泛型类型 `T`，该类型
// 必须实现 trait `Display`。
fn printer<T: Display>(t: T) {
    println!("{}", t);
}
```

设定界限会将泛型限制为符合该界限的类型。也就是说：

```rust
struct S<T: Display>(T);

// 错误！`Vec<T>` 没有实现 `Display`。此
// 特化将会失败。
let s = S(vec![1]);
```

设定界限的另一个作用是，泛型实例可以访问界限中指定的 trait 的[方法]。例如：

```rust
// 一个实现打印标记 `{:?}` 的 trait。
use std::fmt::Debug;

trait HasArea {
    fn area(&self) -> f64;
}

impl HasArea for Rectangle {
    fn area(&self) -> f64 { self.length * self.height }
}

#[derive(Debug)]
struct Rectangle { length: f64, height: f64 }
#[allow(dead_code)]
struct Triangle  { length: f64, height: f64 }

// 泛型 `T` 必须实现 `Debug`。无论
// 是什么类型，这都能正常工作。
fn print_debug<T: Debug>(t: &T) {
    println!("{:?}", t);
}

// `T` 必须实现 `HasArea`。任何满足
// 该界限的类型都可以访问 `HasArea` 的函数 `area`。
fn area<T: HasArea>(t: &T) -> f64 { t.area() }

fn main() {
    let rectangle = Rectangle { length: 3.0, height: 4.0 };
    let _triangle = Triangle  { length: 3.0, height: 4.0 };

    print_debug(&rectangle);
    println!("Area: {}", area(&rectangle));

    //print_debug(&_triangle);
    //println!("Area: {}", area(&_triangle));
    // ^ TODO: 尝试取消注释这些行。
    // | 错误：未实现 `Debug` 或 `HasArea`。
}
```

另外需要注意的是，在某些情况下，`where` 子句也可用于应用界限，以使其更具表现力。
