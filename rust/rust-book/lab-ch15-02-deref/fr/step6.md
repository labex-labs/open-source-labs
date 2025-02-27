# Implicit Deref Coercions with Functions and Methods

La _deref coercion_ convertit une référence à un type qui implémente le trait `Deref` en une référence à un autre type. Par exemple, la deref coercion peut convertir `&String` en `&str` car `String` implémente le trait `Deref` de manière à renvoyer `&str`. La deref coercion est une commodité que Rust applique aux arguments de fonctions et de méthodes, et ne fonctionne que sur les types qui implémentent le trait `Deref`. Elle se produit automatiquement lorsque nous passons une référence à une valeur d'un type particulier en tant qu'argument à une fonction ou à une méthode qui ne correspond pas au type de paramètre dans la définition de la fonction ou de la méthode. Une séquence d'appels à la méthode `deref` convertit le type que nous avons fourni en le type requis par le paramètre.

La deref coercion a été ajoutée à Rust afin que les programmeurs écrivant des appels de fonctions et de méthodes n'aient pas besoin d'ajouter autant de références et de déréférences explicites avec `&` et `*`. La fonction deref coercion nous permet également d'écrire plus de code qui peut fonctionner avec des références ou des pointeurs intelligents.

Pour voir la deref coercion en action, utilisons le type `MyBox<T>` que nous avons défini dans la Liste 15-8 ainsi que l'implémentation de `Deref` que nous avons ajoutée dans la Liste 15-10. La Liste 15-11 montre la définition d'une fonction qui a un paramètre de type slice de chaîne de caractères.

Nom du fichier : `src/main.rs`

```rust
fn hello(name: &str) {
    println!("Hello, {name}!");
}
```

Liste 15-11 : Une fonction `hello` qui a le paramètre `name` de type `&str`

Nous pouvons appeler la fonction `hello` avec une slice de chaîne de caractères en tant qu'argument, par exemple `hello("Rust");`. La deref coercion permet d'appeler `hello` avec une référence à une valeur de type `MyBox<String>`, comme montré dans la Liste 15-12.

Nom du fichier : `src/main.rs`

```rust
fn main() {
    let m = MyBox::new(String::from("Rust"));
    hello(&m);
}
```

Liste 15-12 : Appel de `hello` avec une référence à une valeur `MyBox<String>`, qui fonctionne grâce à la deref coercion

Ici, nous appelons la fonction `hello` avec l'argument `&m`, qui est une référence à une valeur `MyBox<String>`. En raison de l'implémentation du trait `Deref` sur `MyBox<T>` dans la Liste 15-10, Rust peut convertir `&MyBox<String>` en `&String` en appelant `deref`. La bibliothèque standard fournit une implémentation de `Deref` sur `String` qui renvoie une slice de chaîne de caractères, et cela est dans la documentation API de `Deref`. Rust appelle `deref` à nouveau pour convertir le `&String` en `&str`, qui correspond à la définition de la fonction `hello`.

Si Rust n'avait pas implémenté la deref coercion, nous aurions dû écrire le code de la Liste 15-13 au lieu du code de la Liste 15-12 pour appeler `hello` avec une valeur de type `&MyBox<String>`.

Nom du fichier : `src/main.rs`

```rust
fn main() {
    let m = MyBox::new(String::from("Rust"));
    hello(&(*m)[..]);
}
```

Liste 15-13 : Le code que nous aurions dû écrire si Rust n'avait pas la deref coercion

Le `(*m)` déréférence le `MyBox<String>` en une `String`. Ensuite, le `&` et `[..]` prennent une slice de chaîne de caractères de la `String` qui est égale à la chaîne entière pour correspondre à la signature de `hello`. Ce code sans deref coercion est plus difficile à lire, à écrire et à comprendre avec tous ces symboles en jeu. La deref coercion permet à Rust de gérer automatiquement ces conversions pour nous.

Lorsque le trait `Deref` est défini pour les types impliqués, Rust analysera les types et utilisera `Deref::deref` autant de fois que nécessaire pour obtenir une référence qui corresponde au type du paramètre. Le nombre de fois où `Deref::deref` doit être inséré est résolu à la compilation, donc il n'y a pas de pénalité exécution pour profiter de la deref coercion!
