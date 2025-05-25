# Macros

Usamos macros como `println!` ao longo deste livro, mas não exploramos totalmente o que é uma macro e como ela funciona. O termo _macro_ refere-se a uma família de recursos em Rust: macros _declarativas_ com `macro_rules!` e três tipos de macros _procedurais_:

- Macros `#[derive]` customizadas que especificam o código adicionado com o atributo `derive` usado em structs e enums
- Macros semelhantes a atributos que definem atributos personalizados utilizáveis em qualquer item
- Macros semelhantes a funções que se parecem com chamadas de função, mas operam nos tokens especificados como seus argumentos

Falaremos sobre cada um deles por sua vez, mas primeiro, vamos ver por que precisamos de macros quando já temos funções.
