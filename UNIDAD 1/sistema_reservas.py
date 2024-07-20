class Reserva:
    def __init__(self, nombre_cliente, tipo_habitacion, noches):
        # Inicializa la reserva con los datos del cliente, el tipo de habitación y el número de noches
        self.nombre_cliente = nombre_cliente
        self.tipo_habitacion = tipo_habitacion
        self.noches = noches

    def costo_total(self):
        # Calcula el costo total basado en la tarifa de la habitación y el número de noches
        tarifas = {
            'simple': 50,
            'doble': 80,
            'suite': 120
        }
        return tarifas[self.tipo_habitacion] * self.noches

    def mostrar_reserva(self):
        # Muestra los detalles de la reserva
        print(f"Cliente: {self.nombre_cliente}")
        print(f"Tipo de Habitación: {self.tipo_habitacion}")
        print(f"Noches: {self.noches}")
        print(f"Costo Total: ${self.costo_total()}")

# Ejemplo de uso
reserva1 = Reserva("Juan Pérez", "suite", 3)
reserva1.mostrar_reserva()
