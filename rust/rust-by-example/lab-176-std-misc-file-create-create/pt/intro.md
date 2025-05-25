# Introdução

Neste laboratório, temos uma função `create` que abre um ficheiro em modo de escrita exclusiva. Ela cria um novo ficheiro ou destrói o conteúdo antigo se o ficheiro já existir. A função utiliza a biblioteca padrão do Rust para lidar com operações de ficheiros. O exemplo fornecido demonstra como utilizar a função `create` para escrever o conteúdo de uma string estática `LOREM_IPSUM` num ficheiro chamado "lorem_ipsum.txt". A saída mostra uma confirmação de operação de escrita bem-sucedida, e o conteúdo do ficheiro é apresentado utilizando o comando `cat`.

> **Nota:** Se o laboratório não especificar um nome de ficheiro, pode utilizar qualquer nome de ficheiro que desejar. Por exemplo, pode utilizar `main.rs`, compilá-lo e executá-lo com `rustc main.rs && ./main`.
