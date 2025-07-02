# 소개

이 실습에서는 Python 의 scikit-learn 라이브러리에서 나이브 베이즈 분류기를 사용하는 예제를 살펴볼 것입니다. 나이브 베이즈 분류기는 분류 작업에 일반적으로 사용되는 지도 학습 알고리즘 집합입니다. 이 분류기는 클래스 변수의 값을 고려했을 때 모든 특징 쌍 사이의 조건부 독립성을 가정하고 베이즈 정리를 적용하는 데 기반합니다.

이 예제에서는 scikit-learn 의 가우시안 나이브 베이즈 분류기를 사용하여 아이리스 데이터셋을 분류할 것입니다. 아이리스 데이터셋은 머신 러닝 분야에서 널리 사용되는 데이터셋입니다. 이 목표는 꽃잎과 꽃받침의 크기 정보를 바탕으로 아이리스 꽃의 종을 예측하는 것입니다.

## VM 팁

VM 시작이 완료되면 왼쪽 상단 모서리를 클릭하여 **Notebook** 탭으로 전환하여 연습을 위한 [Jupyter Notebook](https://support.labex.io/en/labex-vm/jupyter)에 접근할 수 있습니다.

때때로 Jupyter Notebook 이 완전히 로드되기까지 몇 초 정도 기다려야 할 수 있습니다. Jupyter Notebook 의 제한으로 인해 작업의 유효성 검사를 자동화할 수 없습니다.

학습 중 문제가 발생하면 Labby 에게 문의하십시오. 세션 후 피드백을 제공하면 문제를 신속하게 해결해 드리겠습니다.

<div class="text-xs text-gray-500 dark:text-gray-400 mt-4 border-t border-l-2 border-gray-300 dark:border-gray-600 pt-2 pl-4">
이것은 가이드 실험입니다. 학습과 실습을 돕기 위한 단계별 지침을 제공합니다.각 단계를 완료하고 실무 경험을 쌓기 위해 지침을 주의 깊게 따르세요. 과거 데이터에 따르면, 이것은 <span class="text-green-600 dark:text-green-400">초급</span> 레벨의 실험이며 완료율은 <span class="text-green-600 dark:text-green-400">91%</span>입니다.학습자들로부터 <span class="text-primary-600 dark:text-primary-400">100%</span>의 긍정적인 리뷰율을 받았습니다.
</div>
