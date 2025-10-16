# CIS-117 Lab2
# A collection of fun word operations
# Group# 5
# Names of all group members (first and last)
# James Hay
# Cristian Valverde

# print("Antics alive!")

def palindrome(text):
  return text.lower() == text.lower()[::-1]

def pangram(text):
  if len(text) < 26: return False
  text_letters = []
  for letter in text.lower():
    if not letter.isalpha():
      continue
    if letter in text_letters:
      continue
    text_letters.append(letter)
  return len(text_letters) == 26

def tautogram(text):
  letter = text[0].lower()
  for word in text.lower().split():
    if word[0] != letter:
      return False
  return True

def isogram(text):
  text_letters = []
  for letter in text.lower():
    if not letter.isalpha():
      continue
    if letter in text_letters:
      return False
    text_letters.append(letter)
  return True

def abecedarian(text):
  previous_letter = text[0].lower()
  for letter in text.lower():
    if letter < previous_letter:
      return False
    previous_letter = letter
  return True

def dobloon(text):
  count_once = []
  count_twice = []
  for letter in text.lower():
    if letter in count_twice:
      return False
    elif letter in count_once:
      count_twice.append(letter)
    else:
      count_once.append(letter)
  return len(count_once) == len(count_twice)
