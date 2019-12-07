>>>x=[10,20,30,40]
>>>x=['Crunchy frog','ram bladder']
x=['spam',2.0,5,[10,20]]
x=[]


>>>numbers=[17,123]
>>>numbers[1]=15
>>>print(numbers)

>>>a=[1,2,3]
>>>b=[4,5,6]
>>>c=a+b
>>>print(c)

>>>[0]*4

[1,2,3]*3


>>>t=['a','b','c','d','e','f']
>>>t[1:3]

>>t=['a','b','c','d']
>>>t.append('e')
>>>print(t)


>>>t=['b','d','e','a']
>>>t.sort()

>>>t=['a','b','c','d','e','f']
>>>del t[1:5]
>>>print(t)


>>>s='spam'
>>>t=list(s)
>>>print(t)

>>>a=[1,2,3]
>>>b=a
>>>b is a


>>>orig=t[ : ]
>>>t.sort()


>>>for line in fhand
>>>      words =line.split()
>>>      print('Debug:',words)
>>>      if words[0]!'From'
>>>       print(words[2])

>>>my_list = []
>>>fhand = open('romeo.txt')
>>>for line in fhand:
>>>    words = line.split()              
>>>    for word in words:
>>>        if word in my_list:
>>>            continue                    
>>>       my_list.append(word)        
>>>print(sorted(my_list))   


        fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    words = line.split()
    if len(words) < 3 or words[0] != 'From':
        continue
    print(words[1])
    count += 1
print(count)



my_list = []                        
while True:
    number = 0.0
    input_number = input('Enter a number: ')
    if input_number == 'done':
        break

    try:
        number = float(input_number)
    except ValueError:
        print('Invalid input')
        quit()

    my_list.append(input_number)

print('Maximum: ', max(my_list))




