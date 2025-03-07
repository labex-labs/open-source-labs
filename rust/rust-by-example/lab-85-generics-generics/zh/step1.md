# 泛型

“泛型”是将类型和功能泛化到更广泛情况的主题。这在许多方面对于减少代码重复极为有用，但可能需要相当复杂的语法。也就是说，要实现泛型，需要格外注意指定泛型类型在哪些类型上实际被视为有效。泛型最简单和最常见的用途是用于类型参数。

通过使用尖括号和大写字母将类型参数指定为泛型，通常表示为 `<T>`。在 Rust 中，“泛型”还描述任何接受一个或多个泛型类型参数 `<T>` 的东西。任何被指定为泛型类型参数的类型都是泛型的，而其他所有类型都是具体的（非泛型的）。

例如，定义一个名为 `foo` 的“泛型函数”，它接受任何类型的参数 `T`：

```rust
fn foo<T>(arg: T) {... }
```

因为 `T` 使用 `<T>` 被指定为泛型类型参数，所以当它在这里用作 `(arg: T)` 时被视为泛型。即使 `T` 之前被定义为一个 `struct`，情况也是如此。

这个示例展示了一些实际使用的语法：

```rust
// 一个具体类型 `A`。
struct A;

// 在定义类型 `Single` 时，`A` 的首次使用之前没有 `<A>`。
// 因此，`Single` 是一个具体类型，并且 `A` 如上所定义。
struct Single(A);
//            ^ 这里是 `Single` 对类型 `A` 的首次使用。

// 这里，`<T>` 在 `T` 的首次使用之前，所以 `SingleGen` 是一个泛型类型。
// 因为类型参数 `T` 是泛型的，它可以是任何东西，包括
// 顶部定义的具体类型 `A`。
struct SingleGen<T>(T);

fn main() {
    // `Single` 是具体的，并且明确使用 `A`。
    let _s = Single(A);

    // 创建一个类型为 `SingleGen<char>` 的变量 `_char`
    // 并给它赋值 `SingleGen('a')`。
    // 这里，`SingleGen` 有一个明确指定的类型参数。
    let _char: SingleGen<char> = SingleGen('a');

    // `SingleGen` 也可以隐式指定类型参数：
    let _t    = SingleGen(A); // 使用顶部定义的 `A`。
    let _i32  = SingleGen(6); // 使用 `i32`。
    let _char = SingleGen('a'); // 使用 `char`。
}
```
