# 데이터 유형 이해

NumPy 는 C 프로그래밍 언어의 데이터 유형과 밀접하게 관련된 다양한 숫자 유형을 지원합니다. 다음은 NumPy 에서 가장 일반적으로 사용되는 데이터 유형 중 일부입니다.

- `numpy.bool_`: 부울 (True 또는 False), 바이트로 저장
- `numpy.byte`: 부호 있는 char (플랫폼 정의)
- `numpy.ubyte`: 부호 없는 char (플랫폼 정의)
- `numpy.short`: short (플랫폼 정의)
- `numpy.ushort`: 부호 없는 short (플랫폼 정의)
- `numpy.intc`: int (플랫폼 정의)
- `numpy.uintc`: 부호 없는 int (플랫폼 정의)
- `numpy.int_`: long (플랫폼 정의)
- `numpy.uint`: 부호 없는 long (플랫폼 정의)
- `numpy.longlong`: long long (플랫폼 정의)
- `numpy.ulonglong`: 부호 없는 long long (플랫폼 정의)
- `numpy.half` / `numpy.float16`: 반정밀도 부동 소수점
- `numpy.single`: 단정밀도 부동 소수점 (플랫폼 정의)
- `numpy.double`: 배정밀도 부동 소수점 (플랫폼 정의)
- `numpy.longdouble`: 확장 정밀도 부동 소수점 (플랫폼 정의)
- `numpy.csingle`: 두 개의 단정밀도 부동 소수점으로 표현되는 복소수
- `numpy.cdouble`: 두 개의 배정밀도 부동 소수점으로 표현되는 복소수
- `numpy.clongdouble`: 두 개의 확장 정밀도 부동 소수점으로 표현되는 복소수

이러한 데이터 유형은 플랫폼에 따라 정의되지만, NumPy 는 편의를 위해 고정 크기 별칭도 제공합니다.
