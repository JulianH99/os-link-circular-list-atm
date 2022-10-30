

from circularlist import ATM, Node



def main():
    bank = ATM()
    bank_atm_head = Node(name="ATM", transactions=0)
    bank.add_node(bank_atm_head)

    bank.add_node(Node(name="Customer 1", transactions=10))

    bank.add_node(Node(name="Customer 2", transactions=1))

    bank.add_node(Node(name="Customer 3", transactions=4))

    bank.add_node(Node(name="Customer 6", transactions=7))

    bank.print_list()

    bank.process_atm_line()

    bank.print_list()



if __name__ == '__main__':
    main()