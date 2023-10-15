
from abc import ABC, abstractmethod

class Source(ABC):

  @abstractmethod
  def get_games():
    pass
  
  @abstractmethod
  def add_game():
    pass

class LocalFiles(Source):
  
  def get_games():
    return ([])
 
  def add_game():
    return {}


