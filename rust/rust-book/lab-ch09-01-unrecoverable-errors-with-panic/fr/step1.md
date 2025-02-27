# Erreurs irrécupérables avec panic

Parfois, de mauvaises choses arrivent dans votre code, et il n'y a rien que vous puissiez faire. Dans ces cas, Rust dispose de la macro `panic!`. En pratique, il existe deux façons de déclencher une panique : en effectuant une action qui provoque la panique de notre code (par exemple en accédant à un tableau au-delà de la fin) ou en appelant explicitement la macro `panic!`. Dans les deux cas, nous provoquons une panique dans notre programme. Par défaut, ces panics afficheront un message d'erreur, dérouleront la pile, nettoyeront la pile et quitteront le programme. Via une variable d'environnement, vous pouvez également demander à Rust d'afficher la pile d'appel lorsqu'une panique se produit pour faciliter la recherche de la source de la panique.

> **Déroulement de la pile ou arrêt en cas de panique**
>
> Par défaut, lorsqu'une panique se produit, le programme commence à _dérouler_, ce qui signifie que Rust remonte la pile et nettoie les données de chaque fonction qu'il rencontre. Cependant, remonter et nettoyer prend beaucoup de temps. Rust permet donc de choisir l'alternative consistant à _arrêter immédiatement_, ce qui termine le programme sans nettoyage.
>
> La mémoire utilisée par le programme devra ensuite être nettoyée par le système d'exploitation. Si dans votre projet vous devez rendre le binaire résultant le plus petit possible, vous pouvez passer du déroulement à l'arrêt en cas de panique en ajoutant `panic = 'abort'` aux sections `[profile]` appropriées de votre fichier `Cargo.toml`. Par exemple, si vous voulez arrêter en cas de panique en mode release, ajoutez ceci :
>
> ```toml
> [profile.release]
> panic = 'abort'
> ```

Essayons d'appeler `panic!` dans un programme simple :

Nom de fichier : `src/main.rs`

```rust
fn main() {
    panic!("crash and burn");
}
```

Lorsque vous exécutez le programme, vous verrez quelque chose comme ceci :

    thread 'main' panicked at 'crash and burn', src/main.rs:2:5
    note: run with `RUST_BACKTRACE=1` environment variable to display
    a backtrace

L'appel à `panic!` provoque le message d'erreur contenu dans les deux dernières lignes. La première ligne montre notre message de panique et l'endroit dans notre code source où la panique s'est produite : _src/main.rs:2:5_ indique que c'est la deuxième ligne, cinquième caractère de notre fichier `src/main.rs`.

Dans ce cas, la ligne indiquée est une partie de notre code, et si nous allons à cette ligne, nous voyons l'appel à la macro `panic!`. Dans d'autres cas, l'appel à `panic!` peut être dans du code que notre code appelle, et le nom de fichier et le numéro de ligne rapportés par le message d'erreur seront le code d'un autre et où la macro `panic!` est appelée, pas la ligne de notre code qui a finalement entraîné l'appel à `panic!`.

Nous pouvons utiliser la trace de pile des fonctions provenant de l'appel à `panic!` pour déterminer la partie de notre code qui pose problème. Pour comprendre comment utiliser une trace de pile de `panic!`, considérons un autre exemple et voyons ce que c'est lorsqu'un appel à `panic!` provient d'une bibliothèque en raison d'un bogue dans notre code plutôt que de notre code appelant directement la macro. La liste 9-1 contient du code qui tente d'accéder à un index dans un vecteur au-delà de la plage d'indexes valides.

Nom de fichier : `src/main.rs`

```rust
fn main() {
    let v = vec![1, 2, 3];

    v[99];
}
```

Liste 9-1 : Tentative d'accès à un élément au-delà de la fin d'un vecteur, ce qui entraînera un appel à `panic!`

Ici, nous tentons d'accéder au 100ème élément de notre vecteur (qui se trouve à l'index 99 car l'indexation commence à zéro), mais le vecteur n'a que trois éléments. Dans cette situation, Rust déclenchera une panique. Utiliser `[]` est censé renvoyer un élément, mais si vous passez un index invalide, il n'y a pas d'élément que Rust pourrait renvoyer ici qui serait correct.

En C, tenter de lire au-delà de la fin d'une structure de données est un comportement non défini. Vous pouvez obtenir ce qui se trouve à l'emplacement mémoire correspondant à cet élément dans la structure de données, même si la mémoire n'appartient pas à cette structure. Cela s'appelle une _lecture en dehors des limites_ et peut entraîner des vulnérabilités de sécurité si un attaquant est capable de manipuler l'index de manière à lire des données qu'il ne devrait pas être autorisé à lire qui sont stockées après la structure de données.

Pour protéger votre programme contre ce type de vulnérabilité, si vous essayez de lire un élément à un index qui n'existe pas, Rust arrêtera l'exécution et refusera de continuer. Essayons-le et voyons :

    thread 'main' panicked at 'index out of bounds: the len is 3 but the index is
    99', src/main.rs:4:5
    note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace

Cette erreur pointe vers la ligne 4 de notre `main.rs` où nous tentons d'accéder à `index`.

La ligne `note:` nous indique que nous pouvons définir la variable d'environnement `RUST_BACKTRACE` pour obtenir une trace de pile de ce qui s'est exactement passé pour provoquer l'erreur. Une _trace de pile_ est une liste de toutes les fonctions qui ont été appelées pour arriver à ce point. Les traces de pile en Rust fonctionnent comme dans les autres langages : la clé pour lire la trace de pile est de commencer depuis le haut et de lire jusqu'à ce que vous voyiez des fichiers que vous avez écrits. C'est là que le problème est apparu. Les lignes au-dessus de cet emplacement sont du code que votre code a appelé ; les lignes en-dessous sont du code qui a appelé votre code. Ces lignes d'avant et d'après peuvent inclure du code Rust de base, du code de la bibliothèque standard ou des boîtes à outils que vous utilisez. Essayons d'obtenir une trace de pile en définissant la variable d'environnement `RUST_BACKTRACE` à n'importe quelle valeur autre que `0`. La liste 9-2 montre une sortie similaire à ce que vous verrez.

```bash
$ RUST_BACKTRACE=1 cargo run
thread 'main' panicked at 'index out of bounds: the len is 3 but the index is
99', src/main.rs:4:5
stack backtrace:
0: rust_begin_unwind
at /rustc/e092d0b6b43f2de967af0887873151bb1c0b18d3/library/std
/src/panicking.rs:584:5
1: core::panicking::panic_fmt
at /rustc/e092d0b6b43f2de967af0887873151bb1c0b18d3/library/core
/src/panicking.rs:142:14
2: core::panicking::panic_bounds_check
at /rustc/e092d0b6b43f2de967af0887873151bb1c0b18d3/library/core
/src/panicking.rs:84:5
3: < usize as core::slice::index::SliceIndex < [T] >> ::index
at /rustc/e092d0b6b43f2de967af0887873151bb1c0b18d3/library/core
/src/slice/index.rs:242:10
4: core::slice::index:: core::ops::index::Index [T] < impl < I > for > ::index
at /rustc/e092d0b6b43f2de967af0887873151bb1c0b18d3/library/core
/src/slice/index.rs:18:9
5: < alloc::vec::Vec < T,A > as core::ops::index::Index < I >> ::index
at /rustc/e092d0b6b43f2de967af0887873151bb1c0b18d3/library/alloc
/src/vec/mod.rs:2591:9
6: panic::main
at./src/main.rs:4:5
7: core::ops::function::FnOnce::call_once
at /rustc/e092d0b6b43f2de967af0887873151bb1c0b18d3/library/core
/src/ops/function.rs:248:5
note: Some details are omitted, run with $(RUST_BACKTRACE=full) for a verbose
backtrace.
```

Liste 9-2 : La trace de pile générée par un appel à `panic!` affichée lorsque la variable d'environnement `RUST_BACKTRACE` est définie

C'est beaucoup de sortie! La sortie exacte que vous voyez peut différer selon votre système d'exploitation et votre version de Rust. Pour obtenir des traces de pile avec cette information, les symboles de débogage doivent être activés. Les symboles de débogage sont activés par défaut lorsqu'on utilise `cargo build` ou `cargo run` sans le drapeau `--release`, comme nous l'avons fait ici.

Dans la sortie de la liste 9-2, la ligne 6 de la trace de pile pointe vers la ligne de notre projet qui pose problème : la ligne 4 de `src/main.rs`. Si nous ne voulons pas que notre programme panique, nous devrions commencer notre enquête à l'endroit indiqué par la première ligne mentionnant un fichier que nous avons écrit. Dans la liste 9-1, où nous avons délibérément écrit du code qui provoquerait une panique, la façon de corriger la panique est de ne pas demander un élément au-delà de la plage d'indexes du vecteur. Lorsque votre code panique à l'avenir, vous devrez déterminer quelle action le code effectue avec quelles valeurs pour provoquer la panique et ce que le code devrait faire à la place.

Nous reviendrons sur `panic!` et sur le moment où il faut et ne pas utiliser `panic!` pour gérer les conditions d'erreur dans "To panic! or Not to panic!". Ensuite, nous verrons comment récupérer d'une erreur en utilisant `Result`.
