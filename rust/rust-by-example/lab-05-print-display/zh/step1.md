# 格式化显示

`fmt::Debug` 的输出看起来很难做到紧凑和简洁，因此自定义输出外观通常是很有必要的。这可以通过手动实现 `fmt::Display` 来完成，它使用 `{}` 作为打印标记。实现方式如下：

```rust
// 通过 `use` 导入 `fmt` 模块，使其可用。
use std::fmt;

// 定义一个结构体，并为其实现 `fmt::Display`。这是一个名为 `Structure` 的元组结构体，它包含一个 `i32`。
struct Structure(i32);

// 为了使用 `{}` 标记，必须为该类型手动实现 `fmt::Display` 特性。
impl fmt::Display for Structure {
    // 这个特性要求 `fmt` 具有这个确切的签名。
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        // 只将第一个元素严格写入提供的输出流：`f`。返回 `fmt::Result`，它表示操作是否成功。注意，`write!` 使用的语法与 `println!` 非常相似。
        write!(f, "{}", self.0)
    }
}
```

`fmt::Display` 可能比 `fmt::Debug` 更简洁，但这给标准库带来了一个问题。对于模糊类型应该如何显示呢？例如，如果标准库为所有的 `Vec<T>` 实现一种单一的样式，应该是什么样式呢？会是以下两种中的一种吗？

- `Vec<路径>`：`/:/etc:/home/用户名:/bin`（以 `:` 分割）
- `Vec<数字>`：`1,2,3`（以 `,` 分割）

不，因为对于所有类型来说没有理想的样式，并且标准库也不会擅自规定一种样式。`Vec<T>` 或任何其他通用容器类型都没有实现 `fmt::Display`。对于这些通用情况，必须使用 `fmt::Debug`。

不过这并不是一个问题，因为对于任何新的非通用的 _容器_ 类型，可以实现 `fmt::Display`。

```rust
use std::fmt; // 导入 `fmt`

// 一个包含两个数字的结构体。将派生 `Debug`，以便可以将结果与 `Display` 进行对比。
#[derive(Debug)]
struct MinMax(i64, i64);

// 为 `MinMax` 实现 `Display`。
impl fmt::Display for MinMax {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        // 使用 `self.number` 来引用每个位置的数据点。
        write!(f, "({}, {})", self.0, self.1)
    }
}

// 定义一个结构体，其中的字段是可命名的，以便进行比较。
#[derive(Debug)]
struct Point2D {
    x: f64,
    y: f64,
}

// 同样，为 `Point2D` 实现 `Display`。
impl fmt::Display for Point2D {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        // 进行自定义，以便只显示 `x` 和 `y`。
        write!(f, "x: {}, y: {}", self.x, self.y)
    }
}

fn main() {
    let minmax = MinMax(0, 14);

    println!("比较结构体：");
    println!("格式化显示：{}", minmax);
    println!("调试格式：{:?}", minmax);

    let big_range =   MinMax(-300, 300);
    let small_range = MinMax(-3, 3);

    println!("大的范围是 {big}，小的范围是 {small}",
             small = small_range,
             big = big_range);

    let point = Point2D { x: 3.3, y: 7.2 };

    println!("比较点：");
    println!("格式化显示：{}", point);
    println!("调试格式：{:?}", point);

    // 错误。虽然同时实现了 `Debug` 和 `Display`，但 `{:b}` 需要实现 `fmt::Binary`。这将无法工作。
    // println!("Point2D 的二进制形式是什么样的：{:b}?", point);
}
```

所以，已经实现了 `fmt::Display`，但没有实现 `fmt::Binary`，因此不能使用它。`std::fmt` 有许多这样的 `特性`，每个特性都需要自己的实现。`std::fmt` 中对此有更详细的说明。

## 活动

在检查上述示例的输出后，以 `Point2D` 结构体为指导，在示例中添加一个 `Complex` 结构体。当以相同方式打印时，输出应该是：

```txt
格式化显示：3.3 + 7.2i
调试格式：Complex { real: 3.3, imag: 7.2 }
```
