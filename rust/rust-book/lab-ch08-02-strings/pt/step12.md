# Strings Não São Tão Simples

Em resumo, strings são complicadas. Diferentes linguagens de programação fazem escolhas diferentes sobre como apresentar essa complexidade ao programador. Rust escolheu tornar o tratamento correto de dados `String` o comportamento padrão para todos os programas Rust, o que significa que os programadores precisam pensar mais em lidar com dados UTF-8 desde o início. Essa troca expõe mais da complexidade das strings do que é aparente em outras linguagens de programação, mas impede que você tenha que lidar com erros envolvendo caracteres não-ASCII mais tarde em seu ciclo de vida de desenvolvimento.

A boa notícia é que a biblioteca padrão oferece muita funcionalidade construída a partir dos tipos `String` e `&str` para ajudar a lidar com essas situações complexas corretamente. Certifique-se de verificar a documentação para métodos úteis como `contains` para pesquisar em uma string e `replace` para substituir partes de uma string por outra string.

Vamos mudar para algo um pouco menos complexo: mapas de hash (hash maps)!
