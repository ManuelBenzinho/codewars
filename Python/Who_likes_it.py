""" You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items. We want to create the text that should be displayed next to such an item.

Implement the function which takes an array containing the names of people that like an item. It must return the display text as shown in the examples:

[]                                -->  "no one likes this"
["Peter"]                         -->  "Peter likes this"
["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"
Note: For 4 or more names, the number in "and 2 others" simply increases. """

def likes(names):
  if len(names) == 0:
    result = "no one likes this"
  elif len(names) == 1:
    result =f"{names[-1]} likes this"
  elif len(names) > 1 and len(names) < 4:
      result =", ".join(names[:-1]) + f" and {names[-1]} like this"
  elif len(names) >= 4:
      result =", ".join(names[:2]) + f" and {len(names) - 2} others like this"
  return result