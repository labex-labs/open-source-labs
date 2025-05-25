# O Tipo Caractere

O tipo `char` do Rust é o tipo alfabético mais primitivo da linguagem. Aqui estão alguns exemplos de declaração de valores `char`:

Nome do arquivo: `src/main.rs`

```rust
fn main() {
    let c = 'z';
    let z: char = 'ℤ'; // com anotação de tipo explícita
    let heart_eyed_cat = '😻';
}
```

Observe que especificamos literais `char` com aspas simples, em oposição aos literais de string, que usam aspas duplas. O tipo `char` do Rust tem quatro bytes de tamanho e representa um Valor Escalar Unicode (Unicode Scalar Value), o que significa que pode representar muito mais do que apenas ASCII. Letras acentuadas; caracteres chineses, japoneses e coreanos; emoji; e espaços de largura zero são todos valores `char` válidos em Rust. Os Valores Escalares Unicode variam de `U+0000` a `U+D7FF` e `U+E000` a `U+10FFFF` inclusive. No entanto, um "caractere" não é realmente um conceito no Unicode, então sua intuição humana sobre o que é um "caractere" pode não corresponder ao que um `char` é em Rust. Discutiremos este tópico em detalhes em "Armazenando Texto Codificado em UTF-8 com Strings".
