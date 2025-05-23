# Python 모듈 이해하기

Python 에서 모듈은 Python 정의와 문을 담는 컨테이너와 같습니다. 본질적으로 파일이며, 이 파일의 이름은 끝에 `.py` 확장자가 추가된 모듈 이름입니다. 모듈을 도구 상자라고 생각해보세요. 모듈은 Python 코드를 논리적인 방식으로 구성하여 재사용 및 유지 관리를 용이하게 합니다. 더 나은 구성을 위해 다양한 도구를 별도의 상자에 보관하는 것처럼, 관련 Python 코드를 서로 다른 모듈로 그룹화할 수 있습니다.

이 랩을 위해 설정된 파일을 살펴보겠습니다.

1. 먼저, 편집기에서 `stock.py` 파일을 열어 내부를 확인합니다. 이를 위해 다음 명령을 사용합니다. `cd` 명령은 디렉토리를 파일이 있는 `project` 폴더로 변경하고, `cat` 명령은 파일의 내용을 표시합니다.

```bash
cd ~/project
cat stock.py
```

이 `stock.py` 파일은 `Stock` 클래스를 정의합니다. 클래스는 객체를 생성하기 위한 청사진과 같습니다. 이 경우, `Stock` 클래스는 주식을 나타냅니다. 주식의 이름, 주식 수, 가격에 대한 속성 (특성과 같음) 이 있습니다. 또한 주식의 비용을 계산하는 메서드 (클래스와 관련된 함수와 같음) 도 있습니다.

2. 다음으로, `pcost.py` 파일을 살펴보겠습니다. `cat` 명령을 다시 사용하여 내용을 봅니다.

```bash
cat pcost.py
```

이 파일은 `portfolio_cost()`라는 함수를 정의합니다. 함수는 특정 작업을 수행하는 코드 블록입니다. `portfolio_cost()` 함수는 포트폴리오 파일을 읽고 해당 포트폴리오의 모든 주식의 총 비용을 계산합니다.

3. 이제 샘플 포트폴리오 데이터를 살펴보겠습니다. `cat` 명령을 사용하여 `portfolio.dat` 파일의 내용을 봅니다.

```bash
cat portfolio.dat
```

이 파일에는 간단한 형식의 주식 데이터가 포함되어 있습니다. 각 줄에는 주식의 티커 심볼, 주식 수 및 주당 가격이 있습니다.

## import 문 사용하기

Python 의 `import` 문은 현재 프로그램에서 다른 모듈의 코드를 사용할 수 있게 해주는 강력한 도구입니다. 다른 도구 상자에서 도구를 빌리는 것과 같습니다. 다양한 방식으로 코드를 가져오는 연습을 해보겠습니다.

1. 먼저, Python 인터프리터를 시작해야 합니다. Python 인터프리터는 Python 코드를 실행하는 프로그램입니다. 다음 명령을 사용하여 시작합니다.

```bash
python3
```

2. 이제 `pcost` 모듈을 가져와서 어떤 일이 발생하는지 확인해 보겠습니다. `import` 문을 사용하면 Python 은 `pcost.py` 파일을 찾고 그 안의 코드를 사용할 수 있도록 합니다.

```python
import pcost
```

출력 `44671.15`를 볼 수 있습니다. 이것은 `portfolio.dat` 파일에서 계산된 포트폴리오의 비용입니다. `pcost` 모듈이 가져오면 `pcost.py` 파일의 맨 아래에 있는 코드가 자동으로 실행됩니다.

3. 다른 포트폴리오 파일로 `portfolio_cost()` 함수를 호출해 보겠습니다. `pcost` 모듈에서 함수를 호출하기 위해 `pcost.portfolio_cost()` 구문을 사용합니다.

```python
pcost.portfolio_cost('portfolio2.dat')
```

출력은 `19908.75`여야 하며, 이는 두 번째 포트폴리오 파일의 주식 총 비용을 나타냅니다.

4. 이제 `stock` 모듈에서 특정 클래스를 가져오겠습니다. 전체 모듈을 가져오는 대신 `from...import` 문을 사용하여 `Stock` 클래스만 가져올 수 있습니다.

```python
from stock import Stock
```

5. `Stock` 클래스를 가져온 후 `Stock` 객체를 생성할 수 있습니다. 객체는 클래스의 인스턴스입니다. 이름이 `GOOG`, 주식 수가 100 주, 가격이 `490.10`인 `Stock` 객체를 생성합니다. 그런 다음 주식의 이름을 출력하고 `cost()` 메서드를 사용하여 비용을 계산합니다.

```python
s = Stock('GOOG', 100, 490.10)
print(s.name)
print(s.cost())
```

출력은 다음과 같아야 합니다.

```
GOOG
49010.0
```

6. 마지막으로, Python 인터프리터 사용을 마쳤으면 `exit()` 함수를 사용하여 종료할 수 있습니다.

```python
exit()
```

이 랩에서는 Python 코드를 가져오는 두 가지 방법을 시연했습니다.

- `import module_name` - 전체 모듈을 가져와 해당 모듈의 모든 함수, 클래스 및 변수를 사용할 수 있도록 합니다.
- `from module_name import specific_item` - 모듈에서 특정 항목 (클래스 또는 함수) 만 가져오며, 모듈 기능의 일부만 필요한 경우 유용할 수 있습니다.
