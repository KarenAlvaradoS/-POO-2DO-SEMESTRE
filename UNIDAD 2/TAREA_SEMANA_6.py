# Clase base Animal
class Animal:
    def __init__(self, name, age):
        self._name = name   # Atributo encapsulado
        self._age = age     # Atributo encapsulado

    def speak(self):
        raise NotImplementedError("La subclase debe implementar un método abstracto")

    def info(self):
        print(f"{self._name} tiene {self._age} años.")

# Clase derivada Dog
class perro(Animal):
    def speak(self):
        print(f"{self._name} dice Woof!")

# Clase derivada Cat
class gato(Animal):
    def speak(self):
        print(f"{self._name} dice Meow!")

# Creación de objetos y demostración de funcionalidad
perro = perro("Buddy", 5)
gato = gato("Whiskers", 3)

perro.info()
perro.speak()

gato.info()
gato.speak()
