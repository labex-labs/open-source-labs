# 边界

就像泛型类型可以有边界一样，生命周期（它们本身也是泛型的）也使用边界。在这里，`:` 字符的含义稍有不同，但 `+` 的含义是相同的。请注意以下内容的读法：

1.  `T: 'a`：`T` 中的**所有**引用的生命周期都必须长于 `'a`。
2.  `T: Trait + 'a`：类型 `T` 必须实现 `Trait` 特性，并且 `T` 中的**所有**引用的生命周期都必须长于 `'a`。

下面的示例展示了在 `where` 关键字之后使用上述语法的情况：

```rust
use std::fmt::Debug; // 要绑定的特性。

#[derive(Debug)]
struct Ref<'a, T: 'a>(&'a T);
// `Ref` 包含一个对泛型类型 `T` 的引用，`T` 的生命周期为未知的 `'a`。`T` 有边界限制，即 `T` 中的任何**引用**的生命周期都必须长于 `'a`。此外，`Ref` 的生命周期不能超过 `'a`。

// 一个使用 `Debug` 特性进行打印的泛型函数。
fn print<T>(t: T) where
    T: Debug {
    println!("`print`: t is {:?}", t);
}

// 这里获取了一个对 `T` 的引用，其中 `T` 实现了 `Debug` 特性，并且 `T` 中的所有**引用**的生命周期都长于 `'a`。此外，`'a` 的生命周期必须长于该函数。
fn print_ref<'a, T>(t: &'a T) where
    T: Debug + 'a {
    println!("`print_ref`: t is {:?}", t);
}

fn main() {
    let x = 7;
    let ref_x = Ref(&x);

    print_ref(&ref_x);
    print(ref_x);
}
```
