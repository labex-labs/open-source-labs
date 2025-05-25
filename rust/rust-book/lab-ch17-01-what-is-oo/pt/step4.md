# Herança como um Sistema de Tipos e como Compartilhamento de Código

_Herança_ é um mecanismo pelo qual um objeto pode herdar elementos da definição de outro objeto, ganhando assim os dados e o comportamento do objeto pai sem que você precise defini-los novamente.

Se uma linguagem deve ter herança para ser orientada a objetos, então Rust não é essa linguagem. Não há como definir uma struct que herde os campos e implementações de métodos da struct pai sem usar uma macro.

No entanto, se você está acostumado a ter herança em sua caixa de ferramentas de programação, você pode usar outras soluções em Rust, dependendo do seu motivo para usar herança em primeiro lugar.

Você escolheria herança por duas razões principais. Uma é para reutilização de código: você pode implementar um comportamento específico para um tipo, e a herança permite que você reutilize essa implementação para um tipo diferente. Você pode fazer isso de forma limitada no código Rust usando implementações de métodos de trait padrão, que você viu na Listagem 10-14 quando adicionamos uma implementação padrão do método `summarize` no trait `Summary`. Qualquer tipo que implemente o trait `Summary` teria o método `summarize` disponível nele sem nenhum código adicional. Isso é semelhante a uma classe pai que tem uma implementação de um método e uma classe filha herdeira também tendo a implementação do método. Também podemos substituir a implementação padrão do método `summarize` quando implementamos o trait `Summary`, o que é semelhante a uma classe filha substituindo a implementação de um método herdado de uma classe pai.

A outra razão para usar herança está relacionada ao sistema de tipos: para permitir que um tipo filho seja usado nos mesmos lugares que o tipo pai. Isso também é chamado de _polimorfismo_, o que significa que você pode substituir vários objetos uns pelos outros em tempo de execução se eles compartilharem certas características.

> **Polimorfismo**
>
> Para muitas pessoas, polimorfismo é sinônimo de herança. Mas, na verdade, é um conceito mais geral que se refere ao código que pode trabalhar com dados de vários tipos. Para herança, esses tipos são geralmente subclasses.
>
> Em vez disso, Rust usa genéricos para abstrair sobre diferentes tipos possíveis e limites de trait para impor restrições sobre o que esses tipos devem fornecer. Isso às vezes é chamado de _polimorfismo paramétrico limitado_.

A herança caiu em desuso recentemente como uma solução de design de programação em muitas linguagens de programação porque muitas vezes corre o risco de compartilhar mais código do que o necessário. Subclasses nem sempre devem compartilhar todas as características de sua classe pai, mas o farão com herança. Isso pode tornar o design de um programa menos flexível. Também introduz a possibilidade de chamar métodos em subclasses que não fazem sentido ou que causam erros porque os métodos não se aplicam à subclasse. Além disso, algumas linguagens só permitirão herança única (o que significa que uma subclasse só pode herdar de uma classe), restringindo ainda mais a flexibilidade do design de um programa.

Por essas razões, Rust adota a abordagem diferente de usar objetos de trait em vez de herança. Vamos ver como os objetos de trait permitem o polimorfismo em Rust.
