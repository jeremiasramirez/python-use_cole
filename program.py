name = 1
breaks = 0
cola = []
i = 0
j = 0
while breaks != "n":

    breaks = str(input("Quieres agregar un nombre: "))

    if breaks == "y":
        name = str(input("Diga un nombre para agregar: "))
        if len(name) >= 20:
            print("ERROR: name very long")
        else:
            cola.append(name)
    else:
        break

    i = i + 1


while j < len(cola):
    print(cola[j])
    j = j + 1





