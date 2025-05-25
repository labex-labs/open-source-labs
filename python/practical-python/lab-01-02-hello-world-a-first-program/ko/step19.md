# 연습 1.6: 디버깅 (Debugging)

다음 코드 조각은 시어스 타워 문제의 코드를 포함하고 있습니다. 또한 버그도 포함하고 있습니다.

```python
# sears.py

bill_thickness = 0.11 * 0.001    # Meters (0.11 mm)
sears_height   = 442             # Height (meters)
num_bills      = 1
day            = 1

while num_bills * bill_thickness < sears_height:
    print(day, num_bills, num_bills * bill_thickness)
    day = days + 1
    num_bills = num_bills * 2

print('Number of days', day)
print('Number of bills', num_bills)
print('Final height', num_bills * bill_thickness)
```

위의 코드를 복사하여 `sears.py`라는 새 프로그램에 붙여넣으십시오. 코드를 실행하면 다음과 같이 프로그램이 충돌하게 만드는 오류 메시지가 나타납니다.

```code
Traceback (most recent call last):
  File "sears.py", line 10, in <module>
    day = days + 1
NameError: name 'days' is not defined
```

오류 메시지를 읽는 것은 Python 코드의 중요한 부분입니다. 프로그램이 충돌하면, traceback 메시지의 마지막 줄이 프로그램이 충돌한 실제 이유입니다. 그 위에 소스 코드의 조각과 식별 파일 이름 및 줄 번호가 표시됩니다.

- 오류가 있는 줄은 어디입니까?
- 오류는 무엇입니까?
- 오류를 수정하십시오.
- 프로그램을 성공적으로 실행하십시오.
