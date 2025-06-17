# Usando Box`<T>` para Apontar para Dados no Heap

O smart pointer mais direto é uma _box_ (caixa), cujo tipo é escrito `Box<T>`. Boxes permitem que você armazene dados no heap em vez da stack. O que permanece na stack é o ponteiro para os dados no heap. Consulte o Capítulo 4 para revisar a diferença entre a stack e o heap.

Boxes não têm sobrecarga de desempenho, além de armazenar seus dados no heap em vez da stack. Mas eles também não têm muitos recursos extras. Você os usará com mais frequência nestas situações:

- Quando você tem um tipo cujo tamanho não pode ser conhecido em tempo de compilação e deseja usar um valor desse tipo em um contexto que exige um tamanho exato
- Quando você tem uma grande quantidade de dados e deseja transferir a propriedade, mas garantir que os dados não serão copiados ao fazê-lo
- Quando você deseja possuir um valor e se importa apenas que ele seja um tipo que implementa um trait específico, em vez de ser de um tipo específico

Demonstraremos a primeira situação em "Habilitando Tipos Recursivos com Boxes". No segundo caso, transferir a propriedade de uma grande quantidade de dados pode levar muito tempo porque os dados são copiados na stack. Para melhorar o desempenho nessa situação, podemos armazenar a grande quantidade de dados no heap em uma box. Então, apenas a pequena quantidade de dados do ponteiro é copiada na stack, enquanto os dados que ele referencia permanecem em um só lugar no heap. O terceiro caso é conhecido como um _objeto trait_ (objeto de trait), e "Usando Objetos Trait que Permitem Valores de Diferentes Tipos" é dedicado a esse tópico. Então, o que você aprender aqui, você aplicará novamente nessa seção!
