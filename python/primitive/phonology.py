from enum import Enum, Flag, auto

class IPhoneme:
  glyph : str = "?"
  probability : int = 5

class IPhonemeProperty:
  def __init_subclass__(cls, /, property_name : str, default):
    setattr(cls, property_name, default)
    setattr(cls, "__init_subclass__", lambda: None)

class IPhonologyRule:
  def get_cost(pronunciation : list[type[IPhoneme]]) -> float:
    return 0

class Phonology:
  phoneme_set : set[type[IPhoneme]]
  phonology_rule_set : set[type[IPhonologyRule]]
  def __init__(self):
    self.phoneme_set = set()
    self.phonology_rule_set = set()

# some predefined values for convenience

class OPENNESS(Enum):
  CLOSE = auto()
  NEARCLOSE = auto()
  CLOSEMID = auto()
  MID = auto()
  OPENMID = auto()
  NEAROPEN = auto()
  OPEN = auto()

class BACKNESS(Enum):
  FRONT = auto()
  NEARFRONT = auto()
  CENTRAL = auto()
  NEARBACK = auto()
  BACK = auto()

class PLACE(Enum):
  BILABIAL = auto()
  LABIODENTAL = auto()
  LINGUOLABIAL = auto()
  DENTAL = auto()
  ALVEOLAR = auto()
  POSTALVEOLAR = auto()
  RETROFLEX = auto()
  PALATAL = auto()
  VELAR = auto()
  UVULAR = auto()
  PHARYNGEAL = auto()
  GLOTTAL = auto()

class MANNER(Enum):
  NASAL = auto()
  PLOSIVE = auto()
  SIBILANTAFFRICATE = auto()
  NONSIBILANTAFFRICATE = auto()
  SIBILANTFRICATIVE = auto()
  NONSIBILANTFRICATIVE = auto()
  APPROXIMANT = auto()
  TAP = auto()
  TRILL = auto()
  LATERALAFFRICATE = auto()
  LATERALFRICATIVE = auto()
  LATERALAPPROXIMANT = auto()
  LATERALTAP = auto()

class SYLLABLE(Flag):
  ONSET = auto()
  GLIDE = auto()
  NUCLEUS = auto()
  CODA = auto()

  OPTIONAL = auto()

class OpennessProperty(IPhonemeProperty, property_name = "openness", default = OPENNESS.MID): pass
class BacknessProperty(IPhonemeProperty, property_name = "backness", default = BACKNESS.CENTRAL): pass
class PlaceProperty(IPhonemeProperty, property_name = "place", default = PLACE.RETROFLEX): pass
class MannerProperty(IPhonemeProperty, property_name = "manner", default = MANNER.APPROXIMANT): pass
class RoundingProperty(IPhonemeProperty, property_name = "rounding", default = False): pass
class VoicingProperty(IPhonemeProperty, property_name = "voicing", default = False): pass
class SyllableProperty(IPhonemeProperty, property_name = "syllable", default = SYLLABLE.ONSET | SYLLABLE.OPTIONAL): pass

class IConsonant(IPhoneme, PlaceProperty, MannerProperty, VoicingProperty, SyllableProperty): pass
class IVowel(IPhoneme, OpennessProperty, BacknessProperty, RoundingProperty, SyllableProperty) : pass
