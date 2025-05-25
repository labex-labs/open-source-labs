# Módulo `itertools`

O `itertools` é um módulo de biblioteca com várias funções projetadas para auxiliar com iteradores/geradores.

```python
itertools.chain(s1,s2)
itertools.count(n)
itertools.cycle(s)
itertools.dropwhile(predicate, s)
itertools.groupby(s)
itertools.ifilter(predicate, s)
itertools.imap(function, s1, ... sN)
itertools.repeat(s, n)
itertools.tee(s, ncopies)
itertools.izip(s1, ... , sN)
```

Todas as funções processam dados iterativamente. Elas implementam vários tipos de padrões de iteração.

Mais informações no tutorial [Generator Tricks for Systems Programmers](http://www.dabeaz.com/generators/) da PyCon '08.

Nos exercícios anteriores, você escreveu algum código que acompanhava as linhas sendo escritas em um arquivo de log e as analisava em uma sequência de linhas. Este exercício continua a se basear nisso. Certifique-se de que o `stocksim.py` ainda está em execução.
