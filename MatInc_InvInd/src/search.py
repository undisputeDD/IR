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

        answer = solve(result, files, dictionary)
        for elem in answer:
            print(str(elem) + " -> " + files.files[elem].name)

        query = input("\nEnter your query: ")


def and_op(val1, val2):
    return val1 & val2


def or_op(val1, val2):
    return val1 | val2


def not_op(val, files):
    ids = files.get_ids()
    return ids - val


def solve(result, files, dictionary):
    for i in range(0, len(result)):
        if result[i] != 'AND' and result[i] != 'OR' and result[i] != 'NOT':
            if result[i] not in dictionary.dict:
                result[i] = set()
            else:
                result[i] = dictionary.dict[result[i]]

    res_stack = []
    for elem in result:
        if elem == 'AND':
            val1 = res_stack.pop()
            val2 = res_stack.pop()
            res_stack.append(and_op(val1, val2))
        elif elem == 'OR':
            val1 = res_stack.pop()
            val2 = res_stack.pop()
            res_stack.append(or_op(val1, val2))
        elif elem == 'NOT':
            res_stack.append(not_op(res_stack.pop(), files))
        else:
            res_stack.append(elem)

    return sorted(res_stack.pop())
