# Contagem de Referência Atômica com Arc`<T>`{=html}

Felizmente, `Arc<T>` _é_ um tipo como `Rc<T>` que é seguro para usar em situações concorrentes. O _a_ significa _atômico_ (_atomic_), o que significa que é um tipo com _contagem de referência atômica_ (_atomically reference counted_). Atômicos são um tipo adicional de primitiva de concorrência que não abordaremos em detalhes aqui: consulte a documentação da biblioteca padrão para `std::sync::atomic` para mais detalhes. Neste ponto, você só precisa saber que os atômicos funcionam como tipos primitivos, mas são seguros para compartilhar entre _threads_.

Você pode então se perguntar por que nem todos os tipos primitivos são atômicos e por que os tipos da biblioteca padrão não são implementados para usar `Arc<T>` por padrão. A razão é que a segurança de _thread_ vem com uma penalidade de desempenho que você só quer pagar quando realmente precisa. Se você estiver apenas realizando operações em valores dentro de uma única _thread_, seu código pode ser executado mais rápido se não precisar impor as garantias que os atômicos fornecem.

Vamos retornar ao nosso exemplo: `Arc<T>` e `Rc<T>` têm a mesma API, então corrigimos nosso programa alterando a linha `use`, a chamada para `new` e a chamada para `clone`. O código na Listagem 16-15 finalmente compilará e será executado.

Nome do arquivo: `src/main.rs`

```rust
use std::sync::{Arc, Mutex};
use std::thread;

fn main() {
    let counter = Arc::new(Mutex::new(0));
    let mut handles = vec![];

    for _ in 0..10 {
        let counter = Arc::clone(&counter);
        let handle = thread::spawn(move || {
            let mut num = counter.lock().unwrap();

            *num += 1;
        });
        handles.push(handle);
    }

    for handle in handles {
        handle.join().unwrap();
    }

    println!("Result: {}", *counter.lock().unwrap());
}
```

Listagem 16-15: Usando um `Arc<T>` para encapsular o `Mutex<T>` para poder compartilhar a propriedade entre múltiplas _threads_

Este código imprimirá o seguinte:

```rust
Result: 10
```

Conseguimos! Contamos de 0 a 10, o que pode não parecer muito impressionante, mas nos ensinou muito sobre `Mutex<T>` e segurança de _thread_. Você também pode usar a estrutura deste programa para fazer operações mais complicadas do que apenas incrementar um contador. Usando essa estratégia, você pode dividir um cálculo em partes independentes, dividir essas partes entre _threads_ e, em seguida, usar um `Mutex<T>` para que cada _thread_ atualize o resultado final com sua parte.

Observe que, se você estiver fazendo operações numéricas simples, existem tipos mais simples do que os tipos `Mutex<T>` fornecidos pelo módulo `std::sync::atomic` da biblioteca padrão. Esses tipos fornecem acesso atômico, concorrente e seguro a tipos primitivos. Escolhemos usar `Mutex<T>` com um tipo primitivo para este exemplo para que pudéssemos nos concentrar em como `Mutex<T>` funciona.
