# Usando o Padrão Newtype para Segurança de Tipos e Abstração

> Nota: Esta seção assume que você leu a seção anterior "Usando o Padrão Newtype para Implementar Traits Externos".

O padrão newtype também é útil para tarefas além daquelas que discutimos até agora, incluindo a imposição estática de que os valores nunca sejam confundidos e a indicação das unidades de um valor. Você viu um exemplo de uso de newtypes para indicar unidades na Listagem 19-15: lembre-se que as structs `Millimeters` e `Meters` encapsulavam valores `u32` em um newtype. Se escrevêssemos uma função com um parâmetro do tipo `Millimeters`, não conseguiríamos compilar um programa que acidentalmente tentasse chamar essa função com um valor do tipo `Meters` ou um simples `u32`.

Também podemos usar o padrão newtype para abstrair alguns detalhes de implementação de um tipo: o novo tipo pode expor uma API pública que é diferente da API do tipo interno privado.

Newtypes também podem ocultar a implementação interna. Por exemplo, poderíamos fornecer um tipo `People` para encapsular um `HashMap<i32, String>` que armazena o ID de uma pessoa associado ao seu nome. O código que usa `People` só interagiria com a API pública que fornecemos, como um método para adicionar uma string de nome à coleção `People`; esse código não precisaria saber que atribuímos um ID `i32` aos nomes internamente. O padrão newtype é uma maneira leve de alcançar a encapsulação para ocultar detalhes de implementação, o que discutimos em "Encapsulamento que Oculta Detalhes de Implementação".
