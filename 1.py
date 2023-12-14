def harflar_uzb(a):
    raqamlar = {
        "1": "Bir", "2": "Ikki", "3": "Uch", "4": "To'rt", "5": "Besh", "6": "Olti",
        "7": "Yetti", "8": "Sakkiz", "9": "To'qqiz",
    }
    onliklar = {
        "10": "O'n", "20": "Yigirma", "30": "O'ttiz", "40": "Qirq", "50": "Ellik",
        "60": "Oltmish", "70": "Yetmish", "80": "Sakson", "90": "To'qson"
    }

    SONLAR = str(a)
    UZUNLIK = len(SONLAR)
    harf = []
    if SONLAR=="0":
        print("Nol")

    elif UZUNLIK == 1:
        harf.append(raqamlar.get(SONLAR, ""))

    elif UZUNLIK == 2:
        harf.append(onliklar.get(SONLAR[0] + "0", ""))
        harf.append(raqamlar.get(SONLAR[1], ""))

    elif UZUNLIK == 3:
        harf.append(raqamlar.get(SONLAR[0], "") + " Yuz")
        harf.append(onliklar.get(SONLAR[1] + "0", ""))
        harf.append(raqamlar.get(SONLAR[2], ""))

    elif UZUNLIK == 4:
        harf.append(raqamlar.get(SONLAR[0], "") + " Ming")
        harf.append(raqamlar.get(SONLAR[1], "") + " Yuz")
        harf.append(onliklar.get(SONLAR[2] + "0", ""))
        harf.append(raqamlar.get(SONLAR[3], ""))

    elif UZUNLIK == 5:
        harf.append(onliklar.get(SONLAR[0] + "0", ""))
        harf.append(raqamlar.get(SONLAR[1], "") + " Ming")
        harf.append(raqamlar.get(SONLAR[2], "") + " Yuz")
        harf.append(onliklar.get(SONLAR[3] + "0", ""))
        harf.append(raqamlar.get(SONLAR[4], ""))

    elif UZUNLIK == 6:
        harf.append(raqamlar.get(SONLAR[0], "") + " Yuz")
        harf.append(onliklar.get(SONLAR[1] + "0", ""))
        harf.append(raqamlar.get(SONLAR[2], "") + " Ming")
        harf.append(raqamlar.get(SONLAR[3], "") + " Yuz")
        harf.append(onliklar.get(SONLAR[4] + "0", ""))
        harf.append(raqamlar.get(SONLAR[5], ""))

    elif UZUNLIK == 7:
        harf.append(raqamlar.get(SONLAR[0], "") + " Million")
        harf.append(raqamlar.get(SONLAR[1], "") + " Yuz")
        harf.append(onliklar.get(SONLAR[2] + "0", ""))
        harf.append(raqamlar.get(SONLAR[3], "") + " Ming")
        harf.append(raqamlar.get(SONLAR[4], "") + " Yuz")
        harf.append(onliklar.get(SONLAR[5] + "0", ""))
        harf.append(raqamlar.get(SONLAR[6], ""))

    elif UZUNLIK == 8:
        harf.append(onliklar.get(SONLAR[0] + "0", ""))
        harf.append(raqamlar.get(SONLAR[1], "") + " Million")
        harf.append(raqamlar.get(SONLAR[2], "") + " Yuz")
        harf.append(onliklar.get(SONLAR[3] + "0", ""))
        harf.append(raqamlar.get(SONLAR[4], "") + " Ming")
        harf.append(raqamlar.get(SONLAR[5], "") + " Yuz")
        harf.append(onliklar.get(SONLAR[6] + "0", ""))
        harf.append(raqamlar.get(SONLAR[7], ""))


    return " ".join(harf)



a=int(input("Sonni kiriting"))
result = harflar_uzb(a)
print(result)    




