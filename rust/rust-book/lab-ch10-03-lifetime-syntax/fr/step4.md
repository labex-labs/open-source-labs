# Generic Lifetimes in Functions

Nous allons écrire une fonction qui renvoie la plus longue des deux slices de chaîne de caractères. Cette fonction prendra deux slices de chaîne de caractères et renverra une seule slice de chaîne de caractères. Après avoir implémenté la fonction `longest`, le code de la Liste 10-19 devrait afficher `The longest string is abcd`.

Nom de fichier : `src/main.rs`

```rust
fn main() {
    let string1 = String::from("abcd");
    let string2 = "xyz";

    let result = longest(string1.as_str(), string2);
    println!("The longest string is {result}");
}
```

Liste 10-19: Une fonction `main` qui appelle la fonction `longest` pour trouver la plus longue des deux slices de chaîne de caractères

Notez que nous voulons que la fonction prenne des slices de chaîne de caractères, qui sont des références, plutôt que des chaînes de caractères, car nous ne voulons pas que la fonction `longest` prenne la propriété de ses paramètres. Consultez "String Slices as Parameters" pour plus de discussions sur pourquoi les paramètres que nous utilisons dans la Liste 10-19 sont les paramètres que nous voulons.

Si nous essayons d'implémenter la fonction `longest` comme indiqué dans la Liste 10-20, elle ne compilera pas.

Nom de fichier : `src/main.rs`

```rust
fn longest(x: &str, y: &str) -> &str {
    if x.len() > y.len() {
        x
    } else {
        y
    }
}
```

Liste 10-20: Une implémentation de la fonction `longest` qui renvoie la plus longue des deux slices de chaîne de caractères mais qui ne compile pas encore

Au lieu de cela, nous obtenons l'erreur suivante qui parle des durées de vie :

```bash
error[E0106]: missing lifetime specifier
 --> src/main.rs:9:33
  |
9 | fn longest(x: &str, y: &str) -> &str {
  |               ----     ----     ^ expected named lifetime parameter
  |
  = help: this function's return type contains a borrowed value,
but the signature does not say whether it is borrowed from `x` or `y`
help: consider introducing a named lifetime parameter
  |
9 | fn longest<'a>(x: &'a str, y: &'a str) -> &'a str {
  |           ++++     ++          ++          ++
```

Le texte d'aide révèle que le type de retour a besoin d'un paramètre de durée de vie générique car Rust ne peut pas dire si la référence renvoyée fait référence à `x` ou à `y`. En fait, nous ne savons pas non plus, car le bloc `if` dans le corps de cette fonction renvoie une référence à `x` et le bloc `else` renvoie une référence à `y`!

Lorsque nous définissons cette fonction, nous ne connaissons pas les valeurs concrètes qui seront passées à cette fonction, donc nous ne savons pas si le cas `if` ou le cas `else` s'exécutera. Nous ne connaissons pas non plus les durées de vie concrètes des références qui seront passées, donc nous ne pouvons pas examiner les portées comme nous l'avons fait dans les Listes 10-17 et 10-18 pour déterminer si la référence que nous renvoyons sera toujours valide. Le vérificateur d'emprunt ne peut pas non plus déterminer cela, car il ne sait pas comment les durées de vie de `x` et `y` sont liées à la durée de vie de la valeur de retour. Pour corriger cette erreur, nous allons ajouter des paramètres de durée de vie génériques qui définissent la relation entre les références afin que le vérificateur d'emprunt puisse effectuer son analyse.
