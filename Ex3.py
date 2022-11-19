#Lab4 Ex3.1-3.4
class Node():
    def __init__(self,data):
        self.data = data
        self.Next = ""
class LinkedList():
    def __init__(self):
        self.Header = ""
    def list_append(self,data):
        if self.Header != "":
            self = self.Header
        while self.Next != "" :
            self = self.Next
        self.Next = Node(data) 
    def insert(self,index,data):
        if index > 0:
            count = 1
            TempNode = self.Header.Next
            while count < index-1:
                if TempNode. Next!= "" :
                    TempNode = TempNode.Next
                    count += 1
                else:
                    break
            old_node = TempNode
            new_node = Node(data)
            new_node.Next = TempNode.Next
            old_node.Next = new_node
            
        elif index == 0:
            new_node = Node(data)
            new_node.Next = self.Header
            self.Header = new_node

    def remove(self,index):
        count = 0
        TempNode = self.Header
        if index > 0 and index < (self.findlength()-1): 
            while count < index-1:
                if TempNode.Next!= "" :
                    TempNode = TempNode.Next
                    count += 1
                else:
                    break
            TempNode.Next = TempNode.Next.Next
        elif index == 0:
            self.Header = self.Header.Next
        else:
            if index == self.findlength()-2:
                limit = 1
            else:
                limit = 2
            while count < self.findlength()-limit:
                if TempNode.Next!= "" :
                    TempNode = TempNode.Next
                    count += 1
                else:
                    break
            TempNode.Next = ""
    def findlength(self):
        TempNode = self.Header
        count = 1
        while TempNode.Next!= "":
            count += 1
            TempNode = TempNode.Next
        return count

            
node= LinkedList()
node.Header = Node(44)
node.list_append(36)
node.list_append(90)
node.list_append(10)
node.list_append(60)
node.list_append(99)
node.insert(0,104)
node.list_append(57)
node.remove(4)
