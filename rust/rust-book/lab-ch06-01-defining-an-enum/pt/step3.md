# O Enum Option e Suas Vantagens Sobre Valores Nulos

Esta seção explora um estudo de caso de `Option`, que é outro enum definido pela biblioteca padrão. O tipo `Option` codifica o cenário muito comum em que um valor pode ser algo ou pode ser nada.

Por exemplo, se você solicitar o primeiro item em uma lista contendo vários itens, você obterá um valor. Se você solicitar o primeiro item em uma lista vazia, você não obterá nada. Expressar esse conceito em termos do sistema de tipos significa que o compilador pode verificar se você tratou todos os casos que deveria estar tratando; essa funcionalidade pode evitar bugs que são extremamente comuns em outras linguagens de programação.

O design da linguagem de programação é frequentemente pensado em termos de quais recursos você inclui, mas os recursos que você exclui também são importantes. O Rust não tem o recurso nulo que muitas outras linguagens têm. _Nulo_ é um valor que significa que não há valor lá. Em linguagens com nulo, as variáveis podem sempre estar em um de dois estados: nulo ou não-nulo.

Em sua apresentação de 2009 "Null References: The Billion Dollar Mistake", Tony Hoare, o inventor do nulo, tem a dizer:

> Eu chamo isso de meu erro de um bilhão de dólares. Naquela época, eu estava projetando o primeiro sistema de tipos abrangente para referências em uma linguagem orientada a objetos. Meu objetivo era garantir que todo o uso de referências fosse absolutamente seguro, com a verificação realizada automaticamente pelo compilador. Mas eu não consegui resistir à tentação de colocar uma referência nula, simplesmente porque era tão fácil de implementar. Isso levou a inúmeros erros, vulnerabilidades e falhas no sistema, que provavelmente causaram um bilhão de dólares em dor e danos nos últimos quarenta anos. O problema com valores nulos é que, se você tentar usar um valor nulo como um valor não-nulo, você obterá um erro de algum tipo. Como essa propriedade nula ou não-nula é generalizada, é extremamente fácil cometer esse tipo de erro.

No entanto, o conceito que nulo está tentando expressar ainda é útil: um nulo é um valor que está atualmente inválido ou ausente por algum motivo.

O problema não é realmente com o conceito, mas com a implementação específica. Como tal, o Rust não tem nulos, mas tem um enum que pode codificar o conceito de um valor presente ou ausente. Este enum é `Option<T>`, e é definido pela biblioteca padrão da seguinte forma:

```rust
enum Option<T> {
    None,
    Some(T),
}
```

O enum `Option<T>` é tão útil que está até incluído no prelúdio; você não precisa trazê-lo para o escopo explicitamente. Suas variantes também estão incluídas no prelúdio: você pode usar `Some` e `None` diretamente sem o prefixo `Option::`. O enum `Option<T>` ainda é apenas um enum regular, e `Some(T)` e `None` ainda são variantes do tipo `Option<T>`.

A sintaxe `<T>` é um recurso do Rust sobre o qual ainda não falamos. É um parâmetro de tipo genérico, e cobriremos genéricos com mais detalhes no Capítulo 10. Por enquanto, tudo o que você precisa saber é que `<T>` significa que a variante `Some` do enum `Option` pode conter um pedaço de dados de qualquer tipo, e que cada tipo concreto que é usado no lugar de `T` torna o tipo geral `Option<T>` um tipo diferente. Aqui estão alguns exemplos de como usar valores `Option` para conter tipos numéricos e tipos de string:

```rust
let some_number = Some(5);
let some_char = Some('e');

let absent_number: Option<i32> = None;
```

O tipo de `some_number` é `Option<i32>`. O tipo de `some_char` é `Option<char>`, que é um tipo diferente. O Rust pode inferir esses tipos porque especificamos um valor dentro da variante `Some`. Para `absent_number`, o Rust exige que anotemos o tipo `Option` geral: o compilador não pode inferir o tipo que a variante `Some` correspondente conterá apenas olhando para um valor `None`. Aqui, dizemos ao Rust que queremos que `absent_number` seja do tipo `Option<i32>`.

Quando temos um valor `Some`, sabemos que um valor está presente e o valor é mantido dentro do `Some`. Quando temos um valor `None`, em certo sentido, isso significa a mesma coisa que nulo: não temos um valor válido. Então, por que ter `Option<T>` é melhor do que ter nulo?

Em suma, porque `Option<T>` e `T` (onde `T` pode ser qualquer tipo) são tipos diferentes, o compilador não nos permitirá usar um valor `Option<T>` como se fosse definitivamente um valor válido. Por exemplo, este código não compilará, porque está tentando adicionar um `i8` a um `Option<i8>`:

```rust
let x: i8 = 5;
let y: Option<i8> = Some(5);

let sum = x + y;
```

Se executarmos este código, obteremos uma mensagem de erro como esta:

```bash
error[E0277]: cannot add `Option<i8>` to `i8`
 --> src/main.rs:5:17
  |
5 |     let sum = x + y;
  |                 ^ no implementation for `i8 + Option<i8>`
  |
  = help: the trait `Add<Option<i8>>` is not implemented for `i8`
```

Intenso! Na verdade, esta mensagem de erro significa que o Rust não entende como adicionar um `i8` e um `Option<i8>`, porque eles são tipos diferentes. Quando temos um valor de um tipo como `i8` em Rust, o compilador garantirá que sempre teremos um valor válido. Podemos prosseguir com confiança sem ter que verificar se há nulo antes de usar esse valor. Somente quando temos um `Option<i8>` (ou qualquer tipo de valor com o qual estamos trabalhando) é que precisamos nos preocupar em possivelmente não ter um valor, e o compilador garantirá que tratemos esse caso antes de usar o valor.

Em outras palavras, você deve converter um `Option<T>` em um `T` antes de poder realizar operações `T` com ele. Geralmente, isso ajuda a detectar um dos problemas mais comuns com nulo: presumir que algo não é nulo quando na verdade é.

Eliminar o risco de presumir incorretamente um valor não-nulo ajuda você a ter mais confiança em seu código. Para ter um valor que possivelmente pode ser nulo, você deve optar explicitamente por fazer o tipo desse valor `Option<T>`. Então, quando você usa esse valor, você é obrigado a lidar explicitamente com o caso em que o valor é nulo. Em todos os lugares que um valor tem um tipo que não é um `Option<T>`, você _pode_ com segurança presumir que o valor não é nulo. Esta foi uma decisão de design deliberada para o Rust limitar a onipresença do nulo e aumentar a segurança do código Rust.

Então, como você obtém o valor `T` de uma variante `Some` quando você tem um valor do tipo `Option<T>` para que possa usar esse valor? O enum `Option<T>` tem um grande número de métodos que são úteis em uma variedade de situações; você pode conferi-los em sua documentação. Familiarizar-se com os métodos em `Option<T>` será extremamente útil em sua jornada com Rust.

Em geral, para usar um valor `Option<T>`, você deseja ter um código que lide com cada variante. Você deseja algum código que seja executado somente quando você tiver um valor `Some(T)`, e esse código pode usar o `T` interno. Você deseja que algum outro código seja executado somente se você tiver um valor `None`, e esse código não tem um valor `T` disponível. A expressão `match` é uma construção de fluxo de controle que faz exatamente isso quando usada com enums: ela executará um código diferente dependendo de qual variante do enum ela tem, e esse código pode usar os dados dentro do valor correspondente.
