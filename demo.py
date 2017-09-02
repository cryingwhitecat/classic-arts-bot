class SomeClass:
    name="publicName"
    def __init__(self):
        self.ownName="ownName"
    def someFunc(self):
        print("someFunc")

sc=SomeClass()
print(sc.name)
print(sc.ownName)
sc.someFunc()