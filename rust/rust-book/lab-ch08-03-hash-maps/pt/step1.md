# Armazenando Chaves com Valores Associados em Hash Maps

A última das nossas coleções comuns é o _hash map_ (mapa de hash). O tipo `HashMap<K, V>` armazena um mapeamento de chaves do tipo `K` para valores do tipo `V` usando uma _função de hashing_ (função de hash), que determina como ele coloca essas chaves e valores na memória. Muitas linguagens de programação suportam este tipo de estrutura de dados, mas frequentemente usam um nome diferente, como _hash_, _map_, _object_, _hash table_ (tabela de hash), _dictionary_ (dicionário) ou _associative array_ (array associativo), só para citar alguns.

Hash maps são úteis quando você quer procurar dados não usando um índice, como pode fazer com vetores, mas usando uma chave que pode ser de qualquer tipo. Por exemplo, em um jogo, você pode manter o controle da pontuação de cada equipe em um hash map, no qual cada chave é o nome da equipe e os valores são a pontuação de cada equipe. Dado o nome de uma equipe, você pode recuperar sua pontuação.

Vamos analisar a API básica de hash maps nesta seção, mas muitas outras coisas boas estão escondidas nas funções definidas em `HashMap<K, V>` pela biblioteca padrão. Como sempre, verifique a documentação da biblioteca padrão para mais informações.
