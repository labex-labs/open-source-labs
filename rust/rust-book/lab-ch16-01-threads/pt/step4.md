# Usando Closures `move` com Threads

Frequentemente usaremos a palavra-chave `move` com closures passados para `thread::spawn` porque o closure então assumirá a propriedade dos valores que usa do ambiente, transferindo assim a propriedade desses valores de uma thread para outra. Em "Capturando o Ambiente com Closures", discutimos `move` no contexto de closures. Agora, vamos nos concentrar mais na interação entre `move` e `thread::spawn`.

Observe na Listagem 16-1 que o closure que passamos para `thread::spawn` não recebe argumentos: não estamos usando nenhum dado da thread principal no código da thread gerada. Para usar dados da thread principal na thread gerada, o closure da thread gerada deve capturar os valores de que precisa. A Listagem 16-3 mostra uma tentativa de criar um vetor na thread principal e usá-lo na thread gerada. No entanto, isso ainda não funcionará, como você verá em um momento.

Nome do arquivo: `src/main.rs`

```rust
use std::thread;

fn main() {
    let v = vec![1, 2, 3];

    let handle = thread::spawn(|| {
        println!("Here's a vector: {:?}", v);
    });

    handle.join().unwrap();
}
```

Listagem 16-3: Tentando usar um vetor criado pela thread principal em outra thread

O closure usa `v`, então ele capturará `v` e o tornará parte do ambiente do closure. Como `thread::spawn` executa este closure em uma nova thread, devemos ser capazes de acessar `v` dentro dessa nova thread. Mas quando compilamos este exemplo, obtemos o seguinte erro:

```bash
error[E0373]: closure may outlive the current function, but it borrows `v`,
which is owned by the current function
 --> src/main.rs:6:32
  |
6 |     let handle = thread::spawn(|| {
  |                                ^^ may outlive borrowed value `v`
7 |         println!("Here's a vector: {:?}", v);
  |                                           - `v` is borrowed here
  |
note: function requires argument type to outlive `'static`
 --> src/main.rs:6:18
  |
6 |       let handle = thread::spawn(|| {
  |  __________________^
7 | |         println!("Here's a vector: {:?}", v);
8 | |     });
  | |______^
help: to force the closure to take ownership of `v` (and any other referenced
variables), use the `move` keyword
  |
6 |     let handle = thread::spawn(move || {
  |                                ++++
```

Rust _infere_ como capturar `v` e, como `println!` só precisa de uma referência a `v`, o closure tenta emprestar `v`. No entanto, há um problema: Rust não pode dizer por quanto tempo a thread gerada será executada, então não sabe se a referência a `v` sempre será válida.

A Listagem 16-4 fornece um cenário que é mais provável de ter uma referência a `v` que não será válida.

Nome do arquivo: `src/main.rs`

```rust
use std::thread;

fn main() {
    let v = vec![1, 2, 3];

    let handle = thread::spawn(|| {
        println!("Here's a vector: {:?}", v);
    });

    drop(v); // oh no!

    handle.join().unwrap();
}
```

Listagem 16-4: Uma thread com um closure que tenta capturar uma referência a `v` de uma thread principal que descarta `v`

Se Rust nos permitisse executar este código, haveria a possibilidade de que a thread gerada fosse imediatamente colocada em segundo plano sem ser executada. A thread gerada tem uma referência a `v` dentro, mas a thread principal descarta imediatamente `v`, usando a função `drop` que discutimos no Capítulo 15. Então, quando a thread gerada começa a executar, `v` não é mais válido, então uma referência a ele também é inválida. Oh não!

Para corrigir o erro do compilador na Listagem 16-3, podemos usar o conselho da mensagem de erro:

    help: to force the closure to take ownership of `v` (and any other referenced
    variables), use the `move` keyword
      |
    6 |     let handle = thread::spawn(move || {
      |                                ++++

Adicionando a palavra-chave `move` antes do closure, forçamos o closure a assumir a propriedade dos valores que está usando, em vez de permitir que Rust infira que ele deve emprestar os valores. A modificação na Listagem 16-3 mostrada na Listagem 16-5 compilará e será executada como pretendemos.

Nome do arquivo: `src/main.rs`

```rust
use std::thread;

fn main() {
    let v = vec![1, 2, 3];

    let handle = thread::spawn(move || {
        println!("Here's a vector: {:?}", v);
    });

    handle.join().unwrap();
}
```

Listagem 16-5: Usando a palavra-chave `move` para forçar um closure a assumir a propriedade dos valores que usa

Podemos ser tentados a tentar a mesma coisa para corrigir o código na Listagem 16-4, onde a thread principal chamou `drop`, usando um closure `move`. No entanto, esta correção não funcionará porque o que a Listagem 16-4 está tentando fazer é proibido por um motivo diferente. Se adicionássemos `move` ao closure, moveríamos `v` para o ambiente do closure, e não poderíamos mais chamar `drop` nele na thread principal. Em vez disso, obteríamos este erro do compilador:

```bash
error[E0382]: use of moved value: `v`
  --> src/main.rs:10:10
   |
4  |     let v = vec![1, 2, 3];
   |         - move occurs because `v` has type `Vec<i32>`, which does not
implement the `Copy` trait
5  |
6  |     let handle = thread::spawn(move || {
   |                                ------- value moved into closure here
7  |         println!("Here's a vector: {:?}", v);
   |                                           - variable moved due to use in
closure
...
10 |     drop(v); // oh no!
   |          ^ value used here after move
```

As regras de propriedade do Rust nos salvaram novamente! Recebemos um erro do código na Listagem 16-3 porque Rust estava sendo conservador e apenas emprestando `v` para a thread, o que significava que a thread principal poderia, teoricamente, invalidar a referência da thread gerada. Ao dizer a Rust para mover a propriedade de `v` para a thread gerada, estamos garantindo a Rust que a thread principal não usará mais `v`. Se mudarmos a Listagem 16-4 da mesma forma, estaremos violando as regras de propriedade quando tentarmos usar `v` na thread principal. A palavra-chave `move` substitui o padrão conservador de empréstimo do Rust; ela não nos permite violar as regras de propriedade.

Agora que cobrimos o que são threads e os métodos fornecidos pela API de threads, vamos analisar algumas situações em que podemos usar threads.
