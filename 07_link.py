#利用类实现单链表
class Node(object):
    def __init__(self,data1,next1=None):
        self.data1=data1
        self.next1=next1
'''
#1.存储打印链表
#Node实现链表，从链表尾开始存储
head=0
for count in range(1,6):
    head=Node(count,head)
while head!=0:#第一个链表存的是什么，结束条件就是什么
    print(head.data1)#输出节点后，就从链表结构中删除了，我们一般不需要删除，因此采用一个临时变量probe
    head=head.next1
#第一个链表为空
'''
'''
#2.利用临时变量打印链表
head=None 
probe=head #probe指针是None，head指针仍然引用第一个节点
while probe!=None:
    probe=probe.next1
'''
'''
#3.在开始出插入
head=0
for count in range(1,6):
    head=Node(count,head)
head=Node('B',head)#在链表头插入

while head!=0:#第一个链表存的是什么，结束条件就是什么
    print(head.data1)#输出节点后，就从链表结构中删除了，我们一般不需要删除，因此采用一个临时变量probe
    head=head.next1
'''
#4.在末尾插入
head=None
for count in range(1,6):
    head=Node(count,head)
newNode=Node(8)
if head is None:
    head=newNode
else:
    probe=head
    while probe.next1!=None:
        probe=probe.next1
    probe.next1=newNode

while head!=None:#第一个链表存的是什么，结束条件就是什么
    print(head.data1)#输出节点后，就从链表结构中删除了，我们一般不需要删除，因此采用一个临时变量probe
    head=head.next1
'''
#5.在链表头删除
removed=head.data1
head=head.next1
return removed
'''
#6.在链表尾删除
removed=head.data1
if head.next1 is None:
    head=None
else:
    probe=head#先遍历
    while probe.next1.next1!=None:
        probe=probe.next1
    removed=probe.next1.data1
    probe.next1=None
return removed
