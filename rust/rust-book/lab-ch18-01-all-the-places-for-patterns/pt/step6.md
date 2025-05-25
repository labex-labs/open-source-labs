# Declarações `let`

Antes deste capítulo, discutimos explicitamente o uso de padrões com `match` e `if let`, mas, na verdade, usamos padrões em outros lugares também, incluindo em declarações `let`. Por exemplo, considere esta atribuição de variável direta com `let`:

```rust
let x = 5;
```

Toda vez que você usou uma declaração `let` como esta, você esteve usando padrões, embora possa não ter percebido! Mais formalmente, uma declaração `let` se parece com isto:

```rust
let PATTERN = EXPRESSION;
```

Em declarações como `let x = 5;` com um nome de variável no slot PATTERN, o nome da variável é apenas uma forma particularmente simples de um padrão. Rust compara a expressão com o padrão e atribui quaisquer nomes que encontrar. Então, no exemplo `let x = 5;`, `x` é um padrão que significa "vincular o que corresponde aqui à variável `x`". Como o nome `x` é o padrão inteiro, este padrão efetivamente significa "vincular tudo à variável `x`, seja qual for o valor".

Para ver o aspecto de correspondência de padrões de `let` mais claramente, considere a Listagem 18-4, que usa um padrão com `let` para desestruturar uma tupla.

```rust
let (x, y, z) = (1, 2, 3);
```

Listagem 18-4: Usando um padrão para desestruturar uma tupla e criar três variáveis de uma vez

Aqui, correspondemos uma tupla a um padrão. Rust compara o valor `(1, 2, 3)` ao padrão `(x, y, z)` e vê que o valor corresponde ao padrão, pois vê que o número de elementos é o mesmo em ambos, então Rust vincula `1` a `x`, `2` a `y` e `3` a `z`. Você pode pensar neste padrão de tupla como aninhando três padrões de variáveis individuais dentro dele.

Se o número de elementos no padrão não corresponder ao número de elementos na tupla, o tipo geral não corresponderá e obteremos um erro do compilador. Por exemplo, a Listagem 18-5 mostra uma tentativa de desestruturar uma tupla com três elementos em duas variáveis, o que não funcionará.

```rust
let (x, y) = (1, 2, 3);
```

Listagem 18-5: Construindo incorretamente um padrão cujas variáveis não correspondem ao número de elementos na tupla

Tentar compilar este código resulta neste erro de tipo:

```bash
error[E0308]: mismatched types
 --> src/main.rs:2:9
  |
2 |     let (x, y) = (1, 2, 3);
  |         ^^^^^^   --------- this expression has type `({integer}, {integer},
{integer})`
  |         |
  |         expected a tuple with 3 elements, found one with 2 elements
  |
  = note: expected tuple `({integer}, {integer}, {integer})`
             found tuple `(_, _)`
```

Para corrigir o erro, poderíamos ignorar um ou mais dos valores na tupla usando `_` ou `..`, como você verá em "Ignorando Valores em um Padrão". Se o problema é que temos muitas variáveis no padrão, a solução é fazer com que os tipos correspondam removendo variáveis para que o número de variáveis seja igual ao número de elementos na tupla.
