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


    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        # def recur(node):
        #     if node.left is not None:
        #         print_arr.append(recur(node.left))
        #     if node.right is not None:
        #         print_arr.append(recur(node.right))
        #     return node.value
        # print_arr = []
        # print_arr.append(recur(node))
        # print_arr.sort()
        # for i in print_arr:
        #     print(i)
        if node.left:
            self.in_order_print(node.left)

        print(node.value)

        if node.right:
            self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        current_node = node
        #This should be a linked list, but I don't feel implementing it :)
        bft_list = [current_node]
        while bft_list:
            if current_node.left:
                bft_list.append(current_node.left)
            if current_node.right:
                bft_list.append(current_node.right)
            print(bft_list.pop(0).value)
            if bft_list:
                current_node = bft_list[0]

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        current_node = node
        stack = [current_node]
        while stack:
            print(stack.pop().value)
            if current_node.left:
                stack.append(current_node.left)
            if current_node.right:
                stack.append(current_node.right)
            if stack:
                current_node = stack[-1]

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        if node:
            print(node.value)
            self.pre_order_dft(node.left)
            self.pre_order_dft(node.right)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if node:
            self.post_order_dft(node.left)
            self.post_order_dft(node.right)
            print(node.value)