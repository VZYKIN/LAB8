def  kbig(item):
   return item[1]

unordered = [('b', 'b'), ('c', 'd'), ('d', 'a'), ('a', 'c')]
unordered.sort(key=keyFunc, reverse = True)
print('Ordered list:', unordered)
