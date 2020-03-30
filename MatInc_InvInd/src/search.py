def search(dictionary, files):
    query = input("Enter your query: ")

    while query != "q":
        result = []
        op_stack = []
        sp_query = query.split(' ')
        for elem in sp_query:
            if elem == '(':
                op_stack.append('(')
            elif elem == ')':
                while len(op_stack) != 0:
                    current = op_stack.pop()
                    if current == '(':
                        break
                    result.append(current)
            elif elem == 'NOT':
                while len(op_stack) != 0:
                    current = op_stack.pop()
                    if current == 'OR' or current == 'AND' or current == '(' or current == 'NOT':
                        op_stack.append(current)
                        break
                    result.append(current)

                op_stack.append('NOT')
            elif elem == 'AND':
                while len(op_stack) != 0:
                    current = op_stack.pop()
                    if current == 'OR' or current == '(':
                        op_stack.append(current)
                        break
                    result.append(current)

                op_stack.append('AND')
            elif elem == 'OR':
                while len(op_stack) != 0:
                    current = op_stack.pop()
                    if current == '(':
                        op_stack.append(current)
                        break
                    result.append(current)

                op_stack.append('OR')
            else:
                result.append(elem)
        while len(op_stack) != 0:
            result.append(op_stack.pop())
        #for element in result:
        #   print('[' + element + ']', end=' ')
        query = input("\nEnter your query: ")


def and_op():
    pass


def or_op():
    pass


def not_op():
    pass