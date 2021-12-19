class Node(object):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

n1 = Node("Monday")
n2 = Node("Tuesday")
n3 = Node("Wednesday")
n4 = Node("Thursday")


n1.set_next(n2)
n2.set_next(n3)
n3.set_next(n4)

linkedList = n1

while linkedList.get_data() != "Thursday":
    print(linkedList.get_data())
    linkedList = linkedList.get_next()



