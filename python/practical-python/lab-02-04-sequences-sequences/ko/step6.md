# break 문 (break statement)

`break` 문을 사용하여 루프를 조기에 종료할 수 있습니다.

```python
for name in namelist:
    if name == 'Jake':
        break
    ...
    ...
statements
```

`break` 문이 실행되면, 루프를 종료하고 다음 `statements`로 이동합니다. `break` 문은 가장 안쪽의 루프에만 적용됩니다. 이 루프가 다른 루프 안에 있는 경우, 바깥쪽 루프는 종료되지 않습니다.
