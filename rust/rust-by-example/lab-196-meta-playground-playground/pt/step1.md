# Playground

O [Rust Playground](https://play.rust-lang.org/) é uma forma de experimentar código Rust através de uma interface web.

## Usando-o com `mdbook`

No `mdbook`, você pode tornar exemplos de código executáveis e editáveis.

```rust
fn main() {
    println!("Hello World!");
}
```

Isso permite que o leitor execute a amostra de código, mas também a modifique e ajuste. A chave aqui é adicionar a palavra `editable` ao seu bloco de código, separada por uma vírgula.

````markdown
```rust
//...coloque seu código aqui
```
````

````

Além disso, você pode adicionar `ignore` se quiser que o `mdbook` pule seu código durante a construção e testes.

```markdown
```rust
//...coloque seu código aqui
````

```

## Usando-o com documentação

Você pode ter notado em alguns documentos oficiais do Rust um botão que diz "Executar", que abre a amostra de código em uma nova guia no Rust Playground. Este recurso é ativado se você usar o atributo `#[doc]` chamado `html_playground_url`.
```
