# Foreign Function Interface

Rust предоставляет Foreign Function Interface (FFI) для библиотек на C. Внешние функции должны быть объявлены внутри блока `extern`, аннотированного атрибутом `#[link]`, содержащим имя внешней библиотеки.

```rust
use std::fmt;

// этот extern-блок связывается с библиотекой libm
#[link(name = "m")]
extern {
    // это внешняя функция
    // которая вычисляет квадратный корень из комплексного числа с одинарной точностью
    fn csqrtf(z: Complex) -> Complex;

    fn ccosf(z: Complex) -> Complex;
}

// Поскольку вызов внешних функций считается небезопасным,
// обычно пишут безопасные обертки вокруг них.
fn cos(z: Complex) -> Complex {
    unsafe { ccosf(z) }
}

fn main() {
    // z = -1 + 0i
    let z = Complex { re: -1., im: 0. };

    // вызов внешней функции - это небезопасная операция
    let z_sqrt = unsafe { csqrtf(z) };

    println!("квадратный корень из {:?} равен {:?}", z, z_sqrt);

    // вызов безопасного API, обернутого вокруг небезопасной операции
    println!("cos({:?}) = {:?}", z, cos(z));
}

// Минимальная реализация комплексных чисел с одинарной точностью
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
