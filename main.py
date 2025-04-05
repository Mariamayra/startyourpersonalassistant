
class PersonalAssistant:
  def __init__(self):
    self.contacts = {'Sarah': 'Journalist', 'Thomas': 'Web Developer', 'Nichole': 'Bank Manager'}
    self.todos = []

  def add_todo(self, new_item):
    self.todos.append(new_item)
  
  def remove_todo(self, todo_item):
    if todo_item in self.todos:
      index = self.todos.index(todo_item)
      self.todos.pop(index)
    else:
      print("To-do isn't in the list! ")

  def get_todos(self):
    return self.todos
  
  def get_birthday(self, name):
    if name == "Sarah":
     return "Birthday is 4/9/92!"
    elif name == "Thomas":
     return "Birthday is 6/1/90!"
    elif name == "Jane":
     return "Birthday is 9/30/95!"
    else:
     return "Can't find a birthday for this person..."

  
  def get_contact(self, name):
    if name in self.contacts:
      return self.contacts[name]
    else:
      return "There's no contact with that name."


assistant = PersonalAssistant()
assistant.add_todo("Pick up groceries")
assistant.add_todo("Schedule meeting for next week")
print(assistant.get_todos())
assistant.remove_todo("Pick up groceries")
print(assistant.get_todos())
print(assistant.get_contact("Sarah"))
print(assistant.get_birthday("Thomas"))
