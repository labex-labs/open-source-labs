# Habilitando Tipos Recursivos com Boxes

Um valor de um _tipo recursivo_ pode ter outro valor do mesmo tipo como parte de si mesmo. Tipos recursivos representam um problema porque, em tempo de compilação, o Rust precisa saber quanto espaço um tipo ocupa. No entanto, o aninhamento de valores de tipos recursivos poderia, teoricamente, continuar infinitamente, então o Rust não pode saber quanto espaço o valor precisa. Como as boxes têm um tamanho conhecido, podemos habilitar tipos recursivos inserindo uma box na definição do tipo recursivo.

Como exemplo de um tipo recursivo, vamos explorar a _lista cons_ (cons list). Este é um tipo de dado comumente encontrado em linguagens de programação funcional. O tipo de lista cons que definiremos é simples, exceto pela recursão; portanto, os conceitos no exemplo com o qual trabalharemos serão úteis sempre que você se deparar com situações mais complexas envolvendo tipos recursivos.
