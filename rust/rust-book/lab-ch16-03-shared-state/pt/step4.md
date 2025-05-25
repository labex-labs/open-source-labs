# Compartilhando um Mutex`<T>`{=html} Entre Múltiplas Threads

Agora, vamos tentar compartilhar um valor entre múltiplas _threads_ usando `Mutex<T>`. Vamos iniciar 10 _threads_ e fazer com que cada uma incremente um valor de contador em 1, para que o contador vá de 0 a 10. O exemplo na Listagem 16-13 terá um erro de compilação, e usaremos esse erro para aprender mais sobre como usar `Mutex<T>` e como o Rust nos ajuda a usá-lo corretamente.

Nome do arquivo: `src/main.rs`

```rust
use std::sync::Mutex;
use std::thread;

fn main() {
  1 let counter = Mutex::new(0);
    let mut handles = vec![];

  2 for _ in 0..10 {
      3 let handle = thread::spawn(move || {
          4 let mut num = counter.lock().unwrap();

          5 *num += 1;
        });
      6 handles.push(handle);
    }

    for handle in handles {
      7 handle.join().unwrap();
    }

  8 println!("Result: {}", *counter.lock().unwrap());
}
```

Listagem 16-13: Dez _threads_, cada uma incrementando um contador guardado por um `Mutex<T>`

Criamos uma variável `counter` para armazenar um `i32` dentro de um `Mutex<T>` \[1], como fizemos na Listagem 16-12. Em seguida, criamos 10 _threads_ iterando sobre uma faixa de números \[2]. Usamos `thread::spawn` e damos a todas as _threads_ a mesma _closure_: uma que move o contador para a _thread_ \[3], adquire um bloqueio no `Mutex<T>` chamando o método `lock` \[4] e, em seguida, adiciona 1 ao valor no mutex \[5]. Quando uma _thread_ termina de executar sua _closure_, `num` sairá do escopo e liberará o bloqueio para que outra _thread_ possa adquiri-lo.

Na _thread_ principal, coletamos todos os _join handles_ \[6]. Então, como fizemos na Listagem 16-2, chamamos `join` em cada _handle_ para garantir que todas as _threads_ terminem \[7]. Nesse ponto, a _thread_ principal adquirirá o bloqueio e imprimirá o resultado deste programa \[8].

Sugerimos que este exemplo não compilaria. Agora vamos descobrir o porquê!

```bash
error[E0382]: use of moved value: `counter`
  --> src/main.rs:9:36
   |
5  |     let counter = Mutex::new(0);
   |         ------- move occurs because `counter` has type `Mutex<i32>`, which
does not implement the `Copy` trait
...
9  |         let handle = thread::spawn(move || {
   |                                    ^^^^^^^ value moved into closure here,
in previous iteration of loop
10 |             let mut num = counter.lock().unwrap();
   |                           ------- use occurs due to use in closure
```

A mensagem de erro afirma que o valor `counter` foi movido na iteração anterior do loop. Rust está nos dizendo que não podemos mover a propriedade do bloqueio `counter` para múltiplas _threads_. Vamos corrigir o erro de compilação com o método de propriedade múltipla que discutimos no Capítulo 15.
