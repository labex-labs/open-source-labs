# 外部関数インターフェイス

RustはCライブラリに対して外部関数インターフェイス（FFI）を提供します。外部関数は、外部ライブラリ名を含む`#[link]`属性で注釈付けされた`extern`ブロックの中で宣言する必要があります。

```rust
use std::fmt;

// このexternブロックはlibmライブラリにリンクします
#[link(name = "m")]
extern {
    // これは外部関数です
    // 単精度複素数の平方根を計算します
    fn csqrtf(z: Complex) -> Complex;

    fn ccosf(z: Complex) -> Complex;
}

// 外部関数を呼び出すことは非セーフな操作と考えられるため、
// その周りにセーフなラッパーを書くのが一般的です。
fn cos(z: Complex) -> Complex {
    unsafe { ccosf(z) }
}

fn main() {
    // z = -1 + 0i
    let z = Complex { re: -1., im: 0. };

    // 外部関数を呼び出すことは非セーフな操作です
    let z_sqrt = unsafe { csqrtf(z) };

    println!("the square root of {:?} is {:?}", z, z_sqrt);

    // 非セーフな操作をラップしたセーフなAPIを呼び出す
    println!("cos({:?}) = {:?}", z, cos(z));
}

// 単精度複素数の最小限の実装
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
