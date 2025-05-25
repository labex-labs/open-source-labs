# O Problema

Um `trait` genérico sobre o tipo de seu contêiner tem requisitos de especificação de tipo - os usuários do `trait` _devem_ especificar todos os seus tipos genéricos.

No exemplo abaixo, o `trait` `Contains` permite o uso dos tipos genéricos `A` e `B`. O trait é então implementado para o tipo `Container`, especificando `i32` para `A` e `B`, para que possa ser usado com `fn difference()`.

Como `Contains` é genérico, somos forçados a declarar explicitamente _todos_ os tipos genéricos para `fn difference()`. Na prática, queremos uma maneira de expressar que `A` e `B` são determinados pela entrada `C`. Como você verá na próxima seção, os tipos associados fornecem exatamente essa capacidade.
