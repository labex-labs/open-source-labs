# Comparando o Palpite com o Número Secreto

Agora que temos a entrada do usuário e um número aleatório, podemos compará-los. Essa etapa é mostrada na Listagem 2-4. Observe que este código não compilará ainda, como explicaremos.

Nome do arquivo: `src/main.rs`

```rust
use rand::Rng;
1 use std::cmp::Ordering;
use std::io;

fn main() {
    --snip--

    println!("You guessed: {guess}");

  2 match guess.3 cmp(&secret_number) {
        Ordering::Less => println!("Too small!"),
        Ordering::Greater => println!("Too big!"),
        Ordering::Equal => println!("You win!"),
    }
}
```

Listagem 2-4: Lidando com os possíveis valores de retorno da comparação de dois números

Primeiro, adicionamos outra declaração `use` \[1], trazendo um tipo chamado `std::cmp::Ordering` para o escopo da biblioteca padrão. O tipo `Ordering` é outro enum e tem as variantes `Less`, `Greater` e `Equal`. Esses são os três resultados possíveis quando você compara dois valores.

Em seguida, adicionamos cinco novas linhas na parte inferior que usam o tipo `Ordering`. O método `cmp` \[3] compara dois valores e pode ser chamado em qualquer coisa que possa ser comparada. Ele recebe uma referência ao que você deseja comparar: aqui, ele está comparando `guess` com `secret_number`. Em seguida, ele retorna uma variante do enum `Ordering` que trouxemos para o escopo com a declaração `use`. Usamos uma expressão `match` \[2] para decidir o que fazer a seguir com base em qual variante de `Ordering` foi retornada da chamada para `cmp` com os valores em `guess` e `secret_number`.

Uma expressão `match` é composta por _braços_ (arms). Um braço consiste em um _padrão_ (pattern) para corresponder e o código que deve ser executado se o valor fornecido ao `match` corresponder ao padrão desse braço. Rust pega o valor fornecido ao `match` e percorre o padrão de cada braço por sua vez. Padrões e a construção `match` são recursos poderosos do Rust: eles permitem que você expresse uma variedade de situações que seu código pode encontrar e garantem que você as trate todas. Esses recursos serão abordados em detalhes no Capítulo 6 e no Capítulo 18, respectivamente.

Vamos analisar um exemplo com a expressão `match` que usamos aqui. Digamos que o usuário tenha adivinhado 50 e o número secreto gerado aleatoriamente desta vez seja 38.

Quando o código compara 50 a 38, o método `cmp` retornará `Ordering::Greater` porque 50 é maior que 38. A expressão `match` recebe o valor `Ordering::Greater` e começa a verificar o padrão de cada braço. Ele olha para o padrão do primeiro braço, `Ordering::Less`, e vê que o valor `Ordering::Greater` não corresponde a `Ordering::Less`, então ele ignora o código nesse braço e passa para o próximo braço. O padrão do próximo braço é `Ordering::Greater`, que _corresponde_ a `Ordering::Greater`! O código associado nesse braço será executado e imprimirá `Too big!` na tela. A expressão `match` termina após a primeira correspondência bem-sucedida, portanto, não analisará o último braço nesse cenário.

No entanto, o código na Listagem 2-4 não compilará ainda. Vamos tentar:

```bash
$ cargo build
   Compiling guessing_game v0.1.0 (file:///projects/guessing_game)
error[E0308]: mismatched types
  --> src/main.rs:22:21
   |
22 |     match guess.cmp(&secret_number) {
   |                     ^^^^^^^^^^^^^^ expected struct `String`, found integer
   |
   = note: expected reference `&String`
              found reference `&{integer}`
```

O cerne do erro afirma que há _tipos incompatíveis_. Rust tem um sistema de tipos forte e estático. No entanto, ele também tem inferência de tipo. Quando escrevemos `let mut guess = String::new()`, Rust foi capaz de inferir que `guess` deveria ser um `String` e não nos fez escrever o tipo. O `secret_number`, por outro lado, é um tipo numérico. Alguns dos tipos numéricos do Rust podem ter um valor entre 1 e 100: `i32`, um número de 32 bits; `u32`, um número sem sinal de 32 bits; `i64`, um número de 64 bits; bem como outros. A menos que especificado de outra forma, Rust assume `i32`, que é o tipo de `secret_number`, a menos que você adicione informações de tipo em outro lugar que fariam com que Rust inferisse um tipo numérico diferente. A razão do erro é que Rust não pode comparar uma string e um tipo numérico.

Em última análise, queremos converter o `String` que o programa lê como entrada em um tipo numérico real para que possamos compará-lo numericamente com o número secreto. Fazemos isso adicionando esta linha ao corpo da função `main`:

Nome do arquivo: `src/main.rs`

```rust
use std::io;
use rand::Rng;
use std::cmp::Ordering;

fn main() {
    println!("Guess the number!");

    let secret_number = rand::thread_rng().gen_range(1..=100);

    println!("The secret number is: {secret_number}");

    println!("Please input your guess.");

    let mut guess = String::new();

    io::stdin()
        .read_line(&mut guess)
        .expect("Failed to read line");

    let guess: u32 = guess
        .trim()
        .parse()
        .expect("Please type a number!");

    println!("You guessed: {guess}");

    match guess.cmp(&secret_number) {
        Ordering::Less => println!("Too small!"),
        Ordering::Greater => println!("Too big!"),
        Ordering::Equal => println!("You win!"),
    }
}
```

Criamos uma variável chamada `guess`. Mas espere, o programa já não tem uma variável chamada `guess`? Tem, mas, felizmente, Rust nos permite sombrear o valor anterior de `guess` com um novo. _Shadowing_ (sombreamento) nos permite reutilizar o nome da variável `guess` em vez de nos forçar a criar duas variáveis exclusivas, como `guess_str` e `guess`, por exemplo. Abordaremos isso com mais detalhes no Capítulo 3, mas, por enquanto, saiba que esse recurso é frequentemente usado quando você deseja converter um valor de um tipo para outro tipo.

Vinculamos essa nova variável à expressão `guess.trim().parse()`. O `guess` na expressão se refere à variável `guess` original que continha a entrada como uma string. O método `trim` em uma instância `String` eliminará qualquer espaço em branco no início e no final, o que devemos fazer para poder comparar a string com o `u32`, que só pode conter dados numéricos. O usuário deve pressionar Enter para satisfazer `read_line` e inserir seu palpite, o que adiciona um caractere de nova linha à string. Por exemplo, se o usuário digitar `5` e pressionar Enter, `guess` ficará assim: `5\n`. O `\n` representa "nova linha". (No Windows, pressionar Enter resulta em um retorno de carro e uma nova linha, `\r\n`.) O método `trim` elimina `\n` ou `\r\n`, resultando em apenas `5`.

O método `parse` em strings converte uma string em outro tipo. Aqui, usamos para converter de uma string para um número. Precisamos dizer ao Rust o tipo de número exato que queremos usando `let guess: u32`. Os dois pontos (`:`) após `guess` dizem ao Rust que vamos anotar o tipo da variável. Rust tem alguns tipos numéricos embutidos; o `u32` visto aqui é um inteiro sem sinal de 32 bits. É uma boa escolha padrão para um pequeno número positivo. Você aprenderá sobre outros tipos numéricos no Capítulo 3.

Além disso, a anotação `u32` neste programa de exemplo e a comparação com `secret_number` significam que Rust inferirá que `secret_number` também deve ser um `u32`. Então, agora a comparação será entre dois valores do mesmo tipo!

O método `parse` só funcionará em caracteres que podem ser logicamente convertidos em números e, portanto, pode facilmente causar erros. Se, por exemplo, a string contivesse `A`👍`%`, não haveria como converter isso em um número. Como pode falhar, o método `parse` retorna um tipo `Result`, assim como o método `read_line` (discutido anteriormente em "Lidando com uma possível falha com Result"). Trataremos este `Result` da mesma forma, usando o método `expect` novamente. Se `parse` retornar um `Err` `Result` variante porque não conseguiu criar um número a partir da string, a chamada `expect` travará o jogo e imprimirá a mensagem que lhe damos. Se `parse` puder converter com sucesso a string em um número, ele retornará a variante `Ok` de `Result`, e `expect` retornará o número que queremos do valor `Ok`.

Vamos executar o programa agora:

```bash
$ cargo run
   Compiling guessing_game v0.1.0 (file:///projects/guessing_game)
    Finished dev [unoptimized + debuginfo] target(s) in 0.43s
     Running `target/debug/guessing_game`
Guess the number!
The secret number is: 58
Please input your guess.
  76
You guessed: 76
Too big!
```

Legal! Mesmo que espaços tenham sido adicionados antes do palpite, o programa ainda descobriu que o usuário adivinhou 76. Execute o programa algumas vezes para verificar o comportamento diferente com diferentes tipos de entrada: adivinhe o número corretamente, adivinhe um número muito alto e adivinhe um número muito baixo.

Temos a maior parte do jogo funcionando agora, mas o usuário pode fazer apenas um palpite. Vamos mudar isso adicionando um loop!
