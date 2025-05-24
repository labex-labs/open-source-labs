# Execute Seu Primeiro Contêiner

Vamos usar a CLI do Docker para executar nosso primeiro contêiner.

Abra um terminal na VM do LabEx.

Execute o comando.

```bash
docker container run -t ubuntu top
```

Use o comando `docker container run` para executar um contêiner com a imagem `ubuntu` usando o comando `top`. As flags `-t` alocam um pseudo-TTY, que precisamos para que o `top` funcione corretamente.

```bash
$ docker container run -it ubuntu top
Unable to find image 'ubuntu:latest' locally
latest: Pulling from library/ubuntu
aafe6b5e13de: Pull complete
0a2b43a72660: Pull complete
18bdd1e546d2: Pull complete
8198342c3e05: Pull complete
f56970a44fd4: Pull complete
Digest: sha256:f3a61450ae43896c4332bda5e78b453f4a93179045f20c8181043b26b5e79028
Status: Downloaded newer image for ubuntu:latest
```

O comando `docker run` resultará primeiro em um `docker pull` para baixar a imagem ubuntu para o seu host. Depois de baixada, ele iniciará o contêiner. A saída para o contêiner em execução deve ser semelhante a esta:

```bash
top - 20:32:46 up 3 days, 17:40,  0 users,  load average: 0.00, 0.01, 0.00
Tasks:   1 total,   1 running,   0 sleeping,   0 stopped,   0 zombie
%Cpu(s):  0.0 us,  0.1 sy,  0.0 ni, 99.9 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
KiB Mem :  2046768 total,   173308 free,   117248 used,  1756212 buff/cache
KiB Swap:  1048572 total,  1048572 free,        0 used.  1548356 avail Mem

PID USER      PR  NI    VIRT    RES    SHR S  %CPU %MEM     TIME+ COMMAND
      1 root      20   0   36636   3072   2640 R   0.3  0.2   0:00.04 top
```

`top` é um utilitário linux que imprime os processos em um sistema e os ordena por consumo de recursos. Observe que há apenas um único processo nesta saída: é o próprio processo `top`. Não vemos outros processos do nosso host nesta lista por causa do isolamento do namespace PID.

Contêineres usam namespaces Linux para fornecer isolamento de recursos do sistema de outros contêineres ou do host. O namespace PID fornece isolamento para IDs de processo. Se você executar `top` dentro do contêiner, notará que ele mostra os processos dentro do namespace PID do contêiner, que é muito diferente do que você pode ver se executasse `top` no host.

Embora estejamos usando a imagem `ubuntu`, é importante notar que nosso contêiner não tem seu próprio kernel. Ele usa o kernel do host e a imagem `ubuntu` é usada apenas para fornecer o sistema de arquivos e as ferramentas disponíveis em um sistema ubuntu.

Inspecione o contêiner com `docker container exec`

O comando `docker container exec` é uma maneira de "entrar" nos namespaces de um contêiner em execução com um novo processo.

Abra um novo terminal. selecione `Terminal` > `New Terminal`.

No novo terminal, use o comando `docker container ls` para obter o ID do contêiner em execução que você acabou de criar.

```bash
$ docker container ls
CONTAINER ID IMAGE COMMAND CREATED STATUS PORTS NAMES
b3ad2a23fab3 ubuntu "top" 29 minutes ago Up 29 minutes goofy_nobel
```

Em seguida, use esse ID para executar `bash` dentro desse contêiner usando o comando `docker container exec`. Como estamos usando bash e queremos interagir com este contêiner do nosso terminal, use as flags `-it` para executar no modo interativo enquanto aloca um psuedo-terminal.

```bash
$ docker container exec -it ID < CONTAINER > bash
root@b3ad2a23fab3:/#
```

E Voilá! Acabamos de usar o comando `docker container exec` para "entrar" nos namespaces do nosso contêiner com nosso processo bash. Usar `docker container exec` com `bash` é um padrão comum para inspecionar um contêiner Docker.

Observe a mudança no prefixo do seu terminal. Ex. `root@b3ad2a23fab3:/`. Esta é uma indicação de que estamos executando bash "dentro" do nosso contêiner.

**Observação**: Isso não é o mesmo que fazer ssh em um host separado ou em uma VM. Não precisamos de um servidor ssh para nos conectar com um processo bash. Lembre-se de que os contêineres usam recursos de nível de kernel para obter isolamento e que os contêineres são executados em cima do kernel. Nosso contêiner é apenas um grupo de processos em execução em isolamento no mesmo host, e podemos usar `docker container exec` para entrar nesse isolamento com o processo `bash`. Após executar `docker container exec`, o grupo de processos em execução em isolamento (ou seja, nosso contêiner) inclui `top` e `bash`.

Do mesmo terminal, execute `ps -ef` para inspecionar os processos em execução.

```bash
root@b3ad2a23fab3:/# ps -ef
UID PID PPID C STIME TTY TIME CMD
root 1 0 0 20:34 ? 00:00:00 top
root 17 0 0 21:06 ? 00:00:00 bash
root 27 17 0 21:14 ? 00:00:00 ps -ef
```

Você deve ver apenas o processo `top`, o processo `bash` e nosso processo `ps`.

Para comparação, saia do contêiner e execute `ps -ef` ou `top` no host. Esses comandos funcionarão no linux ou mac. Para Windows, você pode inspecionar os processos em execução usando `tasklist`.

```bash
root@b3ad2a23fab3:/# exit
exit
$ ps -ef
# Lots of processes!
```

_Análise Técnica Detalhada_
PID é apenas um dos namespaces Linux que fornece aos contêineres isolamento de recursos do sistema. Outros namespaces Linux incluem:

- MNT - Montar e desmontar diretórios sem afetar outros namespaces
- NET - Contêineres têm sua própria pilha de rede
- IPC - Mecanismos de comunicação entre processos isolados, como filas de mensagens.
- User - Visão isolada dos usuários no sistema
- UTC - Definir nome de host e nome de domínio por contêiner

Esses namespaces juntos fornecem o isolamento para contêineres que lhes permite executar juntos com segurança e sem conflito com outros contêineres em execução no mesmo sistema. Em seguida, demonstraremos diferentes usos de contêineres e o benefício do isolamento ao executarmos vários contêineres no mesmo host.

**Observação**: Namespaces são um recurso do kernel **linux**. Mas o Docker permite que você execute contêineres no Windows e Mac... como isso funciona? O segredo é que embutido no produto Docker ou no mecanismo Docker está um subsistema linux. O Docker abriu o código-fonte desse subsistema linux para um novo projeto: [LinuxKit](https://github.com/linuxkit/linuxkit). Ser capaz de executar contêineres em muitas plataformas diferentes é uma vantagem de usar as ferramentas Docker com contêineres.

Além de executar contêineres linux no Windows usando um subsistema linux, contêineres nativos do Windows agora são possíveis devido à criação de primitivas de contêiner no sistema operacional Windows. Contêineres nativos do Windows podem ser executados no Windows 10 ou Windows Server 2016 ou posterior.

**Observação**: se você executar este exercício em um terminal em contêiner e executar o comando `ps -ef` no terminal, ainda verá um conjunto limitado de processos após sair do comando `exec`. Você pode tentar executar o comando `ps -ef` em um terminal em sua máquina local para ver todos os processos.

Limpe o contêiner executando os processos `top` digitando: `<ctrl>-c`, liste todos os contêineres e remova os contêineres por seu ID.

```bash
docker ps -a

docker rm <CONTAINER ID>
```
