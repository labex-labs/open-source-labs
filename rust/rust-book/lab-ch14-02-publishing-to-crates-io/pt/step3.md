# Seções Comumente Usadas

Usamos o título Markdown `# Exemplos` na Listagem 14-1 para criar uma seção no HTML com o título "Exemplos". Aqui estão algumas outras seções que os autores de crates comumente usam em sua documentação:

- **Panics** (Pânicos): Os cenários em que a função que está sendo documentada pode entrar em pânico. Os chamadores da função que não querem que seus programas entrem em pânico devem garantir que não chamem a função nessas situações.
- **Errors** (Erros): Se a função retornar um `Result`, descrever os tipos de erros que podem ocorrer e quais condições podem fazer com que esses erros sejam retornados pode ser útil para os chamadores, para que eles possam escrever código para lidar com os diferentes tipos de erros de maneiras diferentes.
- **Safety** (Segurança): Se a função for `unsafe` para chamar (discutimos a insegurança no Capítulo 19), deve haver uma seção explicando por que a função é insegura e cobrindo os invariantes que a função espera que os chamadores mantenham.

A maioria dos comentários de documentação não precisa de todas essas seções, mas esta é uma boa lista de verificação para lembrá-lo dos aspectos do seu código que os usuários estarão interessados em saber.
