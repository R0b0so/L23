list1=[10,20,30,40,50]
list2=[100,200,300,400,500]
for x, y in zip(list1, list2[::-1]):
   print(x,y)
words=["hello","world","hi","apple"]
numbers=[234,345,7544,927]
new_dict = {words: numbers for words,
            numbers in zip (numbers, words)}
print('{}'.format(new_dict))