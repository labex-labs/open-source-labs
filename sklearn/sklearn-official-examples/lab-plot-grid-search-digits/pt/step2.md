# Definir Estratégia de Busca em Grade

Vamos definir uma função a ser passada para o parâmetro `refit` da instância `GridSearchCV`. Ela implementará a estratégia personalizada para selecionar o melhor candidato a partir do atributo `cv_results_` do `GridSearchCV`. Uma vez selecionado o candidato, ele é automaticamente retrabalhado pela instância `GridSearchCV`.

Aqui, a estratégia é criar uma lista curta dos modelos que são os melhores em termos de precisão e revocação. A partir dos modelos selecionados, finalmente selecionamos o modelo mais rápido na previsão. Observe que essas escolhas personalizadas são completamente arbitrárias.

```python
import pandas as pd
from sklearn.metrics import classification_report

def print_dataframe(filtered_cv_results):
    """Imprime o DataFrame filtrado de forma organizada."""
    for mean_precision, std_precision, mean_recall, std_recall, params in zip(
        filtered_cv_results["mean_test_precision"],
        filtered_cv_results["std_test_precision"],
        filtered_cv_results["mean_test_recall"],
        filtered_cv_results["std_test_recall"],
        filtered_cv_results["params"],
    ):
        print(
            f"Precisão: {mean_precision:0.3f} (±{std_precision:0.03f}),"
            f" Revocação: {mean_recall:0.3f} (±{std_recall:0.03f}),"
            f" para {params}"
        )
    print()


def refit_strategy(cv_results):
    """Define a estratégia para selecionar o melhor estimador.

    A estratégia definida aqui é filtrar todos os resultados abaixo de um limiar de precisão
    de 0,98, classificar os restantes por revocação e manter todos os modelos com um desvio
    padrão do melhor em revocação. Uma vez que esses modelos são selecionados, podemos selecionar
    o modelo mais rápido para prever.

    Parâmetros
    ----------
    cv_results : dict de numpy (masked) ndarrays
        Resultados de validação cruzada retornados pelo `GridSearchCV`.

    Retorna
    -------
    best_index : int
        O índice do melhor estimador conforme aparece em `cv_results`.
    """
    # Imprime as informações sobre a busca em grade para as diferentes pontuações
    threshold_precision = 0.98

    cv_results_ = pd.DataFrame(cv_results)
    print("Todos os resultados da busca em grade:")
    print_dataframe(cv_results_)

    # Filtra todos os resultados abaixo do limiar
    resultados_alta_precisao = cv_results_[
        cv_results_["mean_test_precision"] > threshold_precision
    ]

    print(f"Modelos com precisão superior a {threshold_precision}:")
    print_dataframe(resultados_alta_precisao)

    resultados_alta_precisao = resultados_alta_precisao[
        [
            "mean_score_time",
            "mean_test_recall",
            "std_test_recall",
            "mean_test_precision",
            "std_test_precision",
            "rank_test_recall",
            "rank_test_precision",
            "params",
        ]
    ]

    # Seleciona os modelos mais eficientes em termos de revocação
    # (dentro de 1 desvio padrão do melhor)
    desvio_padrao_melhor_revocacao = resultados_alta_precisao["mean_test_recall"].std()
    melhor_revocacao = resultados_alta_precisao["mean_test_recall"].max()
    limiar_melhor_revocacao = melhor_revocacao - desvio_padrao_melhor_revocacao

    resultados_alta_revocacao = resultados_alta_precisao[
        resultados_alta_precisao["mean_test_recall"] > limiar_melhor_revocacao
    ]
    print(
        "Dos modelos de alta precisão selecionados anteriormente, mantemos todos os\n"
        "modelos dentro de um desvio padrão do modelo de maior revocação:"
    )
    print_dataframe(resultados_alta_revocacao)

    # A partir dos melhores candidatos, seleciona o modelo mais rápido para prever
    indice_modelo_mais_rapido = resultados_alta_revocacao[
        "mean_score_time"
    ].idxmin()

    print(
        "\nO modelo final selecionado é o mais rápido para prever entre o subconjunto\n"
        "selecionado de melhores modelos com base em precisão e revocação.\n"
        "Seu tempo de pontuação é:\n\n"
        f"{resultados_alta_revocacao.loc[indice_modelo_mais_rapido]}"
    )

    return indice_modelo_mais_rapido
```
