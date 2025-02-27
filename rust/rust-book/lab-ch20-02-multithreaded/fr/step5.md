# Creating a Finite Number of Threads

Nous voulons que notre thread pool fonctionne de manière similaire et familière, de sorte que passer des threads à un thread pool ne nécessite pas de grandes modifications dans le code utilisant notre API. Le Listing 20-12 montre l'interface hypothétique d'une structure `ThreadPool` que nous souhaitons utiliser au lieu de `thread::spawn`.

Nom de fichier : `src/main.rs`

```rust
fn main() {
    let listener = TcpListener::bind("127.0.0.1:7878").unwrap();
  1 let pool = ThreadPool::new(4);

    for stream in listener.incoming() {
        let stream = stream.unwrap();

      2 pool.execute(|| {
            handle_connection(stream);
        });
    }
}
```

Listing 20-12 : Notre interface idéale pour `ThreadPool`

Nous utilisons `ThreadPool::new` pour créer un nouveau thread pool avec un nombre configurable de threads, ici quatre \[1\]. Ensuite, dans la boucle `for`, `pool.execute` a une interface similaire à `thread::spawn` en ce sens qu'il prend une closure que le pool devrait exécuter pour chaque flux \[2\]. Nous devons implémenter `pool.execute` de sorte qu'il prenne la closure et la donne à un thread dans le pool pour l'exécuter. Ce code ne compilera pas encore, mais nous allons essayer pour que le compilateur puisse nous guider sur la manière de le corriger.
