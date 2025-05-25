# 외래 함수 인터페이스

Rust 는 C 라이브러리와의 상호 작용을 위한 외래 함수 인터페이스 (FFI) 를 제공합니다. 외래 함수는 `extern` 블록 내에 선언되어야 하며, `#[link]` 속성에 외래 라이브러리의 이름이 포함되어 있어야 합니다.

```rust
use std::fmt;

// 이 extern 블록은 libm 라이브러리에 연결됩니다.
#[link(name = "m")]
extern {
    // 이 함수는 단정밀도 복소수의 제곱근을 계산하는 외래 함수입니다.
    fn csqrtf(z: Complex) -> Complex;

    fn ccosf(z: Complex) -> Complex;
}

// 외래 함수 호출은 안전하지 않은 작업으로 간주되므로,
// 일반적으로 안전한 래퍼를 사용합니다.
fn cos(z: Complex) -> Complex {
    unsafe { ccosf(z) }
}

fn main() {
    // z = -1 + 0i
    let z = Complex { re: -1., im: 0. };

    // 외래 함수 호출은 안전하지 않은 작업입니다.
    let z_sqrt = unsafe { csqrtf(z) };

    println!("{:?}의 제곱근은 {:?}", z, z_sqrt);

    // 안전하지 않은 연산을 래핑한 안전한 API 호출
    println!("cos({:?}) = {:?}", z, cos(z));
}

// 단정밀도 복소수의 최소 구현
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
