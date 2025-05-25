# Capturando Referências ou Movendo a Propriedade

Closures podem capturar valores de seu ambiente de três maneiras, que mapeiam diretamente para as três maneiras que uma função pode receber um parâmetro: emprestando imutavelmente, emprestando mutavelmente e tomando posse. A closure decidirá qual delas usar com base no que o corpo da função faz com os valores capturados.

Na Listagem 13-4, definimos uma closure que captura uma referência imutável ao vetor chamado `list` porque ela só precisa de uma referência imutável para imprimir o valor.

Nome do arquivo: `src/main.rs`

```rust
fn main() {
    let list = vec![1, 2, 3];
    println!("Before defining closure: {:?}", list);

  1 let only_borrows = || println!("From closure: {:?}", list);

    println!("Before calling closure: {:?}", list);
  2 only_borrows();
    println!("After calling closure: {:?}", list);
}
```

Listagem 13-4: Definindo e chamando uma closure que captura uma referência imutável

Este exemplo também ilustra que uma variável pode se vincular a uma definição de closure \[1], e podemos mais tarde chamar a closure usando o nome da variável e parênteses como se o nome da variável fosse o nome de uma função \[2].

Como podemos ter várias referências imutáveis a `list` ao mesmo tempo, `list` ainda é acessível a partir do código antes da definição da closure, após a definição da closure, mas antes da closure ser chamada, e após a closure ser chamada. Este código compila, executa e imprime:

    Before defining closure: [1, 2, 3]
    Before calling closure: [1, 2, 3]
    From closure: [1, 2, 3]
    After calling closure: [1, 2, 3]

Em seguida, na Listagem 13-5, alteramos o corpo da closure para que ele adicione um elemento ao vetor `list`. A closure agora captura uma referência mutável.

Nome do arquivo: `src/main.rs`

```rust
fn main() {
    let mut list = vec![1, 2, 3];
    println!("Before defining closure: {:?}", list);

    let mut borrows_mutably = || list.push(7);

    borrows_mutably();
    println!("After calling closure: {:?}", list);
}
```

Listagem 13-5: Definindo e chamando uma closure que captura uma referência mutável

Este código compila, executa e imprime:

```rust
Before defining closure: [1, 2, 3]
After calling closure: [1, 2, 3, 7]
```

Observe que não há mais um `println!` entre a definição e a chamada da closure `borrows_mutably`: quando `borrows_mutably` é definida, ela captura uma referência mutável a `list`. Não usamos a closure novamente após a closure ser chamada, então o empréstimo mutável termina. Entre a definição da closure e a chamada da closure, um empréstimo imutável para imprimir não é permitido porque nenhum outro empréstimo é permitido quando há um empréstimo mutável. Tente adicionar um `println!` lá para ver qual mensagem de erro você recebe!

Se você quiser forçar a closure a tomar posse dos valores que ela usa no ambiente, mesmo que o corpo da closure não precise estritamente da posse, você pode usar a palavra-chave `move` antes da lista de parâmetros.

Essa técnica é principalmente útil ao passar uma closure para uma nova thread para mover os dados para que eles sejam de propriedade da nova thread. Discutiremos threads e por que você gostaria de usá-los em detalhes no Capítulo 16, quando falarmos sobre concorrência, mas por enquanto, vamos explorar brevemente a criação de uma nova thread usando uma closure que precisa da palavra-chave `move`. A Listagem 13-6 mostra a Listagem 13-4 modificada para imprimir o vetor em uma nova thread, em vez de na thread principal.

Nome do arquivo: `src/main.rs`

```rust
use std::thread;

fn main() {
    let list = vec![1, 2, 3];
    println!("Before defining closure: {:?}", list);

  1 thread::spawn(move || {
      2 println!("From thread: {:?}", list)
    }).join().unwrap();
}
```

Listagem 13-6: Usando `move` para forçar a closure para a thread a tomar posse de `list`

Geramos uma nova thread, dando à thread uma closure para executar como um argumento. O corpo da closure imprime a lista. Na Listagem 13-4, a closure só capturou `list` usando uma referência imutável porque essa é a menor quantidade de acesso a `list` necessária para imprimi-la. Neste exemplo, embora o corpo da closure ainda precise apenas de uma referência imutável \[2], precisamos especificar que `list` deve ser movido para a closure colocando a palavra-chave `move` \[1] no início da definição da closure. A nova thread pode terminar antes que o restante da thread principal termine, ou a thread principal pode terminar primeiro. Se a thread principal mantiver a posse de `list`, mas terminar antes da nova thread e descartar `list`, a referência imutável na thread seria inválida. Portanto, o compilador exige que `list` seja movido para a closure fornecida à nova thread para que a referência seja válida. Tente remover a palavra-chave `move` ou usar `list` na thread principal após a closure ser definida para ver quais erros do compilador você recebe!
