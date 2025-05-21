# Explorando o Dicionário Interno de Objetos

Em Python, objetos são um conceito fundamental. Um objeto pode ser pensado como um contêiner que armazena dados e possui certos comportamentos. Um dos aspectos interessantes dos objetos Python é como eles armazenam seus atributos. Atributos são como variáveis que pertencem a um objeto. Python armazena esses atributos em um dicionário especial, que pode ser acessado através do atributo `__dict__`. Este dicionário é uma parte interna do objeto e é onde o Python acompanha todos os dados associados a esse objeto.

Vamos dar uma olhada mais de perto nessa estrutura interna usando nossas instâncias `SimpleStock`. Em Python, uma instância é um objeto individual criado a partir de uma classe. Por exemplo, se `SimpleStock` é uma classe, `goog` e `ibm` são instâncias dessa classe.

Para ver o dicionário interno dessas instâncias, podemos usar o shell interativo do Python. O shell interativo do Python é uma ótima ferramenta para testar rapidamente o código e ver os resultados. No shell interativo do Python, digite os seguintes comandos para inspecionar o atributo `__dict__` de nossas instâncias:

```python
>>> goog.__dict__
{'name': 'GOOG', 'shares': 100, 'price': 490.1}
>>> ibm.__dict__
{'name': 'IBM', 'shares': 50, 'price': 91.23}
```

Quando você executa esses comandos, a saída mostra que cada instância tem seu próprio dicionário interno. Este dicionário contém todos os atributos da instância. Por exemplo, na instância `goog`, os atributos `name`, `shares` e `price` são armazenados no dicionário com seus valores correspondentes. É assim que o Python implementa os atributos do objeto nos bastidores. Cada objeto tem um dicionário privado que contém todos os seus atributos.

É importante entender o que o atributo `__dict__` revela sobre a implementação interna de nossos objetos:

1. As chaves no dicionário correspondem aos nomes dos atributos. Por exemplo, na instância `goog`, a chave `'name'` corresponde ao atributo `name` do objeto.
2. Os valores no dicionário são os valores dos atributos. Portanto, o valor `'GOOG'` é o valor do atributo `name` para a instância `goog`.
3. Cada instância tem seu próprio `__dict__` separado. Isso significa que os atributos de uma instância são independentes dos atributos de outra instância. Por exemplo, o atributo `shares` da instância `goog` pode ser diferente do atributo `shares` da instância `ibm`.

Essa abordagem baseada em dicionário permite que o Python seja muito flexível com objetos. Como veremos na próxima etapa, podemos usar essa flexibilidade para modificar e acessar atributos de objetos de várias maneiras.
