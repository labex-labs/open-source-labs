# Introdução

Neste laboratório, a hierarquia de arquivos dos módulos no exemplo de código pode ser representada da seguinte forma: existe um diretório chamado "my" que contém dois arquivos, "inaccessible.rs" e "nested.rs". Além disso, existe um arquivo chamado "my.rs" e um arquivo chamado "split.rs". O arquivo "split.rs" inclui o módulo "my", que é definido no arquivo "my.rs", e o arquivo "my.rs" inclui os módulos "inaccessible" e "nested", que são definidos nos arquivos "inaccessible.rs" e "nested.rs", respectivamente.

> **Nota:** Se o laboratório não especificar um nome de arquivo, você pode usar qualquer nome de arquivo que desejar. Por exemplo, você pode usar `main.rs`, compilar e executar com `rustc main.rs && ./main`.
