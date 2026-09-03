import primitive.phonology as phono
import algorithm.pronunciation as pronun

### PHONEME LIBRARY

# Declare a phonology
phonology = phono.Phonology()

# Vowels

class UnroundedCloseFrontVowel(phono.IVowel):
  glyph = "i"
  openness = phono.OPENNESS.CLOSE
  backness = phono.BACKNESS.FRONT
  rounding = False
  syllable = phono.SYLLABLE.NUCLEUS
  probability = 3
phonology.phoneme_set.add(UnroundedCloseFrontVowel)

class RoundedCloseFrontVowel(phono.IVowel):
  glyph = "y"
  openness = phono.OPENNESS.CLOSE
  backness = phono.BACKNESS.FRONT
  rounding = True
  syllable = phono.SYLLABLE.NUCLEUS
  probability = 3
phonology.phoneme_set.add(RoundedCloseFrontVowel)
  
class RoundedCloseBackVowel(phono.IVowel):
  glyph = "u"
  openness = phono.OPENNESS.CLOSE
  backness = phono.BACKNESS.BACK
  rounding = True
  syllable = phono.SYLLABLE.NUCLEUS
phonology.phoneme_set.add(RoundedCloseBackVowel)

class UnroundedNearCloseNearFrontVowel(phono.IVowel):
  glyph = "ɪ"
  openness = phono.OPENNESS.NEARCLOSE
  backness = phono.BACKNESS.NEARFRONT
  rounding = False
  syllable = phono.SYLLABLE.NUCLEUS
  probability = 3
phonology.phoneme_set.add(UnroundedNearCloseNearFrontVowel)

class RoundedNearCloseNearFrontVowel(phono.IVowel):
  glyph = "ʏ"
  openness = phono.OPENNESS.NEARCLOSE
  backness = phono.BACKNESS.NEARFRONT
  rounding = True
  syllable = phono.SYLLABLE.NUCLEUS
  probability = 3
phonology.phoneme_set.add(RoundedNearCloseNearFrontVowel)

class UnroundedCloseMidFrontVowel(phono.IVowel):
  glyph = "e"
  openness = phono.OPENNESS.CLOSEMID
  backness = phono.BACKNESS.FRONT
  rounding = False
  syllable = phono.SYLLABLE.NUCLEUS
  probability = 3
phonology.phoneme_set.add(UnroundedCloseMidFrontVowel)

class RoundedCloseMidFrontVowel(phono.IVowel):
  glyph = "ø"
  openness = phono.OPENNESS.CLOSEMID
  backness = phono.BACKNESS.FRONT
  rounding = True
  syllable = phono.SYLLABLE.NUCLEUS
  probability = 3
phonology.phoneme_set.add(RoundedCloseMidFrontVowel)

class RoundedCloseMidBackVowel(phono.IVowel):
  glyph = "o"
  openness = phono.OPENNESS.CLOSEMID
  backness = phono.BACKNESS.BACK
  rounding = True
  syllable = phono.SYLLABLE.NUCLEUS
  probability = 3
phonology.phoneme_set.add(RoundedCloseMidBackVowel)

class UnroundedOpenMidBackVowel(phono.IVowel):
  glyph = "ʌ"
  openness = phono.OPENNESS.OPENMID
  backness = phono.BACKNESS.BACK
  rounding = False
  syllable = phono.SYLLABLE.NUCLEUS
  probability = 3
phonology.phoneme_set.add(UnroundedOpenMidBackVowel)

class UnroundedOpenFrontVowel(phono.IVowel):
  glyph = "a"
  openness = phono.OPENNESS.OPEN
  backness = phono.BACKNESS.FRONT
  rounding = False
  syllable = phono.SYLLABLE.NUCLEUS
  probability = 3
phonology.phoneme_set.add(UnroundedOpenFrontVowel)

class RoundedOpenFrontVowel(phono.IVowel):
  glyph = "ɶ"
  openness = phono.OPENNESS.OPEN
  backness = phono.BACKNESS.FRONT
  rounding = True
  syllable = phono.SYLLABLE.NUCLEUS
phonology.phoneme_set.add(RoundedOpenFrontVowel)

class UnroundedOpenBackVowel(phono.IVowel):
  glyph = "ɑ"
  openness = phono.OPENNESS.OPEN
  backness = phono.BACKNESS.BACK
  rounding = False
  syllable = phono.SYLLABLE.NUCLEUS
  probability = 3
phonology.phoneme_set.add(UnroundedOpenBackVowel)
  
class RoundedOpenBackVowel(phono.IVowel):
  glyph = "ɒ"
  openness = phono.OPENNESS.OPEN
  backness = phono.BACKNESS.BACK
  rounding = True
  syllable = phono.SYLLABLE.NUCLEUS
  probability = 3
phonology.phoneme_set.add(RoundedOpenBackVowel)
  
# Consonants

class VoicedAlveolarNasalConsonant(phono.IConsonant):
  glyph = "n"
  place = phono.PLACE.ALVEOLAR
  manner = phono.MANNER.NASAL
  voicing = True
  syllable = phono.SYLLABLE.CODA
phonology.phoneme_set.add(VoicedAlveolarNasalConsonant)
  
class VoicedAlveolarPlosiveConsonant(phono.IConsonant):
  glyph = "d"
  place = phono.PLACE.ALVEOLAR
  manner = phono.MANNER.PLOSIVE
  voicing = True
  syllable = phono.SYLLABLE.ONSET
phonology.phoneme_set.add(VoicedAlveolarPlosiveConsonant)

class UnvoicedRetroflexPlosiveConsonant(phono.IConsonant):
  glyph = "ʈ"
  place = phono.PLACE.RETROFLEX
  manner = phono.MANNER.PLOSIVE
  voicing = False
  syllable = phono.SYLLABLE.ONSET
phonology.phoneme_set.add(UnvoicedRetroflexPlosiveConsonant)

class UnvoicedVelarPlosiveConsonant(phono.IConsonant):
  glyph = "k"
  place = phono.PLACE.VELAR
  manner = phono.MANNER.PLOSIVE
  voicing = False
  syllable = phono.SYLLABLE.ONSET
phonology.phoneme_set.add(UnvoicedVelarPlosiveConsonant)

class VoicedVelarPlosiveConsonant(phono.IConsonant):
  glyph = "g"
  place = phono.PLACE.VELAR
  manner = phono.MANNER.PLOSIVE
  voicing = True
  syllable = phono.SYLLABLE.ONSET
phonology.phoneme_set.add(VoicedVelarPlosiveConsonant)

class UnvoicedDentalNonsibilantFricativeConsonant(phono.IConsonant):
  glyph = "θ"
  place = phono.PLACE.DENTAL
  manner = phono.MANNER.NONSIBILANTFRICATIVE
  voicing = False
  syllable = phono.SYLLABLE.CODA
phonology.phoneme_set.add(UnvoicedDentalNonsibilantFricativeConsonant)

class UnvoicedAlveolarSibilantFricativeConsonant(phono.IConsonant):
  glyph = "s"
  place = phono.PLACE.ALVEOLAR
  manner = phono.MANNER.SIBILANTFRICATIVE
  voicing = False
  syllable = phono.SYLLABLE.CODA
phonology.phoneme_set.add(UnvoicedAlveolarSibilantFricativeConsonant)

class UnvoicedPostAlveolarSibilantFricativeConsonant(phono.IConsonant):
  glyph = "ʃ"
  place = phono.PLACE.POSTALVEOLAR
  manner = phono.MANNER.SIBILANTFRICATIVE
  voicing = False
  syllable = phono.SYLLABLE.CODA
phonology.phoneme_set.add(UnvoicedPostAlveolarSibilantFricativeConsonant)

class VoicedPostAlveolarSibilantFricativeConsonant(phono.IConsonant):
  glyph = "ʒ"
  place = phono.PLACE.POSTALVEOLAR
  manner = phono.MANNER.SIBILANTFRICATIVE
  voicing = True
  syllable = phono.SYLLABLE.CODA
phonology.phoneme_set.add(VoicedPostAlveolarSibilantFricativeConsonant)

class UnvoicedRetroflexSibilantFricativeConsonant(phono.IConsonant):
  glyph = "ʂ"
  place = phono.PLACE.RETROFLEX
  manner = phono.MANNER.SIBILANTFRICATIVE
  voicing = False
  syllable = phono.SYLLABLE.CODA
phonology.phoneme_set.add(UnvoicedRetroflexSibilantFricativeConsonant)

class UnvoicedVelarNonsibilantFricativeConsonant(phono.IConsonant):
  glyph = "x"
  place = phono.PLACE.VELAR
  manner = phono.MANNER.NONSIBILANTFRICATIVE
  voicing = False
  syllable = phono.SYLLABLE.CODA
phonology.phoneme_set.add(UnvoicedVelarNonsibilantFricativeConsonant)

class UnvoicedUvularNonsibilantFricativeConsonant(phono.IConsonant):
  glyph = "χ"
  place = phono.PLACE.VELAR
  manner = phono.MANNER.NONSIBILANTFRICATIVE
  voicing = False
  syllable = phono.SYLLABLE.CODA
phonology.phoneme_set.add(UnvoicedUvularNonsibilantFricativeConsonant)

class VoicedUvularNonsibilantFricativeConsonant(phono.IConsonant):
  glyph = "ʁ"
  place = phono.PLACE.VELAR
  manner = phono.MANNER.NONSIBILANTFRICATIVE
  voicing = True
  syllable = phono.SYLLABLE.CODA
phonology.phoneme_set.add(VoicedUvularNonsibilantFricativeConsonant)

class VoicedAlveolarLateralApproximantConsonant(phono.IConsonant):
  glyph = "l"
  place = phono.PLACE.ALVEOLAR
  manner = phono.MANNER.LATERALAPPROXIMANT
  voicing = True
  syllable = phono.SYLLABLE.GLIDE
phonology.phoneme_set.add(VoicedAlveolarLateralApproximantConsonant)

class VoicedRetroflexApproximantConsonant(phono.IConsonant):
  glyph = "r"
  place = phono.PLACE.RETROFLEX
  manner = phono.MANNER.APPROXIMANT
  voicing = True
  syllable = phono.SYLLABLE.GLIDE
phonology.phoneme_set.add(VoicedRetroflexApproximantConsonant)

## This is how we make a phonological rule.
## WARNING: You should NOT instantiate a phonological rule. These are *static classes.*
## Using instances of a phonological rule will lead to fatal errors or unintended behavior.

class PENALTY():
  NONE = 0 # Follows phonotactics perfectly
  SMALL = 2 # Not ideal, but still fits
  MEDIUM = 5 # Uncomfortable for ferrets to say
  LARGE = 15 # Avoid words of this penalty
  INSANE = 50 # Immediately Improve

class SIZE():
  NOTHING = 0
  TINY = 1
  SMALL = 3
  MEDIUM = 6
  LARGE = 12
  INSANE = 20

class OptimizeSize(phono.IPhonologyRule):
  def get_penalty(pronunciation : list[type[phono.IPhoneme]]):
    pronunciation_length = len(pronunciation)
    if pronunciation_length <= SIZE.NOTHING:
      raise Exception(f"Pronunciation cannot have a size of zero or lower. ({pronunciation_length})")
    if pronunciation_length <= SIZE.TINY:
      return PENALTY.LARGE
    if pronunciation_length <= SIZE.SMALL:
      return PENALTY.SMALL
    if pronunciation_length <= SIZE.MEDIUM:
      return PENALTY.NONE
    if pronunciation_length <= SIZE.LARGE:
      return PENALTY.SMALL
    if pronunciation_length <= SIZE.INSANE:
      return PENALTY.MEDIUM
    return PENALTY.INSANE
phonology.phonology_rule_set.add(OptimizeSize)

class SyllableCheck(phono.IPhonologyRule):
  pattern = (phono.SYLLABLE.ONSET, phono.SYLLABLE.GLIDE, phono.SYLLABLE.NUCLEUS, phono.SYLLABLE.CODA)
  def get_follows_pattern(phoneme : type[phono.IPhoneme], index : int):
    pattern = SyllableCheck.pattern
    flag = pattern[index]
    optional = phoneme.syllable & phono.SYLLABLE.OPTIONAL
    passes = optional or (phoneme.syllable & flag)
    return bool(passes)
  def get_penalty(pronunciation : list[type[phono.IPhoneme]]):
    penalty = 0
    pattern_index = 0
    for phoneme in pronunciation:
      follows_pattern = SyllableCheck.get_follows_pattern(phoneme, pattern_index)
      if not follows_pattern:
        penalty += PENALTY.MEDIUM
        continue
      pattern_index += 1
      pattern_index %= len(SyllableCheck.pattern)
    return penalty / len(pronunciation)
phonology.phonology_rule_set.add(SyllableCheck)
