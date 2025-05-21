# Python 제너레이터 이해

Python 에서 제너레이터가 무엇인지부터 살펴보겠습니다. Python 에서 제너레이터는 특별한 유형의 함수입니다. 일반 함수와는 다릅니다. 일반 함수를 호출하면 처음부터 끝까지 실행되어 단일 값을 반환합니다. 그러나 제너레이터 함수는 반복 가능한 객체인 이터레이터 (iterator) 를 반환합니다. 즉, 값을 하나씩 접근할 수 있습니다.

제너레이터는 `yield` 문을 사용하여 값을 반환합니다. 일반 함수처럼 모든 값을 한 번에 반환하는 대신, 제너레이터는 값을 한 번에 하나씩 반환합니다. 값을 yield 한 후, 제너레이터는 실행을 일시 중지합니다. 다음에 값을 요청하면 중단된 지점부터 실행을 재개합니다.

## 간단한 제너레이터 생성

이제 간단한 제너레이터를 만들어 보겠습니다. WebIDE 에서 새 파일을 만들어야 합니다. 이 파일에는 제너레이터에 대한 코드가 포함됩니다. 파일 이름을 `generator_demo.py`로 지정하고 `/home/labex/project` 디렉토리에 넣습니다. 파일에 넣어야 할 내용은 다음과 같습니다.

```python
# Generator function that counts down from n
def countdown(n):
    print(f"Starting countdown from {n}")
    while n > 0:
        yield n
        n -= 1
    print("Countdown complete!")

# Create a generator object
counter = countdown(5)

# Drive the generator manually
print(next(counter))  # 5
print(next(counter))  # 4
print(next(counter))  # 3

# Iterate through remaining values
for value in counter:
    print(value)  # 2, 1
```

이 코드에서는 먼저 `countdown`이라는 제너레이터 함수를 정의합니다. 이 함수는 숫자 `n`을 인수로 받아 `n`에서 1 까지 카운트다운합니다. 함수 내부에서 `while` 루프를 사용하여 `n`을 감소시키고 각 값을 yield 합니다. `countdown(5)`를 호출하면 `counter`라는 제너레이터 객체가 생성됩니다.

그런 다음 `next()` 함수를 사용하여 제너레이터에서 값을 수동으로 가져옵니다. `next(counter)`를 호출할 때마다 제너레이터는 중단된 지점부터 실행을 재개하고 다음 값을 yield 합니다. 세 개의 값을 수동으로 가져온 후, `for` 루프를 사용하여 제너레이터의 나머지 값을 반복합니다.

이 코드를 실행하려면 터미널을 열고 다음 명령을 실행합니다.

```bash
python3 /home/labex/project/generator_demo.py
```

코드를 실행하면 다음과 같은 출력이 표시됩니다.

```
Starting countdown from 5
5
4
3
2
1
Countdown complete!
```

제너레이터 함수의 동작 방식을 살펴보겠습니다.

1. 제너레이터 함수는 `next(counter)`를 처음 호출할 때 실행을 시작합니다. 그 전에는 함수가 정의되기만 하고 실제 카운트다운은 시작되지 않습니다.
2. 각 `yield` 문에서 일시 중지됩니다. 값을 yield 한 후, 멈추고 `next()`에 대한 다음 호출을 기다립니다.
3. `next()`를 다시 호출하면 중단된 지점부터 계속됩니다. 예를 들어, 5 를 yield 한 후, 상태를 기억하고 `n`을 감소시키고 다음 값을 yield 합니다.
4. 제너레이터 함수는 마지막 값을 yield 한 후 실행을 완료합니다. 이 경우, 1 을 yield 한 후 "Countdown complete!"를 출력합니다.

이러한 실행 일시 중지 및 재개 기능이 제너레이터를 강력하게 만듭니다. 이는 작업 스케줄링 및 비동기 프로그래밍과 같이 다른 작업의 실행을 차단하지 않고 효율적인 방식으로 여러 작업을 수행해야 하는 작업에 매우 유용합니다.
