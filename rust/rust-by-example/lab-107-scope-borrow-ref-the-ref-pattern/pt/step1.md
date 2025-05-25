# O padrão `ref`

Ao realizar correspondência de padrões (pattern matching) ou desestruturação (destructuring) através da ligação `let`, a palavra-chave `ref` pode ser usada para obter referências aos campos de uma struct/tupla. O exemplo abaixo mostra algumas instâncias onde isso pode ser útil:

```rust
#[derive(Clone, Copy)]
struct Point { x: i32, y: i32 }

fn main() {
    let c = 'Q';

    // Uma referência `ref` no lado esquerdo de uma atribuição é equivalente a
    // uma referência `&` no lado direito.
    let ref ref_c1 = c;
    let ref_c2 = &c;

    println!("ref_c1 equals ref_c2: {}", *ref_c1 == *ref_c2);

    let point = Point { x: 0, y: 0 };

    // `ref` também é válido ao desestruturar uma struct.
    let _copy_of_x = {
        // `ref_to_x` é uma referência ao campo `x` de `point`.
        let Point { x: ref ref_to_x, y: _ } = point;

        // Retorna uma cópia do campo `x` de `point`.
        *ref_to_x
    };

    // Uma cópia mutável de `point`
    let mut mutable_point = point;

    {
        // `ref` pode ser combinado com `mut` para obter referências mutáveis.
        let Point { x: _, y: ref mut mut_ref_to_y } = mutable_point;

        // Muta o campo `y` de `mutable_point` através de uma referência mutável.
        *mut_ref_to_y = 1;
    }

    println!("point is ({}, {})", point.x, point.y);
    println!("mutable_point is ({}, {})", mutable_point.x, mutable_point.y);

    // Uma tupla mutável que inclui um ponteiro
    let mut mutable_tuple = (Box::new(5u32), 3u32);

    {
        // Desestrutura `mutable_tuple` para mudar o valor de `last`.
        let (_, ref mut last) = mutable_tuple;
        *last = 2u32;
    }

    println!("tuple is {:?}", mutable_tuple);
}
```
