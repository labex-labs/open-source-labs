# 소개

이 실험은 서포트 벡터 머신 (SVM) 을 이용한 분류에서 정규화 매개변수의 스케일링 효과를 보여줍니다. SVM 분류에서 우리는 다음 방정식에 대한 위험 최소화에 관심이 있습니다.

```math
C \sum_{i=1, n} \mathcal{L} (f(x_i), y_i) + \Omega (w)
```

여기서:

- `C`는 정규화의 양을 설정하는 데 사용됩니다.
- `L`은 샘플과 모델 매개변수의 손실 함수입니다.
- `Ω`는 모델 매개변수의 페널티 함수입니다.

## VM 팁

VM 시작이 완료되면 왼쪽 상단 모서리를 클릭하여 **Notebook** 탭으로 전환하여 연습을 위한 [Jupyter Notebook](https://support.labex.io/en/labex-vm/jupyter)에 접근할 수 있습니다.

때때로 Jupyter Notebook 이 로드되는 데 몇 초가 걸릴 수 있습니다. Jupyter Notebook 의 제한으로 인해 작업의 유효성 검사는 자동화될 수 없습니다.

학습 중 문제가 발생하면 Labby 에 문의하십시오. 세션 후 피드백을 제공하면 문제를 신속하게 해결해 드리겠습니다.
