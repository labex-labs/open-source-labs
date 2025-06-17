# Cloner un Rc`<T>` augmente le compte de références

Modifions notre exemple fonctionnel de la Liste 15-18 pour voir les comptes de références changer au fur et à mesure que nous créons et supprimons des références au `Rc<List>` dans `a`.

Dans la Liste 15-19, nous modifierons `main` pour qu'il ait une portée interne autour de la liste `c` ; puis nous pourrons voir comment le compte de références change lorsque `c` sort de portée.

Nom de fichier : `src/main.rs`

```rust
--snip--

fn main() {
    let a = Rc::new(Cons(5, Rc::new(Cons(10, Rc::new(Nil)))));
    println!(
        "count after creating a = {}",
        Rc::strong_count(&a)
    );
    let b = Cons(3, Rc::clone(&a));
    println!(
        "count after creating b = {}",
        Rc::strong_count(&a)
    );
    {
        let c = Cons(4, Rc::clone(&a));
        println!(
            "count after creating c = {}",
            Rc::strong_count(&a)
        );
    }
    println!(
        "count after c goes out of scope = {}",
        Rc::strong_count(&a)
    );
}
```

Liste 15-19 : Affichage du compte de références

À chaque étape du programme où le compte de références change, nous affichons le compte de références, que nous obtenons en appelant la fonction `Rc::strong_count`. Cette fonction est nommée `strong_count` plutôt que `count` car le type `Rc<T>` a également un `weak_count` ; nous verrons à quoi sert `weak_count` dans "Prévenir les cycles de références en utilisant Weak`<T>`".

Ce code affiche ceci :

    count after creating a = 1
    count after creating b = 2
    count after creating c = 3
    count after c goes out of scope = 2

Nous pouvons voir que le `Rc<List>` dans `a` a un compte de références initial de 1 ; puis chaque fois que nous appelons `clone`, le compte augmente de 1. Lorsque `c` sort de portée, le compte diminue de 1. Nous n'avons pas besoin d'appeler une fonction pour diminuer le compte de références comme nous devons appeler `Rc::clone` pour augmenter le compte de références : l'implémentation du trait `Drop` diminue automatiquement le compte de références lorsqu'une valeur `Rc<T>` sort de portée.

Ce que nous ne pouvons pas voir dans cet exemple est que lorsque `b` puis `a` sortent de portée à la fin de `main`, le compte est alors 0, et le `Rc<List>` est entièrement nettoyé. Utiliser `Rc<T>` permet à une seule valeur d'avoir plusieurs propriétaires, et le compte assure que la valeur reste valide tant qu'un des propriétaires existe encore.

Via des références immuables, `Rc<T>` vous permet de partager des données entre plusieurs parties de votre programme pour lecture seulement. Si `Rc<T>` vous permettait également d'avoir plusieurs références mutables, vous pourriez violer l'une des règles d'emprunt discutées au chapitre 4 : plusieurs emprunts mutables au même endroit peuvent entraîner des courses de données et des inconvénients. Mais être capable de modifier des données est très utile! Dans la section suivante, nous aborderons le modèle de mutabilité interne et le type `RefCell<T>` que vous pouvez utiliser en conjonction avec un `Rc<T>` pour travailler avec cette restriction d'immuabilité.
