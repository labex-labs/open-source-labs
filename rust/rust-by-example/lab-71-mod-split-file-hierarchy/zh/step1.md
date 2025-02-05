# 文件层次结构

模块可以映射到文件/目录层次结构。让我们详细分析一下文件中的可见性示例：

```shell
$ tree.
.
├── my
│   ├── inaccessible.rs
│   └── nested.rs
├── my.rs
└── split.rs
```

在 `split.rs` 中：

```rust
// 此声明将查找名为 `my.rs` 的文件，并将其内容插入到此作用域下名为 `my` 的模块中
mod my;

fn function() {
    println!("called `function()`");
}

fn main() {
    my::function();

    function();

    my::indirect_access();

    my::nested::function();
}
```

在 `my.rs` 中：

```rust
// 同样，`mod inaccessible` 和 `mod nested` 将定位 `nested.rs`
// 和 `inaccessible.rs` 文件，并将它们插入到各自的模块下
mod inaccessible;
pub mod nested;

pub fn function() {
    println!("called `my::function()`");
}

fn private_function() {
    println!("called `my::private_function()`");
}

pub fn indirect_access() {
    print!("called `my::indirect_access()`, that\n> ");

    private_function();
}
```

在 `my/nested.rs` 中：

```rust
pub fn function() {
    println!("called `my::nested::function()`");
}

#[allow(dead_code)]
fn private_function() {
    println!("called `my::nested::private_function()`");
}
```

在 `my/inaccessible.rs` 中：

```rust
#[allow(dead_code)]
pub fn public_function() {
    println!("called `my::inaccessible::public_function()`");
}
```

让我们检查一下一切是否仍像以前一样正常工作：

```shell
$ rustc split.rs &&./split
called `my::function()`
called `function()`
called `my::indirect_access()`, that
> called `my::private_function()`
called `my::nested::function()`
```
