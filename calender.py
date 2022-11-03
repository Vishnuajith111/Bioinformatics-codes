calender = [('January', 31),
            ('Feburary', 28),
            ('March', 31),
            ('April', 30),
            ('May', 31),
            ('June', 30),
            ('July', 31),
            ('August', 31),
            ('September', 30),
            ('October', 31),
            ('November', 30),
            ('December', 31)]

week = ['Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa', 'Su']

def make_calendar(year, start_day):
    
    start_pos = week.index(start_day)
    if is_leap(year):
        calender[1] = ('Feburary', 29)
    
    for month, days in calender:
        print('{0} {1}'.format(month, year).center(20, ' '))
        print(''.join(['{0:<3}'.format(w) for w in week]))
        print('{0:<3}'.format('')*start_pos, end='')
        
        for day in range(1, days + 1):
            print('{0:<3}'.format(day), end='')
            start_pos += 1
            if start_pos == 7:
                print()
                start_pos = 0 
        print('\n')

def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
yr=int(input('Enter Year \t \n'))
strtday=input('Enter start day of the year Mo,Tu,We,Th,Fr,Sa,Su \t \n')
make_calendar(yr,strtday)