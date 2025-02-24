import picengine as pg

genislik = 800
yukseklik = 600

oyun = pg.Oyun("Nesneler ile oyun", genislik, yukseklik)
oyun.arka_plan_rengi = (68, 6, 144)
sahne = pg.Sahne("ilk sahnem")

yazi1 = pg.Yazi("Merhaba, dünya!")
yazi2 = pg.Yazi("Selamlar!", x=50, y=50)

kedi = pg.Nesne("kedi.png", x=0, y=100, genislik=220, yukseklik=110)

def guncelle(dt):
    kedi.x += 100 * dt

kedi.guncelle = guncelle
sahne.ekle(kedi)

sahne.ekle(yazi1)
sahne.ekle(yazi2)

oyun.sahne = sahne

pg.baslat(oyun)
