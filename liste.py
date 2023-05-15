class node : 
  def __init__(self, data):
    self.data = data
    self.next_node = None
    self.previous_node = None


class historique_commandes:
  def __init__(self):
    self.first_node = None

  def clear(self):
    self.first_node = None

  def add_command(self,data):
    new_node = node(data)
    if self.first_node == None:
      self.first_node = new_node
      return

    current_node = self.first_node
    while current_node.next_node != None:
      current_node = current_node.next_node

    current_node.next_node = new_node
    new_node.previous_node = current_node

  def get_last_command(self):
    if self.first_node == None:
      return "pas d'historique"

    current_node = self.first_node
    while current_node.next_node != None:
      current_node = current_node.next_node
    return current_node.data

  def get_all_commands(self):
    if self.first_node == None:
      return "pas d'historique"
      
    commands = []
    commands.append(self.first_node.data)
    current_node = self.first_node
    while current_node.next_node != None:
      current_node = current_node.next_node
      commands.append(current_node.data)

    return commands
 
class classeur :  
  def __init__(self):
    self.first_node = None
  
  def all_command_user(self,data):
    new_node = node(data)
    if self.first_node == None:
      self.first_node = new_node
      return

    current_node = self.first_node
    while current_node.next_node != None:
      current_node = current_node.next_node

    current_node.next_node = new_node
    new_node.previous_node = current_node
  
  def get_all(self):
    if self.first_node == None:
      return "pas d'historique"
      
    commands = []
    commands.append(self.first_node.data)
    current_node = self.first_node
    while current_node.next_node != None:
      current_node = current_node.next_node
      commands.append(current_node.data)

    return commands
    
    
H = historique_commandes()
H.add_command("!hello")
H.add_command("!hello")
H.add_command("!salut")
H.add_command("!hello")
H.add_command("!yo")
H.add_command("!hello")
#H.clear()
L = H.get_all_commands()
print(L)