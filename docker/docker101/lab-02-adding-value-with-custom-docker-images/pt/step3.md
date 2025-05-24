# Executar a Imagem Docker

Agora que você construiu a imagem, pode executá-la para ver se ela funciona.

Execute a imagem Docker

```bash
docker run -p 5001:5000 -d python-hello-world
```

A flag `-p` mapeia uma porta em execução dentro do container para seu host. Neste caso, estamos mapeando o aplicativo python em execução na porta 5000 dentro do container para a porta 5001 em seu host. Observe que, se a porta 5001 já estiver em uso por outro aplicativo em seu host, você pode precisar substituir 5001 por outro valor, como 5002.

Navegue até a aba **PORTS** na janela do terminal e clique no link para abrir o aplicativo em uma nova aba do navegador.

![Terminal ports tab link](../assets/20230829-13-59-19-e8dZe3aN.png)

Em um terminal, execute `curl localhost:5001`, que retorna `hello world!`.

Verifique a saída de log do container.

Se você quiser ver os logs do seu aplicativo, pode usar o comando `docker container logs`. Por padrão, `docker container logs` imprime o que é enviado para a saída padrão pelo seu aplicativo. Use `docker container ls` para encontrar o ID do seu container em execução.

```bash
labex:project/ $ docker container ls
CONTAINER ID   IMAGE                COMMAND           CREATED         STATUS         PORTS                                       NAMES
52df977e5541   python-hello-world   "python app.py"   2 minutes ago   Up 2 minutes   0.0.0.0:5001->5000/tcp, :::5001->5000/tcp   heuristic_lamport
labex:project/ $ docker container logs 52df977e5541
 * Serving Flask app 'app'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://172.17.0.2:5000
Press CTRL+C to quit
172.17.0.1 - - [23/Jan/2024 02:43:10] "GET / HTTP/1.1" 200 -
172.17.0.1 - - [23/Jan/2024 02:43:10] "GET /favicon.ico HTTP/1.1" 404 -
```

O Dockerfile é como você cria builds reproduzíveis para seu aplicativo. Um fluxo de trabalho comum é ter sua automação CI/CD executar `docker image build` como parte de seu processo de build. Depois que as imagens são construídas, elas serão enviadas para um registro central, onde podem ser acessadas por todos os ambientes (como um ambiente de teste) que precisam executar instâncias desse aplicativo. Na próxima etapa, enviaremos nossa imagem personalizada para o registro público do docker: o docker hub, onde ela pode ser consumida por outros desenvolvedores e operadores.
