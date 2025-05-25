# Tipos Associados

_Tipos associados_ conectam um espaço reservado de tipo com uma trait (característica) de forma que as definições de método da trait possam usar esses tipos de espaço reservado em suas assinaturas. O implementador de uma trait especificará o tipo concreto a ser usado em vez do tipo de espaço reservado para a implementação específica. Dessa forma, podemos definir uma trait que usa alguns tipos sem precisar saber exatamente quais são esses tipos até que a trait seja implementada.

Descrevemos a maioria dos recursos avançados neste capítulo como raramente necessários. Tipos associados estão em algum lugar no meio: eles são usados com mais raridade do que os recursos explicados no restante do livro, mas mais comumente do que muitos dos outros recursos discutidos neste capítulo.

Um exemplo de uma trait com um tipo associado é a trait `Iterator` que a biblioteca padrão fornece. O tipo associado é chamado `Item` e representa o tipo dos valores sobre os quais o tipo que implementa a trait `Iterator` está iterando. A definição da trait `Iterator` é mostrada na Listagem 19-12.

```rust
pub trait Iterator {
    type Item;

    fn next(&mut self) -> Option<Self::Item>;
}
```

Listagem 19-12: A definição da trait `Iterator` que possui um tipo associado `Item`

O tipo `Item` é um espaço reservado, e a definição do método `next` mostra que ele retornará valores do tipo `Option<Self::Item>`. Os implementadores da trait `Iterator` especificarão o tipo concreto para `Item`, e o método `next` retornará um `Option` contendo um valor desse tipo concreto.

Tipos associados podem parecer um conceito semelhante a genéricos, na medida em que estes últimos nos permitem definir uma função sem especificar quais tipos ela pode manipular. Para examinar a diferença entre os dois conceitos, vamos analisar uma implementação da trait `Iterator` em um tipo chamado `Counter` que especifica que o tipo `Item` é `u32`:

Nome do arquivo: `src/lib.rs`

```rust
impl Iterator for Counter {
    type Item = u32;

    fn next(&mut self) -> Option<Self::Item> {
        --snip--
```

Esta sintaxe parece comparável à de genéricos. Então, por que não definir a trait `Iterator` com genéricos, como mostrado na Listagem 19-13?

```rust
pub trait Iterator<T> {
    fn next(&mut self) -> Option<T>;
}
```

Listagem 19-13: Uma definição hipotética da trait `Iterator` usando genéricos

A diferença é que, ao usar genéricos, como na Listagem 19-13, devemos anotar os tipos em cada implementação; porque também podemos implementar `Iterator<``String``> for Counter` ou qualquer outro tipo, poderíamos ter múltiplas implementações de `Iterator` para `Counter`. Em outras palavras, quando uma trait tem um parâmetro genérico, ela pode ser implementada para um tipo várias vezes, alterando os tipos concretos dos parâmetros de tipo genérico a cada vez. Quando usamos o método `next` em `Counter`, teríamos que fornecer anotações de tipo para indicar qual implementação de `Iterator` queremos usar.

Com tipos associados, não precisamos anotar tipos porque não podemos implementar uma trait em um tipo várias vezes. Na Listagem 19-12 com a definição que usa tipos associados, podemos escolher qual será o tipo de `Item` apenas uma vez porque pode haver apenas um `impl Iterator for Counter`. Não precisamos especificar que queremos um iterador de valores `u32` em todos os lugares que chamamos `next` em `Counter`.

Tipos associados também se tornam parte do contrato da trait: os implementadores da trait devem fornecer um tipo para representar o espaço reservado do tipo associado. Tipos associados geralmente têm um nome que descreve como o tipo será usado, e documentar o tipo associado na documentação da API é uma boa prática.
