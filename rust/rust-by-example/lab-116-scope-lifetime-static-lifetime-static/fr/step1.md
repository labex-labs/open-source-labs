# Static

Rust a quelques noms de durée de vie réservés. L'un d'entre eux est `'static`. Vous pouvez le rencontrer dans deux situations :

```rust
// Une référence avec une durée de vie `'static` :
let s: &'static str = "hello world";

// `'static` en tant que partie d'une contrainte de trait :
fn generic<T>(x: T) where T: 'static {}
```

Les deux sont liés mais subtilement différents et c'est une source commune de confusion lorsqu'on apprend Rust. Voici quelques exemples pour chaque situation :

## Durée de vie de la référence

En tant que durée de vie de référence, `'static` indique que les données pointées par la référence existent pour toute la durée de vie du programme exécutant. Elle peut toujours être contraite à une durée de vie plus courte.

Il existe deux façons de créer une variable avec une durée de vie `'static`, et les deux sont stockées dans la mémoire exécutable du binaire :

- Créer une constante avec la déclaration `static`.
- Créer une chaîne littérale qui a le type : `&'static str`.

Voyez l'exemple suivant pour voir chaque méthode en action :

```rust
// Créer une constante avec une durée de vie `'static`.
static NUM: i32 = 18;

// Retourne une référence à `NUM` où sa durée de vie `'static`
// est contraite à celle de l'argument d'entrée.
fn coerce_static<'a>(_: &'a i32) -> &'a i32 {
    &NUM
}

fn main() {
    {
        // Créer une chaîne littérale et l'afficher :
        let static_string = "I'm in read-only memory";
        println!("static_string: {}", static_string);

        // Lorsque `static_string` sort de portée, la référence
        // ne peut plus être utilisée, mais les données restent dans le binaire.
    }

    {
        // Créer un entier pour utiliser avec `coerce_static` :
        let lifetime_num = 9;

        // Contraindre `NUM` à la durée de vie de `lifetime_num` :
        let coerced_static = coerce_static(&lifetime_num);

        println!("coerced_static: {}", coerced_static);
    }

    println!("NUM: {} reste accessible!", NUM);
}
```

## Contrainte de trait

En tant que contrainte de trait, cela signifie que le type ne contient aucune référence non statique. Par exemple, le récepteur peut conserver le type aussi longtemps qu'il le souhaite et il ne deviendra jamais invalide tant qu'il ne le dépose pas.

Il est important de comprendre que cela signifie que toute donnée possédée passe toujours une contrainte de durée de vie `'static`, mais une référence à cette donnée possédée ne le fait généralement pas :

```rust
use std::fmt::Debug;

fn print_it( input: impl Debug + 'static ) {
    println!( "'static value passed in is: {:?}", input );
}

fn main() {
    // i est possédé et ne contient pas de références, donc il est `'static` :
    let i = 5;
    print_it(i);

    // Oups, &i n'a que la durée de vie définie par la portée de
    // main(), donc ce n'est pas `'static` :
    print_it(&i);
}
```

Le compilateur vous dira :

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
