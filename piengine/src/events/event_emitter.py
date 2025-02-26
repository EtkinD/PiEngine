from . import KlavyeOlayi, FareOlayi

"""
    Base class for all event emitters
    Includes virtual methods for handling events
"""
class EventEmitter():
    def klavye_olayi(self, olay: KlavyeOlayi) -> None:
        """
            Virtual method to
            handle keyboard events
        """
        pass

    def fare_olayi(self, olay: FareOlayi) -> None:
        """
            Virtual method to
            handle mouse events
        """
        pass

