import picengine as pg

genislik = 800
yukseklik = 600

oyun = pg.Oyun("Benim İlk Oyunum", genislik, yukseklik)
oyun.arka_plan_rengi = (68, 6, 144)

sahne = pg.Sahne("ilk sahnem")

yazi1 = pg.Yazi("Merhaba, dünya!")
yazi2 = pg.Yazi("Selamlar!", x=50, y=50)

sahne.ekle(yazi1)
sahne.ekle(yazi2)

oyun.sahne = sahne

pg.baslat(oyun)
