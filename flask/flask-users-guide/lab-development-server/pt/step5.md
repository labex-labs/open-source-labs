# Endereço Já em Uso

Se você vir um `OSError` com a mensagem "Address already in use" (Endereço já em uso) ao tentar iniciar o servidor, isso significa que outro programa já está usando a porta 5000, que é a porta padrão para o servidor de desenvolvimento. Você pode identificar e parar o outro programa ou escolher uma porta diferente.

Para identificar o processo que está usando a porta 5000, você pode usar o comando `netstat` ou `lsof`. Aqui estão exemplos para Linux, macOS e Windows:

- Linux:

```bash
netstat -nlp | grep 5000
```

- macOS / Linux:

```bash
lsof -P -i :5000
```

- Windows:

```bash
-ano > netstat | findstr 5000
```

Depois de identificar o processo, você pode usar outras ferramentas do sistema operacional para pará-lo. Após parar o processo, você deverá conseguir executar o servidor de desenvolvimento sem problemas.
