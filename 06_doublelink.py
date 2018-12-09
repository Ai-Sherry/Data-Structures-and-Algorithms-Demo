#利用类实现双链表
class Node(object):
    def __init__(self,data,next=None):
        self.data=data
        self.next=next

class TwoWayNode(Node):
    def __init__(self,data,previous=None,next=None):
        Node.__init__(self,data,next)
        self.previous=previous

head=TwoWayNode(1)
tail=head   #tail可直接访问最后一个节点

#1.给双链表增加四个节点
for data in range(2,6):
    tail.next=TwoWayNode(data,tail)
    tail=tail.next

#2.以相反的顺序打印链表
probe=tail
while probe!=None:
    print(probe.data)
    probe=probe.previous
    
    
