# Implementando o Trait Deref

Como discutido em "Implementando um Trait em um Tipo", para implementar um trait, precisamos fornecer implementações para os métodos exigidos pelo trait. O trait `Deref`, fornecido pela biblioteca padrão, exige que implementemos um método chamado `deref` que empresta `self` e retorna uma referência aos dados internos. A Listagem 15-10 contém uma implementação de `Deref` para adicionar à definição de `MyBox``<T>`.

Nome do arquivo: `src/main.rs`

```rust
use std::ops::Deref;

impl<T> Deref for MyBox<T> {
  1 type Target = T;

    fn deref(&self) -> &Self::Target {
      2 &self.0
    }
}
```

Listagem 15-10: Implementando `Deref` em `MyBox<T>`

A sintaxe `type Target = T;` \[1] define um tipo associado para o trait `Deref` usar. Tipos associados são uma maneira ligeiramente diferente de declarar um parâmetro genérico, mas você não precisa se preocupar com eles por enquanto; abordaremos eles em mais detalhes no Capítulo 19.

Preenchemos o corpo do método `deref` com `&self.0` para que `deref` retorne uma referência ao valor que queremos acessar com o operador `*` \[2]; lembre-se de "Usando Structs de Tupla Sem Campos Nomeados para Criar Tipos Diferentes" que `.0` acessa o primeiro valor em uma struct de tupla. A função `main` na Listagem 15-9 que chama `*` no valor `MyBox<T>` agora compila, e as asserções passam!

Sem o trait `Deref`, o compilador só pode desreferenciar referências `&`. O método `deref` dá ao compilador a capacidade de pegar um valor de qualquer tipo que implemente `Deref` e chamar o método `deref` para obter uma referência `&` que ele sabe como desreferenciar.

Quando inserimos `*y` na Listagem 15-9, nos bastidores o Rust realmente executou este código:

```rust
*(y.deref())
```

Rust substitui o operador `*` por uma chamada ao método `deref` e, em seguida, uma desreferenciação simples para que não tenhamos que pensar se precisamos ou não chamar o método `deref`. Esse recurso do Rust nos permite escrever código que funciona de forma idêntica, quer tenhamos uma referência regular ou um tipo que implemente `Deref`.

A razão pela qual o método `deref` retorna uma referência a um valor, e que a desreferenciação simples fora dos parênteses em `*(y.deref())` ainda é necessária, tem a ver com o sistema de propriedade. Se o método `deref` retornasse o valor diretamente em vez de uma referência ao valor, o valor seria movido de `self`. Não queremos assumir a propriedade do valor interno dentro de `MyBox<T>` neste caso ou na maioria dos casos em que usamos o operador de desreferenciação.

Observe que o operador `*` é substituído por uma chamada ao método `deref` e, em seguida, uma chamada ao operador `*` apenas uma vez, cada vez que usamos um `*` em nosso código. Como a substituição do operador `*` não se repete infinitamente, acabamos com dados do tipo `i32`, que correspondem ao `5` em `assert_eq!` na Listagem 15-9.
