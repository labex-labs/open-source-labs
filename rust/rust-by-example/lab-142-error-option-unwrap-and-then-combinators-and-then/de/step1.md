# Kombinatoren: `and_then`

`map()` wurde als eine kettenfähige Methode beschrieben, um `match`-Anweisungen zu vereinfachen. Wenn jedoch `map()` auf eine Funktion angewendet wird, die ein `Option<T>` zurückgibt, entsteht die verschachtelte `Option<Option<T>>`. Das Kettieren mehrerer Aufrufe kann dann verwirrend werden. Genau hier kommt ein anderer Kombinator namens `and_then()` (in einigen Sprachen auch als flatmap bekannt) ins Spiel.

`and_then()` ruft seine Funktionseingabe mit dem umschlossenen Wert auf und gibt das Ergebnis zurück. Wenn die `Option` `None` ist, gibt es stattdessen `None` zurück.

Im folgenden Beispiel liefert `cookable_v3()` ein `Option<Food>`. Die Verwendung von `map()` anstelle von `and_then()` hätte ein `Option<Option<Food>>` ergeben, was ein ungültiger Typ für `eat()` ist.

```rust
#![allow(dead_code)]

#[derive(Debug)] enum Food { CordonBleu, Steak, Sushi }
#[derive(Debug)] enum Day { Monday, Tuesday, Wednesday }

// Wir haben nicht die Zutaten, um Sushi zu machen.
fn have_ingredients(food: Food) -> Option<Food> {
    match food {
        Food::Sushi => None,
        _           => Some(food),
    }
}

// Wir haben das Rezept für alles außer Cordon Bleu.
fn have_recipe(food: Food) -> Option<Food> {
    match food {
        Food::CordonBleu => None,
        _                => Some(food),
    }
}

// Um ein Gericht zu machen, brauchen wir sowohl das Rezept als auch die Zutaten.
// Wir können die Logik mit einer Kette von `match`-Anweisungen darstellen:
fn cookable_v1(food: Food) -> Option<Food> {
    match have_recipe(food) {
        None       => None,
        Some(food) => have_ingredients(food),
    }
}

// Dies kann bequem kompakter mit `and_then()` umgeschrieben werden:
fn cookable_v3(food: Food) -> Option<Food> {
    have_recipe(food).and_then(have_ingredients)
}

// Ansonsten müssten wir ein `Option<Option<Food>>` mit `flatten()`
// zu einem `Option<Food>` reduzieren:
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
