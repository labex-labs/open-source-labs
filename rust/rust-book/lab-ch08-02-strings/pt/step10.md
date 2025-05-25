# Fatiando Strings (Slicing Strings)

Indexar em uma string é frequentemente uma má ideia porque não está claro qual deve ser o tipo de retorno da operação de indexação da string: um valor de byte, um caractere, um cluster de grafemas ou uma fatia de string (string slice). Se você realmente precisar usar índices para criar fatias de string, o Rust pede que você seja mais específico.

Em vez de indexar usando `[]` com um único número, você pode usar `[]` com um intervalo para criar uma fatia de string contendo bytes específicos:

```rust
let hello = "Здравствуйте";

let s = &hello[0..4];
```

Aqui, `s` será um `&str` que contém os primeiros quatro bytes da string. Anteriormente, mencionamos que cada um desses caracteres tinha dois bytes, o que significa que `s` será `Зд`.

Se tentássemos fatiar apenas parte dos bytes de um caractere com algo como `&hello[0..1]`, o Rust entraria em pânico em tempo de execução da mesma forma que se um índice inválido fosse acessado em um vetor:

```rust
thread 'main' panicked at 'byte index 1 is not a char boundary;
it is inside 'З' (bytes 0..2) of `Здравствуйте`', src/main.rs:4:14
```

Você deve ter cautela ao criar fatias de string com intervalos, porque fazê-lo pode travar seu programa.
