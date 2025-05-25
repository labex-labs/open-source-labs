# Introdução

Neste laboratório, aprendemos sobre a palavra-chave `while`, que é usada para criar um loop que continua a executar enquanto uma condição especificada for verdadeira. Para ilustrar seu uso, escrevemos um programa em Rust chamado FizzBuzz. O programa usa um loop `while` para iterar pelos números de 1 a 100. Dentro do loop, verifica se o número atual é divisível por 3 e 5 (ou seja, um múltiplo de 15) e imprime "fizzbuzz" nesses casos. Se o número for apenas divisível por 3, imprime "fizz", e se for apenas divisível por 5, imprime "buzz". Para todos os outros números, simplesmente imprime o próprio número. O loop continua até que a variável contadora alcance 101, incrementando-a após imprimir cada número ou rótulo.

> **Nota:** Se o laboratório não especificar um nome de arquivo, você pode usar qualquer nome de arquivo que desejar. Por exemplo, você pode usar `main.rs`, compilar e executá-lo com `rustc main.rs && ./main`.
