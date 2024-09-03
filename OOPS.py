class Car:
    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    def drive(self):
        print(f"you drive the {self.color} {self.model}")
    def stop(self):
        print(f"You stop the {self.color} {self.model}")

car1 = Car("BMW",2024,"Blue", False)
car2 = Car("Mustang",2023,"Red", False)

print(f"{car1.color} {car1.model}")
print(f"{car2.color} {car2.model}")

car1.drive()
car2.stop()
