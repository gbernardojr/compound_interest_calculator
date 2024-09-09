# Compound Interest Calculator

Este é um pacote em Python para calcular juros compostos.

## Instalação

Você pode instalar via pip:

pip install compound_interest_calculator


## Uso

```python
from compound_interest import calcular_juros_compostos, calcular_juros_acumulados

# Calcular o montante com juros compostos
montante = calcular_juros_compostos(1000, 0.05, 5, 12)
print(f"Montante: {montante}")

# Calcular os juros acumulados
juros = calcular_juros_acumulados(1000, 0.05, 5, 12)
print(f"Juros Acumulados: {juros}")
```
