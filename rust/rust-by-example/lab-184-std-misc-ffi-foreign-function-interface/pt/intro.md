# Introdução

Neste laboratório, aprendemos sobre a Interface de Função Estrangeira (FFI) do Rust, que permite a interação com bibliotecas C declarando funções estrangeiras dentro de um bloco `extern` e anotando-as com um atributo `#[link]` contendo o nome da biblioteca estrangeira. O exemplo de código demonstra o uso da FFI para chamar funções externas da biblioteca `libm`, como calcular a raiz quadrada de um número complexo de precisão única e calcular o cosseno de um número complexo. Geralmente, são usados wrappers seguros em torno dessas chamadas de funções estrangeiras inseguras. O laboratório também inclui uma implementação mínima de números complexos de precisão única e demonstra como chamar APIs seguras envolvendo operações inseguras.

> **Nota:** Se o laboratório não especificar um nome de arquivo, você pode usar qualquer nome de arquivo que desejar. Por exemplo, você pode usar `main.rs`, compilar e executá-lo com `rustc main.rs && ./main`.
