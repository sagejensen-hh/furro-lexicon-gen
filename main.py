import primitive.phonology as phono
import definitions.def_phonology as def_phono
import algorithm.pronunciation as prono
import random

# naive lexicon optimizer

def repr_pronunciation(pronunciation : list[type[phono.Iphoneme]]) -> str:
  return "".join([_p.glyph for _p in pronunciation])

class Lexeme:
  pronunciation : list[type[phono.IPhoneme]]
  
  def __init__(self, _pronunciation : list[type[phono.IPhoneme]]):
    self.pronunciation = _pronunciation
    
  @classmethod
  def new_from_random(clazz, phonology : phono.Phonology, max_length : int, candidates : int):
    return clazz(prono.new_pronunciation(phonology, max_length, candidates))
    
  @classmethod
  def new_from_merger(clazz, *args):
    _total = [_phon for _phon in _pron for _pron in args]
    return _total

class Lexicon:
  lexemes : set[Lexeme]
  phonology : phono.Phonology
  tick : int = 0
  action_weights : list[tuple[str, int]]

  def __init__(self, phonology : phono.Phonology, action_weights : list[tuple[str,int]] = [("nothing", 7), ("replace", 1), ("remove", 1), ("insert", 1)]):
    self.phonology = phonology
    self.action_weights = action_weights

  def evolve_pronunciation(self, pronunciation : list[type[phono.IPhoneme]]) -> list[type[phono.IPhoneme]]:
    _actions, _weights = zip(*self.action_weights)
    _new_prono = pronunciation.copy()
    _index = 0
    _old_cost = prono.get_pronunciation_cost(self.phonology, pronunciation)
    while _index < len(pronunciation):
      _solution = random.choices(_actions, weights = _weights)[0]
      _random_phoneme = prono.random_phonemes(self.phonology)[0]
      match _solution:
        case "nothing":
          _index += 1
          continue
        case "replace":
          _new_prono[_index] = _random_phoneme
          _index += 1
          continue
        case "remove":
          _new_prono.pop(_index)
        case "insert":
          _new_prono.insert(_index, _random_phoneme)
    _new_cost = prono.get_pronunciation_cost(self.phonology, _new_prono)
    if _old_cost > _new_cost:
      return _new_prono
    return pronunciation

  def cycle(self):
    for _lexeme in self.lexemes:
      _pronunciation = _lexeme.pronunciation
      _old = repr_pronunciation(_pronunciation)
      _pronunciation = self.evolve_pronunciation(_pronunciation)
      _new = repr_pronunciation(_pronunciation)
      print(_old, " -> ", _new)
    self.tick += 1

furro_lexicon = Lexicon(def_phono.phonology)
furro_lexicon.cycle()
