import re

a = "sdhjdfq12123sdfklsdjklfklj"

x = re.findall(r'\d+', a)
print(x)


j = re.findall(r'[a-z]', a)
print(j)

#why we use r: to overcountr escape sequence so that it will not throw error during multiple backslashes (misinterpreting of backslashes )
# if we keep it same then we have to use more backslashes to avoid collide

y = re.findall('\\d+', a)
print(y)


txt = "The rain in Spain"
x = re.search("\\bS\\w+", txt)
print(x.string)
