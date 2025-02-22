# we need to have two interfaces 1 for observable, 1 for observer 
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

# we need to have following things for 
# Interface for observer
class IObserver(ABC):
    @abstractmethod
    def update(self):
        pass

    @property
    @abstractmethod
    def Observable(self):
        pass

# Interface Observable
class IObservable(ABC):
    # this class should have following things
    # list of observers
    # Notify Methods
    # data property
    # add and remove methods for lifecycle of observers
    @property
    @abstractmethod
    def News(self) -> str:
        pass

    @property
    @abstractmethod
    def Observers(self) -> List[IObserver]:
        pass

    @abstractmethod
    def AddObserver(self, observer: IObserver):
        pass

    @abstractmethod
    def RemoveObserver(self, observer: IObserver):
        pass

    @abstractmethod
    def Notify(self):
        pass

    @abstractmethod
    def updateData(self, LatestNews: str):
        pass

class NTV(IObservable):
    def __init__(self):
        self._news = "Nothing yet."
        self._observers = []

    @property
    def News(self) -> str:
        return self._news

    @News.setter
    def News(self, value: str):
        self._news = value

    @property
    def Observers(self) -> List[IObserver]:
        return self._observers

    def AddObserver(self, observer: IObserver):
        self._observers.append(observer)

    def RemoveObserver(self, observer: IObserver):
        self._observers.remove(observer)

    def updateData(self, LatestNews: str):
        self.News = LatestNews
        self.Notify()

    def Notify(self):
        for observer in self.Observers:
            observer.update()

class Prekshakudu(IObserver):
    def __init__(self, Observable: IObservable, name: str):
        self._observable = Observable
        self.name = name

    @property
    def Observable(self):
        return self._observable

    @Observable.setter
    def Observable(self, value: IObservable):
        self._observable = value

    def update(self):
        print(f"from Prekshakudu {self.name}: {self.Observable.News}")

# creating observable first
ntv: IObservable = NTV()

# creating observers
prekshaka1: IObserver = Prekshakudu(ntv, "first")
prekshaka2: IObserver = Prekshakudu(ntv, "second")
prekshaka3: IObserver = Prekshakudu(ntv, "third")
prekshaka4: IObserver = Prekshakudu(ntv, "fourth")

# updating or subscribing in observable
ntv.AddObserver(prekshaka1)
ntv.AddObserver(prekshaka2)
ntv.AddObserver(prekshaka3)
ntv.AddObserver(prekshaka4)

ntv.Notify()
ntv.updateData("Breaking News 1")

ntv.RemoveObserver(prekshaka2)
ntv.updateData("Breaking News 2")
