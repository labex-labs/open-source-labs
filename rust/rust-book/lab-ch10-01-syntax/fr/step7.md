# Performance du code utilisant des génériques

Vous vous demandez peut-être s'il y a un coût d'exécution lorsqu'on utilise des paramètres de type générique. La bonne nouvelle est que l'utilisation de types génériques ne ralentira pas votre programme par rapport à son exécution avec des types concrets.

Rust y parvient en effectuant la monomorphisation du code utilisant des génériques à la compilation. La _monomorphisation_ est le processus consistant à transformer le code générique en code spécifique en remplissant les types concrets utilisés lors de la compilation. Dans ce processus, le compilateur fait l'inverse des étapes que nous avons utilisées pour créer la fonction générique dans la Liste 10-5 : le compilateur examine tous les endroits où le code générique est appelé et génère du code pour les types concrets avec lesquels le code générique est appelé.

Regardons comment cela fonctionne en utilisant l'enum générique `Option<T>` de la bibliothèque standard :

```rust
let integer = Some(5);
let float = Some(5.0);
```

Lorsque Rust compile ce code, il effectue la monomorphisation. Pendant ce processus, le compilateur lit les valeurs qui ont été utilisées dans les instances de `Option<T>` et identifie deux types de `Option<T>` : l'un est `i32` et l'autre est `f64`. En conséquence, il étend la définition générique de `Option<T>` en deux définitions spécialisées pour `i32` et `f64`, remplaçant ainsi la définition générique par les définitions spécifiques.

La version monomorphisée du code ressemble à ceci (le compilateur utilise des noms différents de ceux que nous utilisons ici à des fins d'illustration) :

Nom de fichier : `src/main.rs`

```rust
enum Option_i32 {
    Some(i32),
    None,
}

enum Option_f64 {
    Some(f64),
    None,
}

fn main() {
    let integer = Option_i32::Some(5);
    let float = Option_f64::Some(5.0);
}
```

Le `Option<T>` générique est remplacé par les définitions spécifiques créées par le compilateur. Comme Rust compile le code générique en un code qui spécifie le type dans chaque instance, nous n'assumons aucun coût d'exécution pour utiliser des génériques. Lorsque le code s'exécute, il fonctionne exactement comme s'il nous avait fallu dupliquer chaque définition à la main. Le processus de monomorphisation rend les génériques de Rust extrêmement efficaces à l'exécution.
