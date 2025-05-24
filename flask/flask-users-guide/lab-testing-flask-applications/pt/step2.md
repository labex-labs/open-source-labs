# Escrevendo Testes

Agora que você configurou o ambiente de teste, pode começar a escrever testes para sua aplicação Flask. Aqui estão alguns exemplos de testes comuns que você pode querer escrever:

1.  Testar uma rota:

    ```python
    def test_hello(client):
        response = client.get("/")
        assert response.status_code == 200
        assert b"Hello, World!" in response.data
    ```

    Este teste envia uma requisição GET para a rota raiz ("/") e verifica se o código de status da resposta é 200 e se os dados da resposta contêm a string "Hello, World!".

2.  Testar uma requisição POST:

    ```python
    def test_login(client):
        response = client.post("/login", data={"username": "test", "password": "pass"})
        assert response.status_code == 200
        assert b"Logged in successfully" in response.data
    ```

    Este teste envia uma requisição POST para a rota de login ("/login") com dados de formulário contendo um nome de usuário e senha. Ele verifica se o código de status da resposta é 200 e se os dados da resposta contêm a string "Logged in successfully".

3.  Testar um comando:

    ```python
    def test_hello_command(runner):
        result = runner.invoke(args=["hello"])
        assert result.exit_code == 0
        assert "Hello, World!" in result.output
    ```

    Este teste invoca um comando chamado "hello" e verifica se o comando sai com um código 0 e se a saída contém a string "Hello, World!".
