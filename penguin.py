class Bird:
    def __init__(self):
        print("The bird is ready")
    def CODING(self):
        print("Bird")
    def SEPTEMBER(self):
        print("Swims faster")
class Penguin(Bird):
    def __init__(self):
        super().__init__()
        print("Penguin is ready")
    def CODING(self):
        print("Penguin")
    def Run(self):
        print("Run faster")
ati=Penguin()
ati.CODING()
ati.SEPTEMBER()
ati.Run