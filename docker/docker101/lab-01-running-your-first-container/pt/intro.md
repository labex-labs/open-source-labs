# Introdução

Neste laboratório, você executará seu primeiro contêiner Docker.

Contêineres são apenas um processo (ou um grupo de processos) executando em isolamento. O isolamento é alcançado por meio de namespaces Linux, grupos de controle (cgroups), seccomp e SELinux. Observe que os namespaces Linux e os grupos de controle são integrados ao kernel Linux! Além do próprio kernel Linux, não há nada de especial sobre contêineres.

O que torna os contêineres úteis são as ferramentas que os cercam. Para estes laboratórios, usaremos o Docker, que tem sido uma ferramenta amplamente adotada para usar contêineres para construir aplicações. O Docker fornece aos desenvolvedores e operadores uma interface amigável para construir, enviar e executar contêineres em qualquer ambiente com um mecanismo Docker. Como o cliente Docker requer um mecanismo Docker, uma alternativa é usar o [Podman](https://podman.io/), que é um mecanismo de contêiner sem daemon para desenvolver, gerenciar e executar contêineres [OCI](https://opencontainers.org/) e é capaz de executar contêineres como root ou no modo rootless. Por essas razões, recomendamos o Podman, mas devido à adoção, este laboratório ainda usa o Docker.

Na primeira parte deste laboratório, executaremos nosso primeiro contêiner e aprenderemos como inspecioná-lo. Poderemos testemunhar o isolamento de namespace que adquirimos do kernel Linux.

Depois de executarmos nosso primeiro contêiner, mergulharemos em outros usos de contêineres. Você pode encontrar muitos exemplos disso na Docker Store, e executaremos vários tipos diferentes de contêineres no mesmo host. Isso nos permitirá ver o benefício do isolamento - onde podemos executar vários contêineres no mesmo host sem conflitos.

Usaremos alguns comandos Docker neste laboratório. Para obter a documentação completa sobre os comandos disponíveis, consulte a [documentação oficial](https://docs.docker.com/).

<div class="text-xs text-gray-500 dark:text-gray-400 mt-4 border-t border-l-2 border-gray-300 dark:border-gray-600 pt-2 pl-4">
Este é um Lab Guiado, que fornece instruções passo a passo para ajudá-lo a aprender e praticar. Siga as instruções cuidadosamente para completar cada etapa e ganhar experiência prática. Dados históricos mostram que este é um laboratório de nível <span class="text-green-600 dark:text-green-400">iniciante</span> com uma taxa de conclusão de <span class="text-green-600 dark:text-green-400">89%</span>. Recebeu uma taxa de avaliações positivas de <span class="text-primary-600 dark:text-primary-400">92%</span> dos estudantes.
</div>
