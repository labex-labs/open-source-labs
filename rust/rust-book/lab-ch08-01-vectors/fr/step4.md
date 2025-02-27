# Reading Elements of Vectors

Il existe deux manières de référencer une valeur stockée dans un vecteur : via l'indexation ou en utilisant la méthode `get`. Dans les exemples suivants, nous avons annoté les types des valeurs qui sont renvoyées par ces fonctions pour plus de clarté.

La Liste 8-4 montre les deux méthodes d'accès à une valeur dans un vecteur, avec la syntaxe d'indexation et la méthode `get`.

```rust
let v = vec![1, 2, 3, 4, 5];

1 let third: &i32 = &v[2];
println!("The third element is {third}");

2 let third: Option<&i32> = v.get(2);
match third  {
    Some(third) => println!("The third element is {third}"),
    None => println!("There is no third element."),
}
```

Liste 8-4: Utilisation de la syntaxe d'indexation et de la méthode `get` pour accéder à un élément dans un vecteur

Notez quelques détails ici. Nous utilisons la valeur d'index `2` pour obtenir le troisième élément \[1\] car les vecteurs sont indexés par numéro, en commençant à zéro. En utilisant `&` et `[]`, nous obtenons une référence à l'élément à la valeur d'index. Lorsque nous utilisons la méthode `get` avec l'index passé en argument \[2\], nous obtenons un `Option<&T>` que nous pouvons utiliser avec `match`.

Rust fournit ces deux manières de référencer un élément afin que vous puissiez choisir comment le programme se comporte lorsque vous essayez d'utiliser une valeur d'index en dehors de la plage d'éléments existants. Par exemple, voyons ce qui se passe lorsque nous avons un vecteur de cinq éléments et que nous essayons ensuite d'accéder à un élément à l'index 100 avec chaque technique, comme montré dans la Liste 8-5.

```rust
let v = vec![1, 2, 3, 4, 5];

let does_not_exist = &v[100];
let does_not_exist = v.get(100);
```

Liste 8-5: Tentative d'accès à l'élément à l'index 100 dans un vecteur contenant cinq éléments

Lorsque nous exécutons ce code, la première méthode `[]` fera planter le programme car elle référence un élément qui n'existe pas. Cette méthode est la mieux adaptée lorsque vous voulez que votre programme plante si une tentative d'accès à un élément au-delà de la fin du vecteur est effectuée.

Lorsque la méthode `get` est passée un index qui est en dehors du vecteur, elle renvoie `None` sans planter. Vous utiliseriez cette méthode si l'accès à un élément au-delà de la plage du vecteur peut arriver occasionnellement dans les circonstances normales. Votre code devra alors avoir une logique pour gérer le fait d'avoir soit `Some(&element)` soit `None`, comme discuté au Chapitre 6. Par exemple, l'index pourrait provenir d'un utilisateur qui entre un nombre. S'ils entrent accidentellement un nombre trop grand et que le programme obtient une valeur `None`, vous pourriez dire à l'utilisateur combien d'éléments sont dans le vecteur actuel et leur donner une autre chance d'entrer une valeur valide. Cela serait plus convivial que de faire planter le programme en raison d'une erreur de frappe!

Lorsque le programme a une référence valide, le vérificateur d'emprunt applique les règles de propriété et d'emprunt (couvertes au Chapitre 4) pour vous assurer que cette référence et toute autre référence au contenu du vecteur restent valides. Rappelez-vous la règle qui stipule que vous ne pouvez pas avoir de références mutables et immuables dans la même portée. Cette règle s'applique dans la Liste 8-6, où nous avons une référence immutable au premier élément d'un vecteur et essayons d'ajouter un élément à la fin. Ce programme ne fonctionnera pas si nous essayons également de faire référence à cet élément plus tard dans la fonction.

```rust
let mut v = vec![1, 2, 3, 4, 5];

let first = &v[0];

v.push(6);

println!("The first element is: {first}");
```

Liste 8-6: Tentative d'ajouter un élément à un vecteur tout en maintenant une référence à un élément

La compilation de ce code entraînera cette erreur :

```bash
error[E0502]: cannot borrow `v` as mutable because it is also borrowed as
immutable
 --> src/main.rs:6:5
  |
4 |     let first = &v[0];
  |                  - immutable borrow occurs here
5 |
6 |     v.push(6);
  |     ^^^^^^^^^ mutable borrow occurs here
7 |
8 |     println!("The first element is: {first}");
  |                                      ----- immutable borrow later used here
```

Le code dans la Liste 8-6 peut sembler fonctionner : pourquoi une référence au premier élément devrait-elle se soucier des changements à la fin du vecteur? Cette erreur est due à la manière dont les vecteurs fonctionnent : car les vecteurs placent les valeurs les unes à côté des autres en mémoire, ajouter un nouvel élément à la fin du vecteur peut nécessiter d'allouer de nouvelles mémoires et de copier les anciens éléments dans le nouvel espace, s'il n'y a pas assez de place pour placer tous les éléments les uns à côté des autres où le vecteur est actuellement stocké. Dans ce cas, la référence au premier élément pointerait vers une mémoire désallouée. Les règles d'emprunt empêchent les programmes d'en arriver à cette situation.

> Note: Pour en savoir plus sur les détails d'implémentation du type `Vec<T>`, consultez "The Rustonomicon" à *https://doc.rust-lang.org/nomicon/vec/vec.html*.
