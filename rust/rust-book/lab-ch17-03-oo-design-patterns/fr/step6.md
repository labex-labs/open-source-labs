# Ajout de la méthode approve pour modifier le comportement de content

La méthode `approve` sera similaire à la méthode `request_review` : elle définira `state` sur la valeur que l'état actuel indique qu'il devrait avoir lorsqu'il est approuvé, comme montré dans le Listing 17-16.

Nom de fichier : `src/lib.rs`

```rust
impl Post {
    --snip--
    pub fn approve(&mut self) {
        if let Some(s) = self.state.take() {
            self.state = Some(s.approve())
        }
    }
}

trait State {
    fn request_review(self: Box<Self>) -> Box<dyn State>;
    fn approve(self: Box<Self>) -> Box<dyn State>;
}

struct Draft {}

impl State for Draft {
    --snip--
    fn approve(self: Box<Self>) -> Box<dyn State> {
      1 self
    }
}

struct PendingReview {}

impl State for PendingReview {
    --snip--
    fn approve(self: Box<Self>) -> Box<dyn State> {
      2 Box::new(Published {})
    }
}

struct Published {}

impl State for Published {
    fn request_review(self: Box<Self>) -> Box<dyn State> {
        self
    }

    fn approve(self: Box<Self>) -> Box<dyn State> {
        self
    }
}
```

Listing 17-16 : Implémentation de la méthode `approve` sur `Post` et le trait `State`

Nous ajoutons la méthode `approve` au trait `State` et ajoutons un nouveau struct qui implémente `State`, l'état `Published`.

De manière similaire à la façon dont `request_review` fonctionne sur `PendingReview`, si nous appelons la méthode `approve` sur un `Draft`, elle n'aura aucun effet car `approve` renverra `self` \[1\]. Lorsque nous appelons `approve` sur `PendingReview`, elle renvoie une nouvelle instance emballée du struct `Published` \[2\]. Le struct `Published` implémente le trait `State`, et pour les deux méthodes `request_review` et `approve`, il renvoie lui-même car la publication devrait rester dans l'état `Published` dans ces cas.

Maintenant, nous devons mettre à jour la méthode `content` sur `Post`. Nous voulons que la valeur renvoyée par `content` dépende de l'état actuel du `Post`, donc nous allons faire en sorte que `Post` délègue à une méthode `content` définie sur son `state`, comme montré dans le Listing 17-17.

Nom de fichier : `src/lib.rs`

```rust
impl Post {
    --snip--
    pub fn content(&self) -> &str {
        self.state.as_ref().unwrap().content(self)
    }
    --snip--
}
```

Listing 17-17 : Mise à jour de la méthode `content` sur `Post` pour déléguer à une méthode `content` sur `State`

Comme l'objectif est de conserver toutes ces règles dans les structs qui implémentent `State`, nous appelons une méthode `content` sur la valeur dans `state` et passons l'instance de la publication (c'est-à-dire `self`) en tant qu'argument. Ensuite, nous renvoyons la valeur renvoyée par l'utilisation de la méthode `content` sur la valeur `state`.

Nous appelons la méthode `as_ref` sur l'`Option` car nous voulons une référence à la valeur à l'intérieur de l'`Option` plutôt que la propriété de la valeur. Étant donné que `state` est une `Option<Box<dyn State>>`, lorsqu'on appelle `as_ref`, une `Option<&Box<dyn State>>` est renvoyée. Si nous n'avions pas appelé `as_ref`, nous aurions eu une erreur car nous ne pouvons pas déplacer `state` hors de la référence empruntée `&self` du paramètre de fonction.

Nous appelons ensuite la méthode `unwrap`, que nous savons ne jamais déclencher une panique car nous savons que les méthodes sur `Post` garantissent que `state` contiendra toujours une valeur `Some` une fois que ces méthodes sont terminées. C'est l'un des cas dont nous avons parlé dans "Cas où vous avez plus d'informations que le compilateur" lorsque nous savons qu'une valeur `None` n'est jamais possible, même si le compilateur n'est pas capable de le comprendre.

À ce stade, lorsqu'on appelle `content` sur le `&Box<dyn State>`, la coercition de déréférencement prendra effet sur le `&` et la `Box` de sorte que la méthode `content` sera finalement appelée sur le type qui implémente le trait `State`. Cela signifie que nous devons ajouter `content` à la définition du trait `State`, et c'est là que nous mettrons la logique pour savoir quel contenu renvoyer selon l'état que nous avons, comme montré dans le Listing 17-18.

Nom de fichier : `src/lib.rs`

```rust
trait State {
    --snip--
    fn content<'a>(&self, post: &'a Post) -> &'a str {
      1 ""
    }
}

--snip--
struct Published {}

impl State for Published {
    --snip--
    fn content<'a>(&self, post: &'a Post) -> &'a str {
      2 &post.content
    }
}
```

Listing 17-18 : Ajout de la méthode `content` au trait `State`

Nous ajoutons une implémentation par défaut pour la méthode `content` qui renvoie une chaîne de caractères vide \[1\]. Cela signifie que nous n'avons pas besoin d'implémenter `content` sur les structs `Draft` et `PendingReview`. Le struct `Published` remplacera la méthode `content` et renverra la valeur dans `post.content` \[2\].

Notez que nous avons besoin d'annotations de durée de vie pour cette méthode, comme nous l'avons discuté au Chapitre 10. Nous prenons une référence à un `post` en tant qu'argument et renvoyons une référence à une partie de ce `post`, donc la durée de vie de la référence renvoyée est liée à la durée de vie de l'argument `post`.

Et nous avons terminé --- tout le Listing 17-11 fonctionne désormais! Nous avons implémenté le patron d'état avec les règles du workflow de publication de blog. La logique liée aux règles réside dans les objets d'état plutôt que d'être dispersée dans tout `Post`.

> **Pourquoi pas un enum?**
>
> Vous vous êtes peut-être demandé pourquoi nous n'avons pas utilisé un `enum` avec les différents états possibles de publication comme variantes. C'est certainement une solution possible ; essayez et comparez les résultats finaux pour voir lequel vous préférez! Un inconvénient d'utiliser un enum est que chaque endroit qui vérifie la valeur de l'enum devra avoir une expression `match` ou similaire pour gérer chaque variante possible. Cela pourrait être plus répétitif que cette solution d'objet de trait.
