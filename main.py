def calcular_juros_compostos(principal, taxa, tempo, frequencia=1):
    """
    Calcula o montante com juros compostos.
    
    :param principal: O valor inicial (P).
    :param taxa: A taxa de juros anual em decimal (por exemplo, 0.05 para 5% ao ano).
    :param tempo: O tempo em anos (t).
    :param frequencia: A frequência de capitalização por ano (n).
    :return: O montante total após o tempo (A).
    """
    montante = principal * (1 + taxa / frequencia) ** (frequencia * tempo)
    return montante

def calcular_juros_acumulados(principal, taxa, tempo, frequencia=1):
    """
    Calcula os juros acumulados com juros compostos.
    
    :param principal: O valor inicial (P).
    :param taxa: A taxa de juros anual em decimal.
    :param tempo: O tempo em anos (t).
    :param frequencia: A frequência de capitalização por ano (n).
    :return: O valor dos juros acumulados.
    """
    montante = calcular_juros_compostos(principal, taxa, tempo, frequencia)
    juros_acumulados = montante - principal
    return juros_acumulados
