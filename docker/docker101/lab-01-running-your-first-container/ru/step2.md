# Запустите свой первый контейнер

Мы будем использовать CLI Docker для запуска нашего первого контейнера.

Откройте терминал на виртуальной машине LabEx.

Запустите команду.

```bash
docker container run -t ubuntu top
```

Используйте команду `docker container run` для запуска контейнера с изображением `ubuntu` с использованием команды `top`. Флаг `-t` выделяет псевдо-ТTY, который нам нужен для правильной работы `top`.

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

Команда `docker run` сначала приведет к выполнению `docker pull` для загрузки образа `ubuntu` на ваш хост. После его загрузки контейнер будет запущен. Вывод для запущенного контейнера должен выглядеть так:

```bash
top - 20:32:46 up 3 days, 17:40,  0 users,  load average: 0.00, 0.01, 0.00
Tasks:   1 total,   1 running,   0 sleeping,   0 stopped,   0 zombie
%Cpu(s):  0.0 us,  0.1 sy,  0.0 ni, 99.9 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
KiB Mem :  2046768 total,   173308 free,   117248 used,  1756212 buff/cache
KiB Swap:  1048572 total,  1048572 free,        0 used.  1548356 avail Mem

PID USER      PR  NI    VIRT    RES    SHR S  %CPU %MEM     TIME+ COMMAND
      1 root      20   0   36636   3072   2640 R   0.3  0.2   0:00.04 top
```

`top` - это утилита Linux, которая выводит процессы на системе и упорядочивает их по потреблению ресурсов. Обратите внимание, что в этом выводе есть только один процесс: это сам процесс `top`. Мы не видим другие процессы с нашего хоста в этом списке из-за изоляции пространства имен PID.

Контейнеры используют пространства имен Linux для обеспечения изоляции системных ресурсов от других контейнеров или хоста. Пространство имен PID обеспечивает изоляцию для идентификаторов процессов. Если вы запустите `top` внутри контейнера, вы заметите, что он показывает процессы внутри пространства имен PID контейнера, что сильно отличается от того, что вы можете увидеть, если бы вы запустили `top` на хосте.

Хотя мы используем образ `ubuntu`, важно помнить, что наш контейнер не имеет собственного ядра. Он использует ядро хоста, а образ `ubuntu` используется только для предоставления файловой системы и инструментов, доступных в системе Ubuntu.

Проверьте контейнер с помощью `docker container exec`

Команда `docker container exec` - это способ "войти" в пространства имен запущенного контейнера с новым процессом.

Откройте новый терминал. Выберите `Terminal` > `New Terminal`.

В новом терминале используйте команду `docker container ls`, чтобы получить идентификатор запущенного контейнера, который вы только что создали.

```bash
$ docker container ls
CONTAINER ID IMAGE COMMAND CREATED STATUS PORTS NAMES
b3ad2a23fab3 ubuntu "top" 29 minutes ago Up 29 minutes goofy_nobel
```

Затем используйте этот идентификатор для запуска `bash` внутри этого контейнера с помощью команды `docker container exec`. Поскольку мы используем `bash` и хотим взаимодействовать с этим контейнером из нашего терминала, используйте флаги `-it` для запуска в интерактивном режиме, выделяя псевдо-Терминал.

```bash
$ docker container exec -it ID < CONTAINER > bash
root@b3ad2a23fab3:/#
```

И вуаля! Мы только что использовали команду `docker container exec`, чтобы "войти" в пространства имен нашего контейнера с процессом `bash`. Использование `docker container exec` с `bash` - это распространенный способ проверить контейнер Docker.

Обратите внимание на изменение префикса в терминале. Например, `root@b3ad2a23fab3:/`. Это означает, что мы запускаем `bash` "внутри" нашего контейнера.

**Примечание**: Это не то же самое, что подключаться по SSH к отдельному хосту или виртуальной машине. Мы не нуждаемся в SSH-сервере для подключения к процессу `bash`. Помните, что контейнеры используют функции уровня ядра для обеспечения изоляции, и контейнеры запускаются поверх ядра. Наш контейнер - это просто группа процессов, работающих в изоляции на том же хосте, и мы можем использовать `docker container exec`, чтобы войти в эту изоляцию с процессом `bash`. После выполнения `docker container exec` группа процессов, работающих в изоляции (то есть наш контейнер), включает `top` и `bash`.

Из того же терминала запустите `ps -ef`, чтобы проверить запущенные процессы.

```bash
root@b3ad2a23fab3:/# ps -ef
UID PID PPID C STIME TTY TIME CMD
root 1 0 0 20:34? 00:00:00 top
root 17 0 0 21:06? 00:00:00 bash
root 27 17 0 21:14? 00:00:00 ps -ef
```

Вы должны увидеть только процесс `top`, процесс `bash` и наш процесс `ps`.

Для сравнения выйдите из контейнера и запустите `ps -ef` или `top` на хосте. Эти команды будут работать на Linux или Mac. Для Windows вы можете проверить запущенные процессы с помощью `tasklist`.

```bash
root@b3ad2a23fab3:/# exit
exit
$ ps -ef
# Lots of processes!
```

_Техническое углубление_
PID - это только одно из пространств имен Linux, которое обеспечивает контейнерам изоляцию системных ресурсов. Другие пространства имен Linux включают:

- MNT - Монтировать и демонтировать директории без влияния на другие пространства имен
- NET - Контейнеры имеют свою собственную сеть
- IPC - Изолированные механизмы межпроцессного взаимодействия, такие как очередь сообщений.
- User - Изолированное представление пользователей на системе
- UTC - Устанавливать имя хоста и доменное имя для каждого контейнера

Эти пространства имен вместе обеспечивают изоляцию для контейнеров, которая позволяет им безопасно работать вместе и не конфликтовать с другими контейнерами, запускающимися на том же системном узле. Далее мы покажем разные применения контейнеров и преимущество изоляции при запуске нескольких контейнеров на одном и том же хосте.

**Примечание**: Пространства имен - это функция **Linux**-ядра. Но Docker позволяет запускать контейнеры на Windows и Mac... как это работает? Секрет заключается в том, что встроенный в продукт Docker или Docker-engines подсистема Linux. Docker открыл исходный код этой подсистемы Linux в новый проект: [LinuxKit](https://github.com/linuxkit/linuxkit). Возможность запускать контейнеры на многих разных платформах - это один из преимуществ использования инструментов Docker с контейнерами.

Кроме того, за счет создания примитивов контейнеров в операционной системе Windows теперь возможны нативные контейнеры Windows. Нативные контейнеры Windows можно запускать на Windows 10 или Windows Server 2016 или новее.

**Примечание**: Если вы выполняете это упражнение в контейнеризованном терминале и выполняете команду `ps -ef` в терминале, вы по-прежнему увидите ограниченный набор процессов после выхода из команды `exec`. Вы можете попробовать выполнить команду `ps -ef` в терминале на вашем локальном компьютере, чтобы увидеть все процессы.

Очистите контейнер, запускающий процессы `top`, нажав: `<ctrl>-c`, выведите список всех контейнеров и удалите контейнеры по их идентификатору.

```bash
docker ps -a

docker rm <CONTAINER ID>
```
