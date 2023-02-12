thistuple = input("Choose a car (type sedan/crossover/suv/bus/truck) : ")
class car:
    def __init__(self, name, capacity, wheels, engine):
        self.name = name
        self.capacity = capacity
        self.wheels = wheels
        self.engine = engine

sedan = car("bmw", 4, 4, 6)
crossover = car("Honda", 6, 4, 4)
suv = car("Ford", 8, 4, 8)
bus = car("GMC", 24, 6, 12)
truck = car("Volvo", 2, 18, 12)

if thistuple == "sedan":
    print(sedan.name)
    print(sedan.capacity)
    print(sedan.wheels)
    print(sedan.engine)
elif thistuple == "corssover":
    print(corssover.name)
    print(corssover.capacity)
    print(corssover.wheels)
    print(corssover.engine)
elif thistuple == "suv":
    print(suv.name)
    print(suv.capacity)
    print(suv.wheels)
    print(suv.engine)
elif thistuple == "bus":
    print(bus.name)
    print(bus.capacity)
    print(bus.wheels)
    print(bus.engine)
elif thistuple == "truck":
    print(truck.name)
    print(truck.capacity)
    print(truck.wheels)
    print(truck.engine)
