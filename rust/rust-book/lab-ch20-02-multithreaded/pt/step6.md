# Construindo um ThreadPool Usando Desenvolvimento Orientado pelo Compilador

Faça as alterações na Listagem 20-12 em `src/main.rs` e, em seguida, vamos usar os erros do compilador de `cargo check` para orientar nosso desenvolvimento. Aqui está o primeiro erro que obtemos:

```bash
$ cargo check
    Checking hello v0.1.0 (file:///projects/hello)
error[E0433]: failed to resolve: use of undeclared type `ThreadPool`
  --> src/main.rs:11:16
   |
11 |     let pool = ThreadPool::new(4);
   |                ^^^^^^^^^^ use of undeclared type `ThreadPool`
```

Ótimo! Este erro nos diz que precisamos de um tipo ou módulo `ThreadPool`, então vamos construir um agora. Nossa implementação `ThreadPool` será independente do tipo de trabalho que nosso servidor web está fazendo. Então, vamos mudar o crate `hello` de um crate binário para um crate de biblioteca para conter nossa implementação `ThreadPool`. Depois de mudarmos para um crate de biblioteca, também poderíamos usar a biblioteca de pool de threads separada para qualquer trabalho que quisermos fazer usando um pool de threads, não apenas para servir requisições web.

Crie um arquivo `src/lib.rs` que contenha o seguinte, que é a definição mais simples de uma struct `ThreadPool` que podemos ter por enquanto:

Nome do arquivo: `src/lib.rs`

```rust
pub struct ThreadPool;
```

Em seguida, edite o arquivo `main.rs` para trazer `ThreadPool` para o escopo do crate da biblioteca, adicionando o seguinte código ao topo de `src/main.rs`:

Nome do arquivo: `src/main.rs`

```rust
use hello::ThreadPool;
```

Este código ainda não funcionará, mas vamos verificá-lo novamente para obter o próximo erro que precisamos abordar:

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

Este erro indica que, em seguida, precisamos criar uma função associada chamada `new` para `ThreadPool`. Também sabemos que `new` precisa ter um parâmetro que possa aceitar `4` como um argumento e deve retornar uma instância `ThreadPool`. Vamos implementar a função `new` mais simples que terá essas características:

Nome do arquivo: `src/lib.rs`

```rust
pub struct ThreadPool;

impl ThreadPool {
    pub fn new(size: usize) -> ThreadPool {
        ThreadPool
    }
}
```

Escolhemos `usize` como o tipo do parâmetro `size` porque sabemos que um número negativo de threads não faz sentido. Também sabemos que usaremos este `4` como o número de elementos em uma coleção de threads, que é para o que o tipo `usize` serve, como discutido em "Tipos Inteiros".

Vamos verificar o código novamente:

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

Agora o erro ocorre porque não temos um método `execute` em `ThreadPool`. Lembre-se de "Criando um Número Finito de Threads" que decidimos que nosso pool de threads deveria ter uma interface semelhante a `thread::spawn`. Além disso, implementaremos a função `execute` para que ela receba o closure que lhe é dado e o dê a uma thread ociosa no pool para executar.

Definiremos o método `execute` em `ThreadPool` para receber um closure como um parâmetro. Lembre-se de "Movendo Valores Capturados de Closures e os Traits Fn" que podemos receber closures como parâmetros com três traits diferentes: `Fn`, `FnMut` e `FnOnce`. Precisamos decidir qual tipo de closure usar aqui. Sabemos que acabaremos fazendo algo semelhante à implementação da biblioteca padrão `thread::spawn`, então podemos olhar para quais limites a assinatura de `thread::spawn` tem em seu parâmetro. A documentação nos mostra o seguinte:

```rust
pub fn spawn<F, T>(f: F) -> JoinHandle<T>
    where
        F: FnOnce() -> T,
        F: Send + 'static,
        T: Send + 'static,
```

O parâmetro de tipo `F` é aquele com o qual estamos preocupados aqui; o parâmetro de tipo `T` está relacionado ao valor de retorno, e não estamos preocupados com isso. Podemos ver que `spawn` usa `FnOnce` como o limite de trait em `F`. Isso é provavelmente o que queremos também, porque eventualmente passaremos o argumento que recebemos em `execute` para `spawn`. Podemos ter ainda mais confiança de que `FnOnce` é o trait que queremos usar porque a thread para executar uma requisição só executará o closure dessa requisição uma vez, o que corresponde ao `Once` em `FnOnce`.

O parâmetro de tipo `F` também tem o limite de trait `Send` e o limite de tempo de vida `'static`, que são úteis em nossa situação: precisamos de `Send` para transferir o closure de uma thread para outra e `'static` porque não sabemos quanto tempo a thread levará para executar. Vamos criar um método `execute` em `ThreadPool` que receberá um parâmetro genérico do tipo `F` com esses limites:

Nome do arquivo: `src/lib.rs`

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

Ainda usamos o `()` após `FnOnce` \[1] porque este `FnOnce` representa um closure que não recebe parâmetros e retorna o tipo unit `()`. Assim como as definições de função, o tipo de retorno pode ser omitido da assinatura, mas mesmo que não tenhamos parâmetros, ainda precisamos dos parênteses.

Novamente, esta é a implementação mais simples do método `execute`: ele não faz nada, mas estamos apenas tentando fazer nosso código compilar. Vamos verificá-lo novamente:

```bash
$ cargo check
    Checking hello v0.1.0 (file:///projects/hello)
    Finished dev [unoptimized + debuginfo] target(s) in 0.24s
```

Ele compila! Mas observe que, se você tentar `cargo run` e fizer uma requisição no navegador, verá os erros no navegador que vimos no início do capítulo. Nossa biblioteca ainda não está chamando o closure passado para `execute`!

> Nota: Um ditado que você pode ouvir sobre linguagens com compiladores rigorosos, como Haskell e Rust, é "se o código compila, ele funciona". Mas este ditado não é universalmente verdadeiro. Nosso projeto compila, mas não faz absolutamente nada! Se estivéssemos construindo um projeto real e completo, este seria um bom momento para começar a escrever testes unitários para verificar se o código compila _e_ tem o comportamento que queremos.
