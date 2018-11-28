from .problems import Problems, Node

obj = Problems()

# print(obj.day_one([1, 2, 3, 5, 5], 10))
# print(obj.day_two([1, 2, 3, 4, 5]))

e1 = Node('Monday')
e2 = Node('Tuesday')
e3 = Node('Wednesday')
e4 = Node('Thursday')
e5 = Node('Friday')

e1.nextval = e2
e2.nextval = e3
e3.nextval = e4
e4.nextval = e5

e3.traverse()

obj.day_three()
