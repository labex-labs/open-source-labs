# Tipos Inteiros

Um _inteiro_ é um número sem uma componente fracionária. Usamos um tipo inteiro no Capítulo 2, o tipo `u32`. Esta declaração de tipo indica que o valor associado a ele deve ser um inteiro sem sinal (tipos de inteiro com sinal começam com `i` em vez de `u`) que ocupa 32 bits de espaço. A Tabela 3-1 mostra os tipos inteiros embutidos em Rust. Podemos usar qualquer uma dessas variantes para declarar o tipo de um valor inteiro.

Tabela 3-1: Tipos Inteiros em Rust

| Comprimento | Com Sinal | Sem Sinal |
| ----------- | --------- | --------- |
| 8-bit       | `i8`      | `u8`      |
| 16-bit      | `i16`     | `u16`     |
| 32-bit      | `i32`     | `u32`     |
| 64-bit      | `i64`     | `u64`     |
| 128-bit     | `i128`    | `u128`    |
| arch        | `isize`   | `usize`   |

Cada variante pode ser com ou sem sinal e tem um tamanho explícito. _Com sinal_ e _sem sinal_ referem-se a se é possível que o número seja negativo - em outras palavras, se o número precisa ter um sinal com ele (com sinal) ou se ele será sempre positivo e, portanto, pode ser representado sem um sinal (sem sinal). É como escrever números no papel: quando o sinal importa, um número é mostrado com um sinal de mais ou um sinal de menos; no entanto, quando é seguro assumir que o número é positivo, ele é mostrado sem sinal. Números com sinal são armazenados usando a representação de complemento de dois.

Cada variante com sinal pode armazenar números de -(2^(n-1)) a 2^(n-1) - 1 inclusive, onde _n_ é o número de bits que essa variante usa. Então, um `i8` pode armazenar números de -(2^7) a 2^7 - 1, que é igual a -128 a 127. Variantes sem sinal podem armazenar números de 0 a 2^n - 1, então um `u8` pode armazenar números de 0 a 2^8 - 1, que é igual a 0 a 255.

Além disso, os tipos `isize` e `usize` dependem da arquitetura do computador em que seu programa está sendo executado, o que é denotado na tabela como "arch": 64 bits se você estiver em uma arquitetura de 64 bits e 32 bits se você estiver em uma arquitetura de 32 bits.

Você pode escrever literais inteiros em qualquer uma das formas mostradas na Tabela 3-2. Observe que literais numéricos que podem ser de vários tipos numéricos permitem um sufixo de tipo, como `57u8`, para designar o tipo. Literais numéricos também podem usar `_` como um separador visual para tornar o número mais fácil de ler, como `1_000`, que terá o mesmo valor que se você tivesse especificado `1000`.

Tabela 3-2: Literais Inteiros em Rust

| Literais numéricos | Exemplo       |
| ------------------ | ------------- |
| Decimal            | `98_222`      |
| Hexadecimal        | `0xff`        |
| Octal              | `0o77`        |
| Binário            | `0b1111_0000` |
| Byte (apenas `u8`) | `b'A'`        |

Então, como você sabe qual tipo de inteiro usar? Se você não tiver certeza, os padrões do Rust são geralmente bons lugares para começar: os tipos inteiros são, por padrão, `i32`. A principal situação em que você usaria `isize` ou `usize` é ao indexar algum tipo de coleção.

> **Overflow de Inteiro**
>
> Digamos que você tenha uma variável do tipo `u8` que pode conter valores entre 0 e 255. Se você tentar alterar a variável para um valor fora dessa faixa, como 256, ocorrerá _overflow de inteiro_, o que pode resultar em um de dois comportamentos. Quando você está compilando no modo de depuração, o Rust inclui verificações de overflow de inteiro que fazem com que seu programa _entre em pânico_ em tempo de execução se esse comportamento ocorrer. Rust usa o termo _panicking_ quando um programa sai com um erro; discutiremos pânicos com mais profundidade em "Erros Irrecuperáveis com panic!".
>
> Quando você está compilando no modo de lançamento com a flag `--release`, o Rust _não_ inclui verificações de overflow de inteiro que causam pânicos. Em vez disso, se ocorrer overflow, o Rust executa _two's complement wrapping_. Em resumo, valores maiores que o valor máximo que o tipo pode conter "envolvem" para o mínimo dos valores que o tipo pode conter. No caso de um `u8`, o valor 256 se torna 0, o valor 257 se torna 1 e assim por diante. O programa não entrará em pânico, mas a variável terá um valor que provavelmente não é o que você esperava que tivesse. Confiar no comportamento de wrapping do overflow de inteiro é considerado um erro.
>
> Para lidar explicitamente com a possibilidade de overflow, você pode usar estas famílias de métodos fornecidos pela biblioteca padrão para tipos numéricos primitivos:
>
> - Wrap em todos os modos com os métodos `wrapping_*`, como `wrapping_add`.
> - Retornar o valor `None` se houver overflow com os métodos `checked_*`.
> - Retornar o valor e um booleano indicando se houve overflow com os métodos `overflowing_*`.
> - Saturar nos valores mínimo ou máximo do valor com os métodos `saturating_*`.
