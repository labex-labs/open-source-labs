# Combinateurs : `and_then`

`map()` a été décrit comme un moyen chaînable de simplifier les instructions `match`. Cependant, utiliser `map()` sur une fonction qui renvoie un `Option<T>` conduit à l'imbrication `Option<Option<T>>`. Enchaîner plusieurs appels peut alors devenir confus. C'est là que vient un autre combinateur appelé `and_then()`, connu dans certains langages sous le nom de flatmap.

`and_then()` appelle sa fonction d'entrée avec la valeur encapsulée et renvoie le résultat. Si l'`Option` est `None`, alors elle renvoie `None` à la place.

Dans l'exemple suivant, `cookable_v3()` renvoie un `Option<Food>`. Utiliser `map()` au lieu de `and_then()` aurait donné un `Option<Option<Food>>`, qui est un type invalide pour `eat()`.

```rust
#![allow(dead_code)]

#[derive(Debug)] enum Food { CordonBleu, Steak, Sushi }
#[derive(Debug)] enum Day { Monday, Tuesday, Wednesday }

// Nous n'avons pas les ingrédients pour faire du Sushi.
fn have_ingredients(food: Food) -> Option<Food> {
    match food {
        Food::Sushi => None,
        _           => Some(food),
    }
}

// Nous avons la recette pour tout, sauf le Cordon Bleu.
fn have_recipe(food: Food) -> Option<Food> {
    match food {
        Food::CordonBleu => None,
        _                => Some(food),
    }
}

// Pour préparer un plat, nous avons besoin à la fois de la recette et des ingrédients.
// Nous pouvons représenter la logique avec une chaîne d'`match` :
fn cookable_v1(food: Food) -> Option<Food> {
    match have_recipe(food) {
        None       => None,
        Some(food) => have_ingredients(food),
    }
}

// Cela peut être commodément réécrit de manière plus compacte avec `and_then()` :
fn cookable_v3(food: Food) -> Option<Food> {
    have_recipe(food).and_then(have_ingredients)
}

// Sinon, nous devrions `flatten()` un `Option<Option<Food>>`
// pour obtenir un `Option<Food>` :
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
