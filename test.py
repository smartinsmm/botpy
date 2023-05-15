'''class History:
    def __init__(self,data):
        self.last_node = node(data)

    def add(self, data):
        N = node(data)
        N.next_node = self.last_node
        self.last_node = N
    
    def view_lastcommand_in_history(self):
        return self.last_node.data
      
    def View(self):
        Tab = []
        current_node = self.last_node
        while current_node != None:
            Tab.append(current_node.data)
            current_node = current_node.next_node
        return Tab

    def Delete(self):
        self.last_node = None''' ##test meliha