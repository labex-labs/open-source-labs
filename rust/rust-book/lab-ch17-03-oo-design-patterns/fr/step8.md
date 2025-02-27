# Encodage des états et du comportement sous forme de types

Nous allons vous montrer comment repenser le patron d'état pour obtenir un autre ensemble de choix de compromis. Au lieu d'encapsuler complètement les états et les transitions de sorte que le code externe n'en ait aucune connaissance, nous allons encoder les états dans différents types. En conséquence, le système de vérification de type de Rust empêchera les tentatives d'utilisation de publications brouillons là où seulement les publications publiées sont autorisées en émettant une erreur de compilation.

Considérons la première partie de `main` dans le Listing 17-11 :

Nom de fichier : `src/main.rs`

```rust
fn main() {
    let mut post = Post::new();

    post.add_text("I ate a salad for lunch today");
    assert_eq!("", post.content());
}
```

Nous continuons à autoriser la création de nouvelles publications dans l'état brouillon en utilisant `Post::new` et la possibilité d'ajouter du texte au contenu de la publication. Mais au lieu d'avoir une méthode `content` sur une publication brouillon qui renvoie une chaîne de caractères vide, nous allons faire en sorte que les publications brouillons n'aient pas la méthode `content` du tout. Ainsi, si nous essayons d'obtenir le contenu d'une publication brouillon, nous obtiendrons une erreur de compilation nous disant que la méthode n'existe pas. En conséquence, il sera impossible pour nous d'afficher accidentellement le contenu d'une publication brouillon en production car ce code ne compilera même pas. Le Listing 17-19 montre la définition d'un struct `Post` et d'un struct `DraftPost`, ainsi que les méthodes sur chacun d'eux.

Nom de fichier : `src/lib.rs`

```rust
pub struct Post {
    content: String,
}

pub struct DraftPost {
    content: String,
}

impl Post {
  1 pub fn new() -> DraftPost {
        DraftPost {
            content: String::new(),
        }
    }

  2 pub fn content(&self) -> &str {
        &self.content
    }
}

impl DraftPost {
  3 pub fn add_text(&mut self, text: &str) {
        self.content.push_str(text);
    }
}
```

Listing 17-19 : Un `Post` avec une méthode `content` et un `DraftPost` sans méthode `content`

Les structs `Post` et `DraftPost` ont tous deux un champ privé `content` qui stocke le texte du billet de blog. Les structs n'ont plus le champ `state` car nous déplaçons l'encodage de l'état vers les types des structs. Le struct `Post` représentera une publication publiée, et il a une méthode `content` qui renvoie le `content` \[2\].

Nous avons toujours une fonction `Post::new`, mais au lieu de renvoyer une instance de `Post`, elle renvoie une instance de `DraftPost` \[1\]. Étant donné que `content` est privé et qu'il n'y a pas de fonctions qui renvoient `Post`, il n'est pas possible de créer une instance de `Post` pour le moment.

Le struct `DraftPost` a une méthode `add_text`, de sorte que nous pouvons ajouter du texte à `content` comme avant \[3\], mais notez que `DraftPost` n'a pas de méthode `content` définie! Ainsi, le programme garantit maintenant que toutes les publications commencent comme des publications brouillons, et que le contenu des publications brouillons n'est pas disponible pour l'affichage. Toute tentative de contourner ces contraintes entraînera une erreur de compilation.
