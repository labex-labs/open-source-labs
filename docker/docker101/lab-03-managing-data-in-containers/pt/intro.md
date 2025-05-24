# Introdução

Por padrão, todos os arquivos criados dentro de um container são armazenados em uma camada de container gravável. Isso significa que:

- Se o container não existir mais, os dados são perdidos,
- A camada gravável do container está intimamente ligada à máquina host, e
- Para gerenciar o sistema de arquivos, você precisa de um driver de armazenamento que forneça um sistema de arquivos de união (union file system), usando o kernel Linux. Essa abstração extra reduz o desempenho em comparação com os `volumes de dados` (data volumes), que escrevem diretamente no sistema de arquivos.

O Docker oferece duas opções para armazenar arquivos na máquina host: `volumes` e `bind mounts`. Se você estiver executando o Docker no Linux, também pode usar um `tmpfs mount`, e com o Docker no Windows, você também pode usar um `named pipe`.

![Tipos de Mounts](../assets/types-of-mounts.png)

- `Volumes` são armazenados no sistema de arquivos host que é gerenciado pelo Docker.
- `Bind mounts` são armazenados em qualquer lugar no sistema host.
- `tmpfs mounts` são armazenados apenas na memória host.

Originalmente, a flag `--mount` era usada para serviços Docker Swarm e a flag `--volume` era usada para containers standalone. A partir do Docker 17.06 e superior, você também pode usar `--mount` para containers standalone e, em geral, é mais explícito e verboso do que `--volume`.
