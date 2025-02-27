# Distinction entre des méthodes de même nom

Rien en Rust n'empêche un trait d'avoir une méthode de même nom qu'une méthode d'un autre trait, ni Rust ne vous empêche d'implémenter les deux traits sur un même type. Il est également possible d'implémenter directement une méthode sur le type avec le même nom que des méthodes provenant de traits.

Lorsque vous appelez des méthodes de même nom, vous devrez dire à Rust laquelle vous voulez utiliser. Considérez le code de la Liste 19-16 où nous avons défini deux traits, `Pilot` et `Wizard`, qui ont tous deux une méthode appelée `fly`. Nous implémentons ensuite les deux traits sur un type `Human` qui a déjà une méthode nommée `fly` implémentée sur lui. Chaque méthode `fly` fait quelque chose de différent.

Nom de fichier : `src/main.rs`

```rust
trait Pilot {
    fn fly(&self);
}

trait Wizard {
    fn fly(&self);
}

struct Human;

impl Pilot for Human {
    fn fly(&self) {
        println!("This is your captain speaking.");
    }
}

impl Wizard for Human {
    fn fly(&self) {
        println!("Up!");
    }
}

impl Human {
    fn fly(&self) {
        println!("*waving arms furiously*");
    }
}
```

Liste 19-16 : Deux traits sont définis pour avoir une méthode `fly` et sont implémentés sur le type `Human`, et une méthode `fly` est implémentée directement sur `Human`.

Lorsque nous appelons `fly` sur une instance de `Human`, le compilateur se réfère par défaut à la méthode qui est directement implémentée sur le type, comme montré dans la Liste 19-17.

Nom de fichier : `src/main.rs`

```rust
fn main() {
    let person = Human;
    person.fly();
}
```

Liste 19-17 : Appel de `fly` sur une instance de `Human`

Exécuter ce code imprimera `*waving arms furiously*`, montrant que Rust a appelé la méthode `fly` implémentée directement sur `Human`.

Pour appeler les méthodes `fly` du trait `Pilot` ou du trait `Wizard`, nous devons utiliser une syntaxe plus explicite pour spécifier laquelle des méthodes `fly` nous voulons. La Liste 19-18 montre cette syntaxe.

Nom de fichier : `src/main.rs`

```rust
fn main() {
    let person = Human;
    Pilot::fly(&person);
    Wizard::fly(&person);
    person.fly();
}
```

Liste 19-18 : Spécification de laquelle des méthodes `fly` du trait nous voulons appeler

Spécifier le nom du trait avant le nom de la méthode indique à Rust laquelle des implémentations de `fly` nous voulons appeler. Nous pourrions également écrire `Human::fly(&person)`, qui est équivalent à `person.fly()` que nous avons utilisé dans la Liste 19-18, mais cela est un peu plus long à écrire si nous n'avons pas besoin de faire la distinction.

Exécuter ce code imprime ce qui suit :

    This is your captain speaking.
    Up!
    *waving arms furiously*

Comme la méthode `fly` prend un paramètre `self`, si nous avions deux _types_ qui implémentent tous deux un même _trait_, Rust pourrait déterminer laquelle des implémentations d'un trait utiliser en fonction du type de `self`.

Cependant, les fonctions associées qui ne sont pas des méthodes n'ont pas de paramètre `self`. Lorsqu'il y a plusieurs types ou traits qui définissent des fonctions non méthodes avec le même nom de fonction, Rust ne sait pas toujours laquelle vous voulez utiliser à moins que vous n'utilisiez une syntaxe entièrement qualifiée. Par exemple, dans la Liste 19-19, nous créons un trait pour un refuge animalier qui veut nommer tous les bébés chiens Spot. Nous créons un trait `Animal` avec une fonction associée non méthodique `baby_name`. Le trait `Animal` est implémenté pour la structure `Dog`, sur laquelle nous fournissons également directement une fonction associée non méthodique `baby_name`.

Nom de fichier : `src/main.rs`

```rust
trait Animal {
    fn baby_name() -> String;
}

struct Dog;

impl Dog {
    fn baby_name() -> String {
        String::from("Spot")
    }
}

impl Animal for Dog {
    fn baby_name() -> String {
        String::from("puppy")
    }
}

fn main() {
    println!("A baby dog is called a {}", Dog::baby_name());
}
```

Liste 19-19 : Un trait avec une fonction associée et un type avec une fonction associée de même nom qui implémente également le trait

Nous implémentons le code pour nommer tous les bébés chiens Spot dans la fonction associée `baby_name` définie sur `Dog`. Le type `Dog` implémente également le trait `Animal`, qui décrit les caractéristiques que tous les animaux ont. Les bébés chiens sont appelés des chiots, et cela est exprimé dans l'implémentation du trait `Animal` sur `Dog` dans la fonction `baby_name` associée au trait `Animal`.

Dans `main`, nous appelons la fonction `Dog::baby_name`, qui appelle directement la fonction associée définie sur `Dog`. Ce code imprime ce qui suit :

```rust
A baby dog is called a Spot
```

Ce résultat n'est pas celui que nous voulions. Nous voulons appeler la fonction `baby_name` qui est partie du trait `Animal` que nous avons implémenté sur `Dog` pour que le code imprime `A baby dog is called a puppy`. La technique de spécification du nom du trait que nous avons utilisée dans la Liste 19-18 ne sert pas ici ; si nous modifions `main` pour le code de la Liste 19-20, nous obtiendrons une erreur de compilation.

Nom de fichier : `src/main.rs`

```rust
fn main() {
    println!("A baby dog is called a {}", Animal::baby_name());
}
```

Liste 19-20 : Tentative d'appel de la fonction `baby_name` du trait `Animal`, mais Rust ne sait pas laquelle des implémentations utiliser

Car `Animal::baby_name` n'a pas de paramètre `self`, et il pourrait y avoir d'autres types qui implémentent le trait `Animal`, Rust ne peut pas déterminer laquelle des implémentations de `Animal::baby_name` nous voulons. Nous obtiendrons cette erreur du compilateur :

```bash
error[E0283]: type annotations needed
  --> src/main.rs:20:43
   |
20 |     println!("A baby dog is called a {}", Animal::baby_name());
   |                                           ^^^^^^^^^^^^^^^^^ cannot infer
type
   |
   = note: cannot satisfy `_: Animal`
```

Pour faire la distinction et dire à Rust que nous voulons utiliser l'implémentation de `Animal` pour `Dog` par opposition à l'implémentation de `Animal` pour un autre type, nous devons utiliser une syntaxe entièrement qualifiée. La Liste 19-21 montre comment utiliser une syntaxe entièrement qualifiée.

Nom de fichier : `src/main.rs`

```rust
fn main() {
    println!(
        "A baby dog is called a {}",
        <Dog as Animal>::baby_name()
    );
}
```

Liste 19-21 : Utilisation d'une syntaxe entièrement qualifiée pour spécifier que nous voulons appeler la fonction `baby_name` du trait `Animal` telle qu'elle est implémentée sur `Dog`

Nous fournissons à Rust une annotation de type à l'intérieur des chevrons, ce qui indique que nous voulons appeler la méthode `baby_name` du trait `Animal` telle qu'elle est implémentée sur `Dog` en disant que nous voulons considérer le type `Dog` comme un `Animal` pour cet appel de fonction. Ce code imprimera maintenant ce que nous voulons :

```rust
A baby dog is called a puppy
```

En général, la syntaxe entièrement qualifiée est définie comme suit :

```rust
<Type as Trait>::function(receiver_if_method, next_arg,...);
```

Pour les fonctions associées qui ne sont pas des méthodes, il n'y aurait pas de `receiver` : il n'y aurait que la liste des autres arguments. Vous pouvez utiliser une syntaxe entièrement qualifiée partout où vous appelez des fonctions ou des méthodes. Cependant, vous êtes autorisé à omettre toute partie de cette syntaxe que Rust peut déterminer à partir d'autres informations dans le programme. Vous n'avez besoin d'utiliser cette syntaxe plus verbeuse que dans les cas où il y a plusieurs implémentations qui utilisent le même nom et que Rust a besoin d'aide pour identifier laquelle des implémentations vous voulez appeler.
