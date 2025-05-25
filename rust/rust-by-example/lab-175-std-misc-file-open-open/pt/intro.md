# Introdução

Neste laboratório, a função `open` é apresentada como uma forma de abrir um arquivo em modo de leitura somente, fornecendo o caminho para o arquivo desejado. A função retorna um objeto `File` que possui o descritor do arquivo e cuida do fechamento do arquivo quando não mais necessário.

Para usar a função `open`, é necessário importar os módulos necessários, como `std::fs::File`, `std::io::prelude::*`, e `std::path::Path`. O método `File::open` é então chamado com o caminho como argumento. Se o arquivo for aberto com sucesso, a função retorna um objeto `Result<File, io::Error>`, caso contrário, gera uma falha com uma mensagem de erro.

Uma vez que o arquivo esteja aberto, seu conteúdo pode ser lido usando o método `read_to_string`. Este método lê o conteúdo do arquivo para uma string e retorna um `Result<usize, io::Error>`. Se a operação de leitura for bem-sucedida, a string conterá o conteúdo do arquivo. Caso contrário, gera uma falha com uma mensagem de erro.

No exemplo fornecido, o conteúdo do arquivo `hello.txt` é lido e impresso no console. O traço `drop` é usado para garantir que o arquivo seja fechado quando o objeto `file` sai de escopo.

> **Nota:** Se o laboratório não especificar um nome de arquivo, você pode usar qualquer nome de arquivo que desejar. Por exemplo, você pode usar `main.rs`, compilar e executar com `rustc main.rs && ./main`.
