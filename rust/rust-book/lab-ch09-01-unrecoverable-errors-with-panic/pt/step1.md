# Erros Irrecuperáveis com panic

Às vezes, coisas ruins acontecem em seu código, e não há nada que você possa fazer sobre isso. Nesses casos, o Rust tem a macro `panic!`. Existem duas maneiras de causar um panic na prática: tomando uma ação que faz com que nosso código entre em panic (como acessar um array além do final) ou chamando explicitamente a macro `panic!`. Em ambos os casos, causamos um panic em nosso programa. Por padrão, esses panics imprimirão uma mensagem de falha, farão o unwind, limparão a stack e sairão. Por meio de uma variável de ambiente, você também pode fazer com que o Rust exiba a call stack quando um panic ocorre para facilitar o rastreamento da origem do panic.

> **Unwinding a Stack ou Abortando em Resposta a um Panic**
>
> Por padrão, quando um panic ocorre, o programa começa a _unwind_, o que significa que o Rust volta pela stack e limpa os dados de cada função que encontra. No entanto, voltar e limpar é muito trabalho. O Rust, portanto, permite que você escolha a alternativa de _abortar_ imediatamente, o que encerra o programa sem limpar.
>
> A memória que o programa estava usando precisará ser limpa pelo sistema operacional. Se em seu projeto você precisar tornar o binário resultante o menor possível, você pode mudar de unwinding para abortar em um panic adicionando `panic = 'abort'` às seções `[profile]` apropriadas em seu arquivo `Cargo.toml`. Por exemplo, se você quiser abortar em caso de panic no modo release, adicione isto:
>
> ```toml
> [profile.release]
> panic = 'abort'
> ```

Vamos tentar chamar `panic!` em um programa simples:

Nome do arquivo: `src/main.rs`

```rust
fn main() {
    panic!("crash and burn");
}
```

Quando você executa o programa, verá algo assim:

    thread 'main' panicked at 'crash and burn', src/main.rs:2:5
    note: run with `RUST_BACKTRACE=1` environment variable to display
    a backtrace

A chamada para `panic!` causa a mensagem de erro contida nas duas últimas linhas. A primeira linha mostra nossa mensagem de panic e o local em nosso código-fonte onde o panic ocorreu: _src/main.rs:2:5_ indica que é a segunda linha, quinto caractere do nosso arquivo `src/main.rs`.

Neste caso, a linha indicada faz parte do nosso código, e se formos para essa linha, vemos a chamada da macro `panic!`. Em outros casos, a chamada `panic!` pode estar no código que nosso código chama, e o nome do arquivo e o número da linha relatados pela mensagem de erro serão o código de outra pessoa onde a macro `panic!` é chamada, não a linha do nosso código que eventualmente levou à chamada `panic!`.

Podemos usar o backtrace das funções de onde a chamada `panic!` veio para descobrir a parte do nosso código que está causando o problema. Para entender como usar um backtrace de `panic!`, vamos analisar outro exemplo e ver como é quando uma chamada `panic!` vem de uma biblioteca por causa de um bug em nosso código, em vez de nosso código chamar a macro diretamente. A Listagem 9-1 tem algum código que tenta acessar um índice em um vetor além do intervalo de índices válidos.

Nome do arquivo: `src/main.rs`

```rust
fn main() {
    let v = vec![1, 2, 3];

    v[99];
}
```

Listagem 9-1: Tentando acessar um elemento além do final de um vetor, o que causará uma chamada para `panic!`

Aqui, estamos tentando acessar o 100º elemento do nosso vetor (que está no índice 99 porque a indexação começa em zero), mas o vetor tem apenas três elementos. Nessa situação, o Rust entrará em panic. Usar `[]` é suposto retornar um elemento, mas se você passar um índice inválido, não há nenhum elemento que o Rust possa retornar aqui que seria correto.

Em C, tentar ler além do final de uma estrutura de dados é um comportamento indefinido. Você pode obter o que estiver no local da memória que corresponderia a esse elemento na estrutura de dados, mesmo que a memória não pertença a essa estrutura. Isso é chamado de _buffer overread_ e pode levar a vulnerabilidades de segurança se um invasor conseguir manipular o índice de tal forma a ler dados que não deveriam ser permitidos que são armazenados após a estrutura de dados.

Para proteger seu programa desse tipo de vulnerabilidade, se você tentar ler um elemento em um índice que não existe, o Rust interromperá a execução e se recusará a continuar. Vamos tentar e ver:

    thread 'main' panicked at 'index out of bounds: the len is 3 but the index is
    99', src/main.rs:4:5
    note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace

Este erro aponta para a linha 4 do nosso `main.rs` onde tentamos acessar `index`.

A linha `note:` nos diz que podemos definir a variável de ambiente `RUST_BACKTRACE` para obter um backtrace de exatamente o que aconteceu para causar o erro. Um _backtrace_ é uma lista de todas as funções que foram chamadas para chegar a este ponto. Backtraces em Rust funcionam como em outras linguagens: a chave para ler o backtrace é começar de cima e ler até ver arquivos que você escreveu. Esse é o ponto onde o problema se originou. As linhas acima desse ponto são código que seu código chamou; as linhas abaixo são código que chamou seu código. Essas linhas antes e depois podem incluir código Rust principal, código de biblioteca padrão ou crates que você está usando. Vamos tentar obter um backtrace definindo a variável de ambiente `RUST_BACKTRACE` para qualquer valor, exceto `0`. A Listagem 9-2 mostra uma saída semelhante ao que você verá.

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
at ./src/main.rs:4:5
7: core::ops::function::FnOnce::call_once
at /rustc/e092d0b6b43f2de967af0887873151bb1c0b18d3/library/core
/src/ops/function.rs:248:5
note: Some details are omitted, run with $(RUST_BACKTRACE=full) for a verbose
backtrace.
```

Listagem 9-2: O backtrace gerado por uma chamada para `panic!` exibido quando a variável de ambiente `RUST_BACKTRACE` é definida

Essa é muita saída! A saída exata que você vê pode ser diferente dependendo do seu sistema operacional e da versão do Rust. Para obter backtraces com essas informações, os símbolos de depuração devem estar habilitados. Os símbolos de depuração são habilitados por padrão ao usar `cargo build` ou `cargo run` sem a flag `--release`, como fizemos aqui.

Na saída na Listagem 9-2, a linha 6 do backtrace aponta para a linha em nosso projeto que está causando o problema: a linha 4 de `src/main.rs`. Se não quisermos que nosso programa entre em panic, devemos iniciar nossa investigação no local apontado pela primeira linha que menciona um arquivo que escrevemos. Na Listagem 9-1, onde escrevemos deliberadamente código que entraria em panic, a maneira de corrigir o panic é não solicitar um elemento além do intervalo dos índices do vetor. Quando seu código entrar em panic no futuro, você precisará descobrir qual ação o código está tomando com quais valores para causar o panic e o que o código deve fazer em vez disso.

Voltaremos a `panic!` e quando devemos e não devemos usar `panic!` para lidar com condições de erro em "To panic! or Not to panic!". Em seguida, veremos como se recuperar de um erro usando `Result`.
