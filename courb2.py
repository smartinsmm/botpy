'''class node :
  def __init__(self,data):
    self.data = data
    self.next_node = None
    

class list_chained_sorted :
  def __init__(self, data):
    self.first_node = node(data)

  def add_node(data):
    if data < self.first_node.data:
        N = node(data)
        N.next_node = self.first_node
        self.first_node = N
        
    current_node = self.first_node
    while current_node.next_node != None and current_node.next_node.data < data:
        current_node = current_node.next_node

        N = node(data)
        N.next_node = current_node.next_node
        current_node.next_node = N        
class stack :
    def __init__(self,data):
        self.last_node = node(data)
    
    def push(self,data) :
        #ajoute une data
        N = Node(data)
        N.next_node = self.last_node
        self.lest_node = N
        self.size += 1
    
    def pop(self):
        #recupère une data et on la supprime
        data = self.last_node.data
        self.last_node = self.last_node.next_node
        self.size -= 1
        return data
    
    def peak(self):
        #recupère une data
        return self.last_node.data'''
class nodebinary :
  def __init__(self,data):
    self.data = data
    self.right_node = None
    self.left_node = None
    
  def append(self,data):
    '''N = node(data)
    current_node = self.first_node
    if data <= current_node.data :
      self.left_node.data = N
      current_node = current_node.next_node
    else:
      self.right_node.data = N
      current_node = current_node.next_node'''
    if data < self.data :
      if self.left_node == None:
        self.left_node = nodebinary(data)
      else:
        self.left_node.append(data)
    elif data > self.data:
      if self.right_node == None:
        self.right_node = nodebinary(data)
      else:
        self.right_node.append(data)

  
  def search(self,data):
        
    if data == self.data:
      return True
    elif data < self.data:
      if self.left_node == None:
        return False
      else:
        return self.left_node.search(data)
    else:
      if self.right_node == None:
        return False
      else:
        return self.right_node.search(data)
      
  def __str__(self):
    txt = str(self.data)
    if self.left_node != None:
      txt += "-" +str(self.left_node)
    if self.right_node != None:
      txt += "-" +str(self.right_node)
    return txt
    
class binary_tree:
  def __init__(self,data):
    self.first_node = nodebinary(data)
  
  def append(self,data):
    self.first_node.append(data)

  def search(self,data):
    return self.first_node.search(data)
  
  def __str__(self):
    return str(self.first_node)

T = binary_tree(20)
T.append(5)
T.append(12)
T.append(16)
T.append(9)
T.append(11)
T.append(1)
T.append(2)
print(T)

###################################
class node:
  def __init__(self, answer_to_go_here, question):
    self.answer_to_go_here = answer_to_go_here
    self.question = question
    self.next_nodes = []
    
  def size(self):
    count = 1 
    for node in self.next_nodes:
      count += node.size()  
    return count

  def deepth(self):
    Max = 0
    for node in self.next_nodes:
      if node.deepth() > Max:
        Max = node.deepth()
    return Max + 1
  
  def append(self, question, reponses, question_precedante):
    if question_precedante == self.question:
      self.next_nodes.append(node(reponses, question))
    for n in self.next_nodes:
      n.append(question, reponses, question_precedante)
  

class tree:
  def __init__(self,question):
    self.first_node = node("",question)
    self.current_node = self.first_node

  def size(self):
    return self.first_node.size()

  def deepth(self):
    return self.first_node.deepth()
  
  def append(self, question, reponses, question_precedante):
    self.first_node.append(question, reponses, question_precedante)
  
  def get_question(self):
    return self.current_node.question

  def choice(self, message):
    for i in self.current_node.next_nodes:
      print("test")
      if message == i.answer_to_go_here:
        self.current_node = i
        print("test2")
        return self.current_node.question
    return "try next answer" 
  
Y = tree("tu as faim ?")
Y.append("tu veux manger", "oui", "tu as faim ?")
Y.append("bah manger pas", "non", "tu as faim ?")
print(Y.get_question())
Y.choice("oui")
print(Y.get_question())

##############################################################################
class hashmap:
  def __init__(self, length):
    self.datas = []
    for i in range(length):
      self.datas.append([])
  
  def append(self, key, value):
    hashed_key = hash(key)
    indice = hashed_key % len(self.datas)
    self.datas[indice].append((key, value))
  
  def get(self, key):
    hashed_key = hash(key)
    indice = hashed_key % len(self.datas)
    for key_datas, value_datas in self.datas[indice]:
      if key == key_datas:
        return value_datas
    return None
  
  
###############################################################################
import json

person = {
  "name" : "loic",
  "age" : 32
}

jsonString = json.dumps(person)

jsonFile = open("C:\Users\morai\Documents\cours\python-b2", "w")
jsonFile.write(jsonString)
jsonFile.close()


jsonFile2 = open("C:\Users\morai\Documents\cours\python-b2\data.json")
data = json.load(jsonFile2)

print(json.dumps(person))

################################## encoder #####################################

class test:
    def __init__(self,data):
        self.a = 2
        self.b = 3
        self.c = data
        
class test2:
    def __init__(self):
        self.data = "hello"
    
T1 = test(test2())

#encoder
from json import JSONEncoder

class testEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__

TestJSONData = json.dumps(T1,  cls=testEncoder)
print(TestJSONData)

#################################################################################


class stack :
    def __init__(self,data):
        self.last_node = node(data)
    
    def push(self,data) :
        #ajoute une data
        N = Node(data)
        N.next_node = self.last_node
        self.lest_node = N
        self.size += 1
    
    def pop(self):
        #recupère une data et on la supprime
        data = self.last_node.data
        self.last_node = self.last_node.next_node
        self.size -= 1
        return data
    
    def peak(self):
        #recupère une data
        return self.last_node.data

###############################################################################

class queue:
    def __init__(self, data):
        self.first_node = node(data)
    
    def pop(self):
        if self.first_node == None:
            return
        
        data = self.first_node.data
        self.first_node = self.first_node.next_node
        return data
    
    def append(self, data):
        current_node = self.first_node
        while current_node.next_node != None:
            current_node = current_node.next_node
        current_node.next_node = node(data)