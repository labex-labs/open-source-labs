# Refactoring avec des structs : Ajout de plus de sens

Nous utilisons des structs pour ajouter du sens en étiquetant les données. Nous pouvons transformer le tuple que nous utilisons en un struct avec un nom pour l'ensemble ainsi que des noms pour les parties, comme montré dans la liste 5-10.

Nom de fichier : `src/main.rs`

```rust
1 struct Rectangle {
  2 width: u32,
    height: u32,
}

fn main() {
  3 let rect1 = Rectangle {
        width: 30,
        height: 50,
    };

    println!(
        "L'aire du rectangle est {} pixels carrés.",
        area(&rect1)
    );
}

4 fn area(rectangle: &Rectangle) -> u32 {
  5 rectangle.width * rectangle.height
}
```

Liste 5-10 : Définition d'un struct `Rectangle`

Ici, nous avons défini un struct et l'avons nommé `Rectangle` \[1\]. Dans les accolades, nous avons défini les champs comme `width` et `height`, tous les deux de type `u32` \[2\]. Ensuite, dans `main`, nous avons créé une instance particulière de `Rectangle` qui a une largeur de `30` et une hauteur de `50` \[3\].

Notre fonction `area` est maintenant définie avec un paramètre, que nous avons nommé `rectangle`, dont le type est un emprunt immuable d'une instance de struct `Rectangle` \[4\]. Comme mentionné au chapitre 4, nous voulons emprunter le struct plutôt que prendre sa propriété. De cette manière, `main` conserve sa propriété et peut continuer à utiliser `rect1`, qui est la raison pour laquelle nous utilisons le `&` dans la signature de la fonction et où nous appelons la fonction.

La fonction `area` accède aux champs `width` et `height` de l'instance de `Rectangle` \[5\] (remarquez que l'accès aux champs d'une instance de struct empruntée ne déplace pas les valeurs des champs, c'est pourquoi vous voyez souvent des emprunts de structs). Notre signature de fonction pour `area` indique maintenant exactement ce que nous voulons dire : calculer l'aire de `Rectangle`, en utilisant ses champs `width` et `height`. Cela indique que la largeur et la hauteur sont liées l'une à l'autre, et il donne des noms descriptifs aux valeurs plutôt que d'utiliser les valeurs d'index de tuple de `0` et `1`. C'est un gain en termes de clarté.
