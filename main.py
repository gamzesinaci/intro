print("İlk Sayfa")
krediler = ["Hızlı Kredi", "Maaşını Halkbank'tan alanlara özel", "Mutlu Emekliler"]

#alias
for kredi3 in krediler:
  print("<option>"+kredi3+"<option>")

print("İkinci Sayfa")

krediler = ["Hızlı Kredi", "Maaşını Halkbank'tan alanlara özel", "Mutlu Emekliler"]

#alias
for kredi3 in krediler:
    print("<option>"+kredi3+"<option>")

print("Üçüncü Sayfa")
krediler = ["Hızlı Kredi", "Maaşını Halkbank'tan alanlara özel", "Mutlu Emekliler"]

#alias
for kredi3 in krediler:
    print("<option>"+kredi3+"<option>")

#bu şekil 3 kere ayrı ayrı yazmak yerine fonksiyon oluştur

def kredileriListele():#fonksiyonu tanımladık
  krediler = ["Hızlı Kredi", "Maaşını Halkbank'tan alanlara özel", "Mutlu Emekliler"]
  for kredi in krediler:
    print("<option>"+kredi+"<option>")
kredileriListele()#fonsksiyonu çağırdık