# Foreign Function Interface

Rust bietet eine Foreign Function Interface (FFI) für C-Bibliotheken. Fremde Funktionen müssen innerhalb eines `extern`-Blocks deklariert werden, der mit einem `#[link]`-Attribut versehen ist, das den Namen der fremden Bibliothek enthält.

```rust
use std::fmt;

// Dieser extern-Block verweist auf die libm-Bibliothek
#[link(name = "m")]
extern {
    // Dies ist eine fremde Funktion
    // die die Quadratwurzel einer einfachen Gleitkommazahl berechnet
    fn csqrtf(z: Complex) -> Complex;

    fn ccosf(z: Complex) -> Complex;
}

// Da das Aufrufen von fremden Funktionen als unsicher angesehen wird,
// ist es üblich, sichere Wrapper um sie zu schreiben.
fn cos(z: Complex) -> Complex {
    unsafe { ccosf(z) }
}

fn main() {
    // z = -1 + 0i
    let z = Complex { re: -1., im: 0. };

    // Das Aufrufen einer fremden Funktion ist eine unsichere Operation
    let z_sqrt = unsafe { csqrtf(z) };

    println!("Die Quadratwurzel von {:?} ist {:?}", z, z_sqrt);

    // Aufruf der sicheren API, die um die unsichere Operation gewrappt ist
    println!("cos({:?}) = {:?}", z, cos(z));
}

// Minimalimplementierung von einfachen Gleitkommazahlen
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
