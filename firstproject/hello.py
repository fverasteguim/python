from dataclasses import dataclass

@dataclass
class Deportista:
    nombre: str
    altura: float
    peso: float

deportista1 = Deportista('Francisco', 1.71, 85.4)
print(deportista1)

print("Hello world", "Francisco")