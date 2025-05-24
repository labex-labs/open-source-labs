# O servidor de desenvolvimento

Vamos verificar se o seu projeto Django funciona. Mude para o diretório `mysite` externo, se ainda não o fez, e execute os seguintes comandos:

```bash
cd ~/project/mysite
python manage.py runserver
```

Você verá a seguinte saída na linha de comando:

```plaintext
Performing system checks...

System check identified no issues (0 silenced).

You have unapplied migrations; your app may not work properly until they are applied. Run 'python manage.py migrate' to apply them.

- 15:50:53 Django version , using settings 'mysite.settings' Starting development server at <http://127.0.0.1:8000/> Quit the server with CONTROL-C.
```

Ignore o aviso sobre migrações de banco de dados não aplicadas por enquanto; lidaremos com o banco de dados em breve.

Você iniciou o servidor de desenvolvimento Django, um servidor web leve escrito puramente em Python. Incluímos isso com o Django para que você possa desenvolver as coisas rapidamente, sem ter que lidar com a configuração de um servidor de produção -- como o Apache -- até que esteja pronto para a produção.

Agora é um bom momento para notar: **não** use este servidor em nada que se assemelhe a um ambiente de produção. Ele se destina apenas ao uso durante o desenvolvimento. (Estamos no negócio de fazer frameworks web, não servidores web.)

Agora que o servidor está em execução, visite <http://127.0.0.1:8000/> com seu navegador web. Ou, execute `curl 127.0.0.1:8000` no terminal. Você verá uma página "Parabéns!", com um foguete decolando. Funcionou!

Na VM LabEx, precisamos adicionar o domínio LabEx a `ALLOWED_HOSTS`. Edite `mysite/settings.py` e adicione `*` ao final de `ALLOWED_HOSTS`, para que fique assim:

```python
ALLOWED_HOSTS = ["*"]
```

Isso informa ao Django que ele pode servir solicitações com qualquer cabeçalho de host.

![Django development server running](../assets/20230907-08-56-33-3uvbOwp3.png)

## Alterando a porta

Por padrão, o comando `runserver` inicia o servidor de desenvolvimento no IP interno na porta 8000.

Se você quiser alterar a porta do servidor, passe-a como um argumento de linha de comando. Por exemplo, este comando inicia o servidor na porta 8080:

```bash
python manage.py runserver 8080
```

Se você quiser alterar o IP do servidor, passe-o junto com a porta. Por exemplo, para ouvir em todos os IPs públicos disponíveis (o que é útil se você estiver executando o Vagrant ou quiser mostrar seu trabalho em outros computadores na rede), use:

```bash
python manage.py runserver 0.0.0.0:8080
```

Agora, mude para a aba **Web 8080** na VM LabEx e você verá a mesma página "Parabéns".

![Django development server page](../assets/20230907-08-58-22-M3Luydxk.png)

A documentação completa para o servidor de desenvolvimento pode ser encontrada na referência `runserver`.

> Recarregamento automático de `runserver`
> O servidor de desenvolvimento recarrega automaticamente o código Python para cada solicitação, conforme necessário. Você não precisa reiniciar o servidor para que as alterações no código entrem em vigor. No entanto, algumas ações, como adicionar arquivos, não acionam uma reinicialização, então você terá que reiniciar o servidor nesses casos.
