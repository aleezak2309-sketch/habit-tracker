
import json
from datetime import date
def save_data(data):
    with open('logging.json', 'w') as f:
        json.dump(data, f)


def load_data():
    try:
        with open('logging.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
    data=load_data()

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
                save_data(data)
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
                        save_data(data)
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
      note=input('Please add any notes you would require(press enter to skip): ')
      today=date.today().isoformat()
      if question=='':
            print('Please enter a valid question again')
            return 
      if difficulty=='':
            print('Please enter a valid question again')
            return 
      for item in data[topic]:
            if item['name']==question:
                  print('Question already in data')
                  return
      else:
            data[topic].append({'name':question,'difficulty':difficulty},date:{today},notes:{notes})
            save_data(data)
            print(f'Succesfully logged {question} under {topic}')
def view_topics(data):
 if data=={}:
       print('No topics yet')
       return 
 for topic,questions in data.items():
      print(f'{topic}:{len(questions)} solutions')
      for item in questions:
            print(f'-{item["name"]}: {item["difficulty"]}')
            note=item.get('note','')
            if note != '':
                 print(f'note: {note}')
def search_questions(data):
      if data=={}:
            print('No topic yet')
            return 
      keyword=input('Enter a keyword to search: ').strip().lower()
      found=False
      for topic,questions in data.items():
            for item in questions:
                  if keyword in item["name"].lower():
                        print(f'found: {item["name"]}({item["difficulty"]})-in {topic} date{item['date']} note{item['note']}')
                        found=True
      if not found:
             print('Keyword not found')
def view_sorted(data):
      sorted_topics=sorted(data.items(),key=lambda pair:len(pair[1]),reverse=True)
      for topic,questions in sorted_topics:
            print(f'{topic}:{len(questions)} solved')
def edit_question(data):
    if not data:
        print('No topics yet')
        return

    topics = list(data.keys())
    for i, topic in enumerate(topics, start=1):
        print(f'{i}: {topic}')

    number = input('Please enter the topic number: ').strip()
    if not number.isdigit() or int(number) < 1 or int(number) > len(topics):
        print('Invalid number entered. Please try again')
        return

    number = int(number)
    topic = topics[number - 1]

    questions = data[topic]
    if not questions:
        print('No questions to edit in this topic')
        return

    for i, question in enumerate(questions, start=1):
        print(f'{i}: {question["name"]} ({question["difficulty"]})')

    choice = input('Please enter the question number: ').strip()
    if not choice.isdigit() or int(choice) < 1 or int(choice) > len(questions):
        print('Please enter a valid digit')
        return

    choice = int(choice)
    question_item = questions[choice - 1]

    new_name = input('New name (press Enter to keep current): ').strip()
    if new_name != '':
        question_item['name'] = new_name

    new_difficulty = input('New difficulty (press Enter to keep current): ').strip()
    if new_difficulty != '':
        question_item['difficulty'] = new_difficulty

    print(f"Updated to {question_item['name']} ({question_item['difficulty']})")
    save_data()

while True:
    print('[1].Add Topic')
    print('[2].Log Question Solved')
    print('[3].View Topics')
    print('[4].Quit')
    print('[5].Delete Topic')
    print('[6] Find Question')
    print('[7] Sorted Data')
    choice=(input('Please enter your choice: ')).strip()
    if choice=='1':
          add_topic(data)
    elif choice=='2':
          log_question(data)
    elif choice=='3':
          view_topics(data)
    elif choice=='4':
          print('Delete Topic')
          break
    elif choice=='5':
       delete_topic(data)     
    elif choice=='6':
       search_questions(data)
    elif choice=='7':
          view_sorted(data)
    elif choice=='8':
          edit_question(data)
                

          
         
