import math
def main():
    #escribe tu código abajo de esta línea
    x1 = int(input("Dame x1: "))
    y1 = int(input("Dame y1: "))
    x2 = int(input("Dame X2: "))
    y2 = int(input("Dame y2: "))
    distancia = (math.hypot(x2-x1, y2-y1))
    print('distancia = '+str(round(distancia,2)))

if __name__ == '__main__':
    main()
