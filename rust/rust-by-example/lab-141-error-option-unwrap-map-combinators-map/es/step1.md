# Combinadores: `map`

`match` es un método válido para manejar `Option`s. Sin embargo, es posible que eventualmente encuentres que su uso intensivo es tedioso, especialmente con operaciones que solo son válidas con una entrada. En estos casos, los combinadores se pueden utilizar para manejar el flujo de control de manera modular.

`Option` tiene un método integrado llamado `map()`, un combinador para la simple asignación de `Some -> Some` y `None -> None`. Se pueden encadenar múltiples llamadas a `map()` para mayor flexibilidad.

En el siguiente ejemplo, `process()` reemplaza a todas las funciones anteriores mientras se mantiene compacta.

```rust
#![allow(dead_code)]

#[derive(Debug)] enum Food { Apple, Carrot, Potato }

#[derive(Debug)] struct Peeled(Food);
#[derive(Debug)] struct Chopped(Food);
#[derive(Debug)] struct Cooked(Food);

// Pelando la comida. Si no hay ninguna, entonces devuelve `None`.
// De lo contrario, devuelve la comida pelada.
fn peel(food: Option<Food>) -> Option<Peeled> {
    match food {
        Some(food) => Some(Peeled(food)),
        None       => None,
    }
}

// Cortando la comida. Si no hay ninguna, entonces devuelve `None`.
// De lo contrario, devuelve la comida cortada.
fn chop(peeled: Option<Peeled>) -> Option<Chopped> {
    match peeled {
        Some(Peeled(food)) => Some(Chopped(food)),
        None               => None,
    }
}

// Cocinando la comida. Aquí, mostramos `map()` en lugar de `match` para el manejo de casos.
fn cook(chopped: Option<Chopped>) -> Option<Cooked> {
    chopped.map(|Chopped(food)| Cooked(food))
}

// Una función para pelar, cortar y cocinar la comida en secuencia.
// Encadenamos múltiples usos de `map()` para simplificar el código.
fn process(food: Option<Food>) -> Option<Cooked> {
    food.map(|f| Peeled(f))
     .map(|Peeled(f)| Chopped(f))
     .map(|Chopped(f)| Cooked(f))
}

// Comprueba si hay comida o no antes de intentar comerla!
fn eat(food: Option<Cooked>) {
    match food {
        Some(food) => println!("Mmm. I love {:?}", food),
        None       => println!("Oh no! It wasn't edible."),
    }
}

fn main() {
    let apple = Some(Food::Apple);
    let carrot = Some(Food::Carrot);
    let potato = None;

    let cooked_apple = cook(chop(peel(apple)));
    let cooked_carrot = cook(chop(peel(carrot)));
    // Probemos ahora la más simple de aspecto `process()`.
    let cooked_potato = process(potato);

    eat(cooked_apple);
    eat(cooked_carrot);
    eat(cooked_potato);
}
```
