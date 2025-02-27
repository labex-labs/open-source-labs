# Les boucles `for`

## `for` et plage

La construction `for in` peut être utilisée pour itérer sur un `Iterator`. L'une des façons les plus simples de créer un itérateur est d'utiliser la notation de plage `a..b`. Cela produit des valeurs de `a` (inclus) à `b` (exclus) par pas de un.

Écrivons FizzBuzz en utilisant `for` au lieu de `while`.

```rust
fn main() {
    // `n` prendra les valeurs : 1, 2,..., 100 à chaque itération
    for n in 1..101 {
        if n % 15 == 0 {
            println!("fizzbuzz");
        } else if n % 3 == 0 {
            println!("fizz");
        } else if n % 5 == 0 {
            println!("buzz");
        } else {
            println!("{}", n);
        }
    }
}
```

Alternativement, `a..=b` peut être utilisé pour une plage qui est inclusive des deux extrémités. Le code ci-dessus peut être écrit comme ceci :

```rust
fn main() {
    // `n` prendra les valeurs : 1, 2,..., 100 à chaque itération
    for n in 1..=100 {
        if n % 15 == 0 {
            println!("fizzbuzz");
        } else if n % 3 == 0 {
            println!("fizz");
        } else if n % 5 == 0 {
            println!("buzz");
        } else {
            println!("{}", n);
        }
    }
}
```

## `for` et itérateurs

La construction `for in` est capable d'interagir avec un `Iterator` de plusieurs manières. Comme discuté dans la section sur le trait `Iterator`, par défaut, la boucle `for` appliquera la fonction `into_iter` à la collection. Cependant, ce n'est pas le seul moyen de convertir des collections en itérateurs.

`into_iter`, `iter` et `iter_mut` gèrent tous la conversion d'une collection en itérateur de différentes manières, en offrant des vues différentes sur les données à l'intérieur.

- `iter` - Cela emprunte chaque élément de la collection à chaque itération. La collection reste donc inchangée et disponible pour être réutilisée après la boucle.

```rust
fn main() {
    let names = vec!["Bob", "Frank", "Ferris"];

    for name in names.iter() {
        match name {
            &"Ferris" => println!("There is a rustacean among us!"),
            // TODO ^ Essayez de supprimer le & et de matcher juste "Ferris"
            _ => println!("Hello {}", name),
        }
    }

    println!("names: {:?}", names);
}
```

- `into_iter` - Cela consomme la collection de sorte que les données exactes sont fournies à chaque itération. Une fois que la collection a été consommée, elle n'est plus disponible pour être réutilisée car elle a été'modifiée' dans la boucle.

```rust
fn main() {
    let names = vec!["Bob", "Frank", "Ferris"];

    for name in names.into_iter() {
        match name {
            "Ferris" => println!("There is a rustacean among us!"),
            _ => println!("Hello {}", name),
        }
    }

    println!("names: {:?}", names);
    // FIXME ^ Commenter cette ligne
}
```

- `iter_mut` - Cela emprunte mutuellement chaque élément de la collection, permettant de modifier la collection in situ.

```rust
fn main() {
    let mut names = vec!["Bob", "Frank", "Ferris"];

    for name in names.iter_mut() {
        *name = match name {
            &mut "Ferris" => "There is a rustacean among us!",
            _ => "Hello",
        }
    }

    println!("names: {:?}", names);
}
```

Dans les extraits de code ci-dessus, notez le type de branche `match`, qui est la différence clé dans les types d'itération. La différence de type implique bien sûr des actions différentes qui peuvent être effectuées.
