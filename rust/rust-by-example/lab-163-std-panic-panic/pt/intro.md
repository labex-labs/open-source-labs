# Introdução

Neste laboratório, aprendemos sobre o macro `panic!` em Rust, que pode ser usado para gerar um erro (`panic`) e iniciar o desempilhamento da sua pilha, fazendo com que o programa reporte a mensagem de erro e saia. O tempo de execução cuida de liberar todos os recursos pertencentes à thread, chamando o destrutor dos seus objetos. Também analisamos um exemplo de utilização do macro `panic!` para lidar com divisão por zero e verificamos que não resulta em vazamentos de memória usando o Valgrind.

> **Nota:** Se o laboratório não especificar um nome de ficheiro, pode usar qualquer nome de ficheiro que desejar. Por exemplo, pode usar `main.rs`, compilá-lo e executá-lo com `rustc main.rs && ./main`.
