# Bytes, Valores Escalares e Clusters de Grafemas! Oh, Meu Deus!

Outro ponto sobre UTF-8 é que existem, na verdade, três maneiras relevantes de analisar strings da perspectiva do Rust: como bytes, valores escalares e clusters de grafemas (a coisa mais próxima do que chamaríamos de _letras_).

Se olharmos para a palavra hindi "नमस्ते" escrita no script Devanagari, ela é armazenada como um vetor de valores `u8` que se parece com isto:

```rust
[224, 164, 168, 224, 164, 174, 224, 164, 184, 224, 165, 141, 224,
164, 164, 224, 165, 135]
```

Isso são 18 bytes e é como os computadores, em última análise, armazenam esses dados. Se os olharmos como valores escalares Unicode, que são o que o tipo `char` do Rust é, esses bytes se parecem com isto:

```rust
['न', 'म', 'स', '्', 'त', 'े']
```

Existem seis valores `char` aqui, mas o quarto e o sexto não são letras: são diacríticos que não fazem sentido por conta própria. Finalmente, se os olharmos como clusters de grafemas, obteríamos o que uma pessoa chamaria de as quatro letras que compõem a palavra hindi:

```rust
["न", "म", "स्", "ते"]
```

O Rust fornece diferentes maneiras de interpretar os dados brutos da string que os computadores armazenam, para que cada programa possa escolher a interpretação que precisa, independentemente da linguagem humana em que os dados estão.

Uma razão final pela qual o Rust não nos permite indexar em uma `String` para obter um caractere é que as operações de indexação devem sempre levar tempo constante (O(1)). Mas não é possível garantir esse desempenho com uma `String`, porque o Rust teria que percorrer o conteúdo desde o início até o índice para determinar quantos caracteres válidos existiam.
