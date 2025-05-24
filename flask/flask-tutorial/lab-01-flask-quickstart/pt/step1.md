# Configurando o Flask

Para começar com o Flask, você precisa instalá-lo e configurar um novo projeto. Siga as instruções abaixo:

1. Instale o Flask executando o seguinte comando no seu terminal ou prompt de comando:

   ```bash
   pip install flask
   ```

2. Abra um novo arquivo e salve-o como `app.py`.

   ```bash
   cd ~/project
   touch app.py
   ```

3. Importe o módulo Flask e crie uma instância da classe Flask:

   ```python
   from flask import Flask

   app = Flask(__name__)
   ```
