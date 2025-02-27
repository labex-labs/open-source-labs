# Concatenation with the + Operator or the format! Macro

Souvent, vous voudrez combiner deux chaînes de caractères existantes. Une manière de le faire est d'utiliser l'opérateur `+`, comme montré dans la Liste 8-18.

```rust
let s1 = String::from("Hello, ");
let s2 = String::from("world!");
let s3 = s1 + &s2; // note s1 a été déplacé ici et ne peut plus être utilisé
```

Liste 8-18: Utilisation de l'opérateur `+` pour combiner deux valeurs `String` en une nouvelle valeur `String`

La chaîne de caractères `s3` contiendra `Hello, world!`. La raison pour laquelle `s1` n'est plus valide après l'addition, et la raison pour laquelle nous avons utilisé une référence à `s2`, est liée à la signature de la méthode appelée lorsque nous utilisons l'opérateur `+`. L'opérateur `+` utilise la méthode `add`, dont la signature ressemble à ceci :

```rust
fn add(self, s: &str) -> String {
```

Dans la bibliothèque standard, vous verrez `add` définie à l'aide de types génériques et de types associés. Ici, nous avons remplacé les types concrets, ce qui se produit lorsque nous appelons cette méthode avec des valeurs `String`. Nous aborderons les types génériques au chapitre 10. Cette signature nous donne les indices dont nous avons besoin pour comprendre les points délicats de l'opérateur `+`.

Tout d'abord, `s2` a un `&`, ce qui signifie que nous ajoutons une _référence_ de la deuxième chaîne de caractères à la première chaîne de caractères. C'est en raison du paramètre `s` dans la fonction `add` : nous ne pouvons ajouter qu'un `&str` à une `String` ; nous ne pouvons pas additionner deux valeurs `String` ensemble. Mais attendez - le type de `&s2` est `&String`, et non `&str`, comme spécifié dans le deuxième paramètre de `add`. Alors pourquoi la Liste 8-18 compile-t-elle?

La raison pour laquelle nous pouvons utiliser `&s2` dans l'appel à `add` est que le compilateur peut _coercer_ l'argument `&String` en un `&str`. Lorsque nous appelons la méthode `add`, Rust utilise une _coercition de déréférencement_, qui ici transforme `&s2` en `&s2[..]`. Nous aborderons la coercition de déréférencement plus en détail au chapitre 15. Comme `add` ne prend pas la propriété du paramètre `s`, `s2` sera toujours une `String` valide après cette opération.

Deuxièmement, nous pouvons voir dans la signature que `add` prend la propriété de `self` car `self` n'a pas d'`&`. Cela signifie que `s1` dans la Liste 8-18 sera déplacé dans l'appel à `add` et ne sera plus valide après cela. Ainsi, bien que `let s3 = s1 + &s2;` semble copier les deux chaînes de caractères et créer une nouvelle, cette instruction prend effectivement la propriété de `s1`, ajoute une copie du contenu de `s2`, puis renvoie la propriété du résultat. En d'autres termes, il semble qu'elle fasse beaucoup de copies, mais ce n'est pas le cas ; l'implémentation est plus efficace que la copie.

Si nous devons concaténer plusieurs chaînes de caractères, le comportement de l'opérateur `+` devient difficile à gérer :

```rust
let s1 = String::from("tic");
let s2 = String::from("tac");
let s3 = String::from("toe");

let s = s1 + "-" + &s2 + "-" + &s3;
```

À ce stade, `s` sera `tic-tac-toe`. Avec tous les caractères `+` et `"`, il est difficile de voir ce qui se passe. Pour combiner les chaînes de caractères de manière plus complexe, nous pouvons au lieu de cela utiliser la macro `format!` :

```rust
let s1 = String::from("tic");
let s2 = String::from("tac");
let s3 = String::from("toe");

let s = format!("{s1}-{s2}-{s3}");
```

Ce code définit également `s` sur `tic-tac-toe`. La macro `format!` fonctionne comme `println!`, mais au lieu d'afficher la sortie à l'écran, elle renvoie une `String` avec le contenu. La version du code utilisant `format!` est beaucoup plus facile à lire, et le code généré par la macro `format!` utilise des références de sorte que cet appel ne prenne pas la propriété de l'un de ses paramètres.
