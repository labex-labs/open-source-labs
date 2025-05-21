# 컨텍스트 관리자 만들기

컨텍스트 관리자는 Python 에서 특별한 유형의 객체입니다. Python 에서 객체는 동작을 정의하는 다양한 메서드를 가질 수 있습니다. 컨텍스트 관리자는 특히 `__enter__` 및 `__exit__`의 두 가지 중요한 메서드를 정의합니다. 이러한 메서드는 `with` 문과 함께 작동합니다. `with` 문은 코드 블록에 대한 특정 컨텍스트를 설정하는 데 사용됩니다. 일련의 일이 발생하는 작은 환경을 생성하는 것으로 생각하고, 코드 블록이 완료되면 컨텍스트 관리자가 정리를 처리합니다.

이 단계에서는 매우 유용한 기능을 가진 컨텍스트 관리자를 만들 것입니다. 표준 출력 (`sys.stdout`) 을 임시로 리디렉션합니다. 표준 출력은 Python 프로그램의 일반적인 출력이 가는 곳으로, 일반적으로 콘솔입니다. 이를 리디렉션하여 출력을 대신 파일로 보낼 수 있습니다. 이는 콘솔에 표시될 출력을 저장하려는 경우 유용합니다.

먼저 컨텍스트 관리자 코드를 작성할 새 파일을 만들어야 합니다. 이 파일의 이름을 `redirect.py`로 지정합니다. 터미널에서 다음 명령을 사용하여 만들 수 있습니다.

```bash
touch /home/labex/project/redirect.py
```

이제 파일이 생성되었으므로 편집기에서 엽니다. 열리면 다음 Python 코드를 파일에 추가합니다.

```python
import sys

class redirect_stdout:
    def __init__(self, out_file):
        self.out_file = out_file

    def __enter__(self):
        self.stdout = sys.stdout
        sys.stdout = self.out_file
        return self.out_file

    def __exit__(self, ty, val, tb):
        sys.stdout = self.stdout
```

이 컨텍스트 관리자가 수행하는 작업을 자세히 살펴보겠습니다.

1. `__init__`: 이는 초기화 메서드입니다. `redirect_stdout` 클래스의 인스턴스를 만들 때 파일 객체를 전달합니다. 이 메서드는 해당 파일 객체를 인스턴스 변수 `self.out_file`에 저장합니다. 따라서 출력을 리디렉션하려는 위치를 기억합니다.
2. `__enter__`:
   - 먼저 현재 `sys.stdout`을 저장합니다. 나중에 복원해야 하므로 중요합니다.
   - 그런 다음 현재 `sys.stdout`을 파일 객체로 바꿉니다. 이 시점부터 일반적으로 콘솔로 이동하는 모든 출력은 대신 파일로 이동합니다.
   - 마지막으로 파일 객체를 반환합니다. `with` 블록 내부에서 파일 객체를 사용하려는 경우 유용합니다.
3. `__exit__`:
   - 이 메서드는 원래 `sys.stdout`을 복원합니다. 따라서 `with` 블록이 완료되면 출력이 정상적으로 콘솔로 다시 이동합니다.
   - 예외 유형 (`ty`), 예외 값 (`val`), 추적 정보 (`tb`) 의 세 가지 매개변수를 사용합니다. 이러한 매개변수는 컨텍스트 관리자 프로토콜에 필요합니다. `with` 블록 내에서 발생할 수 있는 예외를 처리하는 데 사용됩니다.

이제 컨텍스트 관리자를 테스트해 보겠습니다. 테이블의 출력을 파일로 리디렉션하는 데 사용합니다. 먼저 Python 인터프리터를 시작합니다.

```bash
python3
```

그런 다음 인터프리터에서 다음 Python 코드를 실행합니다.

```python
>>> import stock, reader, tableformat
>>> from redirect import redirect_stdout
>>> portfolio = reader.read_csv_as_instances('portfolio.csv', stock.Stock)
>>> formatter = tableformat.create_formatter('text')
>>> with redirect_stdout(open('out.txt', 'w')) as file:
...     tableformat.print_table(portfolio, ['name','shares','price'], formatter)
...     file.close()
...
>>> # Let's check the content of the output file
>>> print(open('out.txt').read())
      name     shares      price
---------- ---------- ----------
        AA        100       32.2
       IBM         50       91.1
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50       65.1
       IBM        100      70.44
```

훌륭합니다! 컨텍스트 관리자가 예상대로 작동했습니다. 테이블 출력을 `out.txt` 파일로 성공적으로 리디렉션했습니다.

컨텍스트 관리자는 Python 에서 매우 강력한 기능입니다. 리소스를 적절하게 관리하는 데 도움이 됩니다. 다음은 컨텍스트 관리자의 몇 가지 일반적인 사용 사례입니다.

- 파일 작업: 파일을 열 때 컨텍스트 관리자는 오류가 발생하더라도 파일이 제대로 닫히도록 할 수 있습니다.
- 데이터베이스 연결: 사용을 마친 후 데이터베이스 연결이 닫히도록 할 수 있습니다.
- 스레드 프로그램의 잠금: 컨텍스트 관리자는 안전한 방식으로 리소스를 잠그고 잠금 해제할 수 있습니다.
- 환경 설정 임시 변경: 코드 블록에 대한 일부 설정을 변경한 다음 자동으로 복원할 수 있습니다.

이 패턴은 `with` 블록 내에서 예외가 발생하더라도 리소스가 제대로 정리되도록 보장하므로 매우 중요합니다.

테스트를 마쳤으면 Python 인터프리터를 종료할 수 있습니다.

```python
>>> exit()
```
