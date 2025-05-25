# `Option` & `unwrap`

No último exemplo, mostramos que podemos induzir a falha do programa à vontade. Dissemos ao nosso programa para `panic` se bebêssemos uma limonada açucarada. Mas e se esperarmos _alguma_ bebida, mas não recebermos nenhuma? Esse caso seria igualmente ruim, então precisa ser tratado!

Nós _poderíamos_ testar isso contra a string nula (`""`) como fazemos com uma limonada. Como estamos usando Rust, vamos, em vez disso, fazer com que o compilador aponte casos onde não há bebida.

Um `enum` chamado `Option<T>` na biblioteca `std` é usado quando a ausência é uma possibilidade. Ele se manifesta como uma de duas "opções":

- `Some(T)`: Um elemento do tipo `T` foi encontrado
- `None`: Nenhum elemento foi encontrado

Esses casos podem ser tratados explicitamente via `match` ou implicitamente com `unwrap`. O tratamento implícito retornará o elemento interno ou `panic`.

Observe que é possível personalizar manualmente o `panic` com `expect`, mas `unwrap` caso contrário nos deixa com uma saída menos significativa do que o tratamento explícito. No exemplo a seguir, o tratamento explícito produz um resultado mais controlado, mantendo a opção de `panic` se desejado.

```rust
// The adult has seen it all, and can handle any drink well.
// All drinks are handled explicitly using `match`.
fn give_adult(drink: Option<&str>) {
    // Specify a course of action for each case.
    match drink {
        Some("lemonade") => println!("Yuck! Too sugary."),
        Some(inner)   => println!("{}? How nice.", inner),
        None          => println!("No drink? Oh well."),
    }
}

// Others will `panic` before drinking sugary drinks.
// All drinks are handled implicitly using `unwrap`.
fn drink(drink: Option<&str>) {
    // `unwrap` returns a `panic` when it receives a `None`.
    let inside = drink.unwrap();
    if inside == "lemonade" { panic!("AAAaaaaa!!!!"); }

    println!("I love {}s!!!!!", inside);
}

fn main() {
    let water  = Some("water");
    let lemonade = Some("lemonade");
    let void  = None;

    give_adult(water);
    give_adult(lemonade);
    give_adult(void);

    let coffee = Some("coffee");
    let nothing = None;

    drink(coffee);
    drink(nothing);
}
```
