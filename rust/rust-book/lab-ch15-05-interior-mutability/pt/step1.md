# RefCell`<T>` e o Padrão de Mutabilidade Interior

A _mutabilidade interior_ (interior mutability) é um padrão de design em Rust que permite mutar dados mesmo quando existem referências imutáveis a esses dados; normalmente, essa ação é proibida pelas regras de empréstimo (borrowing rules). Para mutar dados, o padrão usa código `unsafe` dentro de uma estrutura de dados para contornar as regras usuais do Rust que governam a mutação e o empréstimo. Código unsafe indica ao compilador que estamos verificando as regras manualmente, em vez de confiar no compilador para verificá-las por nós; discutiremos o código unsafe com mais detalhes no Capítulo 19.

Podemos usar tipos que usam o padrão de mutabilidade interior somente quando podemos garantir que as regras de empréstimo serão seguidas em tempo de execução, mesmo que o compilador não possa garantir isso. O código `unsafe` envolvido é então encapsulado em uma API segura, e o tipo externo ainda é imutável.

Vamos explorar esse conceito analisando o tipo `RefCell<T>` que segue o padrão de mutabilidade interior.
