def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el descuento y el monto final a pagar.

    :param monto_total: Monto total de la compra.
    :param porcentaje_descuento: Porcentaje de descuento (por defecto 10%).
    :return: Monto del descuento y monto final a pagar.
    """
    descuento = monto_total * (porcentaje_descuento / 100)
    monto_final = monto_total - descuento
    return descuento, monto_final
def main():
    # Primera llamada con el monto total de la compra
    monto_total1 = 100.0
    descuento1, monto_final1 = calcular_descuento(monto_total1)
    print(f"Compra 1: Monto Total = ${monto_total1}, Descuento = ${descuento1}, Monto Final = ${monto_final1}")

    # Segunda llamada con el monto total de la compra y un porcentaje de descuento específico
    monto_total2 = 200.0
    porcentaje_descuento2 = 15
    descuento2, monto_final2 = calcular_descuento(monto_total2, porcentaje_descuento2)
    print(f"Compra 2: Monto Total = ${monto_total2}, Descuento = ${descuento2}, Monto Final = ${monto_final2}")

if __name__ == "__main__":
    main()