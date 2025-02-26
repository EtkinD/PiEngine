from __future__ import annotations
from .event_emitter import EventEmitter
from .event import Event
from .keyboard_event import KlavyeOlayi
from .mouse_event import FareOlayi

"""
    EventDispatcher virutal class
    This class is used to dispatch events to the listeners
"""
class EventDispatcher():
    # TODO: Create constructor
    __event_listeners: list[EventEmitter | EventDispatcher] = []

    def add_event_listener(self, listener: EventEmitter | EventDispatcher) -> None:
        """
            Add an event listener to the dispatcher
        """
        self.__event_listeners.append(listener)
    
    def remove_event_listener(self, listener: EventEmitter | EventDispatcher) -> None:
        """
            Remove an event listener from the dispatcher
        """
        self.__event_listeners.remove(listener)
    
    def dispatch_event(self, event: Event) -> None:
        for listener in self.__event_listeners:
            if isinstance(listener, EventEmitter):
                if isinstance(event, KlavyeOlayi):
                    listener.klavye_olayi(event)
                elif isinstance(event, FareOlayi):
                    listener.fare_olayi(event)
                else:
                    raise ValueError("Event type not supported")
            if isinstance(listener, EventDispatcher):
                listener.dispatch_event(event)

