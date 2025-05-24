# Executando o Servidor de Desenvolvimento a partir do Python

Além de usar o comando da CLI (Command Line Interface) do Flask, você também pode iniciar o servidor de desenvolvimento a partir do código Python. Adicione o seguinte código no final do seu arquivo `app.py`:

```python
if __name__ == "__main__":
    app.run(debug=True)
```

Agora, você pode executar o servidor de desenvolvimento executando o arquivo `app.py` com Python:

```bash
python app.py
```

Isso iniciará o servidor de desenvolvimento e você poderá acessar sua aplicação Flask da mesma forma que antes.
