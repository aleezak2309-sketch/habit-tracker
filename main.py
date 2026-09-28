data={}
def add_topic(data):
            name=input('Please enter the topic name: ').strip().lower()
            if name=='':
                print('Please enter another name: ')
                return 
            if name in data:
                print('Sorry topic already in data')
                return 
            else:
                data[name]=[]
                print(f'Added {name} to study')
def log_question(data):
      if not data:
            print('No topics avaialble to see curently')
            return 
      topics=list(data.keys())
      for i,topic in enumerate(topic,start=1):
            print(f'{i},{topic}')
      number=input('Please choose the topic that you are intrested in: ').strip()
      if not number.isdigit() or int(number)<1 or int(number) >len(topics):
            print('Invalid number topic')
            return
      number=int(number)
      topic=topics[number-1]
      print(f'You picked: {topic}')
while True:
    print('[1].Add Topic')
    print('[2].Log Question Solved')
    print('[3].View Topics')
    print('[4].Quit')
    choice=int(input('Please enter your choice: ')).strip()
    if choice==1:
          add_topic(data)
    elif choice==2:
          log_question(data)
    elif choice==3:
          print('Coming Soon')
    elif choice==4:
          print('GoodBye!')
          break 
    else:
          print('Please choose a option from 1-4')

