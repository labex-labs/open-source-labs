# O Tipo _Slice_

_Slices_ permitem que você referencie uma sequência contígua de elementos em uma coleção, em vez da coleção inteira. Um _slice_ é um tipo de referência, portanto, não possui _ownership_ (propriedade).

Aqui está um pequeno problema de programação: escreva uma função que recebe uma string de palavras separadas por espaços e retorna a primeira palavra que encontra nessa string. Se a função não encontrar um espaço na string, a string inteira deve ser uma palavra, então a string inteira deve ser retornada.

Vamos analisar como escreveríamos a assinatura desta função sem usar _slices_, para entender o problema que os _slices_ resolverão:

```rust
fn first_word(s: &String) -> ?
```

A função `first_word` tem um `&String` como parâmetro. Não queremos _ownership_, então isso está correto. Mas o que devemos retornar? Realmente não temos como falar sobre _parte_ de uma string. No entanto, poderíamos retornar o índice do final da palavra, indicado por um espaço. Vamos tentar isso, como mostrado na Listagem 4-7.

Nome do arquivo: `src/main.rs`

```rust
fn first_word(s: &String) -> usize {
  1 let bytes = s.as_bytes();

    for (2 i, &item) in 3 bytes.iter().enumerate() {
      4 if item == b' ' {
            return i;
        }
    }

  5 s.len()
}
```

Listagem 4-7: A função `first_word` que retorna um valor de índice de byte para o parâmetro `String`

Como precisamos percorrer o elemento `String` por elemento e verificar se um valor é um espaço, converteremos nossa `String` em um array de bytes usando o método `as_bytes` \[1].

Em seguida, criamos um iterador sobre o array de bytes usando o método `iter` \[3]. Discutiremos iteradores com mais detalhes no Capítulo 13. Por enquanto, saiba que `iter` é um método que retorna cada elemento em uma coleção e que `enumerate` envolve o resultado de `iter` e retorna cada elemento como parte de uma tupla. O primeiro elemento da tupla retornada de `enumerate` é o índice, e o segundo elemento é uma referência ao elemento. Isso é um pouco mais conveniente do que calcular o índice nós mesmos.

Como o método `enumerate` retorna uma tupla, podemos usar padrões para desestruturar essa tupla. Discutiremos padrões com mais detalhes no Capítulo 6. No loop `for`, especificamos um padrão que tem `i` para o índice na tupla e `&item` para o byte único na tupla \[2]. Como obtemos uma referência ao elemento de `.iter().enumerate()`, usamos `&` no padrão.

Dentro do loop `for`, procuramos o byte que representa o espaço usando a sintaxe literal de byte \[4]. Se encontrarmos um espaço, retornamos a posição. Caso contrário, retornamos o comprimento da string usando `s.len()` \[5].

Agora temos uma maneira de descobrir o índice do final da primeira palavra na string, mas há um problema. Estamos retornando um `usize` por conta própria, mas é apenas um número significativo no contexto do `&String`. Em outras palavras, como é um valor separado do `String`, não há garantia de que ainda será válido no futuro. Considere o programa na Listagem 4-8 que usa a função `first_word` da Listagem 4-7.

    // src/main.rs
    fn main() {
        let mut s = String::from("hello world");

        let word = first_word(&s); // word will get the value 5

        s.clear(); // this empties the String, making it equal to ""

        // word still has the value 5 here, but there's no more string that
        // we could meaningfully use the value 5 with. word is now totally invalid!
    }

Listagem 4-8: Armazenando o resultado da chamada da função `first_word` e, em seguida, alterando o conteúdo da `String`

Este programa compila sem erros e também o faria se usássemos `word` após chamar `s.clear()`. Como `word` não está conectado ao estado de `s` de forma alguma, `word` ainda contém o valor `5`. Poderíamos usar esse valor `5` com a variável `s` para tentar extrair a primeira palavra, mas isso seria um bug porque o conteúdo de `s` mudou desde que salvamos `5` em `word`.

Ter que se preocupar com o índice em `word` ficando fora de sincronia com os dados em `s` é tedioso e propenso a erros! Gerenciar esses índices é ainda mais frágil se escrevermos uma função `second_word`. Sua assinatura teria que ser assim:

```rust
fn second_word(s: &String) -> (usize, usize) {
```

Agora estamos rastreando um índice inicial _e_ um final, e temos ainda mais valores que foram calculados a partir de dados em um estado específico, mas não estão vinculados a esse estado de forma alguma. Temos três variáveis não relacionadas flutuando por aí que precisam ser mantidas em sincronia.

Felizmente, Rust tem uma solução para este problema: _string slices_.
