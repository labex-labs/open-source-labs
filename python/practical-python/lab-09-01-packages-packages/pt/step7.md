# Problema: Scripts Principais

Executar um submódulo de pacote como um script principal quebra.

```bash
$ python porty/pcost.py # QUEBRA
...
```

_Razão: Você está executando Python em um único arquivo e Python não vê o restante da estrutura do pacote corretamente (`sys.path` está errado)._

Todos os imports quebram. Para corrigir isso, você precisa executar seu programa de uma maneira diferente, usando a opção `-m`.

```bash
$ python -m porty.pcost # FUNCIONA
...
```
