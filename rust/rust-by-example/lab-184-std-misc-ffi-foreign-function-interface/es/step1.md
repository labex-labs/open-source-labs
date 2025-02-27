# Interfaz de Funciones Extranjeras

Rust proporciona una Interfaz de Funciones Extranjeras (FFI, por sus siglas en inglés) para bibliotecas C. Las funciones externas deben declararse dentro de un bloque `extern` anotado con un atributo `#[link]` que contiene el nombre de la biblioteca externa.

```rust
use std::fmt;

// este bloque extern se vincula a la biblioteca libm
#[link(name = "m")]
extern {
    // esta es una función externa
    // que calcula la raíz cuadrada de un número complejo de precisión simple
    fn csqrtf(z: Complex) -> Complex;

    fn ccosf(z: Complex) -> Complex;
}

// Dado que llamar a funciones externas se considera inseguro,
// es común escribir envoltorios seguros alrededor de ellas.
fn cos(z: Complex) -> Complex {
    unsafe { ccosf(z) }
}

fn main() {
    // z = -1 + 0i
    let z = Complex { re: -1., im: 0. };

    // llamar a una función externa es una operación insegura
    let z_sqrt = unsafe { csqrtf(z) };

    println!("la raíz cuadrada de {:?} es {:?}", z, z_sqrt);

    // llamar a la API segura envuelta en una operación insegura
    println!("cos({:?}) = {:?}", z, cos(z));
}

// Implementación mínima de números complejos de precisión simple
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
