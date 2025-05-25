# Aplicando as Regras de Empréstimo em Tempo de Execução com RefCell`<T>`

Ao contrário de `Rc<T>`, o tipo `RefCell<T>` representa propriedade única sobre os dados que ele contém. Então, o que torna `RefCell<T>` diferente de um tipo como `Box<T>`? Recorde as regras de empréstimo que você aprendeu no Capítulo 4:

- A qualquer momento, você pode ter _ou_ uma referência mutável ou qualquer número de referências imutáveis (mas não ambos).
- As referências devem ser sempre válidas.

Com referências e `Box<T>`, os invariantes das regras de empréstimo são aplicados em tempo de compilação. Com `RefCell<T>`, esses invariantes são aplicados _em tempo de execução_. Com referências, se você quebrar essas regras, você receberá um erro do compilador. Com `RefCell<T>`, se você quebrar essas regras, seu programa entrará em pânico e sairá.

As vantagens de verificar as regras de empréstimo em tempo de compilação são que os erros serão detectados mais cedo no processo de desenvolvimento, e não há impacto no desempenho em tempo de execução porque toda a análise é concluída antecipadamente. Por essas razões, verificar as regras de empréstimo em tempo de compilação é a melhor escolha na maioria dos casos, e é por isso que esta é a configuração padrão do Rust.

A vantagem de verificar as regras de empréstimo em tempo de execução é que certos cenários seguros para a memória são então permitidos, onde teriam sido proibidos pelas verificações em tempo de compilação. A análise estática, como o compilador Rust, é inerentemente conservadora. Algumas propriedades do código são impossíveis de detectar analisando o código: o exemplo mais famoso é o Problema da Parada (Halting Problem), que está além do escopo deste livro, mas é um tópico interessante para pesquisar.

Como alguma análise é impossível, se o compilador Rust não puder ter certeza de que o código está em conformidade com as regras de propriedade, ele poderá rejeitar um programa correto; dessa forma, ele é conservador. Se o Rust aceitasse um programa incorreto, os usuários não poderiam confiar nas garantias que o Rust faz. No entanto, se o Rust rejeitar um programa correto, o programador será inconveniente, mas nada catastrófico pode ocorrer. O tipo `RefCell<T>` é útil quando você tem certeza de que seu código segue as regras de empréstimo, mas o compilador não consegue entender e garantir isso.

Semelhante a `Rc<T>`, `RefCell<T>` é apenas para uso em cenários de thread único e fornecerá um erro em tempo de compilação se você tentar usá-lo em um contexto multithread. Falaremos sobre como obter a funcionalidade de `RefCell<T>` em um programa multithreaded no Capítulo 16.

Aqui está um resumo das razões para escolher `Box<T>`, `Rc<T>` ou `RefCell<T>`:

- `Rc<T>` permite múltiplos proprietários dos mesmos dados; `Box<T>` e `RefCell<T>` têm proprietários únicos.
- `Box<T>` permite empréstimos imutáveis ou mutáveis verificados em tempo de compilação; `Rc<T>` permite apenas empréstimos imutáveis verificados em tempo de compilação; `RefCell<T>` permite empréstimos imutáveis ou mutáveis verificados em tempo de execução.
- Como `RefCell<T>` permite empréstimos mutáveis verificados em tempo de execução, você pode mutar o valor dentro do `RefCell<T>` mesmo quando o `RefCell<T>` é imutável.

Mutar o valor dentro de um valor imutável é o padrão de _mutabilidade interior_ (interior mutability). Vamos analisar uma situação em que a mutabilidade interior é útil e examinar como isso é possível.
