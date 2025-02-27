# Implémentation du trait

Maintenant, nous allons ajouter quelques types qui implémentent le trait `Draw`. Nous fournirons le type `Button`. Encore une fois, la mise en œuvre réelle d'une bibliothèque GUI est en dehors des limites de ce livre, donc la méthode `draw` n'aura pas d'implémentation utile dans son corps. Pour imaginer à quoi pourrait ressembler l'implémentation, une struct `Button` pourrait avoir des champs pour `width`, `height` et `label`, comme montré dans la liste 17-7.

Nom de fichier : `src/lib.rs`

```rust
pub struct Button {
    pub width: u32,
    pub height: u32,
    pub label: String,
}

impl Draw for Button {
    fn draw(&self) {
        // code pour effectivement dessiner un bouton
    }
}
```

Liste 17-7 : Une struct `Button` qui implémente le trait `Draw`

Les champs `width`, `height` et `label` sur `Button` différeront des champs sur d'autres composants ; par exemple, un type `TextField` pourrait avoir les mêmes champs plus un champ `placeholder`. Chacun des types que nous voulons dessiner à l'écran implémentera le trait `Draw` mais utilisera du code différent dans la méthode `draw` pour définir la manière de dessiner ce type particulier, comme le fait `Button` ici (sans le code GUI réel, comme mentionné). Le type `Button`, par exemple, pourrait avoir un bloc `impl` supplémentaire contenant des méthodes liées à ce qui se passe lorsqu'un utilisateur clique sur le bouton. Ces types de méthodes ne s'appliqueront pas à des types comme `TextField`.

Si quelqu'un utilisant notre bibliothèque décide d'implémenter une struct `SelectBox` qui a des champs `width`, `height` et `options`, ils implémenteront également le trait `Draw` sur le type `SelectBox`, comme montré dans la liste 17-8.

Nom de fichier : `src/main.rs`

```rust
use gui::Draw;

struct SelectBox {
    width: u32,
    height: u32,
    options: Vec<String>,
}

impl Draw for SelectBox {
    fn draw(&self) {
        // code pour effectivement dessiner une zone de sélection
    }
}
```

Liste 17-8 : Un autre crate utilisant `gui` et implémentant le trait `Draw` sur une struct `SelectBox`

L'utilisateur de notre bibliothèque peut maintenant écrire sa fonction `main` pour créer une instance de `Screen`. À l'instance de `Screen`, ils peuvent ajouter une `SelectBox` et un `Button` en les mettant chacun dans un `Box<T>` pour en faire un objet de trait. Ils peuvent ensuite appeler la méthode `run` sur l'instance de `Screen`, qui appellera `draw` sur chacun des composants. La liste 17-9 montre cette implémentation.

Nom de fichier : `src/main.rs`

```rust
use gui::{Button, Screen};

fn main() {
    let screen = Screen {
        components: vec![
            Box::new(SelectBox {
                width: 75,
                height: 10,
                options: vec![
                    String::from("Yes"),
                    String::from("Maybe"),
                    String::from("No"),
                ],
            }),
            Box::new(Button {
                width: 50,
                height: 10,
                label: String::from("OK"),
            }),
        ],
    };

    screen.run();
}
```

Liste 17-9 : Utilisation d'objets de trait pour stocker des valeurs de différents types qui implémentent le même trait

Lorsque nous avons écrit la bibliothèque, nous ne savions pas que quelqu'un pourrait ajouter le type `SelectBox`, mais notre implémentation de `Screen` a été capable de fonctionner sur le nouveau type et de le dessiner car `SelectBox` implémente le trait `Draw`, ce qui signifie qu'il implémente la méthode `draw`.

Ce concept - de ne s'intéresser qu'aux messages à laquelle une valeur répond plutôt que au type concret de la valeur - est similaire au concept de _duck typing_ dans les langages à typage dynamique : si ça marche comme un canard et quack comme un canard, alors ça doit être un canard! Dans l'implémentation de `run` sur `Screen` dans la liste 17-5, `run` n'a pas besoin de savoir quel est le type concret de chaque composant. Il ne vérifie pas si un composant est une instance d'un `Button` ou d'un `SelectBox`, il appelle simplement la méthode `draw` sur le composant. En spécifiant `Box<dyn Draw>` comme le type des valeurs dans le vecteur `components`, nous avons défini `Screen` pour avoir besoin de valeurs sur lesquelles nous pouvons appeler la méthode `draw`.

L'avantage d'utiliser des objets de trait et le système de types de Rust pour écrire du code similaire au code utilisant le duck typing est que nous n'avons jamais besoin de vérifier si une valeur implémente une méthode particulière à l'exécution ou de nous inquiéter d'obtenir des erreurs si une valeur n'implémente pas une méthode mais que nous l'appelons malgré tout. Rust ne compilera pas notre code si les valeurs n'implémentent pas les traits que les objets de trait nécessitent.

Par exemple, la liste 17-10 montre ce qui se passe si nous essayons de créer un `Screen` avec une `String` comme composant.

Nom de fichier : `src/main.rs`

```rust
use gui::Screen;

fn main() {
    let screen = Screen {
        components: vec![Box::new(String::from("Hi"))],
    };

    screen.run();
}
```

Liste 17-10 : Tentative d'utilisation d'un type qui n'implémente pas le trait de l'objet de trait

Nous obtiendrons cette erreur car `String` n'implémente pas le trait `Draw` :

```bash
error[E0277]: the trait bound `String: Draw` is not satisfied
 --> src/main.rs:5:26
  |
5 |         components: vec![Box::new(String::from("Hi"))],
  |                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^ the trait `Draw` is
not implemented for `String`
  |
  = note: required for the cast to the object type `dyn Draw`
```

Cette erreur nous informe que soit nous passons quelque chose à `Screen` que nous n'avions pas l'intention de passer et que nous devrions donc passer un autre type, soit nous devrions implémenter `Draw` sur `String` pour que `Screen` soit capable d'appeler `draw` sur elle.
