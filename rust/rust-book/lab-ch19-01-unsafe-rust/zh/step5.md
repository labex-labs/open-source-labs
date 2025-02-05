# 为不安全代码创建安全抽象

仅仅因为一个函数包含不安全代码，并不意味着我们需要将整个函数标记为不安全。事实上，将不安全代码包装在一个安全函数中是一种常见的抽象方式。例如，让我们研究一下标准库中的 `split_at_mut` 函数，它需要一些不安全代码。我们将探讨如何实现它。这个安全方法是在可变切片上定义的：它接受一个切片，并通过在作为参数给出的索引处分割切片，将其分成两个切片。清单 19-4 展示了如何使用 `split_at_mut`。

```rust
let mut v = vec![1, 2, 3, 4, 5, 6];

let r = &mut v[..];

let (a, b) = r.split_at_mut(3);

assert_eq!(a, &mut [1, 2, 3]);
assert_eq!(b, &mut [4, 5, 6]);
```

清单 19-4：使用安全的 `split_at_mut` 函数

我们不能仅使用安全的 Rust 来实现这个函数。一个尝试可能类似于清单 19-5，它不会编译。为了简单起见，我们将把 `split_at_mut` 实现为一个函数，而不是一个方法，并且只针对 `i32` 值的切片，而不是通用类型 `T` 的切片。

```rust
fn split_at_mut(
    values: &mut [i32],
    mid: usize,
) -> (&mut [i32], &mut [i32]) {
    let len = values.len();

    assert!(mid <= len);

    (&mut values[..mid], &mut values[mid..])
}
```

清单 19-5：仅使用安全的 Rust 对 `split_at_mut` 的尝试实现

这个函数首先获取切片的总长度。然后通过检查它是否小于或等于长度，来断言作为参数给出的索引在切片范围内。这个断言意味着，如果我们传递一个大于切片长度的索引来分割切片，函数将在尝试使用该索引之前发生恐慌。

然后我们在一个元组中返回两个可变切片：一个从原始切片的开头到 `mid` 索引，另一个从 `mid` 到切片的末尾。

当我们尝试编译清单 19-5 中的代码时，我们会得到一个错误：

```bash
error[E0499]: cannot borrow `*values` as mutable more than once at a time
 --> src/main.rs:9:31
  |
2 |     values: &mut [i32],
  |             - let's call the lifetime of this reference `'1`
...
9 |     (&mut values[..mid], &mut values[mid..])
  |     --------------------------^^^^^^--------
  |     |     |                   |
  |     |     |                   second mutable borrow occurs here
  |     |     first mutable borrow occurs here
  |     returning this value requires that `*values` is borrowed for `'1`
```

Rust 的借用检查器无法理解我们是在借用切片的不同部分；它只知道我们从同一个切片借用了两次。从根本上来说，借用切片的不同部分是没问题的，因为这两个切片没有重叠，但是 Rust 还不够智能，无法理解这一点。当我们知道代码没问题，但 Rust 不知道时，就该使用不安全代码了。

清单 19-6 展示了如何使用一个 `unsafe` 块、一个裸指针以及一些对不安全函数的调用来使 `split_at_mut` 的实现能够正常工作。

```rust
use std::slice;

fn split_at_mut(
    values: &mut [i32],
    mid: usize,
) -> (&mut [i32], &mut [i32]) {
  1 let len = values.len();
  2 let ptr = values.as_mut_ptr();

  3 assert!(mid <= len);

  4 unsafe {
        (
          5 slice::from_raw_parts_mut(ptr, mid),
          6 slice::from_raw_parts_mut(ptr.add(mid), len - mid),
        )
    }
}
```

清单 19-6：在 `split_at_mut` 函数的实现中使用不安全代码

从“切片类型”中回忆一下，切片是指向某些数据和切片长度的指针。我们使用 `len` 方法来获取切片的长度 \[1\]，并使用 `as_mut_ptr` 方法来访问切片的裸指针 \[2\]。在这种情况下，因为我们有一个指向 `i32` 值的可变切片，`as_mut_ptr` 返回一个类型为 `*mut i32` 的裸指针，我们将其存储在变量 `ptr` 中。

我们保留 `mid` 索引在切片范围内的断言 \[3\]。然后我们进入不安全代码 \[4\]：`slice::from_raw_parts_mut` 函数接受一个裸指针和一个长度，并创建一个切片。我们用它来创建一个从 `ptr` 开始、长度为 `mid` 个元素的切片 \[5\]。然后我们以 `mid` 作为参数调用 `ptr` 上的 `add` 方法，以获取一个从 `mid` 开始的裸指针，并使用该指针和 `mid` 之后的剩余元素数量作为长度来创建一个切片 \[6\]。

函数 `slice::from_raw_parts_mut` 是不安全的，因为它接受一个裸指针，并且必须信任这个指针是有效的。裸指针上的 `add` 方法也是不安全的，因为它必须信任偏移位置也是一个有效的指针。因此，我们必须在对 `slice::from_raw_parts_mut` 和 `add` 的调用周围放置一个 `unsafe` 块，这样我们才能调用它们。通过查看代码并添加 `mid` 必须小于或等于 `len` 的断言，我们可以知道在 `unsafe` 块中使用的所有裸指针都将是指向切片内数据的有效指针。这是对 `unsafe` 的一种可接受且合适的使用方式。

请注意，我们不需要将最终的 `split_at_mut` 函数标记为 `unsafe`，并且我们可以从安全的 Rust 中调用这个函数。我们已经为不安全代码创建了一个安全抽象，其函数实现以安全的方式使用了不安全代码，因为它仅从该函数可以访问的数据创建有效的指针。

相比之下，清单 19-7 中对 `slice::from_raw_parts_mut` 的使用在使用切片时可能会导致程序崩溃。这段代码获取一个任意的内存位置，并创建一个长度为 10000 个元素的切片。

```rust
use std::slice;

let address = 0x01234usize;
let r = address as *mut i32;

let values: &[i32] = unsafe {
    slice::from_raw_parts_mut(r, 10000)
};
```

清单 19-7：从任意内存位置创建切片

我们并不拥有这个任意位置的内存，并且不能保证这段代码创建的切片包含有效的 `i32` 值。试图将 `values` 当作一个有效的切片来使用会导致未定义行为。
