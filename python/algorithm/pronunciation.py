import primitive.phonology as phono
import random

def get_pronunciation_cost(phonology : phono.Phonology, pronunciation : list[type[phono.IPhoneme]]) -> int:
  _rules = phonology.phonology_rule_set
  _penalty = 0
  for rule in _rules:
    _cost = rule.get_penalty(pronunciation)
    _penalty += _cost
  return _penalty

def random_phonemes(phonology : phono.Phonology, count : int = 1) -> type[phono.IPhoneme]:
  _phonemes = list(phonology.phoneme_set)
  _phoneme_weight_cache = [_phon.probability for _phon in phonology.phoneme_set]
  _word = random.choices(_phonemes, _phoneme_weight_cache, k = _word_length)
  return _word
  
def new_pronunciation(phonology : phono.Phonology, max_length : int = 20, maximum_search : int = 50) -> list[type[phono.IPhoneme]]:
  _best_candidate : list[type[phono.IPhoneme]] = []
  _best_candidate_cost = 0

  for _iter in range(maximum_search):
    _word_length = random.randrange(1, max_length + 1)
    _word = random_phonemes(phonology, _word_length)
    _cost = get_pronunciation_cost(phonology, _word)
    if _best_candidate == [] or _cost < _best_candidate_cost:
      _best_candidate = _word
      _best_candidate_cost = _cost
  return _best_candidate
