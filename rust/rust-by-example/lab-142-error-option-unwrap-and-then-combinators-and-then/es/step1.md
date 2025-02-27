# Combinadores: `and_then`

`map()` se describió como una forma encadenable de simplificar las declaraciones `match`. Sin embargo, usar `map()` en una función que devuelve un `Option<T>` da como resultado el anidado `Option<Option<T>>`. Encadenar múltiples llamadas juntas puede luego resultar confuso. Aquí es donde entra en juego otro combinador llamado `and_then()`, conocido en algunos lenguajes como flatmap.

`and_then()` llama a su función de entrada con el valor envuelto y devuelve el resultado. Si el `Option` es `None`, entonces devuelve `None` en lugar de eso.

En el siguiente ejemplo, `cookable_v3()` devuelve un `Option<Food>`. Usar `map()` en lugar de `and_then()` habría dado un `Option<Option<Food>>`, que es un tipo no válido para `eat()`.

```rust
#![allow(dead_code)]

#[derive(Debug)] enum Food { CordonBleu, Steak, Sushi }
#[derive(Debug)] enum Day { Monday, Tuesday, Wednesday }

// No tenemos los ingredientes para hacer Sushi.
fn have_ingredients(food: Food) -> Option<Food> {
    match food {
        Food::Sushi => None,
        _           => Some(food),
    }
}

// Tenemos la receta para todo excepto Cordon Bleu.
fn have_recipe(food: Food) -> Option<Food> {
    match food {
        Food::CordonBleu => None,
        _                => Some(food),
    }
}

// Para preparar un plato, necesitamos tanto la receta como los ingredientes.
// Podemos representar la lógica con una cadena de `match`:
fn cookable_v1(food: Food) -> Option<Food> {
    match have_recipe(food) {
        None       => None,
        Some(food) => have_ingredients(food),
    }
}

// Esto se puede escribir convenientemente de forma más compacta con `and_then()`:
fn cookable_v3(food: Food) -> Option<Food> {
    have_recipe(food).and_then(have_ingredients)
}

// De lo contrario, tendríamos que `aplanar()` un `Option<Option<Food>>`
// para obtener un `Option<Food>`:
fn cookable_v2(food: Food) -> Option<Food> {
    have_recipe(food).map(have_ingredients).flatten()
}

fn eat(food: Food, day: Day) {
    match cookable_v3(food) {
        Some(food) => println!("Yay! On {:?} we get to eat {:?}.", day, food),
        None       => println!("Oh no. We don't get to eat on {:?}?", day),
    }
}

fn main() {
    let (cordon_bleu, steak, sushi) = (Food::CordonBleu, Food::Steak, Food::Sushi);

    eat(cordon_bleu, Day::Monday);
    eat(steak, Day::Tuesday);
    eat(sushi, Day::Wednesday);
}
```
