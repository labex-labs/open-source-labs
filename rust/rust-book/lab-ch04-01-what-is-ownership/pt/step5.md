# Memória e Alocação

No caso de um literal de _string_, conhecemos o conteúdo no tempo de compilação, então o texto é codificado diretamente no executável final. É por isso que os literais de _string_ são rápidos e eficientes. Mas essas propriedades vêm apenas da imutabilidade do literal de _string_. Infelizmente, não podemos colocar um bloco de memória no binário para cada pedaço de texto cujo tamanho é desconhecido no tempo de compilação e cujo tamanho pode mudar durante a execução do programa.

Com o tipo `String`, para suportar um pedaço de texto mutável e expansível, precisamos alocar uma quantidade de memória na _heap_, desconhecida no tempo de compilação, para conter o conteúdo. Isso significa:

- A memória deve ser solicitada ao alocador de memória em tempo de execução.
- Precisamos de uma maneira de retornar essa memória ao alocador quando terminarmos com nossa `String`.

Essa primeira parte é feita por nós: quando chamamos `String::from`, sua implementação solicita a memória de que precisa. Isso é praticamente universal em linguagens de programação.

No entanto, a segunda parte é diferente. Em linguagens com um _coletor de lixo (GC)_, o GC acompanha e limpa a memória que não está mais sendo usada, e não precisamos pensar nisso. Na maioria das linguagens sem um GC, é nossa responsabilidade identificar quando a memória não está mais sendo usada e chamar o código para liberá-la explicitamente, assim como fizemos para solicitá-la. Fazê-lo corretamente tem sido historicamente um problema de programação difícil. Se esquecermos, desperdiçaremos memória. Se fizermos isso muito cedo, teremos uma variável inválida. Se fizermos isso duas vezes, isso também é um _bug_. Precisamos emparelhar exatamente um `allocate` com exatamente um `free`.

Rust segue um caminho diferente: a memória é retornada automaticamente assim que a variável que a possui sai do escopo. Aqui está uma versão do nosso exemplo de escopo da Listagem 4-1 usando um `String` em vez de um literal de _string_:

    {
        let s = String::from("hello"); // s é válido a partir deste ponto

        // faça algo com s
    }                                  // este escopo acabou, e s não é mais
                                       // válido

Há um ponto natural em que podemos retornar a memória que nossa `String` precisa para o alocador: quando `s` sai do escopo. Quando uma variável sai do escopo, o Rust chama uma função especial para nós. Essa função é chamada `drop`, e é onde o autor de `String` pode colocar o código para retornar a memória. Rust chama `drop` automaticamente na chave de fechamento.

> Nota: Em C++, esse padrão de desalocar recursos no final da vida útil de um item às vezes é chamado de _Aquisição de Recursos é Inicialização_ _(RAII)_. A função `drop` em Rust será familiar para você se você usou padrões RAII.

Esse padrão tem um impacto profundo na forma como o código Rust é escrito. Pode parecer simples agora, mas o comportamento do código pode ser inesperado em situações mais complicadas quando queremos que várias variáveis usem os dados que alocamos na _heap_. Vamos explorar algumas dessas situações agora.
