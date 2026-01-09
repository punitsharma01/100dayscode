def add(*args):
    res = 0
    for n in args:
        res += n
    return res


total = add(2, 4, 5, 6, 8, 10)
print(total)


class Car:
    def __init__(self, **kwargs):
        self.make = kwargs["make"] # give KeyError if key does not found
        self.model = kwargs.get("model") # return none even if key is not found
        self.color = kwargs.get("color")


audi = Car(make="Audi", model="Q5")
print(audi.make, audi.model)
