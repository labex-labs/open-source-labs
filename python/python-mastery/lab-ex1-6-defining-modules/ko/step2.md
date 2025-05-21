# Python 의 메인 모듈 이해하기

Python 에서 스크립트를 직접 실행하면 "메인" 모듈 역할을 합니다. Python 에는 `__name__`이라는 특수한 변수가 있습니다. 파일을 직접 실행하면 Python 은 `__name__`의 값을 `"__main__"`으로 설정합니다. 이는 파일을 모듈로 가져올 때와는 다릅니다.

이 기능은 파일이 직접 실행되는지 또는 가져오는지에 따라 다르게 동작하는 코드를 작성할 수 있으므로 매우 유용합니다. 예를 들어, 스크립트로 파일을 실행할 때만 실행되고 다른 스크립트에서 가져올 때는 실행되지 않는 코드가 있을 수 있습니다.

## 메인 모듈 패턴을 사용하도록 pcost.py 수정하기

이 패턴을 활용하기 위해 `pcost.py` 프로그램을 수정해 보겠습니다.

1. 먼저, 편집기에서 `pcost.py` 파일을 열어야 합니다. 다음 명령을 사용하여 프로젝트 디렉토리로 이동하고 파일이 없는 경우 파일을 만들 수 있습니다.

```bash
cd ~/project
touch pcost.py
```

`cd` 명령은 현재 디렉토리를 홈 디렉토리의 `project` 디렉토리로 변경합니다. `touch` 명령은 `pcost.py`라는 새 파일을 만듭니다 (아직 없는 경우).

2. 이제 `pcost.py` 파일을 다음과 같이 수정합니다.

```python
# pcost.py

def portfolio_cost(filename):
    total_cost = 0.0

    with open(filename, 'r') as f:
        for line in f:
            fields = line.split()
            try:
                nshares = int(fields[1])
                price = float(fields[2])
                total_cost += nshares * price
            except (ValueError, IndexError):
                print(f"Couldn't parse: {line}")

    return total_cost

# This code only runs when the file is executed as a script
if __name__ == "__main__":
    total = portfolio_cost('portfolio.dat')
    print(total)
```

여기서 주요 변경 사항은 마지막 부분의 코드를 `if __name__ == "__main__":` 조건으로 묶었다는 것입니다. 즉, 이 블록 내부의 코드는 파일이 모듈로 가져올 때가 아니라 스크립트로 직접 실행될 때만 실행됩니다.

3. 이러한 변경을 수행한 후 파일을 저장하고 편집기를 종료합니다.

## 수정된 모듈 테스트하기

이제 수정된 모듈이 어떻게 동작하는지 확인하기 위해 두 가지 방법으로 테스트해 보겠습니다.

1. 먼저, 다음 명령을 사용하여 프로그램을 스크립트로 직접 실행합니다.

```bash
python3 pcost.py
```

이전과 마찬가지로 출력 `44671.15`를 볼 수 있습니다. 이는 스크립트를 직접 실행하면 `__name__` 변수가 `"__main__"`으로 설정되므로 `if __name__ == "__main__":` 블록 내부의 코드가 실행되기 때문입니다.

2. 다음으로, Python 인터프리터를 다시 시작하고 모듈을 가져옵니다.

```bash
python3
```

```python
import pcost
```

이번에는 아무런 출력도 보이지 않습니다. 모듈을 가져오면 `__name__` 변수가 `"__main__"`이 아닌 `"pcost"`(모듈 이름) 로 설정됩니다. 따라서 `if __name__ == "__main__":` 블록 내부의 코드는 실행되지 않습니다.

3. `portfolio_cost` 함수가 여전히 작동하는지 확인하려면 다음과 같이 호출할 수 있습니다.

```python
pcost.portfolio_cost('portfolio.dat')
```

함수는 `44671.15`를 반환해야 하며, 이는 제대로 작동하고 있음을 의미합니다.

4. 마지막으로, 다음 명령을 사용하여 Python 인터프리터를 종료합니다.

```python
exit()
```

이 패턴은 가져올 수 있는 모듈과 독립 실행형 스크립트 모두로 사용할 수 있는 Python 파일을 만들 때 매우 유용합니다. `if __name__ == "__main__":` 블록 내부의 코드는 파일이 모듈로 가져올 때가 아니라 직접 실행될 때만 실행됩니다.
