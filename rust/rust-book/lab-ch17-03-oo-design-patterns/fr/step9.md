# Implémentation des transitions sous forme de transformations en différents types

Alors, comment obtenons-nous une publication publiée? Nous voulons appliquer la règle selon laquelle une publication brouillon doit être revue et approuvée avant d'être publiée. Une publication dans l'état en attente de révision ne devrait toujours pas afficher de contenu. Implémentons ces contraintes en ajoutant un autre struct, `PendingReviewPost`, en définissant la méthode `request_review` sur `DraftPost` pour renvoyer un `PendingReviewPost` et en définissant une méthode `approve` sur `PendingReviewPost` pour renvoyer un `Post`, comme montré dans le Listing 17-20.

Nom de fichier : `src/lib.rs`

```rust
impl DraftPost {
    --snip--
    pub fn request_review(self) -> PendingReviewPost {
        PendingReviewPost {
            content: self.content,
        }
    }
}

pub struct PendingReviewPost {
    content: String,
}

impl PendingReviewPost {
    pub fn approve(self) -> Post {
        Post {
            content: self.content,
        }
    }
}
```

Listing 17-20 : Un `PendingReviewPost` créé en appelant `request_review` sur `DraftPost` et une méthode `approve` qui transforme un `PendingReviewPost` en un `Post` publié

Les méthodes `request_review` et `approve` prennent la propriété de `self`, consommant ainsi les instances `DraftPost` et `PendingReviewPost` et les transformant respectivement en un `PendingReviewPost` et en un `Post` publié. De cette manière, nous n'aurons pas d'instances `DraftPost` en suspens après avoir appelé `request_review` sur elles, et ainsi de suite. Le struct `PendingReviewPost` n'a pas de méthode `content` définie sur lui, donc tenter de lire son contenu entraîne une erreur de compilation, comme pour `DraftPost`. Étant donné que le seul moyen d'obtenir une instance de `Post` publié qui a une méthode `content` définie est d'appeler la méthode `approve` sur un `PendingReviewPost`, et que le seul moyen d'obtenir un `PendingReviewPost` est d'appeler la méthode `request_review` sur un `DraftPost`, nous avons maintenant encodé le workflow de publication de blog dans le système de types.

Mais nous devons également apporter quelques petits changements à `main`. Les méthodes `request_review` et `approve` renvoient de nouvelles instances plutôt que de modifier la struct sur laquelle elles sont appelées, donc nous devons ajouter plus d'affectations de masquage `let post =` pour enregistrer les instances renvoyées. Nous ne pouvons également pas avoir les assertions selon lesquelles le contenu des publications brouillons et en attente de révision est une chaîne de caractères vide, et nous n'avons même pas besoin d'elles : nous ne pouvons plus compiler le code qui tente d'utiliser le contenu des publications dans ces états. Le code mis à jour de `main` est montré dans le Listing 17-21.

Nom de fichier : `src/main.rs`

```rust
use blog::Post;

fn main() {
    let mut post = Post::new();

    post.add_text("I ate a salad for lunch today");

    let post = post.request_review();

    let post = post.approve();

    assert_eq!("I ate a salad for lunch today", post.content());
}
```

Listing 17-21 : Modifications apportées à `main` pour utiliser la nouvelle implémentation du workflow de publication de blog

Les modifications que nous avons dû apporter à `main` pour réaffecter `post` signifient que cette implémentation ne suit plus tout à fait le patron d'état orienté objet : les transformations entre les états ne sont plus entièrement encapsulées dans l'implémentation de `Post`. Cependant, notre gain est que les états invalides sont désormais impossibles en raison du système de types et de la vérification de type qui se produit à la compilation! Cela garantit que certains bugs, tels que l'affichage du contenu d'une publication non publiée, seront détectés avant qu'ils ne passent en production.

Essayez les tâches suggérées au début de cette section sur le crate `blog` tel qu'il est après le Listing 17-21 pour voir ce que vous en pensez du design de cette version du code. Notez que certaines des tâches peuvent déjà être complétées dans ce design.

Nous avons vu que même si Rust est capable d'implémenter des patrons de conception orientés objet, d'autres patrons, tels que l'encodage de l'état dans le système de types, sont également disponibles en Rust. Ces patrons ont différents choix de compromis. Bien que vous puissiez être très familier avec les patrons orientés objet, repenser le problème pour tirer parti des fonctionnalités de Rust peut apporter des avantages, tels que la prévention de certains bugs à la compilation. Les patrons orientés objet ne seront pas toujours la meilleure solution en Rust en raison de certaines fonctionnalités, telles que la propriété, que les langages orientés objet n'ont pas.
