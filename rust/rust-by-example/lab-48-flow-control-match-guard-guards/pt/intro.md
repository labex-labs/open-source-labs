# Introdução

Neste laboratório, aprendemos a utilizar _match guards_ em Rust para filtrar ramos com base em condições. O _match guard_ é adicionado após o padrão e é representado pela palavra-chave `if`, seguida de uma condição. A condição do _guard_ permite refinar ainda mais a correspondência de padrões e realizar verificações adicionais antes de executar o ramo correspondente da expressão _match_. No entanto, é importante notar que o compilador não considera as condições do _guard_ ao verificar a cobertura de padrões, por isso é necessário garantir que todos os padrões ainda estejam cobertos pela expressão _match_.

> **Nota:** Se o laboratório não especificar um nome de ficheiro, pode utilizar qualquer nome de ficheiro que desejar. Por exemplo, pode utilizar `main.rs`, compilá-lo e executá-lo com `rustc main.rs && ./main`.
