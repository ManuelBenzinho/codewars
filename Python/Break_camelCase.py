""" Complete the solution so that the function will break up camel casing, using a space between words.

Example
"camelCasing"  =>  "camel Casing"
"identifier"   =>  "identifier"
""             =>  "" """

def solution(s):
  new_str=""
  if s.islower():
    return s
  else:
    for i in s:
      if i.isupper():
        new_str+=' '
      new_str+=i
    return new_str