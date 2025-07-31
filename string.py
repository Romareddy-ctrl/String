##check if all characters in a string are alphabets only
s=input('Enter a string: ')
if s.isalpha():
    print('All characters in a string are alphabets')
else:
    print('All Characters in string not alphabets')


#count totals words,characters,and spaces,in sentence
s=input('Enter a sentence: ')
words=len(s.split())
characters=len(s)
spaces=s.count(' ')
print('words: ',words)
print('characters:',characters)
print('spaces:',spaces)
    
#replace all vowels with *
s=input('Enter  a string: ')
vowels='aeiouAEIOU'
result=''
for char in s:
    if char in vowels:
       result+='*'
    else:
        result+=char
print(result)        


#count frequency of each character in string
s=input()
freq={}
for char in s:
    if char in freq:
        freq[char]+=1
    else:
         freq[char]=1
print(freq)         



#reverse a string without [::-1]
s=input()
reversed_str=' '.join(reversed(s))
print(reversed_str)


#print all characters at even and odd places
s=input('Enter a word: ')
even_place=''
odd_place=''
for index, char in enumerate(s):
    if index%2==0:
        even_place+=char
    else:
        odd_place+=char
print('Even place characters: ',even_place)
print('Odd place characters: ',odd_place)


#check string are unquie
s=input()
unique_chars=''
for char in s:
    if char not in unique_chars:
        unique_chars+=char
print('Unique:',unique_chars)        





























