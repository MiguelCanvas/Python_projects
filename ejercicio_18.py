# // You get an array of numbers, return the sum of all of the positives ones.

# // Example [1,-4,7,12] => 1 + 7 + 12 = 20

# // Note: if there is nothing to sum, the sum is default to 0.



suarray = [10,1,-5,-9,-15]

def numeroCompleto(array):
    contador = 0

    def positivo(numero):
        return numero > 0
    newArray = list(filter(positivo,array))

    for x in newArray:
        contador += x

    return contador



print(numeroCompleto(suarray))