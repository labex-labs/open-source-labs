# Configurando o Ambiente de Teste

Antes de começar a escrever testes para sua aplicação Flask, você precisa configurar o ambiente de teste. Aqui estão os passos para fazer isso:

1.  Instale o framework `pytest` executando o seguinte comando:

    ```bash
    pip install pytest
    ```

2.  Crie um novo arquivo chamado `conftest.py` na pasta `tests` da sua aplicação Flask.

3.  No arquivo `conftest.py`, importe os módulos necessários:

    ```python
    import pytest
    from my_app import create_app
    ```

4.  Defina uma fixture chamada `app` que cria e configura uma instância da aplicação:

    ```python
    @pytest.fixture()
    def app():
        app = create_app()
        app.config.update({
            "TESTING": True,
        })
        yield app
    ```

    Observe que, se você estiver usando um padrão de fábrica de aplicações (application factory pattern), você deve modificar a fixture de acordo.

5.  Defina fixtures para o cliente de teste e o executor de CLI (CLI runner):

    ```python
    @pytest.fixture()
    def client(app):
        return app.test_client()

    @pytest.fixture()
    def runner(app):
        return app.test_cli_runner()
    ```
