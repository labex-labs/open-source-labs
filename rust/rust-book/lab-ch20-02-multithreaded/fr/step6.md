# Building ThreadPool Using Compiler-Driven Development

Apportez les modifications du Listing 20-12 à `src/main.rs`, puis utilisons les erreurs du compilateur provenant de `cargo check` pour guider notre développement. Voici la première erreur que nous obtenons :

```bash
$ cargo check
    Checking hello v0.1.0 (file:///projects/hello)
error[E0433]: failed to resolve: use of undeclared type `ThreadPool`
  --> src/main.rs:11:16
   |
11 |     let pool = ThreadPool::new(4);
   |                ^^^^^^^^^^ use of undeclared type `ThreadPool`
```

Parfait! Cette erreur nous indique que nous avons besoin d'un type ou d'un module `ThreadPool`, donc nous allons en construire un maintenant. Notre implémentation de `ThreadPool` sera indépendante du type de travail que fait notre serveur web. Alors, passons le crate `hello` d'un crate binaire à un crate bibliothèque pour y conserver notre implémentation de `ThreadPool`. Après avoir changé en un crate bibliothèque, nous pourrions également utiliser la bibliothèque de thread pool séparée pour tout travail que nous voudrions effectuer à l'aide d'un thread pool, pas seulement pour servir des requêtes web.

Créez un fichier `src/lib.rs` qui contient ce qui suit, qui est la définition la plus simple d'une structure `ThreadPool` que nous pouvons avoir pour l'instant :

Nom de fichier : `src/lib.rs`

```rust
pub struct ThreadPool;
```

Ensuite, éditez le fichier `main.rs` pour porter `ThreadPool` dans la portée à partir du crate bibliothèque en ajoutant le code suivant en haut de `src/main.rs` :

Nom de fichier : `src/main.rs`

```rust
use hello::ThreadPool;
```

Ce code ne fonctionnera toujours pas, mais vérifions-le à nouveau pour obtenir la prochaine erreur que nous devons résoudre :

```bash
$ cargo check
    Checking hello v0.1.0 (file:///projects/hello)
error[E0599]: no function or associated item named `new` found for struct
`ThreadPool` in the current scope
  --> src/main.rs:12:28
   |
12 |     let pool = ThreadPool::new(4);
   |                            ^^^ function or associated item not found in
`ThreadPool`
```

Cette erreur indique que nous devons ensuite créer une fonction associée nommée `new` pour `ThreadPool`. Nous savons également que `new` doit avoir un paramètre qui peut accepter `4` en tant qu'argument et devrait renvoyer une instance de `ThreadPool`. Implémentons la fonction `new` la plus simple qui aura ces caractéristiques :

Nom de fichier : `src/lib.rs`

```rust
pub struct ThreadPool;

impl ThreadPool {
    pub fn new(size: usize) -> ThreadPool {
        ThreadPool
    }
}
```

Nous avons choisi `usize` comme type du paramètre `size` car nous savons qu'un nombre négatif de threads n'a pas de sens. Nous savons également que nous utiliserons ce `4` comme nombre d'éléments dans une collection de threads, ce qui est ce que le type `usize` est destiné à, comme discuté dans "Types entiers".

Vérifions le code à nouveau :

```bash
$ cargo check
    Checking hello v0.1.0 (file:///projects/hello)
error[E0599]: no method named `execute` found for struct `ThreadPool` in the
current scope
  --> src/main.rs:17:14
   |
17 |         pool.execute(|| {
   |              ^^^^^^^ method not found in `ThreadPool`
```

Maintenant, l'erreur se produit parce que nous n'avons pas de méthode `execute` sur `ThreadPool`. Rappelez-vous de "Creating a Finite Number of Threads" que nous avons décidé que notre thread pool devrait avoir une interface similaire à `thread::spawn`. De plus, nous allons implémenter la fonction `execute` de sorte qu'elle prenne la closure qui lui est donnée et la donne à un thread inactif dans le pool pour l'exécuter.

Nous allons définir la méthode `execute` sur `ThreadPool` pour prendre une closure en tant que paramètre. Rappelez-vous de "Moving Captured Values Out of Closures and the Fn Traits" que nous pouvons prendre des closures en tant que paramètres avec trois traits différents : `Fn`, `FnMut` et `FnOnce`. Nous devons décider quel type de closure utiliser ici. Nous savons que nous finirons par faire quelque chose de similaire à l'implémentation de `thread::spawn` de la bibliothèque standard, donc nous pouvons regarder quelles contraintes a la signature de `thread::spawn` sur son paramètre. La documentation nous montre ce qui suit :

```rust
pub fn spawn<F, T>(f: F) -> JoinHandle<T>
    where
        F: FnOnce() -> T,
        F: Send + 'static,
        T: Send + 'static,
```

Le paramètre de type `F` est celui qui nous intéresse ici ; le paramètre de type `T` est lié à la valeur de retour, et nous n'avons pas à nous en occuper. Nous pouvons voir que `spawn` utilise `FnOnce` comme contrainte de trait sur `F`. C'est probablement ce que nous voulons également, car nous finirons par passer l'argument que nous obtenons dans `execute` à `spawn`. Nous pouvons être encore plus convaincus que `FnOnce` est le trait que nous voulons utiliser car le thread pour exécuter une requête n'exécutera la closure de cette requête qu'une seule fois, ce qui correspond à l'`Once` dans `FnOnce`.

Le paramètre de type `F` a également la contrainte de trait `Send` et la contrainte de durée de vie `'static`, qui sont utiles dans notre cas : nous avons besoin de `Send` pour transférer la closure d'un thread à un autre et `'static` car nous ne savons pas combien de temps le thread mettra pour s'exécuter. Créons une méthode `execute` sur `ThreadPool` qui prendra un paramètre générique de type `F` avec ces contraintes :

Nom de fichier : `src/lib.rs`

```rust
impl ThreadPool {
    --snip--
    pub fn execute<F>(&self, f: F)
    where
        F: FnOnce() 1 + Send + 'static,
    {
    }
}
```

Nous utilisons toujours les `()` après `FnOnce` \[1\] car ce `FnOnce` représente une closure qui prend aucun paramètre et renvoie le type unité `()`. Tout comme les définitions de fonctions, le type de retour peut être omis de la signature, mais même si nous n'avons pas de paramètres, nous avons toujours besoin des parenthèses.

Encore une fois, c'est la plus simple implémentation de la méthode `execute` : elle ne fait rien, mais nous essayons seulement de compiler notre code. Vérifions-le à nouveau :

```bash
$ cargo check
    Checking hello v0.1.0 (file:///projects/hello)
    Finished dev [unoptimized + debuginfo] target(s) in 0.24s
```

Ça compile! Mais notez que si vous essayez `cargo run` et que vous effectuez une requête dans le navigateur, vous verrez les erreurs dans le navigateur que nous avons vues au début du chapitre. Notre bibliothèque n'appelle pas encore la closure passée à `execute`!

> Note : Vous pourriez entendre dire à propos de langages avec des compilateurs stricts, tels que Haskell et Rust, que "si le code compile, ça fonctionne". Mais cette expression n'est pas universellement vraie. Notre projet compile, mais il ne fait absolument rien! Si nous construisions un projet réel et complet, il serait temps de commencer à écrire des tests unitaires pour vérifier que le code compile _et_ a le comportement que nous voulons.
