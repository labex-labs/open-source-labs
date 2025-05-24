# 사용자 정의 명령어 생성

Flask CLI 를 사용하면 명령줄에서 실행할 수 있는 사용자 정의 명령어를 생성할 수 있습니다. 인수로 이름을 받아 인사 메시지를 출력하는 `greet`라는 사용자 정의 명령어를 생성해 보겠습니다.

`commands.py`라는 새 Python 파일을 생성하고 다음 코드를 추가합니다:

```python
import click

@click.command()
@click.argument('name')
def greet(name):
    click.echo(f'Hello, {name}!')

if __name__ == '__main__':
    greet()
```

파일을 저장하고 다음 명령을 사용하여 실행합니다:

```
python commands.py John
```

터미널에 "Hello, John!" 메시지가 출력되는 것을 확인할 수 있습니다.
