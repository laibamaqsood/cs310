count = 0
dictionary_words = dict()                
fhand = open('words.txt')
for line in fhand:
    words = line.split()
    for word in words:
        count += 1
        if word in dictionary_words:
            continue                      
        dictionary_words[word] = count   

if 'Python' in dictionary_words:
    print('True')
    else:
    print('False')
    
    
dictionary_days = dict()                      
fname = input('Enter a file name: ')
try:
    fhand = open(fname)
except FileNotFoundError:
    print('File cannot be opened:', fname)
    exit()

for line in fhand:
    words = line.split()
    if len(words) < 3 or words[0] != 'From':
        continue
    else:
        if words[2] not in dictionary_days:
            dictionary_days[words[2]] = 1       
        else:
            dictionary_days[words[2]] += 1     

print(dictionary_days)

dictionary_addresses = dict()                
fname = input('Enter file name: ')
try:
    fhand = open(fname)
except FileNotFoundError:
    print('File cannot be opened:', fname)
    exit()

for line in fhand:
    words = line.split()
    if len(words) < 2 or words[0] != 'From':
        continue
        else:
        if words[1] not in dictionary_addresses:
            dictionary_addresses[words[1]] = 1
        else:
            dictionary_addresses[words[1]] += 1     

print(dictionary_addresses)



dictionary_addresses = dict()                 
maximum = 0
maximum_address = ''

fname = input('Enter file name: ')
try:
    fhand = open(fname)
except FileNotFoundError:
    print('File cannot be opened:', fname)
    quit()

for line in fhand:
    words = line.split()
    if len(words) < 2 or words[0] != 'From':
        continue

    if words[1] not in dictionary_addresses:
        dictionary_addresses[words[1]] = 1      
    else:
        dictionary_addresses[words[1]] += 1     

for address in dictionary_addresses:
    if dictionary_addresses[address] > maximum:    
        
        maximum = dictionary_addresses[address]
        
        maximum_address = address

print(maximum_address, maximum)



