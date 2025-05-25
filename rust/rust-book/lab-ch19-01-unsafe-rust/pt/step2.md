# Superpoderes Unsafe

Para mudar para o Unsafe Rust, use a palavra-chave `unsafe` e, em seguida, inicie um novo bloco que contém o código unsafe. Você pode realizar cinco ações no Unsafe Rust que não pode no Rust seguro, que chamamos de _superpoderes unsafe_. Esses superpoderes incluem a capacidade de:

1.  Desreferenciar um ponteiro bruto (raw pointer)
2.  Chamar uma função ou método unsafe
3.  Acessar ou modificar uma variável estática mutável
4.  Implementar uma trait unsafe
5.  Acessar campos de `union`s

É importante entender que `unsafe` não desliga o verificador de empréstimos (borrow checker) ou desabilita qualquer outra verificação de segurança do Rust: se você usar uma referência em código unsafe, ela ainda será verificada. A palavra-chave `unsafe` apenas dá acesso a esses cinco recursos que, então, não são verificados pelo compilador quanto à segurança da memória. Você ainda terá algum grau de segurança dentro de um bloco unsafe.

Além disso, `unsafe` não significa que o código dentro do bloco é necessariamente perigoso ou que definitivamente terá problemas de segurança de memória: a intenção é que, como programador, você garanta que o código dentro de um bloco `unsafe` acessará a memória de uma maneira válida.

As pessoas são falíveis e erros acontecerão, mas ao exigir que essas cinco operações unsafe estejam dentro de blocos anotados com `unsafe`, você saberá que quaisquer erros relacionados à segurança da memória devem estar dentro de um bloco `unsafe`. Mantenha os blocos `unsafe` pequenos; você agradecerá mais tarde quando investigar bugs de memória.

Para isolar o código unsafe o máximo possível, é melhor encapsular esse código dentro de uma abstração segura e fornecer uma API segura, o que discutiremos mais tarde no capítulo quando examinarmos funções e métodos unsafe. Partes da biblioteca padrão são implementadas como abstrações seguras sobre código unsafe que foi auditado. Envolver código unsafe em uma abstração segura impede que o uso de `unsafe` vaze para todos os lugares onde você ou seus usuários podem querer usar a funcionalidade implementada com código `unsafe`, porque usar uma abstração segura é seguro.

Vamos analisar cada um dos cinco superpoderes unsafe por sua vez. Também veremos algumas abstrações que fornecem uma interface segura para código unsafe.
