# 外部函数接口

Rust 为 C 库提供了一个外部函数接口（FFI）。外部函数必须在一个用包含外部库名称的 `#[link]` 属性注释的 `extern` 块内声明。

```rust
use std::fmt;

// 这个 extern 块链接到 libm 库
#[link(name = "m")]
extern {
    // 这是一个外部函数
    // 用于计算单精度复数的平方根
    fn csqrtf(z: Complex) -> Complex;

    fn ccosf(z: Complex) -> Complex;
}

// 由于调用外部函数被认为是不安全的，
// 所以通常会在它们周围编写安全包装器。
fn cos(z: Complex) -> Complex {
    unsafe { ccosf(z) }
}

fn main() {
    // z = -1 + 0i
    let z = Complex { re: -1., im: 0. };

    // 调用外部函数是一个不安全的操作
    let z_sqrt = unsafe { csqrtf(z) };

    println!("the square root of {:?} is {:?}", z, z_sqrt);

    // 调用围绕不安全操作包装的安全 API
    println!("cos({:?}) = {:?}", z, cos(z));
}

// 单精度复数的最小实现
#[repr(C)]
#[derive(Clone, Copy)]
struct Complex {
    re: f32,
    im: f32,
}

impl fmt::Debug for Complex {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        if self.im < 0. {
            write!(f, "{}-{}i", self.re, -self.im)
        } else {
            write!(f, "{}+{}i", self.re, self.im)
        }
    }
}
```
