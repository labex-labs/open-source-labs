# Comentários

Qualquer programa requer comentários, e Rust suporta algumas variedades diferentes:

- _Comentários regulares_ que são ignorados pelo compilador:
  - `// Comentários de linha que vão até o final da linha.`
  - `/* Comentários de bloco que vão até o delimitador de fechamento. */`
- _Comentários de documentação (Doc comments)_ que são analisados em documentação HTML da biblioteca:
  - `/// Gera documentação da biblioteca para o item seguinte.`
  - `//! Gera documentação da biblioteca para o item envolvente.`

```rust
fn main() {
    // Este é um exemplo de um comentário de linha.
    // Existem duas barras no início da linha.
    // E nada escrito após estas será lido pelo compilador.

    // println!("Olá, mundo!");

    // Execute-o. Viu? Agora tente deletar as duas barras e execute-o novamente.

    /*
     * Este é outro tipo de comentário, um comentário de bloco. Em geral,
     * comentários de linha são o estilo de comentário recomendado. Mas comentários de bloco
     * são extremamente úteis para desabilitar temporariamente pedaços de código.
     * /* Comentários de bloco podem ser /* aninhados, */ */ então leva apenas algumas
     * teclas para comentar tudo nesta função main().
     * /*/*/* Tente você mesmo! */*/*/
     */

    /*
    Nota: A coluna anterior de `*` foi inteiramente por estilo. Não há
    nenhuma necessidade real disso.
    */

    // Você pode manipular expressões mais facilmente com comentários de bloco
    // do que com comentários de linha. Tente deletar os delimitadores de comentário
    // para alterar o resultado:
    let x = 5 + /* 90 + */ 5;
    println!("`x` é 10 ou 100? x = {}", x);
}
```
