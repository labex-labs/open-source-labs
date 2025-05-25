# Tratando Ponteiros Inteligentes como Referências Regulares com Deref

Implementar o trait `Deref` permite que você personalize o comportamento do _operador de desreferenciação_ `*` (não deve ser confundido com o operador de multiplicação ou glob). Ao implementar `Deref` de tal forma que um ponteiro inteligente possa ser tratado como uma referência regular, você pode escrever código que opera em referências e usar esse código também com ponteiros inteligentes.

Vamos primeiro analisar como o operador de desreferenciação funciona com referências regulares. Em seguida, tentaremos definir um tipo personalizado que se comporte como `Box<T>` e veremos por que o operador de desreferenciação não funciona como uma referência em nosso tipo recém-definido. Exploraremos como a implementação do trait `Deref` torna possível que ponteiros inteligentes funcionem de maneira semelhante às referências. Em seguida, analisaremos o recurso de _coerção deref_ do Rust e como ele nos permite trabalhar com referências ou ponteiros inteligentes.

> Nota: Há uma grande diferença entre o tipo `MyBox<T>` que estamos prestes a construir e o `Box<T>` real: nossa versão não armazenará seus dados no heap. Estamos focando este exemplo em `Deref`, então onde os dados são realmente armazenados é menos importante do que o comportamento semelhante a um ponteiro.
