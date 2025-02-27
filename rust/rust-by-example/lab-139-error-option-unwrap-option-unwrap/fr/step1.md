# `Option` & `unwrap`

Dans le dernier exemple, nous avons montré que nous pouvons provoquer une erreur dans le programme à volonté. Nous avons dit à notre programme de générer une panique si nous buvons un citronnade sucrée. Mais que se passe-t-il si nous attendons _quelque_ boisson mais ne la recevons pas? Ce cas serait tout aussi mauvais, donc il doit être géré!

Nous _pourrions_ tester cela contre la chaîne nulle (`""`), comme nous le faisons avec une citronnade. Puisque nous utilisons Rust, demandons plutôt au compilateur de signaler les cas où il n'y a pas de boisson.

Un `enum` appelé `Option<T>` dans la bibliothèque `std` est utilisé lorsque l'absence est possible. Il se manifeste sous l'une des deux "options" suivantes :

- `Some(T)` : Un élément de type `T` a été trouvé
- `None` : Aucun élément n'a été trouvé

Ces cas peuvent soit être traités explicitement via `match` soit implicitement avec `unwrap`. Le traitement implicite renverra soit l'élément interne soit générera une panique.

Notez qu'il est possible de personnaliser manuellement la panique avec `expect`, mais `unwrap` nous laisse dans les autres cas un résultat moins significatif que le traitement explicite. Dans l'exemple suivant, le traitement explicite produit un résultat plus contrôlé tout en conservant l'option de générer une panique si souhaité.

```rust
// L'adulte a vu tout et peut bien gérer n'importe quelle boisson.
// Toutes les boissons sont traitées explicitement à l'aide de `match`.
fn give_adult(drink: Option<&str>) {
    // Spécifiez une action pour chaque cas.
    match drink {
        Some("lemonade") => println!("Yuck! Trop sucré."),
        Some(inner)   => println!("{}? Comme c'est bon.", inner),
        None          => println!("Pas de boisson? Oh bien."),
    }
}

// Les autres vont générer une panique avant de boire des boissons sucrées.
// Toutes les boissons sont traitées implicitement à l'aide de `unwrap`.
fn drink(drink: Option<&str>) {
    // `unwrap` génère une panique lorsqu'il reçoit un `None`.
    let inside = drink.unwrap();
    if inside == "lemonade" { panic!("AAAaaaaa!!!!"); }

    println!("J'adore les {}!!!!!", inside);
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
