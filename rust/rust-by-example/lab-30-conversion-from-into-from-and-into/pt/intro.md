# Introdução

Neste laboratório, exploramos os conceitos dos traits `From` e `Into` em Rust, utilizados para conversão entre diferentes tipos. Estes traits estão intrinsecamente ligados, sendo `Into` o recíproco de `From`. O trait `From` permite que um tipo defina como criar a si próprio a partir de outro tipo, permitindo uma conversão fácil entre tipos. O trait `Into` chama automaticamente a implementação de `From` quando necessário. Ambos os traits podem ser implementados para tipos personalizados, proporcionando flexibilidade nas conversões de tipo.

> **Nota:** Se o laboratório não especificar um nome de ficheiro, pode utilizar qualquer nome de ficheiro que desejar. Por exemplo, pode utilizar `main.rs`, compilá-lo e executá-lo com `rustc main.rs && ./main`.
