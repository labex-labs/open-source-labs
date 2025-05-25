# _String Slices_

Um _string slice_ é uma referência a parte de uma `String`, e se parece com isto:

```rust
let s = String::from("hello world");

let hello = &s[0..5];
let world = &s[6..11];
```

Em vez de uma referência à `String` inteira, `hello` é uma referência a uma porção da `String`, especificada no bit extra `[0..5]`. Criamos _slices_ usando um intervalo dentro de colchetes, especificando `[índice_inicial..índice_final]`, onde `índice_inicial` é a primeira posição no _slice_ e `índice_final` é um a mais que a última posição no _slice_. Internamente, a estrutura de dados do _slice_ armazena a posição inicial e o comprimento do _slice_, que corresponde a `índice_final` menos `índice_inicial`. Portanto, no caso de `let world = &s[6..11];`, `world` seria um _slice_ que contém um ponteiro para o byte no índice 6 de `s` com um valor de comprimento de `5`.

A Figura 4-6 mostra isso em um diagrama.

Figura 4-6: _String slice_ referenciando parte de uma `String`

Com a sintaxe de intervalo `..` do Rust, se você quiser começar no índice 0, pode remover o valor antes dos dois pontos. Em outras palavras, estes são iguais:

```rust
let s = String::from("hello");

let slice = &s[0..2];
let slice = &s[..2];
```

Da mesma forma, se seu _slice_ incluir o último byte da `String`, você pode remover o número final. Isso significa que estes são iguais:

```rust
let s = String::from("hello");

let len = s.len();

let slice = &s[3..len];
let slice = &s[3..];
```

Você também pode remover ambos os valores para obter um _slice_ da string inteira. Então, estes são iguais:

```rust
let s = String::from("hello");

let len = s.len();

let slice = &s[0..len];
let slice = &s[..];
```

> Nota: Os índices de intervalo de _string slice_ devem ocorrer em limites de caracteres UTF-8 válidos. Se você tentar criar um _string slice_ no meio de um caractere multibyte, seu programa sairá com um erro. Para fins de introdução de _string slices_, estamos assumindo apenas ASCII nesta seção; uma discussão mais completa sobre o tratamento de UTF-8 está em "Armazenando Texto Codificado em UTF-8 com Strings".

Com todas essas informações em mente, vamos reescrever `first_word` para retornar um _slice_. O tipo que significa "string slice" é escrito como `&str`:

Nome do arquivo: `src/main.rs`

```rust
fn first_word(s: &String) -> &str {
    let bytes = s.as_bytes();

    for (i, &item) in bytes.iter().enumerate() {
        if item == b' ' {
            return &s[0..i];
        }
    }

    &s[..]
}
```

Obtemos o índice para o final da palavra da mesma forma que fizemos na Listagem 4-7, procurando a primeira ocorrência de um espaço. Quando encontramos um espaço, retornamos um _string slice_ usando o início da string e o índice do espaço como os índices inicial e final.

Agora, quando chamamos `first_word`, recebemos um único valor que está vinculado aos dados subjacentes. O valor é composto por uma referência ao ponto de partida do _slice_ e o número de elementos no _slice_.

Retornar um _slice_ também funcionaria para uma função `second_word`:

```rust
fn second_word(s: &String) -> &str {
```

Agora temos uma API direta que é muito mais difícil de bagunçar porque o compilador garantirá que as referências na `String` permaneçam válidas. Lembre-se do bug no programa na Listagem 4-8, quando obtivemos o índice para o final da primeira palavra, mas depois limpamos a string para que nosso índice fosse inválido? Esse código era logicamente incorreto, mas não mostrava nenhum erro imediato. Os problemas apareceriam mais tarde se continuássemos tentando usar o índice da primeira palavra com uma string vazia. _Slices_ tornam esse bug impossível e nos permitem saber que temos um problema com nosso código muito mais cedo. Usar a versão _slice_ de `first_word` lançará um erro de tempo de compilação:

Nome do arquivo: `src/main.rs`

```rust
fn main() {
    let mut s = String::from("hello world");

    let word = first_word(&s);

    s.clear(); // error!

    println!("the first word is: {word}");
}
```

Aqui está o erro do compilador:

```bash
error[E0502]: cannot borrow `s` as mutable because it is also borrowed as
immutable
  --> src/main.rs:18:5
   |
16 |     let word = first_word(&s);
   |                           -- immutable borrow occurs here
17 |
18 |     s.clear(); // error!
   |     ^^^^^^^^^ mutable borrow occurs here
19 |
20 |     println!("the first word is: {word}");
   |                                   ---- immutable borrow later used here
```

Lembre-se das regras de _borrowing_ (empréstimo) que, se tivermos uma referência imutável a algo, também não podemos ter uma referência mutável. Como `clear` precisa truncar a `String`, ele precisa obter uma referência mutável. O `println!` após a chamada para `clear` usa a referência em `word`, então a referência imutável ainda deve estar ativa nesse ponto. Rust proíbe a referência mutável em `clear` e a referência imutável em `word` de existirem ao mesmo tempo, e a compilação falha. Rust não apenas tornou nossa API mais fácil de usar, mas também eliminou toda uma classe de erros em tempo de compilação!
