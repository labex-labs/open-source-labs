# Representação Interna

Uma `String` é um wrapper sobre um `Vec<u8>`. Vamos analisar algumas de nossas strings de exemplo UTF-8 devidamente codificadas da Listagem 8-14. Primeiro, esta:

```rust
let hello = String::from("Hola");
```

Neste caso, `len` será `4`, o que significa que o vetor que armazena a string `"Hola"` tem 4 bytes de comprimento. Cada uma dessas letras ocupa um byte quando codificada em UTF-8. A seguinte linha, no entanto, pode surpreendê-lo (observe que esta string começa com a letra cirílica maiúscula _Ze_, não com o número arábico 3):

```rust
let hello = String::from("Здравствуйте");
```

Se lhe perguntassem qual o comprimento da string, você poderia dizer 12. Na verdade, a resposta do Rust é 24: esse é o número de bytes necessários para codificar "Здравствуйте" em UTF-8, porque cada valor escalar Unicode nessa string ocupa 2 bytes de armazenamento. Portanto, um índice nos bytes da string nem sempre se correlacionará com um valor escalar Unicode válido. Para demonstrar, considere este código Rust inválido:

```rust
let hello = "Здравствуйте";
let answer = &hello[0];
```

Você já sabe que `answer` não será `З`, a primeira letra. Quando codificado em UTF-8, o primeiro byte de `З` é `208` e o segundo é `151`, então pareceria que `answer` deveria, na verdade, ser `208`, mas `208` não é um caractere válido por si só. Retornar `208` provavelmente não é o que um usuário gostaria se pedisse a primeira letra desta string; no entanto, esses são os únicos dados que o Rust tem no índice de byte 0. Os usuários geralmente não querem o valor do byte retornado, mesmo que a string contenha apenas letras latinas: se `&"hello"[0]` fosse um código válido que retornasse o valor do byte, ele retornaria `104`, não `h`.

A resposta, então, é que, para evitar retornar um valor inesperado e causar bugs que podem não ser descobertos imediatamente, o Rust não compila este código e impede mal-entendidos no início do processo de desenvolvimento.
