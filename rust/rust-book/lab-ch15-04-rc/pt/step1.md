# Rc`<T>`{=html}, o Ponteiro Inteligente com Contagem de Referências

Na maioria dos casos, a propriedade é clara: você sabe exatamente qual variável possui um determinado valor. No entanto, existem casos em que um único valor pode ter múltiplos proprietários. Por exemplo, em estruturas de dados de grafos, múltiplas arestas podem apontar para o mesmo nó, e esse nó é conceitualmente possuído por todas as arestas que apontam para ele. Um nó não deve ser limpo a menos que não tenha nenhuma aresta apontando para ele e, portanto, não tenha proprietários.

Você deve habilitar a propriedade múltipla explicitamente usando o tipo Rust `Rc<T>`, que é uma abreviação para _contagem de referências_ (reference counting). O tipo `Rc<T>` acompanha o número de referências a um valor para determinar se o valor ainda está em uso. Se houver zero referências a um valor, o valor pode ser limpo sem que nenhuma referência se torne inválida.

Imagine `Rc<T>` como uma TV em uma sala de estar. Quando uma pessoa entra para assistir TV, ela a liga. Outras pessoas podem entrar na sala e assistir à TV. Quando a última pessoa sai da sala, ela desliga a TV porque ela não está mais sendo usada. Se alguém desligar a TV enquanto outros ainda estão assistindo, haveria uma comoção dos telespectadores restantes!

Usamos o tipo `Rc<T>` quando queremos alocar alguns dados no heap (heap) para que várias partes do nosso programa leiam e não podemos determinar em tempo de compilação qual parte terminará de usar os dados por último. Se soubéssemos qual parte terminaria por último, poderíamos simplesmente fazer com que essa parte fosse a proprietária dos dados, e as regras normais de propriedade aplicadas em tempo de compilação entrariam em vigor.

Observe que `Rc<T>` é apenas para uso em cenários de thread único. Quando discutirmos concorrência no Capítulo 16, abordaremos como fazer contagem de referências em programas multithreaded.
