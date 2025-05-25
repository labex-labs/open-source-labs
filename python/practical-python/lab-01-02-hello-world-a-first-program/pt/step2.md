# Modo Interativo

Quando você inicia o Python, você obtém um modo _interativo_ onde pode experimentar.

Se você começar a digitar instruções, elas serão executadas imediatamente. Não há ciclo de edição/compilação/execução/depuração (edit/compile/run/debug).

```python
>>> print('hello world')
hello world
>>> 37*42
1554
>>> for i in range(5):
...     print(i)
...
0
1
2
3
4
>>>
```

Este chamado _read-eval-print-loop_ (ou REPL) é muito útil para depuração e exploração.

**PARE**: Se você não conseguir descobrir como interagir com o Python, pare o que está fazendo e descubra como fazê-lo. Se você estiver usando uma IDE, ela pode estar escondida atrás de uma opção de menu ou outra janela. Muitas partes deste curso assumem que você pode interagir com o interpretador.

Vamos dar uma olhada mais de perto nos elementos do REPL:

- `>>>` é o prompt do interpretador para iniciar uma nova instrução.
- `...` é o prompt do interpretador para continuar uma instrução. Insira uma linha em branco para terminar a digitação e executar o que você digitou.

O prompt `...` pode ou não ser exibido, dependendo do seu ambiente. Para este curso, ele é mostrado como espaços em branco para facilitar o corte/colagem de exemplos de código.

O sublinhado `_` armazena o último resultado.

```python
>>> 37 * 42
1554
>>> _ * 2
3108
>>> _ + 50
3158
>>>
```

_Isso só é verdade no modo interativo._ Você nunca usa `_` em um programa.
