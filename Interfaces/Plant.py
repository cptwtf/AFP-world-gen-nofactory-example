from __future__ import annotations
from abc import ABC, abstractmethod


class Plant(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def do_plant_stuff(self):
        pass

    def get_name(self) -> str:
        return self.name
