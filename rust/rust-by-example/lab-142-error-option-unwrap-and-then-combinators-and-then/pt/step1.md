# Combinadores: `and_then`

`map()` foi descrito como uma forma encadeável de simplificar as instruções `match`. No entanto, usar `map()` em uma função que retorna um `Option<T>` resulta no aninhamento `Option<Option<T>>`. Encadeando múltiplas chamadas juntas, isso pode se tornar confuso. É aí que entra outro combinador chamado `and_then()`, conhecido em algumas linguagens como flatmap.

`and_then()` chama sua função de entrada com o valor encapsulado e retorna o resultado. Se o `Option` for `None`, ele retorna `None` em vez disso.

No exemplo a seguir, `cookable_v3()` resulta em um `Option<Food>`. Usar `map()` em vez de `and_then()` teria dado um `Option<Option<Food>>`, que é um tipo inválido para `eat()`.

```rust
#![allow(dead_code)]

#[derive(Debug)] enum Food { CordonBleu, Steak, Sushi }
#[derive(Debug)] enum Day { Monday, Tuesday, Wednesday }

// We don't have the ingredients to make Sushi.
fn have_ingredients(food: Food) -> Option<Food> {
    match food {
        Food::Sushi => None,
        _           => Some(food),
    }
}

// We have the recipe for everything except Cordon Bleu.
fn have_recipe(food: Food) -> Option<Food> {
    match food {
        Food::CordonBleu => None,
        _                => Some(food),
    }
}

// To make a dish, we need both the recipe and the ingredients.
// We can represent the logic with a chain of `match`es:
fn cookable_v1(food: Food) -> Option<Food> {
    match have_recipe(food) {
        None       => None,
        Some(food) => have_ingredients(food),
    }
}

// This can conveniently be rewritten more compactly with `and_then()`:
fn cookable_v3(food: Food) -> Option<Food> {
    have_recipe(food).and_then(have_ingredients)
}

// Otherwise we'd need to `flatten()` an `Option<Option<Food>>`
// to get an `Option<Food>`:
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
