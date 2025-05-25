# _Bounds_ (Limites)

Assim como os tipos genéricos podem ser limitados, os _lifetimes_ (que são genéricos em si) também usam _bounds_. O caractere `:` tem um significado ligeiramente diferente aqui, mas `+` é o mesmo. Observe como o seguinte é lido:

1.  `T: 'a`: _Todas_ as referências em `T` devem sobreviver ao _lifetime_ `'a`.
2.  `T: Trait + 'a`: O tipo `T` deve implementar a _trait_ `Trait` e _todas_ as referências em `T` devem sobreviver a `'a`.

O exemplo abaixo mostra a sintaxe acima em ação, usada após a palavra-chave `where`:

```rust
use std::fmt::Debug; // Trait to bound with.

#[derive(Debug)]
struct Ref<'a, T: 'a>(&'a T);
// `Ref` contém uma referência a um tipo genérico `T` que tem
// um lifetime desconhecido `'a`. `T` é limitado de forma que qualquer
// *referência* em `T` deve sobreviver a `'a`. Adicionalmente, o lifetime
// de `Ref` pode não exceder `'a`.

// Uma função genérica que imprime usando a trait `Debug`.
fn print<T>(t: T) where
    T: Debug {
    println!("`print`: t is {:?}", t);
}

// Aqui uma referência a `T` é tomada onde `T` implementa
// `Debug` e todas as *referências* em `T` sobrevivem a `'a`. Em
// adição, `'a` deve sobreviver à função.
fn print_ref<'a, T>(t: &'a T) where
    T: Debug + 'a {
    println!("`print_ref`: t is {:?}", t);
}

fn main() {
    let x = 7;
    let ref_x = Ref(&x);

    print_ref(&ref_x);
    print(ref_x);
}
```
