# Suivi des emprunts à l'exécution avec RefCell`<T>`{=html}

Lors de la création de références immuables et mutables, nous utilisons respectivement la syntaxe `&` et `&mut`. Avec `RefCell<T>`, nous utilisons les méthodes `borrow` et `borrow_mut`, qui font partie de l'API sécurisée qui appartient à `RefCell<T>`. La méthode `borrow` renvoie le type de pointeur intelligent `Ref<T>`, et `borrow_mut` renvoie le type de pointeur intelligent `RefMut<T>`. Les deux types implémentent `Deref`, de sorte que nous pouvons les traiter comme des références normales.

`RefCell<T>` suit le nombre de pointeurs intelligents `Ref<T>` et `RefMut<T>` actuellement actifs. Chaque fois que nous appelons `borrow`, `RefCell<T>` augmente son compteur du nombre d'emprunts immuables actifs. Lorsqu'une valeur `Ref<T>` sort de portée, le compteur d'emprunts immuables diminue de 1. Tout comme les règles d'emprunt à la compilation, `RefCell<T>` nous permet d'avoir de nombreux emprunts immuables ou un emprunt mutable à n'importe quel moment.

Si nous essayons de violer ces règles, au lieu d'obtenir une erreur du compilateur comme nous le ferions avec les références, l'implémentation de `RefCell<T>` provoquera une panique à l'exécution. La liste 15-23 montre une modification de l'implémentation de `send` dans la liste 15-22. Nous essayons délibérément de créer deux emprunts mutables actifs pour la même portée pour illustrer que `RefCell<T>` nous empêche de le faire à l'exécution.

Nom de fichier : `src/lib.rs`

```rust
impl Messenger for MockMessenger {
    fn send(&self, message: &str) {
        let mut one_borrow = self.sent_messages.borrow_mut();
        let mut two_borrow = self.sent_messages.borrow_mut();

        one_borrow.push(String::from(message));
        two_borrow.push(String::from(message));
    }
}
```

Liste 15-23 : Création de deux références mutables dans la même portée pour voir que `RefCell<T>` provoquera une panique

Nous créons une variable `one_borrow` pour le pointeur intelligent `RefMut<T>` renvoyé par `borrow_mut`. Ensuite, nous créons un autre emprunt mutable de la même manière dans la variable `two_borrow`. Cela crée deux références mutables dans la même portée, ce qui n'est pas autorisé. Lorsque nous exécutons les tests de notre bibliothèque, le code de la liste 15-23 compilera sans erreur, mais le test échouera :

    ---- tests::it_sends_an_over_75_percent_warning_message stdout ----
    thread 'main' panicked at 'already borrowed: BorrowMutError', src/lib.rs:60:53
    note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace

Remarquez que le code a été interrompu avec le message `already borrowed: BorrowMutError`. C'est ainsi que `RefCell<T>` gère les violations des règles d'emprunt à l'exécution.

Choisir de capturer les erreurs d'emprunt à l'exécution plutôt qu'à la compilation, comme nous l'avons fait ici, signifie que vous risquez de découvrir des erreurs dans votre code plus tard dans le processus de développement : peut-être pas avant que votre code ne soit déployé en production. De plus, votre code subira une légère pénalité de performance à l'exécution en raison du suivi des emprunts à l'exécution plutôt qu'à la compilation. Cependant, l'utilisation de `RefCell<T>` permet d'écrire un objet de mock qui peut se modifier pour suivre les messages qu'il a reçus tandis que vous l'utilisez dans un contexte où seulement des valeurs immuables sont autorisées. Vous pouvez utiliser `RefCell<T>` malgré ses inconvénients pour obtenir plus de fonctionnalité que les références normales ne le permettent.
