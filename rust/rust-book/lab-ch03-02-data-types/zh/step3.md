# 整数类型

_整数_ 是一个没有小数部分的数字。我们在第 2 章中使用了一种整数类型，即 `u32` 类型。这种类型声明表明，它所关联的值应该是一个无符号整数（有符号整数类型以 `i` 开头而不是 `u`），它占用 32 位空间。表 3-1 显示了 Rust 中的内置整数类型。我们可以使用这些变体中的任何一个来声明整数值的数据类型。

表 3-1：Rust 中的整数类型

长度 有符号 无符号

---

8 位 `i8` `u8`
16 位 `i16` `u16`
32 位 `i32` `u32`
64 位 `i64` `u64`
128 位 `i128` `u128`
arch `isize` `usize`

每个变体可以是带符号的或无符号的，并且具有显式的大小。_有符号_ 和 _无符号_ 指的是数字是否可能为负数——换句话说，数字是否需要带有符号（有符号），或者它是否只会是正数，因此可以在没有符号的情况下表示（无符号）。这就像在纸上写数字：当符号很重要时，数字会显示一个加号或减号；但是，当可以安全地假设数字为正数时，它会显示为没有符号。有符号数字使用补码表示法存储。

每个有符号变体可以存储从 -(2^(n-1)) 到 2^(n-1) - 1（包含）的数字，其中 _n_ 是该变体使用的位数。因此，`i8` 可以存储从 -(2^7) 到 2^7 - 1 的数字，即 -128 到 127。无符号变体可以存储从 0 到 2^n - 1 的数字，因此 `u8` 可以存储从 0 到 2^8 - 1 的数字，即 0 到 255。

此外，`isize` 和 `usize` 类型取决于你的程序运行的计算机的架构，在表中表示为 "arch"：如果你使用的是 64 位架构，则为 64 位；如果你使用的是 32 位架构，则为 32 位。

你可以使用表 3-2 中显示的任何形式编写整数字面量。请注意，可以有多种数值类型的数字字面量允许使用类型后缀，例如 `57u8`，以指定类型。数字字面量也可以使用 `_` 作为视觉分隔符，使数字更易于阅读，例如 `1_000`，它将与你指定 `1000` 时的值相同。

表 3-2：Rust 中的整数字面量

数字字面量 示例

---

十进制 `98_222`
十六进制 `0xff`
八进制 `0o77`
二进制 `0b1111_0000`
字节（仅限 `u8`）`b'A'`

那么，你如何知道使用哪种整数类型呢？如果你不确定，Rust 的默认值通常是很好的起点：整数类型默认为 `i32`。你使用 `isize` 或 `usize` 的主要情况是索引某种集合时。

> **整数溢出（Integer Overflow）**
>
> 假设你有一个 `u8` 类型的变量，它可以容纳 0 到 255 之间的值。如果你尝试将变量更改为该范围之外的值，例如 256，则会发生*整数溢出*，这可能导致两种行为之一。当你在调试模式下编译时，Rust 包含对整数溢出的检查，如果发生此行为，会导致你的程序在运行时*panic*。当程序因错误退出时，Rust 使用术语 _panic_；我们将在“使用 panic! 的不可恢复错误”中更深入地讨论 panic。
>
> 当你使用 `--release` 标志在发布模式下编译时，Rust _不_ 包含对导致 panic 的整数溢出的检查。相反，如果发生溢出，Rust 会执行*补码包装*。简而言之，大于该类型可以容纳的最大值的值会“环绕”到该类型可以容纳的最小值。对于 `u8`，值 256 变为 0，值 257 变为 1，依此类推。程序不会 panic，但变量将具有一个可能不是你期望的值。依赖于整数溢出的包装行为被认为是一个错误。
>
> 为了显式地处理溢出的可能性，你可以使用标准库为基本数值类型提供的这些方法系列：
>
> - 在所有模式下使用 `wrapping_*` 方法进行包装，例如 `wrapping_add`。
> - 如果发生溢出，则使用 `checked_*` 方法返回 `None` 值。
> - 使用 `overflowing_*` 方法返回该值和一个布尔值，指示是否发生了溢出。
> - 使用 `saturating_*` 方法在值的最小值或最大值处饱和。
