# Encapsulamento que Oculta Detalhes de Implementação

Outro aspecto comumente associado à OOP é a ideia de _encapsulamento_, o que significa que os detalhes de implementação de um objeto não são acessíveis ao código que usa esse objeto. Portanto, a única maneira de interagir com um objeto é através de sua API pública; o código que usa o objeto não deve ser capaz de acessar os detalhes internos do objeto e alterar dados ou comportamento diretamente. Isso permite que o programador altere e refatore os detalhes internos de um objeto sem precisar alterar o código que usa o objeto.

Discutimos como controlar o encapsulamento no Capítulo 7: podemos usar a palavra-chave `pub` para decidir quais módulos, tipos, funções e métodos em nosso código devem ser públicos, e por padrão todo o resto é privado. Por exemplo, podemos definir uma struct `AveragedCollection` que possui um campo contendo um vetor de valores `i32`. A struct também pode ter um campo que contém a média dos valores no vetor, o que significa que a média não precisa ser calculada sob demanda sempre que alguém precisar dela. Em outras palavras, `AveragedCollection` irá armazenar em cache a média calculada para nós. A Listagem 17-1 tem a definição da struct `AveragedCollection`.

Nome do arquivo: `src/lib.rs`

```rust
pub struct AveragedCollection {
    list: Vec<i32>,
    average: f64,
}
```

Listagem 17-1: Uma struct `AveragedCollection` que mantém uma lista de inteiros e a média dos itens na coleção

A struct é marcada como `pub` para que outro código possa usá-la, mas os campos dentro da struct permanecem privados. Isso é importante neste caso porque queremos garantir que sempre que um valor for adicionado ou removido da lista, a média também seja atualizada. Fazemos isso implementando os métodos `add`, `remove` e `average` na struct, conforme mostrado na Listagem 17-2.

Nome do arquivo: `src/lib.rs`

```rust
impl AveragedCollection {
    pub fn add(&mut self, value: i32) {
        self.list.push(value);
        self.update_average();
    }

    pub fn remove(&mut self) -> Option<i32> {
        let result = self.list.pop();
        match result {
            Some(value) => {
                self.update_average();
                Some(value)
            }
            None => None,
        }
    }

    pub fn average(&self) -> f64 {
        self.average
    }

    fn update_average(&mut self) {
        let total: i32 = self.list.iter().sum();
        self.average = total as f64 / self.list.len() as f64;
    }
}
```

Listagem 17-2: Implementações dos métodos públicos `add`, `remove` e `average` em `AveragedCollection`

Os métodos públicos `add`, `remove` e `average` são as únicas maneiras de acessar ou modificar dados em uma instância de `AveragedCollection`. Quando um item é adicionado à `list` usando o método `add` ou removido usando o método `remove`, as implementações de cada um chamam o método privado `update_average` que lida com a atualização do campo `average` também.

Deixamos os campos `list` e `average` privados para que não haja como o código externo adicionar ou remover itens para ou da campo `list` diretamente; caso contrário, o campo `average` pode ficar fora de sincronia quando a `list` muda. O método `average` retorna o valor no campo `average`, permitindo que o código externo leia a `average`, mas não a modifique.

Como encapsulamos os detalhes de implementação da struct `AveragedCollection`, podemos facilmente alterar aspectos, como a estrutura de dados, no futuro. Por exemplo, poderíamos usar um `HashSet<i32>` em vez de um `Vec<i32>` para o campo `list`. Contanto que as assinaturas dos métodos públicos `add`, `remove` e `average` permanecessem as mesmas, o código que usa `AveragedCollection` não precisaria ser alterado. Se tornássemos `list` público, isso não seria necessariamente o caso: `HashSet<i32>` e `Vec<i32>` têm métodos diferentes para adicionar e remover itens, então o código externo provavelmente teria que mudar se estivesse modificando `list` diretamente.

Se o encapsulamento é um aspecto obrigatório para que uma linguagem seja considerada orientada a objetos, então Rust atende a esse requisito. A opção de usar `pub` ou não para diferentes partes do código permite o encapsulamento de detalhes de implementação.
