# Static (Estático)

Rust possui alguns nomes de tempo de vida (lifetime) reservados. Um deles é `'static`. Você pode encontrá-lo em duas situações:

```rust
// Uma referência com tempo de vida 'static:
let s: &'static str = "hello world";

// 'static como parte de uma restrição de trait (trait bound):
fn generic<T>(x: T) where T: 'static {}
```

Ambos estão relacionados, mas sutilmente diferentes, e esta é uma fonte comum de confusão ao aprender Rust. Aqui estão alguns exemplos para cada situação:

## Tempo de vida da referência (Reference lifetime)

Como um tempo de vida de referência, `'static` indica que os dados apontados pela referência vivem durante todo o tempo de vida do programa em execução. Ele ainda pode ser coagido a um tempo de vida mais curto.

Existem duas maneiras de criar uma variável com tempo de vida `'static`, e ambas são armazenadas na memória somente leitura do binário:

- Crie uma constante com a declaração `static`.
- Crie um literal `string` que possui o tipo: `&'static str`.

Veja o exemplo a seguir para uma demonstração de cada método:

```rust
// Crie uma constante com tempo de vida `'static`.
static NUM: i32 = 18;

// Retorna uma referência a `NUM` onde seu tempo de vida `'static`
// é coagido ao do argumento de entrada.
fn coerce_static<'a>(_: &'a i32) -> &'a i32 {
    &NUM
}

fn main() {
    {
        // Crie um literal `string` e imprima-o:
        let static_string = "I'm in read-only memory";
        println!("static_string: {}", static_string);

        // Quando `static_string` sai do escopo, a referência
        // não pode mais ser usada, mas os dados permanecem no binário.
    }

    {
        // Crie um inteiro para usar para `coerce_static`:
        let lifetime_num = 9;

        // Coagir `NUM` ao tempo de vida de `lifetime_num`:
        let coerced_static = coerce_static(&lifetime_num);

        println!("coerced_static: {}", coerced_static);
    }

    println!("NUM: {} permanece acessível!", NUM);
}
```

## Restrição de trait (Trait bound)

Como uma restrição de trait, isso significa que o tipo não contém nenhuma referência não estática. Ex. o receptor pode manter o tipo pelo tempo que quiser e ele nunca se tornará inválido até que o descarte.

É importante entender que isso significa que quaisquer dados próprios (owned data) sempre passam por uma restrição de tempo de vida `'static`, mas uma referência a esses dados próprios geralmente não:

```rust
use std::fmt::Debug;

fn print_it( input: impl Debug + 'static ) {
    println!( "'static value passed in is: {:?}", input );
}

fn main() {
    // i é próprio (owned) e não contém referências, portanto, é 'static:
    let i = 5;
    print_it(i);

    // ops, &i só tem o tempo de vida definido pelo escopo de
    // main(), então não é 'static:
    print_it(&i);
}
```

O compilador dirá:

```ignore
error[E0597]: `i` does not live long enough
  --> src/lib.rs:15:15
   |
15 |     print_it(&i);
   |     ---------^^--
   |     |         |
   |     |         borrowed value does not live long enough
   |     argument requires that `i` is borrowed for `'static`
16 | }
   | - `i` dropped here while still borrowed
```
