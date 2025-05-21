# Experimentação Interativa

Python oferece um modo interativo que permite executar código imediatamente. Isso é super útil para testar seu código e experimentar coisas novas. Nesta etapa, aprenderemos como chamar uma função diretamente do interpretador Python.

## Executando Python no Modo Interativo

Para executar um script Python e, em seguida, entrar no modo interativo, você pode usar a flag `-i`. Essa flag informa ao Python para continuar sendo executado em um estado interativo após a execução do script. Veja como você faz isso:

```bash
cd /home/labex/project
python3 -i pcost.py
```

Vamos detalhar o que este comando faz:

1.  Primeiro, `cd /home/labex/project` altera o diretório atual para `/home/labex/project`. É aqui que nosso script `pcost.py` está localizado.
2.  Em seguida, `python3 -i pcost.py` executa o script `pcost.py`. Após a conclusão da execução do script, o Python permanece no modo interativo.
3.  No modo interativo, você pode digitar comandos Python diretamente no terminal.

Após executar o comando, você verá a saída do script `pcost.py`, seguido pelo prompt do Python (`>>>`). Este prompt indica que você agora pode inserir comandos Python.

## Chamando Sua Função Interativamente

Depois de estar no modo interativo, você pode chamar a função `portfolio_cost()` com diferentes nomes de arquivos. Isso permite que você veja como a função se comporta com várias entradas. Aqui está um exemplo:

```python
>>> portfolio_cost('/home/labex/project/portfolio.dat')
44671.15
>>> portfolio_cost('/home/labex/project/portfolio2.dat')
19908.75
>>> portfolio_cost('/home/labex/project/portfolio3.dat')
Couldn't parse: 'C - 53.08
'
Reason: invalid literal for int() with base 10: '-'
Couldn't parse: 'DIS - 34.20
'
Reason: invalid literal for int() with base 10: '-'
44671.15
```

Usando essa abordagem interativa, você pode:

- Testar sua função com diferentes entradas para ver se ela funciona como esperado.
- Experimentar o comportamento da função em várias condições.
- Depurar seu código em tempo real, vendo os resultados imediatos de suas chamadas de função.

## Benefícios do Modo Interativo

O modo interativo tem vários benefícios:

1.  Você pode testar rapidamente diferentes cenários sem ter que executar o script inteiro toda vez.
2.  Você pode inspecionar variáveis e resultados de expressões imediatamente, o que ajuda a entender o que está acontecendo em seu código.
3.  Você pode testar pequenos pedaços de código sem criar um programa completo. Isso é ótimo para aprender e experimentar novas ideias.
4.  É uma excelente maneira de aprender e experimentar com Python porque você recebe feedback instantâneo.

## Saindo do Modo Interativo

Quando terminar de experimentar, você pode sair do modo interativo de duas maneiras:

- Digite `exit()` e pressione Enter. Esta é uma maneira direta de encerrar a sessão interativa.
- Pressione Ctrl+D (no Unix/Linux). Este é um atalho que também sai do modo interativo.

Ao longo de sua jornada de programação em Python, a técnica de definir funções e testá-las interativamente será extremamente valiosa para desenvolvimento e depuração. Ele permite que você itere rapidamente em seu código e encontre e corrija problemas.
