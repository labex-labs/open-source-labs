# Stockage du texte du contenu de la publication

Dans le Listing 17-11, nous avons vu que nous voulons être en mesure d'appeler une méthode nommée `add_text` et de lui passer une `&str` qui sera ensuite ajoutée comme contenu textuel de la publication de blog. Nous l'implémentons comme une méthode, plutôt que d'exposer le champ `content` en tant que `pub`, afin que plus tard nous puissions implémenter une méthode qui contrôlera la lecture des données du champ `content`. La méthode `add_text` est assez simple, donc ajoutons l'implémentation dans le Listing 17-13 au bloc `impl Post`.

Nom de fichier : `src/lib.rs`

```rust
impl Post {
    --snip--
    pub fn add_text(&mut self, text: &str) {
        self.content.push_str(text);
    }
}
```

Listing 17-13 : Implémentation de la méthode `add_text` pour ajouter du texte au `content` d'une publication

La méthode `add_text` prend une référence mutable à `self` car nous modifions l'instance de `Post` sur laquelle nous appelons `add_text`. Nous appelons ensuite `push_str` sur la `String` dans `content` et passons l'argument `text` pour l'ajouter au `content` enregistré. Ce comportement ne dépend pas de l'état de la publication, donc il n'est pas partie du patron d'état. La méthode `add_text` n'interagit pas du tout avec le champ `state`, mais elle fait partie du comportement que nous voulons prendre en charge.
