baslik = "Haberiniz olsun! "  #python ile tek tırnak içerisinde de yazılabilir
vade = 12  #sayısal veri tırnaksız yazılır
faizOrani1 = 1.47
faizOranı2 = 1.44
faizOranı = 1.47

print(baslik)
print(type(baslik))
print(type(vade))
print(type(faizOrani1))

mesaj = "Hoşgeldin"
musteriAdi = "Ahmet"
musteriSoyadi = "Yılmaz"

print(mesaj + " " + musteriAdi + " " +
      musteriSoyadi)  #yazılar bitişik olmasın diye çift boş tırnak koyuldu

mesaj = "Hoşgeldin"
musteriAdi = "Ahmet"
musteriSoyadi = "Yılmaz"
sonucMesaj = mesaj + " " + musteriAdi + " " + musteriSoyadi  #verilerideğişkende tutup hepsini tek tek yazmak yerine değişken tanımlayabilirz
print(sonucMesaj)
