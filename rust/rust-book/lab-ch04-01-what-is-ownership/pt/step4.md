# O Tipo String

Para ilustrar as regras de _ownership_, precisamos de um tipo de dado que seja mais complexo do que aqueles que cobrimos em "Tipos de Dados". Os tipos cobertos anteriormente são de um tamanho conhecido, podem ser armazenados na _stack_ (pilha) e removidos da _stack_ quando seu escopo termina, e podem ser rápida e trivialmente copiados para criar uma nova instância independente se outra parte do código precisar usar o mesmo valor em um escopo diferente. Mas queremos analisar dados que são armazenados na _heap_ (área de memória dinâmica) e explorar como o Rust sabe quando limpar esses dados, e o tipo `String` é um ótimo exemplo.

Vamos nos concentrar nas partes de `String` que se relacionam com _ownership_. Esses aspectos também se aplicam a outros tipos de dados complexos, sejam eles fornecidos pela biblioteca padrão ou criados por você. Discutiremos `String` com mais profundidade no Capítulo 8.

Já vimos literais de _string_, onde um valor de _string_ é codificado em nosso programa. Literais de _string_ são convenientes, mas não são adequados para todas as situações em que podemos querer usar texto. Uma razão é que eles são imutáveis. Outra é que nem todo valor de _string_ pode ser conhecido quando escrevemos nosso código: por exemplo, e se quisermos obter a entrada do usuário e armazená-la? Para essas situações, o Rust tem um segundo tipo de _string_, `String`. Este tipo gerencia dados alocados na _heap_ e, como tal, é capaz de armazenar uma quantidade de texto que é desconhecida para nós no tempo de compilação. Você pode criar um `String` a partir de um literal de _string_ usando a função `from`, assim:

```rust
let s = String::from("hello");
```

O operador de dois pontos `::` nos permite _namespace_ (definir um espaço de nomes) esta função `from` específica sob o tipo `String`, em vez de usar algum tipo de nome como `string_from`. Discutiremos essa sintaxe mais em "Sintaxe de Métodos" e quando falarmos sobre _namespacing_ com módulos em "Caminhos para Referenciar um Item na Árvore de Módulos".

Este tipo de _string_ _pode_ ser mutado:

```rust
let mut s = String::from("hello");

s.push_str(", world!"); // push_str() adiciona um literal a um String

println!("{s}"); // Isso imprimirá `hello, world!`
```

Então, qual é a diferença aqui? Por que `String` pode ser mutado, mas os literais não podem? A diferença está em como esses dois tipos lidam com a memória.
