#Ф-ия лямбда
radius = lambda Lstar, Lsun: (Lstar / Lsun) ** 0.5

def main():
    #Светимость солнца
    Lsun = 3.86 * 10**33
    #Ввод светимости звезды
    Lstar = float(input("Введите светимость звезды: "))
    #Радиус
    d = radius(Lstar, Lsun) * 149597870700

    print("Средний радиус обитаемой зоны в метрах:", d)

if __name__ == "__main__":
    main()
