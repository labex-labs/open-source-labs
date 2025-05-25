# Ambientes Virtuais

Uma solução comum para problemas de instalação de pacotes é criar o que se chama de "ambiente virtual" para você. Naturalmente, não existe uma "única maneira" de fazer isso - na verdade, existem várias ferramentas e técnicas concorrentes. No entanto, se você estiver usando uma instalação padrão do Python, pode tentar digitar o seguinte:

```bash
$ sudo apt install python3-venv
$ python -m venv mypython
bash %
```

Após alguns momentos de espera, você terá um novo diretório `mypython` que é sua própria pequena instalação do Python. Dentro desse diretório, você encontrará um diretório `bin/` (Unix) ou um diretório `Scripts/` (Windows). Se você executar o script `activate` encontrado lá, ele "ativará" esta versão do Python, tornando-a o comando `python` padrão para o shell. Por exemplo:

```bash
$ source mypython/bin/activate
(mypython) bash %
```

A partir daqui, você pode começar a instalar pacotes Python para você mesmo. Por exemplo:

    (mypython) $ python -m pip install pandas
    ...

Para fins de experimentação e teste de diferentes pacotes, um ambiente virtual geralmente funcionará bem. Se, por outro lado, você estiver criando um aplicativo e ele tiver dependências específicas de pacotes, esse é um problema um pouco diferente.
