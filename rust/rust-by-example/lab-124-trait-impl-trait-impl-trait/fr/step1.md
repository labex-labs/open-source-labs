# `impl Trait`

`impl Trait` peut être utilisé en deux emplacements :

1.  comme type d'argument
2.  comme type de retour

## Comme type d'argument

Si votre fonction est générique sur un trait mais que vous n'avez pas besoin de spécifier le type exact, vous pouvez simplifier la déclaration de la fonction en utilisant `impl Trait` comme type de l'argument.

Par exemple, considérez le code suivant :

```rust
fn parse_csv_document<R: std::io::BufRead>(src: R) -> std::io::Result<Vec<Vec<String>>> {
    src.lines()
     .map(|line| {
            // Pour chaque ligne dans la source
            line.map(|line| {
                // Si la ligne a été lue avec succès, la traiter, sinon, retourner l'erreur
                line.split(',') // Diviser la ligne séparée par des virgules
                 .map(|entry| String::from(entry.trim())) // Supprimer les espaces blancs en début et en fin de ligne
                 .collect() // Collecter toutes les chaînes d'une ligne dans un Vec<String>
            })
        })
     .collect() // Collecter toutes les lignes dans un Vec<Vec<String>>
}
```

`parse_csv_document` est générique, ce qui lui permet de prendre n'importe quel type qui implémente `BufRead`, tel que `BufReader<File>` ou `[u8]`, mais le type de `R` n'est pas important et `R` est seulement utilisé pour déclarer le type de `src`, donc la fonction peut également être écrite comme suit :

```rust
fn parse_csv_document(src: impl std::io::BufRead) -> std::io::Result<Vec<Vec<String>>> {
    src.lines()
     .map(|line| {
            // Pour chaque ligne dans la source
            line.map(|line| {
                // Si la ligne a été lue avec succès, la traiter, sinon, retourner l'erreur
                line.split(',') // Diviser la ligne séparée par des virgules
                 .map(|entry| String::from(entry.trim())) // Supprimer les espaces blancs en début et en fin de ligne
                 .collect() // Collecter toutes les chaînes d'une ligne dans un Vec<String>
            })
        })
     .collect() // Collecter toutes les lignes dans un Vec<Vec<String>>
}
```

Notez que l'utilisation de `impl Trait` comme type d'argument signifie que vous ne pouvez pas spécifier explicitement quelle forme de la fonction vous utilisez, c'est-à-dire que `parse_csv_document::<std::io::Empty>(std::io::empty())` ne fonctionnera pas avec le second exemple.

## Comme type de retour

Si votre fonction renvoie un type qui implémente `MyTrait`, vous pouvez écrire son type de retour comme `-> impl MyTrait`. Cela peut grandement aider à simplifier vos signatures de type!

```rust
use std::iter;
use std::vec::IntoIter;

// Cette fonction combine deux `Vec<i32>` et renvoie un itérateur sur celui-ci.
// Regardez combien son type de retour est compliqué!
fn combine_vecs_explicit_return_type(
    v: Vec<i32>,
    u: Vec<i32>,
) -> iter::Cycle<iter::Chain<IntoIter<i32>, IntoIter<i32>>> {
    v.into_iter().chain(u.into_iter()).cycle()
}

// C'est exactement la même fonction, mais son type de retour utilise `impl Trait`.
// Regardez combien c'est plus simple!
fn combine_vecs(
    v: Vec<i32>,
    u: Vec<i32>,
) -> impl Iterator<Item=i32> {
    v.into_iter().chain(u.into_iter()).cycle()
}

fn main() {
    let v1 = vec![1, 2, 3];
    let v2 = vec![4, 5];
    let mut v3 = combine_vecs(v1, v2);
    assert_eq!(Some(1), v3.next());
    assert_eq!(Some(2), v3.next());
    assert_eq!(Some(3), v3.next());
    assert_eq!(Some(4), v3.next());
    assert_eq!(Some(5), v3.next());
    println!("tout fait");
}
```

Plus important, certains types Rust ne peuvent pas être écrits explicitement. Par exemple, chaque closure a son propre type concret non nommé. Avant la syntaxe `impl Trait`, vous deviez allouer sur le tas pour renvoyer une closure. Mais maintenant, vous pouvez le faire statiquement, comme ceci :

```rust
// Renvoie une fonction qui ajoute `y` à son entrée
fn make_adder_function(y: i32) -> impl Fn(i32) -> i32 {
    let closure = move |x: i32| { x + y };
    closure
}

fn main() {
    let plus_one = make_adder_function(1);
    assert_eq!(plus_one(2), 3);
}
```

Vous pouvez également utiliser `impl Trait` pour renvoyer un itérateur qui utilise des closures `map` ou `filter`! Cela facilite l'utilisation de `map` et `filter`. Parce que les types de closures n'ont pas de noms, vous ne pouvez pas écrire un type de retour explicite si votre fonction renvoie des itérateurs avec des closures. Mais avec `impl Trait`, vous pouvez le faire facilement :

```rust
fn double_positives<'a>(numbers: &'a Vec<i32>) -> impl Iterator<Item = i32> + 'a {
    numbers
     .iter()
     .filter(|x| x > &&0)
     .map(|x| x * 2)
}

fn main() {
    let singles = vec![-3, -2, 2, 3];
    let doubles = double_positives(&singles);
    assert_eq!(doubles.collect::<Vec<i32>>(), vec![4, 6]);
}
```
