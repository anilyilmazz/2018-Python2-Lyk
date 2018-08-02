import csv


def pythonistanbul():
    toplam = 0
    sira = 0
    with open("yazilimci-maaslari.csv") as csvfile:
        reader = csv.reader(csvfile)
        for item in (reader):
            if "İstanbul" in item and "Junior" in item[1]:
                sira = sira + 1
                toplam = toplam + int(item[5].split(" ")[0].replace(".", ""))
                try:
                    toplam = toplam + int(item[5].split(" ")[3].replace(".", ""))
                except:
                    toplam = 2000 + toplam

    print(int((toplam / sira) / 2))

def sehir(sehir):
    toplam = 0
    sira = 0

    if sehir[0] not in ["i", "İ"]:
        sehir = sehir.upper()[0] + sehir[1:]
    else:
        sehir = 'İ' + sehir[1:]

    with open("yazilimci-maaslari.csv") as csvfile:
        reader = csv.reader(csvfile)
        for item in (reader):
            if str(sehir) in item :
                sira = sira + 1
                toplam = toplam + int(item[5].split(" ")[0].replace(".", ""))
                try:
                    toplam = toplam + int(item[5].split(" ")[3].replace(".", ""))
                except:
                    toplam = 2000 + toplam
    try:
        print(int((toplam / sira) / 2))
    except ZeroDivisionError:
        print(sehir+" iline ait maaş ortalaması bulunamadı.")


pythonistanbul()


