# Aceitando Argumentos da Linha de Comando

Vamos criar um novo projeto com, como sempre, `cargo new`. Chamaremos nosso projeto de `minigrep` para distingui-lo da ferramenta `grep` que você pode já ter em seu sistema.

```bash
$ cargo new minigrep
     Created binary (application) `minigrep` project
$ cd minigrep
```

A primeira tarefa é fazer com que `minigrep` aceite seus dois argumentos da linha de comando: o caminho do arquivo e uma string para pesquisar. Ou seja, queremos ser capazes de executar nosso programa com `cargo run`, dois hífens para indicar que os argumentos a seguir são para nosso programa, em vez de para o `cargo`, uma string para pesquisar e um caminho para um arquivo para pesquisar, assim:

```bash
cargo run -- searchstring example-filename.txt
```

No momento, o programa gerado por `cargo new` não pode processar os argumentos que lhe damos. Algumas bibliotecas existentes em *https://crates.io* podem ajudar a escrever um programa que aceite argumentos da linha de comando, mas como você está apenas aprendendo este conceito, vamos implementar essa capacidade nós mesmos.
