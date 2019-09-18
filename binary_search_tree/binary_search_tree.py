import sys

class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        insert_val = BinarySearchTree(value)
        current_node = self
        placed = False
        while placed == False:
            if value < current_node.value:
                if current_node.left:
                    current_node = current_node.left
                else:
                    current_node.left = insert_val
                    placed = True
            if value >= current_node.value:
                if current_node.right:
                    current_node = current_node.right
                else:
                    current_node.right = insert_val
                    placed = True


    def contains(self, target):
        current_node = self
        found = False
        end = False
        while found == False and end == False:
            if target < current_node.value:
                if current_node.left:
                    current_node = current_node.left
                else:
                    end = True
            if target > current_node.value:
                if current_node.right:
                    current_node = current_node.right
                else:
                    end = True
            if target == current_node.value:
                found = True
        return found

    def get_max(self):
        current_node = self
        end = False
        while end == False:
            if current_node.right:
                current_node = current_node.right
            else:
                end = True
        return current_node.value

    def for_each(self, cb):
        if self.value == None:
            return
        cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)