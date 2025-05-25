# Tipos de Tamanho Dinâmico e o Trait Sized

O Rust precisa saber certos detalhes sobre seus tipos, como quanto espaço alocar para um valor de um tipo específico. Isso deixa um canto de seu sistema de tipos um pouco confuso no início: o conceito de _tipos de tamanho dinâmico_ (dynamically sized types). Às vezes referidos como _DSTs_ ou _tipos sem tamanho_ (unsized types), esses tipos nos permitem escrever código usando valores cujo tamanho só podemos saber em tempo de execução.

Vamos analisar os detalhes de um tipo de tamanho dinâmico chamado `str`, que temos usado ao longo do livro. É isso mesmo, não `&str`, mas `str` sozinho, é um DST. Não podemos saber quanto tempo a string tem até o tempo de execução, o que significa que não podemos criar uma variável do tipo `str`, nem podemos receber um argumento do tipo `str`. Considere o seguinte código, que não funciona:

```rust
let s1: str = "Hello there!";
let s2: str = "How's it going?";
```

O Rust precisa saber quanta memória alocar para qualquer valor de um tipo específico, e todos os valores de um tipo devem usar a mesma quantidade de memória. Se o Rust nos permitisse escrever este código, esses dois valores `str` precisariam ocupar a mesma quantidade de espaço. Mas eles têm comprimentos diferentes: `s1` precisa de 12 bytes de armazenamento e `s2` precisa de 15. É por isso que não é possível criar uma variável que contenha um tipo de tamanho dinâmico.

Então, o que fazemos? Neste caso, você já sabe a resposta: tornamos os tipos de `s1` e `s2` um `&str` em vez de um `str`. Recorde de "Fatias de String" que a estrutura de dados de fatia apenas armazena a posição inicial e o comprimento da fatia. Então, embora um `&T` seja um único valor que armazena o endereço de memória de onde o `T` está localizado, um `&str` são _dois_ valores: o endereço do `str` e seu comprimento. Como tal, podemos saber o tamanho de um valor `&str` em tempo de compilação: é o dobro do comprimento de um `usize`. Ou seja, sempre sabemos o tamanho de um `&str`, não importa o quão longa seja a string a que ele se refere. Em geral, esta é a maneira pela qual os tipos de tamanho dinâmico são usados no Rust: eles têm um bit extra de metadados que armazena o tamanho da informação dinâmica. A regra de ouro dos tipos de tamanho dinâmico é que sempre devemos colocar valores de tipos de tamanho dinâmico atrás de um ponteiro de algum tipo.

Podemos combinar `str` com todos os tipos de ponteiros: por exemplo, `Box<str>` ou `Rc<str>`. Na verdade, você já viu isso antes, mas com um tipo de tamanho dinâmico diferente: traits. Cada trait é um tipo de tamanho dinâmico ao qual podemos nos referir usando o nome do trait. Em "Usando Objetos de Trait que Permitem Valores de Tipos Diferentes", mencionamos que para usar traits como objetos de trait, devemos colocá-los atrás de um ponteiro, como `&dyn Trait` ou `Box<dyn Trait>` (`Rc<dyn Trait>` também funcionaria).

Para trabalhar com DSTs, o Rust fornece o trait `Sized` para determinar se o tamanho de um tipo é conhecido em tempo de compilação. Este trait é implementado automaticamente para tudo cujo tamanho é conhecido em tempo de compilação. Além disso, o Rust adiciona implicitamente um limite em `Sized` para cada função genérica. Ou seja, uma definição de função genérica como esta:

```rust
fn generic<T>(t: T) {
    --snip--
}
```

é realmente tratada como se tivéssemos escrito isto:

```rust
fn generic<T: Sized>(t: T) {
    --snip--
}
```

Por padrão, funções genéricas funcionarão apenas em tipos que têm um tamanho conhecido em tempo de compilação. No entanto, você pode usar a seguinte sintaxe especial para relaxar esta restrição:

```rust
fn generic<T: ?Sized>(t: &T) {
    --snip--
}
```

Um limite de trait em `?Sized` significa "`T` pode ou não ser `Sized`" e esta notação substitui o padrão de que tipos genéricos devem ter um tamanho conhecido em tempo de compilação. A sintaxe `?Trait` com este significado só está disponível para `Sized`, não para quaisquer outros traits.

Observe também que mudamos o tipo do parâmetro `t` de `T` para `&T`. Como o tipo pode não ser `Sized`, precisamos usá-lo atrás de algum tipo de ponteiro. Neste caso, escolhemos uma referência.

Em seguida, falaremos sobre funções e closures!
