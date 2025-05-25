# Anatomia de um Programa Rust

Vamos analisar este programa "Hello, world!" em detalhes. Aqui está a primeira parte do quebra-cabeça:

```rust
fn main() {

}
```

Essas linhas definem uma função chamada `main`. A função `main` é especial: ela é sempre o primeiro código que é executado em todo programa Rust executável. Aqui, a primeira linha declara uma função chamada `main` que não possui parâmetros e não retorna nada. Se houvesse parâmetros, eles estariam dentro dos parênteses `()`.

O corpo da função está envolvido em `{}`. Rust exige chaves ao redor de todos os corpos de função. É um bom estilo colocar a chave de abertura na mesma linha da declaração da função, adicionando um espaço entre elas.

> Nota: Se você deseja manter um estilo padrão em todos os projetos Rust, você pode usar uma ferramenta de formatação automática chamada `rustfmt` para formatar seu código em um estilo específico (mais sobre `rustfmt` no Apêndice D). A equipe Rust incluiu esta ferramenta com a distribuição Rust padrão, assim como `rustc`, então ela já deve estar instalada em seu computador!

O corpo da função `main` contém o seguinte código:

```rust
    println!("Hello, world!");
```

Esta linha faz todo o trabalho neste pequeno programa: ela imprime texto na tela. Existem quatro detalhes importantes a serem observados aqui.

Primeiro, o estilo Rust é indentar com quatro espaços, não uma tabulação.

Segundo, `println!` chama uma macro Rust. Se tivesse chamado uma função em vez disso, seria inserido como `println` (sem o `!`). Discutiremos as macros Rust com mais detalhes no Capítulo 19. Por enquanto, você só precisa saber que usar um `!` significa que você está chamando uma macro em vez de uma função normal e que as macros nem sempre seguem as mesmas regras que as funções.

Terceiro, você vê a string `"Hello, world!"`. Passamos esta string como um argumento para `println!`, e a string é impressa na tela.

Quarto, terminamos a linha com um ponto e vírgula (`;`), que indica que esta expressão acabou e a próxima está pronta para começar. A maioria das linhas de código Rust termina com um ponto e vírgula.
