# Interface de Fonctions Étrangères

Rust fournit une Interface de Fonctions Étrangères (FFI) pour les bibliothèques C. Les fonctions étrangères doivent être déclarées à l'intérieur d'un bloc `extern` annoté avec un attribut `#[link]` contenant le nom de la bibliothèque étrangère.

```rust
use std::fmt;

// ce bloc extern se lie à la bibliothèque libm
#[link(name = "m")]
extern {
    // c'est une fonction étrangère
    // qui calcule la racine carrée d'un nombre complexe à précision simple
    fn csqrtf(z: Complex) -> Complex;

    fn ccosf(z: Complex) -> Complex;
}

// Étant donné que l'appel de fonctions étrangères est considéré comme non sécurisé,
// il est courant d'écrire des enveloppes sécurisées autour d'elles.
fn cos(z: Complex) -> Complex {
    unsafe { ccosf(z) }
}

fn main() {
    // z = -1 + 0i
    let z = Complex { re: -1., im: 0. };

    // appeler une fonction étrangère est une opération non sécurisée
    let z_sqrt = unsafe { csqrtf(z) };

    println!("la racine carrée de {:?} est {:?}", z, z_sqrt);

    // appeler une API sécurisée encapsulant une opération non sécurisée
    println!("cos({:?}) = {:?}", z, cos(z));
}

// Implémentation minimale de nombres complexes à précision simple
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
