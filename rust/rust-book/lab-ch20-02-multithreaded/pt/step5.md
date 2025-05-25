# Criando um Número Finito de Threads

Queremos que nosso pool de threads funcione de maneira semelhante e familiar, para que a mudança de threads para um pool de threads não exija grandes alterações no código que usa nossa API. A Listagem 20-12 mostra a interface hipotética para uma struct `ThreadPool` que queremos usar em vez de `thread::spawn`.

Nome do arquivo: `src/main.rs`

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

Listagem 20-12: Nossa interface `ThreadPool` ideal

Usamos `ThreadPool::new` para criar um novo pool de threads com um número configurável de threads, neste caso quatro \[1]. Então, no loop `for`, `pool.execute` tem uma interface semelhante a `thread::spawn`, pois recebe um closure que o pool deve executar para cada fluxo \[2]. Precisamos implementar `pool.execute` para que ele receba o closure e o dê a uma thread no pool para executar. Este código ainda não compilará, mas tentaremos para que o compilador possa nos guiar em como corrigi-lo.
