krediler = ["Hızlı Kredi", "Maaşını Halkbank'tan alanlara özel", "Mutlu Emekliler"]

#alias
for kredi3 in krediler:#dongu sırasıyla nereyi gezeceğini gösterir(yazdığımız listeyi gezer)
    print(kredi3)#gezdiği yerleri ekrana yazdırmak için bir değer verdik o değeri yazdırdık. kredi3 yerine gamze de çiçek de yazılır. takma isim verildi

for i in range(10):#10 kere tekrarlanacak döngü
  print(i)

for i in range(len(krediler)):
  print(krediler[i])

for i in range(3,10): #3 ile 10 arasındaki sayıları yazdırır
  print(i)

for i in range(0,10,2) : #0 ile 10 arasındaki sayıları 2 er 2 er yazdırır
  print(i)