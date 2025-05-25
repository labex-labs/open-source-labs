# Escrevendo Código para Passar no Teste

Atualmente, nosso teste está falhando porque sempre retornamos um vetor vazio. Para corrigir isso e implementar `search`, nosso programa precisa seguir estas etapas:

1.  Iterar por cada linha do conteúdo.
2.  Verificar se a linha contém nossa string de consulta.
3.  Se contiver, adicione-a à lista de valores que estamos retornando.
4.  Se não contiver, não faça nada.
5.  Retornar a lista de resultados que correspondem.

Vamos trabalhar em cada etapa, começando com a iteração pelas linhas.
