# Resumo

Neste laboratório, você começou a agregar valor criando seus próprios contêineres Docker personalizados.

Principais Conclusões:

- O Dockerfile é como você cria builds reproduzíveis para sua aplicação e como você integra sua aplicação com o Docker no pipeline CI/CD.
- Imagens Docker podem ser disponibilizadas para todos os seus ambientes através de um registro central. O Docker Hub é um exemplo de registro, mas você pode implantar seu próprio registro em servidores que você controla.
- Imagens Docker contêm todas as dependências que precisam para executar uma aplicação dentro da imagem. Isso é útil porque não precisamos mais lidar com a deriva de ambiente (diferenças de versão) quando dependemos de dependências que são instaladas em cada ambiente que implantamos.
- O Docker utiliza o sistema de arquivos de união (union file system) e "copy on write" (cópia sob escrita) para reutilizar camadas de imagens. Isso diminui a pegada de armazenamento de imagens e aumenta significativamente o desempenho da inicialização de contêineres.
- As camadas de imagem são armazenadas em cache pelo sistema de build e push do Docker. Não há necessidade de reconstruir ou reenviar as camadas de imagem que já estão presentes no sistema desejado.
- Cada linha em um Dockerfile cria uma nova camada e, por causa do cache de camadas, as linhas que mudam com mais frequência (por exemplo, adicionar código-fonte a uma imagem) devem ser listadas perto da parte inferior do arquivo.
