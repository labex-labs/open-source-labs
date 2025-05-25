# Ponteiros de Função

Falamos sobre como passar closures para funções; você também pode passar funções regulares para funções! Essa técnica é útil quando você deseja passar uma função que já definiu, em vez de definir uma nova closure. Funções convertem-se para o tipo `fn` (com um _f_ minúsculo), não deve ser confundido com o trait de closure `Fn`. O tipo `fn` é chamado de _ponteiro de função_. Passar funções com ponteiros de função permitirá que você use funções como argumentos para outras funções.

A sintaxe para especificar que um parâmetro é um ponteiro de função é semelhante à de closures, como mostrado na Listagem 19-27, onde definimos uma função `add_one` que adiciona 1 ao seu parâmetro. A função `do_twice` recebe dois parâmetros: um ponteiro de função para qualquer função que receba um parâmetro `i32` e retorne um `i32`, e um valor `i32`. A função `do_twice` chama a função `f` duas vezes, passando a ela o valor `arg`, e então soma os dois resultados da chamada da função. A função `main` chama `do_twice` com os argumentos `add_one` e `5`.

Nome do arquivo: `src/main.rs`

```rust
fn add_one(x: i32) -> i32 {
    x + 1
}

fn do_twice(f: fn(i32) -> i32, arg: i32) -> i32 {
    f(arg) + f(arg)
}

fn main() {
    let answer = do_twice(add_one, 5);

    println!("The answer is: {answer}");
}
```

Listagem 19-27: Usando o tipo `fn` para aceitar um ponteiro de função como um argumento

Este código imprime `The answer is: 12`. Especificamos que o parâmetro `f` em `do_twice` é um `fn` que recebe um parâmetro do tipo `i32` e retorna um `i32`. Podemos então chamar `f` no corpo de `do_twice`. Em `main`, podemos passar o nome da função `add_one` como o primeiro argumento para `do_twice`.

Ao contrário de closures, `fn` é um tipo em vez de um trait, então especificamos `fn` como o tipo de parâmetro diretamente, em vez de declarar um parâmetro de tipo genérico com um dos traits `Fn` como uma restrição de trait.

Ponteiros de função implementam todos os três traits de closure (`Fn`, `FnMut` e `FnOnce`), o que significa que você sempre pode passar um ponteiro de função como um argumento para uma função que espera uma closure. É melhor escrever funções usando um tipo genérico e um dos traits de closure para que suas funções possam aceitar funções ou closures.

Dito isso, um exemplo de onde você gostaria de aceitar apenas `fn` e não closures é ao interagir com código externo que não possui closures: funções C podem aceitar funções como argumentos, mas C não possui closures.

Como um exemplo de onde você pode usar uma closure definida inline ou uma função nomeada, vamos analisar o uso do método `map` fornecido pelo trait `Iterator` na biblioteca padrão. Para usar a função `map` para transformar um vetor de números em um vetor de strings, podemos usar uma closure, assim:

```rust
let list_of_numbers = vec![1, 2, 3];
let list_of_strings: Vec<String> = list_of_numbers
    .iter()
    .map(|i| i.to_string())
    .collect();
```

Ou poderíamos nomear uma função como o argumento para `map` em vez da closure, assim:

```rust
let list_of_numbers = vec![1, 2, 3];
let list_of_strings: Vec<String> = list_of_numbers
    .iter()
    .map(ToString::to_string)
    .collect();
```

Observe que devemos usar a sintaxe totalmente qualificada de que falamos em "Traits Avançados" porque existem várias funções disponíveis chamadas `to_string`.

Aqui, estamos usando a função `to_string` definida no trait `ToString`, que a biblioteca padrão implementou para qualquer tipo que implemente `Display`.

Lembre-se de "Valores de Enum" que o nome de cada variante de enum que definimos também se torna uma função inicializadora. Podemos usar essas funções inicializadoras como ponteiros de função que implementam os traits de closure, o que significa que podemos especificar as funções inicializadoras como argumentos para métodos que recebem closures, assim:

```rust
enum Status {
    Value(u32),
    Stop,
}

let list_of_statuses: Vec<Status> = (0u32..20)
    .map(Status::Value)
    .collect();
```

Aqui, criamos instâncias `Status::Value` usando cada valor `u32` no intervalo em que `map` é chamado, usando a função inicializadora de `Status::Value`. Algumas pessoas preferem este estilo e algumas pessoas preferem usar closures. Eles compilam para o mesmo código, então use o estilo que for mais claro para você.
