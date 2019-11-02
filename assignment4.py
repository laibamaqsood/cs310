>>>input_hours = input('Enter Hours: ')
>>>input_rate = input('Enter Rate: ')
>>>hours = float(input_hours)                  
>>>rate = float(input_rate)                    

>>>if hours < 40:
    pay = rate * hours                      
>>>else:
    overtime = hours - 40                   
    pay = (rate * 40.0) + (1.5 * rate * overtime)

>>>print('Pay: ', pay)


>>>input_hours = input('Enter Hours: ')
>>>try:
    hours = float(input_hours)             
>>>except:
>>> print('invalid')
    

>>>input_rate = input('Enter Rate: ')
>>>try:
    rate = float(input_rate)                
>>>except:
>>>print('invalid')
    

>>>if hours < 40:
    pay = rate * hours                    
>>>else:
    overtime = hours - 40                
    pay = (rate * 40.0) + (1.5 * rate * overtime)

>>>print('Pay: ', pay)



>>>input = input('Enter score: ')
>>>try:
    score = float(input)                  
>>>except:
>>> print('invalid')
   

>>>if 0.0 <= score <= 1.0:                    
    if score >= 0.9:
        grade = 'A '
    elif score >= 0.8:
        grade = 'B'
    elif score >= 0.7:
        grade = 'C'
    elif score >= 0.6:
        grade = 'D'
    else:
        grade = 'F'
>>>else:
    grade = 'Bad score'
   
>>>print(grade)

>>>repeat_lyrics()

>>>def repeat_lyrics():
    print_lyrics()
    print_lyrics()

>>>def print_lyrics():
>>>print("I'm a lumberjack, and I'm okay.")
>>> print('I sleep all night and I work all day.')




>>>def computepay(tmp_hours, tmp_raif tmp_hours <= 40.0:)
        return tmp_rate * tmp_hours                

    overtime = tmp_hours - 40.0                
    return (tmp_rate * 40.0) + (1.5 * tmp_rate * overtime)

>>> def check_for_float(input1):
    
>>>try:
        val = float(input1)                
        return val
 >>>except:
          return ( invalid)
          
>>> input_hours = input('Enter Hours: ')
hours = check_for_float(input_hours)

>>>input_rate = input('Enter Rate: ')
rate = check_for_float(input_rate)

>>>pay = computepay(hours, rate)
>>>print('Pay: ', pay)


>>>def computegrade(tmp_score):
   
 >>>   if 0.0 <= tmp_score <= 1.0:
        if tmp_score >= 0.9:
            return 'A'
        if tmp_score >= 0.8:
            return 'B'
        if tmp_score >= 0.7:
            return 'C'
              if tmp_score >= 0.6:
            return 'D'
        return 'F'
    
 >>>   return 'Bad score'


>>>input_score = input('Enter score: ')

>>>try:
    score = float(input_score)             
>>>except:
   return ('invalid')

grade = computegrade(score)
>>>print(grade)