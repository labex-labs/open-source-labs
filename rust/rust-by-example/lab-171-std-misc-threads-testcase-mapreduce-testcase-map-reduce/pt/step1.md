# Caso de Teste: map-reduce

O Rust torna muito fácil a paralelização do processamento de dados, sem muitas das dificuldades tradicionalmente associadas a essa tentativa.

A biblioteca padrão fornece excelentes primitivas de threading prontamente disponíveis. Estas, combinadas com o conceito de Propriedade e regras de aliasing do Rust, evitam automaticamente as corridas de dados.

As regras de aliasing (uma referência gravável XOR muitas referências de leitura) impedem automaticamente a manipulação de estados visíveis a outras threads. (Onde a sincronização é necessária, existem primitivas de sincronização como `Mutex`s ou `Channel`s.)

Neste exemplo, calcularemos a soma de todos os dígitos num bloco de números. Faremos isto dividindo os pedaços do bloco em diferentes threads. Cada thread somará o seu pequeno bloco de dígitos e, posteriormente, somaremos as somas intermediárias produzidas por cada thread.

Note que, embora estejamos a passar referências através de fronteiras de threads, o Rust compreende que estamos apenas a passar referências de leitura-somente e que, portanto, não podem ocorrer problemas de segurança ou corridas de dados. Também porque as referências que estamos a passar têm lifetimes `'static`, o Rust compreende que os nossos dados não serão destruídos enquanto estas threads estiverem a ser executadas. (Quando precisa de partilhar dados não `static` entre threads, pode usar um ponteiro inteligente como `Arc` para manter os dados vivos e evitar lifetimes não `static`.)

```rust
use std::thread;

// Esta é a thread `main`
fn main() {

    // Estes são os nossos dados a processar.
    // Calcularemos a soma de todos os dígitos através de um algoritmo map-reduce baseado em threads.
    // Cada bloco separado por espaços será tratado numa thread diferente.
    //
    // TODO: veja o que acontece à saída se inserir espaços!
    let data = "86967897737416471853297327050364959
11861322575564723963297542624962850
70856234701860851907960690014725639
38397966707106094172783238747669219
52380795257888236525459303330302837
58495327135744041048897885734297812
69920216438980873548808413720956532
16278424637452589860345374828574668";

    // Crie um vetor para armazenar as threads filhas que vamos criar.
    let mut children = vec![];

    /*************************************************************************
     * Fase "Map"
     *
     * Divida os nossos dados em segmentos e aplique o processamento inicial
     ************************************************************************/

    // divida os nossos dados em segmentos para cálculo individual
    // cada bloco será uma referência (&str) aos dados reais
    let chunked_data = data.split_whitespace();

    // Itera sobre os segmentos de dados.
    // .enumerate() adiciona o índice do loop atual a qualquer coisa que seja iterada
    // a tupla resultante "(índice, elemento)" é então imediatamente
    // "desestruturada" em duas variáveis, "i" e "data_segment", com uma
    // "atribuição de desestruturação"
    for (i, data_segment) in chunked_data.enumerate() {
        println!("segmento de dados {} é \"{}\"", i, data_segment);

        // Processa cada segmento de dados numa thread separada
        //
        // spawn() retorna um manipulador para a nova thread,
        // que DEVEMOS manter para aceder ao valor devolvido
        //
        // 'move || -> u32' é a sintaxe para um closure que:
        // * não recebe argumentos ('||')
        // * assume a propriedade das suas variáveis capturadas ('move') e
        // * retorna um inteiro sem sinal de 32 bits ('-> u32')
        //
        // O Rust é inteligente o suficiente para inferir o '-> u32' do
        // próprio closure, pelo que poderíamos ter omitido isso.
        //
        // TODO: tente remover o 'move' e veja o que acontece
        children.push(thread::spawn(move || -> u32 {
            // Calcula a soma intermediária deste segmento:
            let result = data_segment
                        // itera sobre os caracteres do nosso segmento..
                        .chars()
                        // .. converte caracteres de texto para o seu valor numérico..
                        .map(|c| c.to_digit(10).expect("deve ser um dígito"))
                        // .. e soma o iterador resultante de números
                        .sum();

            // println! bloqueia o stdout, por isso não ocorre entrelaçamento de texto
            println!("segmento processado {}, resultado={}", i, result);

            // "return" não é necessário, porque o Rust é uma "linguagem de expressões", a
            // última expressão avaliada em cada bloco é automaticamente o seu valor.
            result

        }));
    }


    /*************************************************************************
     * Fase "Reduce"
     *
     * Recolha os nossos resultados intermediários e combine-os num resultado final
     ************************************************************************/

    // combina os resultados intermediários de cada thread numa única soma final.
    //
    // usamos o "turbofish" ::<> para fornecer sum() com uma dica de tipo.
    //
    // TODO: tente sem o turbofish, especificando explicitamente o tipo de final_result
    let final_result = children.into_iter().map(|c| c.join().unwrap()).sum::<u32>();

    println!("Resultado final da soma: {}", final_result);
}

```

## Tarefas

Não é aconselhável deixar o número de threads depender de dados introduzidos pelo utilizador. E se o utilizador decidir inserir muitos espaços? Queremos realmente criar 2000 threads? Modifique o programa para que os dados sejam sempre divididos em um número limitado de blocos, definidos por uma constante estática no início do programa.
