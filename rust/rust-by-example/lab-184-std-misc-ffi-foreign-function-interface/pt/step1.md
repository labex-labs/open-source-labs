# Interface de Função Estrangeira

O Rust fornece uma Interface de Função Estrangeira (FFI) para bibliotecas C. As funções estrangeiras devem ser declaradas dentro de um bloco `extern` anotado com um atributo `#[link]` contendo o nome da biblioteca estrangeira.

```rust
use std::fmt;

// este bloco extern faz ligação com a biblioteca libm
#[link(name = "m")]
extern {
    // esta é uma função estrangeira
    // que calcula a raiz quadrada de um número complexo de precisão única
    fn csqrtf(z: Complex) -> Complex;

    fn ccosf(z: Complex) -> Complex;
}

// Como chamar funções estrangeiras é considerado inseguro,
// é comum criar wrappers seguros em torno delas.
fn cos(z: Complex) -> Complex {
    unsafe { ccosf(z) }
}

fn main() {
    // z = -1 + 0i
    let z = Complex { re: -1., im: 0. };

    // chamar uma função estrangeira é uma operação insegura
    let z_sqrt = unsafe { csqrtf(z) };

    println!("a raiz quadrada de {:?} é {:?}", z, z_sqrt);

    // chamando API segura envolvendo operação insegura
    println!("cos({:?}) = {:?}", z, cos(z));
}

// Implementação mínima de números complexos de precisão única
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
