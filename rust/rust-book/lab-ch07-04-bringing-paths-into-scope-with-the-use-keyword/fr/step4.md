# Re-exporting Names with pub use

Lorsque nous amenons un nom dans la portée avec le mot-clé `use`, le nom disponible dans la nouvelle portée est privé. Pour permettre au code qui appelle notre code de faire référence à ce nom comme s'il avait été défini dans la portée de ce code, nous pouvons combiner `pub` et `use`. Cette technique est appelée _re-exportation_ car nous amenons un élément dans la portée mais nous le rendons également disponible pour que les autres le rapportent dans leur portée.

La Liste 7-17 montre le code de la Liste 7-11 avec `use` dans le module racine remplacé par `pub use`.

Nom de fichier : `src/lib.rs`

```rust
mod front_of_house {
    pub mod hosting {
        pub fn add_to_waitlist() {}
    }
}

pub use crate::front_of_house::hosting;

pub fn eat_at_restaurant() {
    hosting::add_to_waitlist();
}
```

Liste 7-17 : Rendre un nom disponible pour tout code à utiliser à partir d'une nouvelle portée avec `pub use`

Avant ce changement, le code externe aurait dû appeler la fonction `add_to_waitlist` en utilisant le chemin `restaurant::front_of_house::hosting::add_to_waitlist()`. Maintenant que ce `pub use` a re-exporté le module `hosting` à partir du module racine, le code externe peut utiliser le chemin `restaurant::hosting::add_to_waitlist()` à la place.

La re-exportation est utile lorsque la structure interne de votre code est différente de la manière dont les programmeurs appelant votre code pensent au domaine. Par exemple, dans cette métaphore du restaurant, les personnes qui gèrent le restaurant pensent à "l'avant de la maison" et "l'arrière de la maison". Mais les clients qui visitent un restaurant probablement ne penseront pas aux parties du restaurant de cette manière. Avec `pub use`, nous pouvons écrire notre code avec une structure mais exposer une structure différente. En faisant cela, nous rendons notre bibliothèque bien organisée pour les programmeurs travaillant sur la bibliothèque et les programmeurs appelant la bibliothèque. Nous examinerons un autre exemple de `pub use` et comment cela affecte la documentation de votre crate dans "Exporting a Convenient Public API with pub use".
