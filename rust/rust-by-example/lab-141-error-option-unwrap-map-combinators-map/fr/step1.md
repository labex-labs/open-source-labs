# Combinateurs : `map`

`match` est une méthode valide pour gérer les `Option`. Cependant, vous finirez peut-être par trouver qu'un usage intensif est fastidieux, en particulier avec des opérations valides uniquement pour une entrée. Dans ces cas, les combinateurs peuvent être utilisés pour gérer le flux de contrôle de manière modulaire.

`Option` a une méthode intégrée appelée `map()`, un combinateur pour la simple transformation de `Some -> Some` et `None -> None`. Plusieurs appels de `map()` peuvent être chaînés ensemble pour une plus grande flexibilité.

Dans l'exemple suivant, `process()` remplace toutes les fonctions précédentes tout en restant compact.

```rust
#![allow(dead_code)]

#[derive(Debug)] enum Food { Apple, Carrot, Potato }

#[derive(Debug)] struct Peeled(Food);
#[derive(Debug)] struct Chopped(Food);
#[derive(Debug)] struct Cooked(Food);

// Épluchez les aliments. S'il n'y en a pas, renvoyez `None`.
// Sinon, renvoyez l'aliment épluché.
fn peel(food: Option<Food>) -> Option<Peeled> {
    match food {
        Some(food) => Some(Peeled(food)),
        None       => None,
    }
}

// Coupez les aliments. S'il n'y en a pas, renvoyez `None`.
// Sinon, renvoyez l'aliment coupé.
fn chop(peeled: Option<Peeled>) -> Option<Chopped> {
    match peeled {
        Some(Peeled(food)) => Some(Chopped(food)),
        None               => None,
    }
}

// Cuisez les aliments. Ici, nous présentons `map()` au lieu de `match` pour la gestion des cas.
fn cook(chopped: Option<Chopped>) -> Option<Cooked> {
    chopped.map(|Chopped(food)| Cooked(food))
}

// Une fonction pour éplucher, couper et cuire les aliments dans cet ordre.
// Nous chainons plusieurs utilisations de `map()` pour simplifier le code.
fn process(food: Option<Food>) -> Option<Cooked> {
    food.map(|f| Peeled(f))
     .map(|Peeled(f)| Chopped(f))
     .map(|Chopped(f)| Cooked(f))
}

// Vérifiez s'il y a des aliments ou non avant d'essayer de les manger!
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
    // Essayons maintenant la plus simple `process()`.
    let cooked_potato = process(potato);

    eat(cooked_apple);
    eat(cooked_carrot);
    eat(cooked_potato);
}
```
