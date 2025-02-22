from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

#Reference used
#https://refactoring.guru/
#context Object
#which will call the strategy object which will do one particular functionality but with many ways as suggested by the client.
class Context:

    def __init__(self,strategy:Strategy)->None:
        """This context accepts the strategy through contructor injection or """
        self._strategy=strategy
    @property
    def strategy(self)->Strategy:
        return self._strategy
    @strategy.setter
    def strategy(self,strategy:Strategy)->None:
        self._strategy=strategy
    def do_some_business_logic(self)->None:
        result=self._strategy.do_algorithm(["a","b","c","d"])  
        print(",".join(result))

class Strategy(ABC):
    @abstractmethod
    def do_algorithm(self,data:List):
        pass
class ConceteStrategyA(Strategy):
    def do_algorithm(self, data:List)->List:
        return sorted(data)
class ConcreteStragtegyB(Strategy):
    def do_algorithm(self,data:List)->List:
        return reversed(sorted(data))
if __name__=="__main__":
    context=Context(ConceteStrategyA())
    context.do_some_business_logic()
    print()
    context.strategy=ConcreteStragtegyB()
    context.do_some_business_logic()