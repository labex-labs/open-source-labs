# Demande d'une révision qui change l'état de la publication

Ensuite, nous devons ajouter une fonctionnalité pour demander une révision d'une publication, ce qui devrait changer son état de `Draft` à `PendingReview`. Le Listing 17-15 montre ce code.

Nom de fichier : `src/lib.rs`

```rust
impl Post {
    --snip--
  1 pub fn request_review(&mut self) {
      2 if let Some(s) = self.state.take() {
          3 self.state = Some(s.request_review())
        }
    }
}

trait State {
  4 fn request_review(self: Box<Self>) -> Box<dyn State>;
}

struct Draft {}

impl State for Draft {
    fn request_review(self: Box<Self>) -> Box<dyn State> {
      5 Box::new(PendingReview {})
    }
}

struct PendingReview {}

impl State for PendingReview {
    fn request_review(self: Box<Self>) -> Box<dyn State> {
      6 self
    }
}
```

Listing 17-15 : Implémentation des méthodes `request_review` sur `Post` et le trait `State`

Nous donnons à `Post` une méthode publique nommée `request_review` qui prendra une référence mutable à `self` \[1\]. Ensuite, nous appelons une méthode interne `request_review` sur l'état actuel de `Post` \[3\], et cette deuxième méthode `request_review` consomme l'état actuel et renvoie un nouvel état.

Nous ajoutons la méthode `request_review` au trait `State` \[4\] ; tous les types qui implémentent le trait devront désormais implémenter la méthode `request_review`. Notez que plutôt que d'avoir `self`, `&self` ou `&mut self` comme premier paramètre de la méthode, nous avons `self: Box<Self>`. Cette syntaxe signifie que la méthode n'est valide que lorsqu'elle est appelée sur une `Box` contenant le type. Cette syntaxe prend la propriété de `Box<Self>`, invalidant l'ancien état afin que la valeur d'état de `Post` puisse se transformer en un nouvel état.

Pour consommer l'ancien état, la méthode `request_review` doit prendre la propriété de la valeur d'état. C'est là que l'`Option` dans le champ `state` de `Post` intervient : nous appelons la méthode `take` pour extraire la valeur `Some` du champ `state` et laisser un `None` à sa place car Rust ne nous permet pas d'avoir des champs non initialisés dans les structs \[2\]. Cela nous permet de déplacer la valeur `state` hors de `Post` plutôt que de la prêter. Ensuite, nous définirons la valeur d'état de la publication sur le résultat de cette opération.

Nous devons définir `state` sur `None` temporairement plutôt que de le définir directement avec du code comme `self.state = self.state.request_review();` pour obtenir la propriété de la valeur `state`. Cela garantit que `Post` ne peut pas utiliser l'ancienne valeur d'état après avoir été transformé en un nouvel état.

La méthode `request_review` sur `Draft` renvoie une nouvelle instance emballée d'un nouveau struct `PendingReview`, qui représente l'état lorsqu'une publication est en attente d'une révision \[5\]. Le struct `PendingReview` implémente également la méthode `request_review` mais ne fait aucune transformation. Au contraire, il renvoie lui-même \[6\] car lorsqu'on demande une révision d'une publication déjà dans l'état `PendingReview`, elle devrait rester dans l'état `PendingReview`.

Maintenant, nous commençons à voir les avantages du patron d'état : la méthode `request_review` sur `Post` est la même peu importe sa valeur d'état. Chaque état est responsable de ses propres règles.

Nous laisserons la méthode `content` sur `Post` inchangée, renvoyant une chaîne de caractères vide. Maintenant, nous pouvons avoir un `Post` dans l'état `PendingReview` ainsi que dans l'état `Draft`, mais nous voulons le même comportement dans l'état `PendingReview`. Le Listing 17-11 fonctionne désormais jusqu'à la ligne \[5\]!
