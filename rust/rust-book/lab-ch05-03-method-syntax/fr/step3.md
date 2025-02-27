# Méthodes avec plus de paramètres

Pratiquons l'utilisation des méthodes en implémentant une deuxième méthode sur la structure `Rectangle`. Cette fois, nous voulons qu'une instance de `Rectangle` prenne une autre instance de `Rectangle` et renvoie `true` si la deuxième `Rectangle` peut s'insérer entièrement dans `self` (la première `Rectangle`); sinon, elle devrait renvoyer `false`. C'est-à-dire que une fois que nous avons défini la méthode `can_hold`, nous voulons être capable d'écrire le programme montré dans la Liste 5-14.

Nom de fichier : `src/main.rs`

```rust
fn main() {
    let rect1 = Rectangle {
        width: 30,
        height: 50,
    };
    let rect2 = Rectangle {
        width: 10,
        height: 40,
    };
    let rect3 = Rectangle {
        width: 60,
        height: 45,
    };

    println!("Can rect1 hold rect2? {}", rect1.can_hold(&rect2));
    println!("Can rect1 hold rect3? {}", rect1.can_hold(&rect3));
}
```

Liste 5-14 : Utilisation de la méthode `can_hold` non encore écrite

La sortie attendue serait la suivante car les deux dimensions de `rect2` sont plus petites que les dimensions de `rect1`, mais `rect3` est plus large que `rect1` :

```rust
Can rect1 hold rect2? true
Can rect1 hold rect3? false
```

Nous savons que nous voulons définir une méthode, donc elle sera à l'intérieur du bloc `impl Rectangle`. Le nom de la méthode sera `can_hold`, et elle prendra un emprunt immuable d'une autre `Rectangle` en tant que paramètre. Nous pouvons déterminer le type du paramètre en regardant le code qui appelle la méthode : `rect1.can_hold(&rect2)` passe `&rect2`, qui est un emprunt immuable de `rect2`, une instance de `Rectangle`. Cela a du sens car nous avons seulement besoin de lire `rect2` (plutôt que d'écrire, ce qui signifierait que nous aurions besoin d'un emprunt mutable), et nous voulons que `main` conserve la propriété de `rect2` pour pouvoir la réutiliser après avoir appelé la méthode `can_hold`. La valeur de retour de `can_hold` sera un booléen, et l'implémentation vérifiera si la largeur et la hauteur de `self` sont respectivement plus grandes que la largeur et la hauteur de l'autre `Rectangle`. Ajoutons la nouvelle méthode `can_hold` au bloc `impl` de la Liste 5-13, comme montré dans la Liste 5-15.

Nom de fichier : `src/main.rs`

```rust
impl Rectangle {
    fn area(&self) -> u32 {
        self.width * self.height
    }

    fn can_hold(&self, other: &Rectangle) -> bool {
        self.width > other.width && self.height > other.height
    }
}
```

Liste 5-15 : Implémentation de la méthode `can_hold` sur `Rectangle` qui prend une autre instance de `Rectangle` en tant que paramètre

Lorsque nous exécutons ce code avec la fonction `main` de la Liste 5-14, nous obtiendrons la sortie souhaitée. Les méthodes peuvent prendre plusieurs paramètres que nous ajoutons à la signature après le paramètre `self`, et ces paramètres fonctionnent exactement comme les paramètres dans les fonctions.
