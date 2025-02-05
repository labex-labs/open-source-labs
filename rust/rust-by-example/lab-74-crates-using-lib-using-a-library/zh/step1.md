# 使用库

要将一个板条箱链接到这个新库，你可以使用 `rustc` 的 `--extern` 标志。然后，其所有项将在一个与库同名的模块下被导入。这个模块的行为通常与任何其他模块相同。

```rust
// extern crate rary; // 对于 Rust 2015 版本或更早版本可能需要
fn main() {
    rary::public_function();

    // 错误！`private_function` 是私有的
    //rary::private_function();

    rary::indirect_access();
}
```

```txt
# 其中 library.rlib 是编译后的库的路径，假设它
# 在这里的同一目录中：
$ rustc executable.rs --extern rary=library.rlib &&./executable
调用了 rary 的 `public_function()`
调用了 rary 的 `indirect_access()`，它
> 调用了 rary 的 `private_function()`
```
