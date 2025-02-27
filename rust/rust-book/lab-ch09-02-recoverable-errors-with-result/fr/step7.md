# Where the? Operator Can Be Used

L'opérateur `?` ne peut être utilisé que dans des fonctions dont le type de retour est compatible avec la valeur sur laquelle l'opérateur `?` est utilisé. C'est parce que l'opérateur `?` est défini pour effectuer un retour anticipé d'une valeur hors de la fonction, de la même manière que l'expression `match` que nous avons définie dans la liste 9-6. Dans la liste 9-6, le `match` utilisait une valeur `Result`, et le bras de retour anticipé renvoyait une valeur `Err(e)`. Le type de retour de la fonction doit être un `Result` pour être compatible avec ce `return`.

Dans la liste 9-10, regardons l'erreur que nous obtiendrons si nous utilisons l'opérateur `?` dans une fonction `main` dont le type de retour est incompatible avec le type de la valeur sur laquelle nous utilisons `?`.

Nom du fichier : `src/main.rs`

```rust
use std::fs::File;

fn main() {
    let greeting_file = File::open("hello.txt")?;
}
```

Liste 9-10 : Tentative d'utilisation de `?` dans la fonction `main` qui renvoie `()` ne compilera pas.

Ce code ouvre un fichier, ce qui peut échouer. L'opérateur `?` suit la valeur `Result` renvoyée par `File::open`, mais cette fonction `main` a le type de retour `()`, pas `Result`. Lorsque nous compilons ce code, nous obtenons le message d'erreur suivant :

```bash
error[E0277]: the `?` operator can only be used in a function that returns
`Result` or `Option` (or another type that implements `FromResidual`)
 --> src/main.rs:4:48
  |
3 | / fn main() {
4 | |     let greeting_file = File::open("hello.txt")?;
  | |                                                ^ cannot use the `?`
operator in a function that returns `()`
5 | | }
  | |_- this function should return `Result` or `Option` to accept `?`
  |
  = help: the trait `FromResidual<Result<Infallible, std::io::Error>>` is not
implemented for `()`
```

Ce message d'erreur indique que nous ne sommes autorisés à utiliser l'opérateur `?` que dans une fonction qui renvoie `Result`, `Option` ou un autre type qui implémente `FromResidual`.

Pour corriger l'erreur, vous avez deux choix. Un choix est de changer le type de retour de votre fonction pour qu'il soit compatible avec la valeur sur laquelle vous utilisez l'opérateur `?`, tant que vous n'avez pas de restrictions empêchant cela. L'autre choix est d'utiliser un `match` ou l'une des méthodes de `Result<T, E>` pour gérer le `Result<T, E>` de la manière appropriée.

Le message d'erreur a également mentionné que `?` peut également être utilisé avec des valeurs `Option<T>`. Comme pour utiliser `?` sur `Result`, vous ne pouvez utiliser `?` sur `Option` que dans une fonction qui renvoie une `Option`. Le comportement de l'opérateur `?` lorsqu'il est appelé sur une `Option<T>` est similaire à son comportement lorsqu'il est appelé sur un `Result<T, E>` : si la valeur est `None`, le `None` sera renvoyé anticipément depuis la fonction à ce moment-là. Si la valeur est `Some`, la valeur à l'intérieur du `Some` est la valeur résultante de l'expression, et la fonction continue. La liste 9-11 a un exemple d'une fonction qui trouve le dernier caractère de la première ligne dans le texte donné.

```rust
fn last_char_of_first_line(text: &str) -> Option<char> {
    text.lines().next()?.chars().last()
}
```

Liste 9-11 : Utilisation de l'opérateur `?` sur une valeur `Option<T>`

Cette fonction renvoie `Option<char>` parce qu'il est possible qu'il y ait un caractère là, mais il est également possible qu'il n'y en ait pas. Ce code prend l'argument `text` de type `&str` et appelle la méthode `lines` dessus, qui renvoie un itérateur sur les lignes du texte. Comme cette fonction veut examiner la première ligne, elle appelle `next` sur l'itérateur pour obtenir la première valeur de l'itérateur. Si `text` est une chaîne de caractères vide, cet appel à `next` renverra `None`, auquel cas nous utilisons `?` pour arrêter et renvoyer `None` depuis `last_char_of_first_line`. Si `text` n'est pas une chaîne de caractères vide, `next` renverra une valeur `Some` contenant une tranche de chaîne de la première ligne dans `text`.

Le `?` extrait la tranche de chaîne, et nous pouvons appeler `chars` sur cette tranche de chaîne pour obtenir un itérateur de ses caractères. Nous sommes intéressés par le dernier caractère dans cette première ligne, donc nous appelons `last` pour renvoyer le dernier élément de l'itérateur. Ceci est une `Option` parce que la première ligne peut être une chaîne de caractères vide ; par exemple, si `text` commence par une ligne vide mais contient des caractères sur d'autres lignes, comme dans `"\nhi"`. Cependant, s'il y a un dernier caractère sur la première ligne, il sera renvoyé dans la variante `Some`. L'opérateur `?` au milieu nous donne une manière concise d'exprimer cette logique, nous permettant d'implémenter la fonction en une seule ligne. Si nous ne pouvions pas utiliser l'opérateur `?` sur `Option`, nous devrions implémenter cette logique en utilisant plus d'appels de méthodes ou une expression `match`.

Notez que vous pouvez utiliser l'opérateur `?` sur un `Result` dans une fonction qui renvoie `Result`, et vous pouvez utiliser l'opérateur `?` sur une `Option` dans une fonction qui renvoie `Option`, mais vous ne pouvez pas mélanger. L'opérateur `?` ne convertit pas automatiquement un `Result` en une `Option` ou vice versa ; dans ces cas, vous pouvez utiliser des méthodes telles que la méthode `ok` sur `Result` ou la méthode `ok_or` sur `Option` pour effectuer la conversion explicitement.

Jusqu'à présent, toutes les fonctions `main` que nous avons utilisées renvoient `()`. La fonction `main` est spéciale parce qu'elle est le point d'entrée et de sortie d'un programme exécutable, et il y a des restrictions sur le type de retour qu'elle peut avoir pour que le programme se comporte comme prévu.

Heureusement, `main` peut également renvoyer un `Result<(), E>`. La liste 9-12 a le code de la liste 9-10, mais nous avons changé le type de retour de `main` pour qu'il soit `Result<(), Box<dyn Error>>` et ajouté une valeur de retour `Ok(())` à la fin. Ce code compilera désormais.

Nom du fichier : `src/main.rs`

```rust
use std::error::Error;
use std::fs::File;

fn main() -> Result<(), Box<dyn Error>> {
    let greeting_file = File::open("hello.txt")?;

    Ok(())
}
```

Liste 9-12 : Changement de `main` pour renvoyer `Result<(), E>` permet l'utilisation de l'opérateur `?` sur des valeurs `Result`.

Le type `Box<dyn Error>` est un _objet de trait_, dont nous parlerons dans "Utilisation d'objets de trait qui autorisent des valeurs de différents types". Pour l'instant, vous pouvez lire `Box<dyn Error>` comme signifiant "n'importe quel type d'erreur". Utiliser `?` sur une valeur `Result` dans une fonction `main` avec le type d'erreur `Box<dyn Error>` est autorisé car cela permet tout `Err` valeur d'être renvoyée anticipément. Même si le corps de cette fonction `main` ne renverra jamais d'erreurs que du type `std::io::Error`, en spécifiant `Box<dyn Error>`, cette signature continuera d'être correcte même si plus de code renvoyant d'autres erreurs est ajouté au corps de `main`.

Lorsqu'une fonction `main` renvoie un `Result<(), E>`, l'exécutable se terminera avec une valeur de `0` si `main` renvoie `Ok(())` et se terminera avec une valeur non nulle si `main` renvoie une valeur `Err`. Les exécutables écrits en C renvoient des entiers lorsqu'ils se terminent : les programmes qui se terminent avec succès renvoient l'entier `0`, et les programmes qui rencontrent une erreur renvoient un entier différent de `0`. Rust renvoie également des entiers depuis les exécutables pour être compatible avec cette convention.

La fonction `main` peut renvoyer tout type qui implémente le trait `std::process::Termination`, qui contient une fonction `report` qui renvoie un `ExitCode`. Consultez la documentation de la bibliothèque standard pour plus d'informations sur l'implémentation du trait `Termination` pour vos propres types.

Maintenant que nous avons discuté les détails de l'appel à `panic!` ou du retour de `Result`, revenons au sujet de la manière de décider laquelle est appropriée à utiliser dans chaque cas.
