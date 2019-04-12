#cambios desde git
valOne: int = 123
valTwo: int = 20


text: str = 0


if valOne == valTwo:
    print(valOne, valTwo, " son equals")

if valOne != valTwo:
    print("is different")

if valOne > valTwo:
    print(valOne, " es mayor que: ", valTwo)

if valTwo >= valOne:
    print(valTwo, "es mayor o equal que: ", valOne)


text = input("Write a text: ")

if (len(text)) >= 3 and (len(text) < 10):
    print(text, " Yes..")
    print(type(text))

else:
    print("Not")

