# Exécution de code lors de la nettoyage avec le trait Drop

Le second trait important pour le modèle de pointeur intelligent est `Drop`, qui vous permet de personnaliser ce qui se passe lorsqu'une valeur est sur le point de sortir de portée. Vous pouvez fournir une implémentation pour le trait `Drop` sur n'importe quel type, et ce code peut être utilisé pour libérer des ressources telles que des fichiers ou des connexions réseau.

Nous présentons `Drop` dans le contexte des pointeurs intelligents car la fonctionnalité du trait `Drop` est presque toujours utilisée lors de la mise en œuvre d'un pointeur intelligent. Par exemple, lorsqu'un `Box<T>` est supprimé, il libérera l'espace sur le tas que le boîtier pointe.

Dans certains langages, pour certains types, le programmeur doit appeler du code pour libérer la mémoire ou les ressources chaque fois qu'il a fini d'utiliser une instance de ces types. Des exemples incluent les descripteurs de fichiers, les sockets et les verrous. Si ils oublient, le système peut être surchargé et planter. En Rust, vous pouvez spécifier qu'un certain morceau de code doit être exécuté chaque fois qu'une valeur sort de portée, et le compilateur insérera ce code automatiquement. Par conséquent, vous n'avez pas besoin d'être prudent pour placer le code de nettoyage partout dans un programme lorsque l'instance d'un type particulier est terminée - vous n'allez toujours pas laisser fuit des ressources!

Vous spécifiez le code à exécuter lorsqu'une valeur sort de portée en implémentant le trait `Drop`. Le trait `Drop` vous oblige à implémenter une méthode appelée `drop` qui prend une référence mutable à `self`. Pour voir quand Rust appelle `drop`, implémentons `drop` avec des instructions `println!` pour l'instant.

L'Listing 15-14 montre une structure `CustomSmartPointer` dont la seule fonctionnalité personnalisée est qu'elle imprimera `Dropping CustomSmartPointer!` lorsque l'instance sort de portée, pour montrer quand Rust exécute la méthode `drop`.

Nom de fichier : `src/main.rs`

```rust
struct CustomSmartPointer {
    data: String,
}

1 impl Drop for CustomSmartPointer {
    fn drop(&mut self) {
      2 println!(
            "Dropping CustomSmartPointer with data `{}`!",
            self.data
        );
    }
}

fn main() {
  3 let c = CustomSmartPointer {
        data: String::from("my stuff"),
    };
  4 let d = CustomSmartPointer {
        data: String::from("other stuff"),
    };
  5 println!("CustomSmartPointers created.");
6 }
```

Listing 15-14 : Une structure `CustomSmartPointer` qui implémente le trait `Drop` où nous placerions notre code de nettoyage

Le trait `Drop` est inclus dans le préambule, donc nous n'avons pas besoin de le porter dans la portée. Nous implémentons le trait `Drop` sur `CustomSmartPointer` \[1\] et fournissons une implémentation pour la méthode `drop` qui appelle `println!` \[2\]. Le corps de la méthode `drop` est où vous placeriez toute la logique que vous voulez exécuter lorsqu'une instance de votre type sort de portée. Nous imprimons ici du texte pour démontrer visuellement quand Rust appellera `drop`.

Dans `main`, nous créons deux instances de `CustomSmartPointer` à \[3\] et \[4\] puis imprimons `CustomSmartPointers created` \[5\]. À la fin de `main` \[6\], nos instances de `CustomSmartPointer` sortiront de portée, et Rust appellera le code que nous avons mis dans la méthode `drop` \[2\], imprimant notre message final. Notez que nous n'avons pas eu besoin d'appeler explicitement la méthode `drop`.

Lorsque nous exécutons ce programme, nous verrons la sortie suivante :

    CustomSmartPointers created.
    Dropping CustomSmartPointer with data `other stuff`!
    Dropping CustomSmartPointer with data `my stuff`!

Rust a automatiquement appelé `drop` pour nous lorsque nos instances sont sorties de portée, appelant le code que nous avons spécifié. Les variables sont supprimées dans l'ordre inverse de leur création, donc `d` a été supprimé avant `c`. Le but de cet exemple est de vous donner un guide visuel sur la façon dont la méthode `drop` fonctionne ; généralement, vous spécifieriez le code de nettoyage que votre type doit exécuter plutôt qu'un message d'impression.

Malheureusement, il n'est pas simple de désactiver la fonctionnalité `drop` automatique. Désactiver `drop` n'est généralement pas nécessaire ; le tout du trait `Drop` est qu'il est géré automatiquement. Parfois, cependant, vous voudrez peut-être nettoyer une valeur tôt. Un exemple est lorsqu'on utilise des pointeurs intelligents qui gèrent des verrous : vous voudriez peut-être forcer la méthode `drop` qui libère le verrou pour que d'autres codes dans la même portée puissent acquérir le verrou. Rust ne vous permet pas d'appeler la méthode `drop` du trait `Drop` manuellement ; au lieu de cela, vous devez appeler la fonction `std::mem::drop` fournie par la bibliothèque standard si vous voulez forcer une valeur à être supprimée avant la fin de sa portée.

Si nous essayons d'appeler manuellement la méthode `drop` du trait `Drop` en modifiant la fonction `main` de l'Listing 15-14, comme montré dans l'Listing 15-15, nous obtiendrons une erreur du compilateur.

Nom de fichier : `src/main.rs`

```rust
fn main() {
    let c = CustomSmartPointer {
        data: String::from("some data"),
    };
    println!("CustomSmartPointer created.");
    c.drop();
    println!(
        "CustomSmartPointer dropped before the end of main."
    );
}
```

Listing 15-15 : Tentative d'appeler la méthode `drop` du trait `Drop` manuellement pour nettoyer tôt

Lorsque nous essayons de compiler ce code, nous obtiendrons cette erreur :

```bash
error[E0040]: explicit use of destructor method
  --> src/main.rs:16:7
   |
16 |     c.drop();
   |     --^^^^--
   |     | |
   |     | explicit destructor calls not allowed
   |     help: consider using `drop` function: `drop(c)`
```

Ce message d'erreur indique que nous ne sommes pas autorisés à appeler explicitement `drop`. Le message d'erreur utilise le terme _destructeur_, qui est le terme de programmation général pour une fonction qui nettoie une instance. Un _destructeur_ est analogue à un _constructeur_, qui crée une instance. La fonction `drop` en Rust est un destructeur particulier.

Rust ne nous permet pas d'appeler `drop` explicitement car Rust appellerait toujours automatiquement `drop` sur la valeur à la fin de `main`. Cela entraînerait une erreur de _double libération_ car Rust essayerait de nettoyer la même valeur deux fois.

Nous ne pouvons pas désactiver l'insertion automatique de `drop` lorsqu'une valeur sort de portée, et nous ne pouvons pas appeler explicitement la méthode `drop`. Donc, si nous devons forcer une valeur à être nettoyée tôt, nous utilisons la fonction `std::mem::drop`.

La fonction `std::mem::drop` est différente de la méthode `drop` dans le trait `Drop`. Nous l'appelons en passant en argument la valeur que nous voulons forcer à être supprimée. La fonction est dans le préambule, donc nous pouvons modifier `main` dans l'Listing 15-15 pour appeler la fonction `drop`, comme montré dans l'Listing 15-16.

Nom de fichier : `src/main.rs`

```rust
fn main() {
    let c = CustomSmartPointer {
        data: String::from("some data"),
    };
    println!("CustomSmartPointer created.");
    drop(c);
    println!(
        "CustomSmartPointer dropped before the end of main."
    );
}
```

Listing 15-16 : Appel de `std::mem::drop` pour supprimer explicitement une valeur avant qu'elle sorte de portée

En exécutant ce code, on obtiendra l'affichage suivant :

    CustomSmartPointer created.
    Dropping CustomSmartPointer with data `some data`!
    CustomSmartPointer dropped before the end of main.

Le texte `Dropping CustomSmartPointer with data`some data`!` est imprimé entre le texte `CustomSmartPointer created.` et `CustomSmartPointer dropped before the end of main.`, montrant que le code de la méthode `drop` est appelé pour supprimer `c` à ce moment-là.

Vous pouvez utiliser le code spécifié dans une implémentation de trait `Drop` de nombreuses manières pour rendre le nettoyage pratique et sûr : par exemple, vous pourriez l'utiliser pour créer votre propre allocateur de mémoire! Avec le trait `Drop` et le système de propriété de Rust, vous n'avez pas besoin de vous souvenir de nettoyer car Rust le fait automatiquement.

Vous n'avez pas non plus à vous inquiéter des problèmes résultant d'un nettoyage accidentel de valeurs encore en cours d'utilisation : le système de propriété qui assure que les références sont toujours valides garantit également que `drop` est appelé seulement une fois lorsque la valeur n'est plus utilisée.

Maintenant que nous avons examiné `Box<T>` et certaines des caractéristiques des pointeurs intelligents, regardons quelques autres pointeurs intelligents définis dans la bibliothèque standard.
