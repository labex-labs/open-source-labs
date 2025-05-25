# Caminho de Busca de Módulos

Como observado, `sys.path` contém os caminhos de busca. Você pode ajustar manualmente se precisar.

```python
import sys
sys.path.append('/project/foo/pyfiles')
```

Os caminhos também podem ser adicionados via variáveis de ambiente.

```python
% env PYTHONPATH=/project/foo/pyfiles python3
Python 3.6.0 (default, Feb 3 2017, 05:53:21)
[GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.38)]
>>> import sys
>>> sys.path
['','/project/foo/pyfiles', ...]
```

Como regra geral, não deve ser necessário ajustar manualmente o caminho de busca de módulos. No entanto, isso às vezes surge se você estiver tentando importar código Python que está em um local incomum ou não é facilmente acessível a partir do diretório de trabalho atual.

Para este exercício envolvendo módulos, é fundamental garantir que você esteja executando o Python em um ambiente adequado. Módulos frequentemente apresentam aos novos programadores problemas relacionados ao diretório de trabalho atual ou às configurações de caminho do Python. Para este curso, presume-se que você está escrevendo todo o seu código no diretório `~/project`. Para obter os melhores resultados, você deve garantir que também está nesse diretório ao iniciar o interpretador. Caso contrário, você precisa garantir que `~/project` seja adicionado a `sys.path`.
