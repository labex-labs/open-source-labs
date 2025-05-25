# Organização de Testes

Como mencionado no início do capítulo, testes são uma disciplina complexa, e diferentes pessoas usam diferentes terminologias e organizações. A comunidade Rust pensa sobre testes em termos de duas categorias principais: testes unitários (unit tests) e testes de integração (integration tests). _Testes unitários_ são pequenos e mais focados, testando um módulo em isolamento por vez, e podem testar interfaces privadas. _Testes de integração_ são inteiramente externos à sua biblioteca e usam seu código da mesma forma que qualquer outro código externo faria, usando apenas a interface pública e potencialmente exercitando múltiplos módulos por teste.

Escrever ambos os tipos de testes é importante para garantir que as partes da sua biblioteca estão fazendo o que você espera que façam, separadamente e em conjunto.
