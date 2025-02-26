from ..base import Drawable, Updateable
from .scene import Sahne
from ..events import EventDispatcher

"""
    Oyun sınıfı, oyunun başlığını, genişliğini ve yüksekliğini tutar.
    Ayrıca oyunun aktif sahnesini de tutar.
"""
class Oyun(EventDispatcher, Drawable, Updateable):
    def __init__(self, baslik: str = "'piengine' Oyunu", genislik: int = 800, yukseklik: int = 600) -> None:
        self.__title = baslik
        self.__width = genislik
        self.__height = yukseklik
        self.__scene = None
        self.__bg_color = (0, 0, 0)

    def guncelle(self, dt: float) -> None:
        if self.sahne:
            self.sahne.guncelle(dt)

    def ciz(self) -> None:
        if self.sahne:
            self.sahne.ciz()

    @property
    def baslik(self) -> str:
        return self.__title

    @property
    def genislik(self) -> int:
        return self.__width
    
    @property
    def yukseklik(self) -> int:
        return self.__height
    
    @property
    def sahne(self) -> Sahne:
        return self.__scene
    
    @sahne.setter
    def sahne(self, value: Sahne) -> None:
        if self.__scene:
            self.remove_event_listener(self.__scene)
        self.__scene = value
        self.add_event_listener(value)

    @property
    def arka_plan_rengi(self) -> tuple[int, int, int]:
        return self.__bg_color
    
    @arka_plan_rengi.setter
    def arka_plan_rengi(self, value: tuple[int, int, int]) -> None:
        self.__bg_color = (
            min(max(value[0], 0), 255),
            min(max(value[1], 0), 255),
            min(max(value[2], 0), 255)
            )

    def __str__(self) -> str:
        res = f"Oyun: {self.__title}"
        if self.sahne:
            res += f"\nSahne: {self.sahne.isim}"
        res += f"\nEkran boyutu: ({self.__width}X{self.__height})"
        return res

