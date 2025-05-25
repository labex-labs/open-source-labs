# Prós e Contras do Padrão de Estado

Mostramos que o Rust é capaz de implementar o padrão de estado orientado a objetos para encapsular os diferentes tipos de comportamento que uma postagem deve ter em cada estado. Os métodos em `Post` não sabem nada sobre os vários comportamentos. Da maneira como organizamos o código, precisamos olhar apenas em um lugar para conhecer as diferentes maneiras como uma postagem publicada pode se comportar: a implementação do trait `State` na struct `Published`.

Se fôssemos criar uma implementação alternativa que não usasse o padrão de estado, poderíamos, em vez disso, usar expressões `match` nos métodos em `Post` ou mesmo no código `main` que verifica o estado da postagem e altera o comportamento nesses lugares. Isso significaria que teríamos que olhar em vários lugares para entender todas as implicações de uma postagem estar no estado publicado! Isso só aumentaria quanto mais estados adicionássemos: cada uma dessas expressões `match` precisaria de outro braço.

Com o padrão de estado, os métodos `Post` e os lugares onde usamos `Post` não precisam de expressões `match`, e para adicionar um novo estado, só precisaríamos adicionar uma nova struct e implementar os métodos de trait nessa struct.

A implementação usando o padrão de estado é fácil de estender para adicionar mais funcionalidades. Para ver a simplicidade de manter o código que usa o padrão de estado, experimente algumas dessas sugestões:

- Adicione um método `reject` que altere o estado da postagem de `PendingReview` de volta para `Draft`.
- Exija duas chamadas para `approve` antes que o estado possa ser alterado para `Published`.
- Permita que os usuários adicionem conteúdo de texto somente quando uma postagem estiver no estado `Draft`. Dica: faça com que o objeto de estado seja responsável pelo que pode mudar sobre o conteúdo, mas não seja responsável por modificar o `Post`.

Uma desvantagem do padrão de estado é que, como os estados implementam as transições entre os estados, alguns dos estados são acoplados uns aos outros. Se adicionarmos outro estado entre `PendingReview` e `Published`, como `Scheduled`, teríamos que alterar o código em `PendingReview` para fazer a transição para `Scheduled` em vez disso. Seria menos trabalho se `PendingReview` não precisasse mudar com a adição de um novo estado, mas isso significaria mudar para outro padrão de design.

Outra desvantagem é que duplicamos alguma lógica. Para eliminar parte da duplicação, podemos tentar fazer implementações padrão para os métodos `request_review` e `approve` no trait `State` que retornam `self`. No entanto, isso não funcionaria: ao usar `State` como um objeto de trait, o trait não sabe qual será o `self` concreto exatamente, então o tipo de retorno não é conhecido no tempo de compilação.

Outra duplicação inclui as implementações semelhantes dos métodos `request_review` e `approve` em `Post`. Ambos os métodos delegam à implementação do mesmo método no valor no campo `state` de `Option` e definem o novo valor do campo `state` para o resultado. Se tivéssemos muitos métodos em `Post` que seguissem esse padrão, poderíamos considerar a definição de uma macro para eliminar a repetição (consulte "Macros").

Ao implementar o padrão de estado exatamente como ele é definido para linguagens orientadas a objetos, não estamos aproveitando totalmente os pontos fortes do Rust como poderíamos. Vamos analisar algumas alterações que podemos fazer no crate `blog` que podem transformar estados e transições inválidos em erros de tempo de compilação.
