def calcular_amperaje(watts, voltios=120):
    """Calcula la corriente en Amperios a partir de la potencia y el voltaje."""
    return round(watts / voltios, 2)

def recomendar_calibre_awg(amperios):
    """Sugiere el calibre AWG mínimo de cobre (aislamiento THHN) para uso residencial."""
    if amperios <= 15:
        return "14 AWG (Breaker recomendado: 15A)"
    elif amperios <= 20:
        return "12 AWG (Breaker recomendado: 20A)"
    elif amperios <= 30:
        return "10 AWG (Breaker recomendado: 30A)"
    elif amperios <= 40:
        return "8 AWG (Breaker recomendado: 40A)"
    elif amperios <= 55:
        return "6 AWG (Breaker recomendado: 50A)"
    else:
        return "4 AWG o superior (Consultar tabla NEC completa)"

if __name__ == "__main__":
    print("=== Calculadora Eléctrica Residencial Básica ===")
    potencia = float(input("Ingresa la potencia total de la carga (Watts): "))
    voltaje = float(input("Ingresa el voltaje del circuito (120 o 240): "))
    
    corriente = calcular_amperaje(potencia, voltaje)
    calibre = recomendar_calibre_awg(corriente)
    
    print(f"\nCorriente estimada: {corriente} A")
    print(f"Calibre sugerido: {calibre}")
