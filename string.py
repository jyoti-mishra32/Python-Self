#str1 = "This is a strings"
#str2 = 'this is a string'
#str3 = """this is a string"""

str1 = "This is a string. \nwe are creating it in python."
print(str1)

#Basic operations:-
#concatenation
str1 = "Apna"
str2 = "College"
print(str1+str2)


#length
str1 = "Apna"
len1 = len(str1)
print(len1)

str2 = "College"
len2 = len(str2)
print(len2)

final_str = str1 + " " + str2
print(final_str)
print(len(final_str))


#Indexing
str = "Apnna college"
ch = str[0]
print(ch)


#Slicing
str = "apna college"
print(str[1:4])
print(str[:4])    #[0:4]
print(str[5:])    #[5:len(str)]


str = "apple"
print(str[-3:-1])