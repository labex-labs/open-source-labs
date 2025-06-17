# Correspondance avec Option`<T>`

Dans la section précédente, nous voulions extraire la valeur interne `T` dans le cas `Some` lorsqu'on utilise `Option<T>` ; nous pouvons également traiter `Option<T>` avec `match`, comme nous l'avons fait avec l'enum `Coin`! Au lieu de comparer des pièces, nous allons comparer les variantes de `Option<T>`, mais la manière dont fonctionne l'expression `match` reste la même.

Disons que nous voulons écrire une fonction qui prend une `Option<i32>` et, s'il y a une valeur à l'intérieur, ajoute 1 à cette valeur. S'il n'y a pas de valeur à l'intérieur, la fonction devrait renvoyer la valeur `None` et ne pas tenter d'effectuer aucune opération.

Cette fonction est très facile à écrire, grâce à `match`, et ressemblera à la liste 6-5.

```rust
fn plus_one(x: Option<i32>) -> Option<i32> {
    match x {
      1 None => None,
      2 Some(i) => Some(i + 1),
    }
}

let five = Some(5);
let six = plus_one(five); 3
let none = plus_one(None); 4
```

Liste 6-5 : Une fonction qui utilise une expression `match` sur une `Option<i32>`

Examnons plus en détail la première exécution de `plus_one`. Lorsque nous appelons `plus_one(five)` \[3\], la variable `x` dans le corps de `plus_one` aura la valeur `Some(5)`. Nous comparons ensuite cela avec chaque branche de correspondance :

```rust
None => None,
```

La valeur `Some(5)` ne correspond pas au modèle `None` \[1\], donc nous passons à la branche suivante :

```rust
Some(i) => Some(i + 1),
```

`Some(5)` correspond-il à `Some(i)` \[2\]? Oui, bien sûr! Nous avons la même variante. La variable `i` se lie à la valeur contenue dans `Some`, donc `i` prend la valeur `5`. Le code de la branche de correspondance est ensuite exécuté, donc nous ajoutons 1 à la valeur de `i` et créons une nouvelle valeur `Some` avec notre total `6` à l'intérieur.

Maintenant, considérons le second appel de `plus_one` dans la liste 6-5, où `x` est `None` \[4\]. Nous entrons dans la `match` et comparons avec la première branche \[1\].

Elle correspond! Il n'y a pas de valeur à laquelle ajouter, donc le programme s'arrête et renvoie la valeur `None` du côté droit de `=>`. Comme la première branche a correspondu, aucune autre branche n'est comparée.

La combinaison de `match` et d'enums est utile dans de nombreuses situations. Vous verrez ce modèle très souvent dans le code Rust : effectuer une correspondance sur un enum, lier une variable aux données à l'intérieur, puis exécuter du code en fonction de cela. C'est un peu difficile au début, mais une fois que vous vous y êtes habitué, vous souhaiterez l'avoir dans toutes les langues. C'est constamment un favori des utilisateurs.
