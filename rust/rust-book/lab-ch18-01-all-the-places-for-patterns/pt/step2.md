# Ramos `match`

Como discutido no Capítulo 6, usamos padrões nos ramos das expressões `match`. Formalmente, as expressões `match` são definidas pela palavra-chave `match`, um valor para corresponder e um ou mais ramos de correspondência que consistem em um padrão e uma expressão para executar se o valor corresponder ao padrão desse ramo, assim:

    match VALUE {
        PATTERN => EXPRESSION,
        PATTERN => EXPRESSION,
        PATTERN => EXPRESSION,
    }

Por exemplo, aqui está a expressão `match` da Listagem 6-5 que corresponde a um valor `Option<i32>` na variável `x`:

    match x {
        None => None,
        Some(i) => Some(i + 1),
    }

Os padrões nesta expressão `match` são `None` e `Some(i)` à esquerda de cada seta.

Um requisito para as expressões `match` é que elas precisam ser _exaustivas_ no sentido de que todas as possibilidades para o valor na expressão `match` devem ser consideradas. Uma maneira de garantir que você cobriu todas as possibilidades é ter um padrão genérico para o último ramo: por exemplo, um nome de variável correspondendo a qualquer valor nunca pode falhar e, portanto, cobre todos os casos restantes.

O padrão específico `_` corresponderá a qualquer coisa, mas nunca se vincula a uma variável, por isso é frequentemente usado no último ramo `match`. O padrão `_` pode ser útil quando você deseja ignorar qualquer valor não especificado, por exemplo. Abordaremos o padrão `_` com mais detalhes em "Ignorando Valores em um Padrão".
