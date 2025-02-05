# 静态生命周期

Rust有一些保留的生命周期名称。其中之一是`'static`。你可能会在两种情况下遇到它：

```rust
// 具有'static生命周期的引用：
let s: &'static str = "hello world";

// 'static作为trait约束的一部分：
fn generic<T>(x: T) where T: 'static {}
```

两者相关但又略有不同，这是学习Rust时常见的混淆来源。以下是每种情况的一些示例：

## 引用生命周期

作为引用生命周期，`'static`表示引用所指向的数据在整个运行程序的生命周期内都存在。它仍然可以被强制转换为更短的生命周期。

有两种方法可以创建具有`'static`生命周期的变量，并且它们都存储在二进制文件的只读内存中：

- 使用`static`声明创建常量。
- 创建具有`&'static str`类型的字符串字面量。

以下是每种方法的示例：

```rust
// 创建具有'static生命周期的常量。
static NUM: i32 = 18;

// 返回对NUM的引用，其'static生命周期被强制转换为输入参数的生命周期。
fn coerce_static<'a>(_: &'a i32) -> &'a i32 {
    &NUM
}

fn main() {
    {
        // 创建一个字符串字面量并打印它：
        let static_string = "I'm in read-only memory";
        println!("static_string: {}", static_string);

        // 当static_string超出作用域时，引用不再可用，但数据仍保留在二进制文件中。
    }

    {
        // 创建一个整数用于coerce_static：
        let lifetime_num = 9;

        // 将NUM的生命周期强制转换为lifetime_num的生命周期：
        let coerced_static = coerce_static(&lifetime_num);

        println!("coerced_static: {}", coerced_static);
    }

    println!("NUM: {} stays accessible!", NUM);
}
```

## trait约束

作为trait约束，它意味着类型不包含任何非静态引用。例如，接收者可以根据需要长时间持有该类型，并且在丢弃它之前它永远不会变得无效。

重要的是要理解这意味着任何拥有的数据总是通过`'static`生命周期约束，但对该拥有数据的引用通常不是：

```rust
use std::fmt::Debug;

fn print_it( input: impl Debug + 'static ) {
    println!( "'static value passed in is: {:?}", input );
}

fn main() {
    // i是拥有的且不包含引用，因此它是'static的：
    let i = 5;
    print_it(i);

    // 哎呀，&i仅具有由main()作用域定义的生命周期，因此它不是'static的：
    print_it(&i);
}
```

编译器会告诉你：

```ignore
error[E0597]: `i` does not live long enough
  --> src/lib.rs:15:15
   |
15 |     print_it(&i);
   |     ---------^^--
   |     |         |
   |     |         borrowed value does not live long enough
   |     argument requires that `i` is borrowed for `'static`
16 | }
   | - `i` dropped here while still borrowed
```
