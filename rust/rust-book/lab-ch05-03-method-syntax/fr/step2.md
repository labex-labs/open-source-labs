# Définition de méthodes

Modifions la fonction `area` qui prend une instance de `Rectangle` en paramètre et définissons plutôt une méthode `area` sur la structure `Rectangle`, comme indiqué dans la Liste 5-13.

Nom de fichier : `src/main.rs`

```rust
#[derive(Debug)]
struct Rectangle {
    width: u32,
    height: u32,
}

1 impl Rectangle {
  2 fn area(&self) -> u32 {
        self.width * self.height
    }
}

fn main() {
    let rect1 = Rectangle {
        width: 30,
        height: 50,
    };

    println!(
        "The area of the rectangle is {} square pixels.",
      3 rect1.area()
    );
}
```

Liste 5-13 : Définition d'une méthode `area` sur la structure `Rectangle`

Pour définir la fonction dans le contexte de `Rectangle`, nous commençons un bloc `impl` (implémentation) pour `Rectangle` \[1\]. Tout ce qui se trouve à l'intérieur de ce bloc `impl` sera associé au type `Rectangle`. Ensuite, nous déplaçons la fonction `area` à l'intérieur des accolades `impl` \[2\] et changeons le premier (et dans ce cas, unique) paramètre pour qu'il soit `self` dans la signature et partout dans le corps. Dans `main`, où nous appelions la fonction `area` et passions `rect1` en argument, nous pouvons maintenant utiliser la _syntaxe des méthodes_ pour appeler la méthode `area` sur notre instance de `Rectangle` \[3\]. La syntaxe des méthodes suit une instance : nous ajoutons un point suivi du nom de la méthode, des parenthèses et de tout argument.

Dans la signature de `area`, nous utilisons `&self` au lieu de `rectangle: &Rectangle`. Le `&self` est en fait une abréviation de `self: &Self`. Dans un bloc `impl`, le type `Self` est un alias pour le type sur lequel porte le bloc `impl`. Les méthodes doivent avoir un paramètre nommé `self` du type `Self` pour leur premier paramètre, donc Rust vous permet d'abréger cela en utilisant seulement le nom `self` dans le premier emplacement de paramètre. Notez que nous devons toujours utiliser le `&` devant l'abréviation `self` pour indiquer que cette méthode emprunte l'instance `Self`, tout comme nous l'avons fait avec `rectangle: &Rectangle`. Les méthodes peuvent prendre la propriété de `self`, emprunter `self` de manière immuable, comme nous l'avons fait ici, ou emprunter `self` de manière mutable, tout comme elles peuvent tout autre paramètre.

Nous avons choisi `&self` ici pour la même raison que nous avons utilisé `&Rectangle` dans la version fonction : nous ne voulons pas prendre la propriété, et nous ne voulons que lire les données dans la structure, pas les modifier. Si nous avions voulu modifier l'instance sur laquelle nous avons appelé la méthode en tant que partie de ce que fait la méthode, nous aurions utilisé `&mut self` comme premier paramètre. Il est rare d'avoir une méthode qui prend la propriété de l'instance en utilisant seulement `self` comme premier paramètre ; cette technique est généralement utilisée lorsque la méthode transforme `self` en quelque chose d'autre et que vous voulez empêcher l'appelant d'utiliser l'instance d'origine après la transformation.

La principale raison d'utiliser des méthodes plutôt que des fonctions, en plus de fournir la syntaxe des méthodes et de ne pas avoir à répéter le type de `self` dans la signature de chaque méthode, est pour l'organisation. Nous avons regroupé tout ce que nous pouvons faire avec une instance d'un type dans un seul bloc `impl` plutôt que de forcer les futurs utilisateurs de notre code à chercher les capacités de `Rectangle` à différents endroits dans la bibliothèque que nous fournissons.

Notez que nous pouvons choisir de donner à une méthode le même nom qu'un des champs de la structure. Par exemple, nous pouvons définir une méthode sur `Rectangle` qui s'appelle également `width` :

Nom de fichier : `src/main.rs`

```rust
impl Rectangle {
    fn width(&self) -> bool {
        self.width > 0
    }
}

fn main() {
    let rect1 = Rectangle {
        width: 30,
        height: 50,
    };

    if rect1.width() {
        println!(
            "The rectangle has a nonzero width; it is {}",
            rect1.width
        );
    }
}
```

Ici, nous choisissons de faire en sorte que la méthode `width` renvoie `true` si la valeur dans le champ `width` de l'instance est supérieure à `0` et `false` si la valeur est `0` : nous pouvons utiliser un champ dans une méthode du même nom pour n'importe quel but. Dans `main`, lorsque nous suivons `rect1.width` de parenthèses, Rust sait que nous voulons dire la méthode `width`. Lorsque nous n'utilisons pas de parenthèses, Rust sait que nous voulons dire le champ `width`.

Souvent, mais pas toujours, lorsque nous donnons à des méthodes le même nom qu'un champ, nous voulons qu'elles ne fassent que renvoyer la valeur dans le champ et ne fassent rien d'autre. Les méthodes comme celles-ci sont appelées _getters_, et Rust ne les implémente pas automatiquement pour les champs de structure comme le font certaines autres langues. Les getters sont utiles car vous pouvez rendre le champ privé mais la méthode publique, et ainsi autoriser un accès en lecture seulement à ce champ en tant que partie de l'API publique du type. Nous discuterons de ce qu'est public et privé et de la manière de désigner un champ ou une méthode comme public ou privé au Chapitre 7.

> **Où est l'opérateur -\>?**
>
> En C et C++, deux opérateurs différents sont utilisés pour appeler des méthodes : vous utilisez `.` si vous appelez une méthode directement sur l'objet et `->` si vous appelez la méthode sur un pointeur vers l'objet et que vous devez d'abord déréférencer le pointeur. En d'autres termes, si `object` est un pointeur, `object->`quelque chose`()` est similaire à `(*object).`quelque chose`()`.
>
> Rust n'a pas d'équivalent à l'opérateur `->` ; au lieu de cela, Rust a une fonctionnalité appelée _référence et déréférence automatiques_. Appeler des méthodes est l'un des rares endroits dans Rust où ce comportement existe.
>
> Voici comment cela fonctionne : lorsque vous appelez une méthode avec `object.`quelque chose`()`, Rust ajoute automatiquement `&`, `&mut` ou `*` de sorte que `object` corresponde à la signature de la méthode. En d'autres termes, les suivantes sont équivalentes :
>
>     p1.distance(&p2);
>     (&p1).distance(&p2);
>
> La première semble beaucoup plus propre. Ce comportement de référence automatique fonctionne car les méthodes ont un récepteur clair - le type de `self`. Étant donné le récepteur et le nom d'une méthode, Rust peut déterminer de manière définitive si la méthode lit (`&self`), modifie (`&mut self`) ou consomme (`self`). Le fait que Rust rende l'emprunt implicite pour les récepteurs de méthodes est une grande partie de ce qui rend la propriété ergonomique en pratique.
