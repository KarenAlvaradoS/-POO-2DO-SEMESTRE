class Clima:
    def __init__(self):
        self.temperaturas = []

    def ingresar_temperaturas(self):
        for i in range(7):
            temp = float(input(f"Ingrese la temperatura del día {i+1}: "))
            self.temperaturas.append(temp)

    def calcular_promedio(self):
        return sum(self.temperaturas) / len(self.temperaturas)

# Función principal
def main():
    clima_semanal = Clima()
    clima_semanal.ingresar_temperaturas()
    promedio = clima_semanal.calcular_promedio()
    print(f"El promedio semanal de la temperatura es: {promedio:.2f}°C")

# Ejecutar la función principal
if __name__ == "__main__":
    main()
