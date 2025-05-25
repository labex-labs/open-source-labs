# Introdução

Neste laboratório, aprenderemos sobre conversão para e de strings em Rust. Para converter qualquer tipo para uma string, podemos implementar o traço `ToString` para o tipo. Alternativamente, podemos implementar o traço `fmt::Display`, que automaticamente fornece o traço `ToString` e permite imprimir o tipo usando `println!`. Por outro lado, para analisar uma string em um tipo específico, como um número, podemos usar a função `parse` juntamente com a inferência de tipo ou especificando o tipo usando a sintaxe "turbofish". Isso depende do traço `FromStr`, que é implementado para muitos tipos na biblioteca padrão. Se quisermos analisar uma string em um tipo definido pelo usuário, podemos implementar o traço `FromStr` para esse tipo.

> **Nota:** Se o laboratório não especificar um nome de arquivo, você pode usar qualquer nome de arquivo que desejar. Por exemplo, você pode usar `main.rs`, compilar e executá-lo com `rustc main.rs && ./main`.
