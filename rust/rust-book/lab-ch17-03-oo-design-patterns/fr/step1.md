# Implementing an Object-Oriented Design Pattern

Le _patron d'état_ est un patron de conception orienté objet. Le cœur du patron est que nous définissons un ensemble d'états qu'une valeur peut avoir en interne. Les états sont représentés par un ensemble d'_objets d'état_, et le comportement de la valeur change en fonction de son état. Nous allons travailler sur un exemple d'une structure de publication de blog qui a un champ pour stocker son état, qui sera un objet d'état de l'ensemble "brouillon", "en revue" ou "publié".

Les objets d'état partagent des fonctionnalités : en Rust, bien sûr, nous utilisons des structs et des traits plutôt qu'objets et héritage. Chaque objet d'état est responsable de son propre comportement et de la gouvernance du moment où il devrait changer en un autre état. La valeur qui contient un objet d'état ne sait rien sur le comportement différent des états ou sur le moment de passer d'un état à l'autre.

L'avantage d'utiliser le patron d'état est que, lorsque les exigences commerciales du programme changent, nous n'aurons pas besoin de modifier le code de la valeur contenant l'état ou le code qui utilise la valeur. Nous n'aurons qu'à mettre à jour le code à l'intérieur d'un des objets d'état pour changer ses règles ou peut-être ajouter plus d'objets d'état.

Tout d'abord, nous allons implémenter le patron d'état d'une manière plus traditionnelle orientée objet, puis nous utiliserons une approche qui est un peu plus naturelle en Rust. Plongeons-nous pour implémenter progressivement un workflow de publication de blog en utilisant le patron d'état.

La fonctionnalité finale ressemblera à ceci :

1.  Une publication de blog commence comme un brouillon vide.
2.  Lorsque le brouillon est terminé, une révision de la publication est demandée.
3.  Lorsque la publication est approuvée, elle est publiée.
4.  Seules les publications de blog publiées renvoient du contenu pour imprimer, de sorte que les publications non approuvées ne peuvent pas être publiées par accident.

Toute autre modification tentée sur une publication ne devrait avoir aucun effet. Par exemple, si nous essayons d'approuver une publication de blog en brouillon avant d'avoir demandé une révision, la publication devrait rester un brouillon non publié.

Le Listing 17-11 montre ce workflow sous forme de code : c'est un exemple d'utilisation de l'API que nous allons implémenter dans une boîte à outils nommée `blog`. Cela ne compilera pas encore car nous n'avons pas implémenté la boîte à outils `blog`.

Nom de fichier : `src/main.rs`

```rust
use blog::Post;

fn main() {
  1 let mut post = Post::new();

  2 post.add_text("I ate a salad for lunch today");
  3 assert_eq!("", post.content());

  4 post.request_review();
  5 assert_eq!("", post.content());

  6 post.approve();
  7 assert_eq!("I ate a salad for lunch today", post.content());
}
```

Listing 17-11 : Code qui démontre le comportement souhaité que nous voulons que notre boîte à outils `blog` ait

Nous voulons autoriser l'utilisateur à créer une nouvelle publication de blog en brouillon avec `Post::new` \[1\]. Nous voulons autoriser le texte à être ajouté à la publication de blog \[2\]. Si nous essayons d'obtenir le contenu de la publication immédiatement, avant l'approbation, nous ne devrions pas obtenir de texte car la publication est toujours un brouillon. Nous avons ajouté `assert_eq!` dans le code à des fins de démonstration \[3\]. Un excellent test d'unité pour cela serait d'affirmer qu'une publication de blog en brouillon renvoie une chaîne de caractères vide à partir de la méthode `content`, mais nous ne allons pas écrire de tests pour cet exemple.

Ensuite, nous voulons autoriser une demande de révision de la publication \[4\], et nous voulons que `content` renvoie une chaîne de caractères vide pendant que la publication est en attente d'être revue \[5\]. Lorsque la publication reçoit l'approbation \[6\], elle devrait être publiée, ce qui signifie que le texte de la publication sera renvoyé lorsqu'on appelle `content` \[7\].

Remarquez que le seul type avec lequel nous interagissons à partir de la boîte à outils est le type `Post`. Ce type utilisera le patron d'état et contiendra une valeur qui sera l'un des trois objets d'état représentant les différents états dans lesquels une publication peut se trouver - brouillon, en revue ou publié. Passer d'un état à l'autre sera géré en interne dans le type `Post`. Les états changent en réponse aux méthodes appelées par les utilisateurs de notre bibliothèque sur l'instance `Post`, mais ils n'ont pas besoin de gérer directement les changements d'état. De plus, les utilisateurs ne peuvent pas se tromper sur les états, par exemple en publiant une publication avant qu'elle ne soit revue.
