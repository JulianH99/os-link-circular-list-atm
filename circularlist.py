
from time import sleep


class Node:
    name: str = ''
    transactions: int = 0
    next = None

    def __init__(self, name: str, transactions: int) -> None:
        self.name = name
        self.transactions = transactions
    
    def __str__(self) -> str:
        return f"{self.name}/{self.transactions}"

    def process_node(self) -> None: 
        for t in range(0, self.transactions):
            print(f"Transaction {t+1}")
            sleep(1)


class ATM:
    head: Node = None

    def add_node(self, node: Node):
        if not self.head:
            self.head = node
            node.next = node
        else:
            temp = self.head
            while temp.next is not None and temp.next != self.head:
                temp = temp.next
            temp.next = node
            node.next = self.head
            


    def print_list(self):
        head = self.head

        while(head):
            print(f"Node {head}")

            head = head.next

    def process_atm_line(self) -> None:
        head = self.head
        first_in_line = head.next

        while first_in_line:
            print(f"Processing customer {first_in_line}")
            first_in_line.process_node()
            first_in_line = first_in_line.next

        self.clear_line()

    
    def clear_line(self):
        self.head.next = None
            