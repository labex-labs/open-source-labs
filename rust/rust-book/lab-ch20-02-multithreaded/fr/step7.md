# Validating the Number of Threads in new

Nous ne faisons rien avec les paramètres de `new` et `execute`. Implémentons le corps de ces fonctions avec le comportement que nous voulons. Pour commencer, pensons à `new`. Plus tôt, nous avons choisi un type non signé pour le paramètre `size` car un pool avec un nombre négatif de threads n'a pas de sens. Cependant, un pool avec zéro threads n'a pas de sens non plus, et pourtant zéro est un `usize` parfaitement valide. Nous allons ajouter du code pour vérifier que `size` est supérieur à zéro avant de renvoyer une instance de `ThreadPool` et faire planter le programme s'il reçoit un zéro en utilisant le macro `assert!`, comme montré dans le Listing 20-13.

Nom de fichier : `src/lib.rs`

```rust
impl ThreadPool {
    /// Crée un nouveau ThreadPool.
    ///
    /// La taille est le nombre de threads dans le pool.
    ///
  1 /// # Panics
    ///
    /// La fonction `new` provoquera une panique si la taille est égale à zéro.
    pub fn new(size: usize) -> ThreadPool {
      2 assert!(size > 0);

        ThreadPool
    }

    --snip--
}
```

Listing 20-13 : Implémentation de `ThreadPool::new` pour provoquer une panique si `size` est égal à zéro

Nous avons également ajouté de la documentation pour notre `ThreadPool` avec des commentaires de doc. Notez que nous avons suivi les bonnes pratiques de documentation en ajoutant une section qui indique les situations dans lesquelles notre fonction peut provoquer une panique \[1\], comme discuté au Chapitre 14. Essayez d'exécuter `cargo doc --open` et cliquez sur la structure `ThreadPool` pour voir à quoi ressemblent les docs générées pour `new`!

Au lieu d'ajouter le macro `assert!` comme nous l'avons fait ici \[2\], nous pourrions changer `new` en `build` et renvoyer un `Result` comme nous l'avons fait avec `Config::build` dans le projet I/O du Listing 12-9. Mais dans ce cas, nous avons décidé qu'essayer de créer un thread pool sans aucun thread devrait être une erreur irrécupérable. Si vous êtes ambitieux, essayez d'écrire une fonction nommée `build` avec la signature suivante pour la comparer avec la fonction `new` :

```rust
pub fn build(
    size: usize
) -> Result<ThreadPool, PoolCreationError> {
```
