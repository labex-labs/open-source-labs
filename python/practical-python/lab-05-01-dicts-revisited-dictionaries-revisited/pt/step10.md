# Lendo Atributos com Herança

Logicamente, o processo de encontrar um atributo é o seguinte. Primeiro, verifique no `__dict__` local. Se não for encontrado, procure em `__dict__` da classe. Se não for encontrado na classe, procure nas classes base através de `__bases__`. No entanto, existem alguns aspectos sutis disso que serão discutidos a seguir.
