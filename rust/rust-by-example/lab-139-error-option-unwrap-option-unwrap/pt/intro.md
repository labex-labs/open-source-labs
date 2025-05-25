# Introdução

Neste laboratório, aprendemos sobre o enum `Option` na biblioteca `std` do Rust, que é usado para lidar com casos onde a ausência é uma possibilidade. Ele oferece duas opções: `Some(T)` para quando um elemento do tipo `T` é encontrado, e `None` para quando nenhum elemento é encontrado. Esses casos podem ser explicitamente tratados usando `match` ou implicitamente usando `unwrap`. O tratamento explícito permite maior controle e uma saída significativa, enquanto `unwrap` pode retornar o elemento interno ou induzir um pânico.

> **Nota:** Se o laboratório não especificar um nome de arquivo, você pode usar qualquer nome de arquivo que desejar. Por exemplo, você pode usar `main.rs`, compilar e executá-lo com `rustc main.rs && ./main`.
