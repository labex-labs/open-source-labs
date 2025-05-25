# Compreendendo Cópias e Visualizações (Views)

Arrays NumPy consistem em duas partes: o buffer de dados e os metadados. O buffer de dados contém os elementos de dados reais, enquanto os metadados incluem informações como o tipo de dados e os _strides_ (passos).

Ao operar em arrays NumPy, é importante entender a diferença entre cópias e visualizações:

- Uma **visualização (view)** permite que você acesse o array de forma diferente, alterando certos metadados sem alterar o buffer de dados. Quaisquer alterações feitas em uma visualização serão refletidas no array original.

- Uma **cópia (copy)** é um novo array que duplica tanto o buffer de dados quanto os metadados. As alterações feitas em uma cópia não afetarão o array original.
