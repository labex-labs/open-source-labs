# A API de Mutex`<T>`{=html}

Como exemplo de como usar um mutex, vamos começar usando um mutex em um contexto de _single-threaded_ (única _thread_), conforme mostrado na Listagem 16-12.

Nome do arquivo: `src/main.rs`

```rust
use std::sync::Mutex;

fn main() {
  1 let m = Mutex::new(5);

    {
      2 let mut num = m.lock().unwrap();
      3 *num = 6;
  4 }

  5 println!("m = {:?}", m);
}
```

Listagem 16-12: Explorando a API de `Mutex<T>` em um contexto de _single-threaded_ para simplificar

Como acontece com muitos tipos, criamos um `Mutex<T>` usando a função associada `new` \[1]. Para acessar os dados dentro do mutex, usamos o método `lock` para adquirir o bloqueio \[2]. Essa chamada bloqueará a _thread_ atual para que ela não possa fazer nenhum trabalho até que seja nossa vez de ter o bloqueio.

A chamada para `lock` falharia se outra _thread_ que detém o bloqueio entrasse em pânico. Nesse caso, ninguém seria capaz de obter o bloqueio, então escolhemos `unwrap` e fazemos com que esta _thread_ entre em pânico se estivermos nessa situação.

Depois de adquirir o bloqueio, podemos tratar o valor de retorno, chamado `num` neste caso, como uma referência mutável aos dados internos. O sistema de tipos garante que adquirimos um bloqueio antes de usar o valor em `m`. O tipo de `m` é `Mutex<i32>`, não `i32`, então _devemos_ chamar `lock` para poder usar o valor `i32`. Não podemos esquecer; o sistema de tipos não nos permitirá acessar o `i32` interno de outra forma.

Como você pode suspeitar, `Mutex<T>` é um _smart pointer_ (ponteiro inteligente). Mais precisamente, a chamada para `lock` _retorna_ um _smart pointer_ chamado `MutexGuard`, encapsulado em um `LockResult` que tratamos com a chamada para `unwrap`. O _smart pointer_ `MutexGuard` implementa `Deref` para apontar para nossos dados internos; o _smart pointer_ também possui uma implementação `Drop` que libera o bloqueio automaticamente quando um `MutexGuard` sai do escopo, o que acontece no final do escopo interno \[4]. Como resultado, não corremos o risco de esquecer de liberar o bloqueio e bloquear o mutex de ser usado por outras _threads_ porque a liberação do bloqueio acontece automaticamente.

Depois de descartar o bloqueio, podemos imprimir o valor do mutex e ver que fomos capazes de alterar o `i32` interno para `6` \[5].
