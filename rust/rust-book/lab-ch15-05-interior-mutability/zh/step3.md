# 内部可变性：对不可变值的可变借用

借用规则的一个结果是，当你有一个不可变值时，你不能对其进行可变借用。例如，这段代码无法编译：

文件名：`src/main.rs`

```rust
fn main() {
    let x = 5;
    let y = &mut x;
}
```

如果你尝试编译这段代码，会得到以下错误：

```bash
error[E0596]: cannot borrow `x` as mutable, as it is not declared
as mutable
 --> src/main.rs:3:13
  |
2 |     let x = 5;
  |         - help: consider changing this to be mutable: `mut x`
3 |     let y = &mut x;
  |             ^^^^^^ cannot borrow as mutable
```

然而，在某些情况下，一个值在其方法中自我变异但对其他代码看起来是不可变的会很有用。该值的方法外部的代码将无法变异该值。使用 `RefCell<T>` 是获得内部可变性的一种方法，但 `RefCell<T>` 并没有完全避开借用规则：编译器中的借用检查器允许这种内部可变性，并且借用规则在运行时进行检查。如果你违反了规则，将会得到一个 `panic!` 而不是编译时错误。

让我们来看一个实际的例子，在这个例子中我们可以使用 `RefCell<T>` 来变异一个不可变值，并看看为什么这很有用。
