
data={}
def add_topic(data):
            topic=input('Please enter the topic name: ').strip().lower()
            if topic=='':
                print('Please enter another name: ')
                return 
            if topic in data:
                print('Sorry topic already in data')
                return 
            else:
                data[topic]=[]
                print(f'Added {topic} to study')
def delete_topic(data):
      if data =={}:
            print('No topics available to delete')
            return 
      else:
            topics=list(data.keys())
            for i,topic in enumerate(topics,start=1):
                  print(f'{i}:{topic}')
            delete=input('Please enter which topic to delete: ').strip()
            if not delete.isdigit() or int(delete)<1 or int(delete)>len(topics):
                        print('Incorrect number')
            else:
                        delete=int(delete)
                        topic=topics[delete-1]
                        del data[topic]
                        print(f'{topic} topic sucessfully deleted')
def log_question(data):
      if not data:
            print('No topics avaialble to see curently')
            return 
      topics=list(data.keys())
      for i,topic in enumerate(topics,start=1):
            print(f'{i},{topic}')
      number=input('Please choose the topic that you are intrested in: ').strip()
      if not number.isdigit() or int(number)<1 or int(number) >len(topics):
            print('Invalid number topic')
            return
      number=int(number)
      topic=topics[number-1]
      print(f'You picked: {topic}')
      question=input('Please enter question name: ').strip()
      difficulty=input('Difficulty:(Easy/Medium/Hard): ').strip()
      if question=='':
            print('Please enter a valid question again')
            return 
      if difficulty=='':
            print('Please enter a valid question again')
      for item in data[topic]:
            if item['name']==question:
            print('Question already in data')
            return
      else:
            data[topic].append({'name'}:question,'difficulty':difficulty})
            print(f'Succesfully logged {question} under {topic}')
def view_topics(data):
 if data=={}:
       print('No topics yet')
       return 
 for topic,questions in data.items():
       print(f'{topic}: {len(questions)}')
while True:
    print('[1].Add Topic')
    print('[2].Log Question Solved')
    print('[3].View Topics')
    print('[4].Quit')
    print('[5].Delete Topic')
    choice=(input('Please enter your choice: ')).strip()
    if choice=='1':
          add_topic(data)
    elif choice=='2':
          log_question(data)
    elif choice=='3':
          view_topics(data)
    elif choice=='4':
          print('Delete Topic')
    elif choice=='5':
          print('Goodbye')
