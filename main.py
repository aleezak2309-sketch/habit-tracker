def add_habit(data):
            name=input('Please enter the habit name: ').strip().lower()
            if name=='':
                print('Please enter another name: ').strip().lower()
                return 
            if name in data:
                print('Sorry task already in data')
                return 
            else:
                data[name]=[]
                print(f'Added {name} to study')
data={}
while True:
    print('[1].Add Habit')
    print('[2].Mark Habit Done Today')
    print('[3].View Habits')
    print('[4].Quit')
    print('[5].Others')
    choice=int(input('Please enter your choice: '))
    if choice==1:
          add_habit(data)
    elif choice==2:
          print('Coming Soon')
    elif choice==3:
          print('Coming Soon')
    elif choice==4:
          print('GoodBye!')
          break 
    else:
          print('Please choose a option from 1-4')

