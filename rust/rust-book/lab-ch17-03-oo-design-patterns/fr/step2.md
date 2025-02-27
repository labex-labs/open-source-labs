# Définition de Post et création d'une nouvelle instance dans l'état brouillon

Commencons l'implémentation de la bibliothèque! Nous savons que nous avons besoin d'une structure publique `Post` qui contient du contenu, donc nous allons commencer par la définition de la structure et d'une fonction publique associée `new` pour créer une instance de `Post`, comme montré dans le Listing 17-12. Nous allons également créer un trait privé `State` qui définira le comportement que tous les objets d'état d'un `Post` doivent avoir.

Ensuite, `Post` contiendra un objet de trait `Box<dyn State>` dans un `Option<T>` dans un champ privé nommé `state` pour stocker l'objet d'état. Vous allez voir pourquoi l'`Option<T>` est nécessaire dans un instant.

Nom de fichier : `src/lib.rs`

```rust
pub struct Post {
    state: Option<Box<dyn State>>,
    content: String,
}

impl Post {
    pub fn new() -> Post {
        Post {
          1 state: Some(Box::new(Draft {})),
          2 content: String::new(),
        }
    }
}

trait State {}

struct Draft {}

impl State for Draft {}
```

Listing 17-12 : Définition d'une structure `Post` et d'une fonction `new` qui crée une nouvelle instance de `Post`, d'un trait `State` et d'une structure `Draft`

Le trait `State` définit le comportement partagé par différents états de publication. Les objets d'état sont `Draft`, `PendingReview` et `Published`, et ils implémenteront tous le trait `State`. Pour l'instant, le trait n'a pas de méthodes, et nous allons commencer par définir seulement l'état `Draft` car c'est l'état dans lequel nous voulons que commencent les publications.

Lorsque nous créons une nouvelle instance de `Post`, nous définissons son champ `state` sur une valeur `Some` qui contient une `Box` \[1\]. Cette `Box` pointe vers une nouvelle instance de la structure `Draft`. Cela garantit que chaque fois que nous créons une nouvelle instance de `Post`, elle commencera comme un brouillon. Étant donné que le champ `state` de `Post` est privé, il n'est pas possible de créer un `Post` dans un autre état! Dans la fonction `Post::new`, nous définissons le champ `content` sur une nouvelle chaîne de caractères vide `String` \[2\].
