# Dans les définitions de fonctions

Lorsque nous définissons une fonction qui utilise des génériques, nous plaçons les génériques dans la signature de la fonction où nous spécifierions normalement les types de données des paramètres et de la valeur de retour. Cela rend notre code plus flexible et offre plus de fonctionnalités aux appelants de notre fonction tout en évitant la duplication de code.

En continuant avec notre fonction `largest`, la Liste 10-4 montre deux fonctions qui trouvent toutes la plus grande valeur dans une tranche. Nous allons ensuite les combiner en une seule fonction qui utilise des génériques.

Nom de fichier : `src/main.rs`

```rust
fn largest_i32(list: &[i32]) -> &i32 {
    let mut largest = &list[0];

    for item in list {
        if item > largest {
            largest = item;
        }
    }

    largest
}

fn largest_char(list: &[char]) -> &char {
    let mut largest = &list[0];

    for item in list {
        if item > largest {
            largest = item;
        }
    }

    largest
}

fn main() {
    let number_list = vec![34, 50, 25, 100, 65];

    let result = largest_i32(&number_list);
    println!("The largest number is {result}");

    let char_list = vec!['y','m', 'a', 'q'];

    let result = largest_char(&char_list);
    println!("The largest char is {result}");
}
```

Liste 10-4 : Deux fonctions qui ne diffèrent que par leur nom et les types de leurs signatures

La fonction `largest_i32` est celle que nous avons extraite dans la Liste 10-3 qui trouve le plus grand `i32` dans une tranche. La fonction `largest_char` trouve le plus grand `char` dans une tranche. Les corps des fonctions ont le même code, donc éliminons la duplication en introduisant un paramètre de type générique dans une seule fonction.

Pour paramétrer les types dans une nouvelle fonction unique, nous devons nommer le paramètre de type, tout comme nous le faisons pour les paramètres de valeur d'une fonction. Vous pouvez utiliser n'importe quel identifiant comme nom de paramètre de type. Mais nous utiliserons `T` car, par convention, les noms de paramètres de type en Rust sont courts, souvent une seule lettre, et la convention de nommage des types en Rust est en CamelCase. Court pour _type_, `T` est le choix par défaut de la plupart des programmeurs Rust.

Lorsque nous utilisons un paramètre dans le corps de la fonction, nous devons déclarer le nom du paramètre dans la signature pour que le compilateur sache ce que signifie ce nom. De même, lorsque nous utilisons un nom de paramètre de type dans une signature de fonction, nous devons déclarer le nom du paramètre de type avant de l'utiliser. Pour définir la fonction générique `largest`, nous plaçons les déclarations de noms de type entre crochets angulaires, `< >`, entre le nom de la fonction et la liste de paramètres, comme ceci :

```rust
fn largest<T>(list: &[T]) -> &T {
```

Nous lisons cette définition comme suit : la fonction `largest` est générique sur un certain type `T`. Cette fonction a un paramètre nommé `list`, qui est une tranche de valeurs du type `T`. La fonction `largest` retournera une référence à une valeur du même type `T`.

La Liste 10-5 montre la définition combinée de la fonction `largest` utilisant le type de données générique dans sa signature. La liste montre également comment nous pouvons appeler la fonction avec une tranche de valeurs `i32` ou de valeurs `char`. Notez que ce code ne compilera pas encore, mais nous le corrigerons plus tard dans ce chapitre.

Nom de fichier : `src/main.rs`

```rust
fn largest<T>(list: &[T]) -> &T {
    let mut largest = &list[0];

    for item in list {
        if item > largest {
            largest = item;
        }
    }

    largest
}

fn main() {
    let number_list = vec![34, 50, 25, 100, 65];

    let result = largest(&number_list);
    println!("The largest number is {result}");

    let char_list = vec!['y','m', 'a', 'q'];

    let result = largest(&char_list);
    println!("The largest char is {result}");
}
```

Liste 10-5 : La fonction `largest` utilisant des paramètres de type générique ; ceci ne compile pas encore

Si nous compilons ce code maintenant, nous obtiendrons cette erreur :

```bash
error[E0369]: binary operation `>` cannot be applied to type `&T`
 --> src/main.rs:5:17
  |
5 |         if item > largest {
  |            ---- ^ ------- &T
  |            |
  |            &T
  |
help: consider restricting type parameter `T`
  |
1 | fn largest<T: std::cmp::PartialOrd>(list: &[T]) -> &T {
  |             ++++++++++++++++++++++
```

Le texte d'aide mentionne `std::cmp::PartialOrd`, qui est un _trait_, et nous allons parler des traits dans la section suivante. Pour l'instant, sachez que cet avertissement indique que le corps de `largest` ne fonctionnera pas pour tous les types possibles que `T` pourrait être. Parce que nous voulons comparer des valeurs du type `T` dans le corps, nous ne pouvons utiliser que des types dont les valeurs peuvent être ordonnées. Pour autoriser les comparaisons, la bibliothèque standard a le trait `std::cmp::PartialOrd` que vous pouvez implémenter sur des types (voir l'Annexe C pour en savoir plus sur ce trait). En suivant la suggestion du texte d'aide, nous restreignons les types valides pour `T` à ceux qui implémentent `PartialOrd` et cet exemple compilera, car la bibliothèque standard implémente `PartialOrd` sur `i32` et `char`.
