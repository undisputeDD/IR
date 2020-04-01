from DIndex_CIndex.src.File import File

def search(index, files):
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

        answer = solve(result, files, index)
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


def solve(result, files, index):
    for i in range(0, len(result)):
        #print('res[i] = ' + result[i], end=' ')
        if result[i] != 'AND' and result[i] != 'OR' and result[i] != 'NOT':
            if result[i] not in index.dict:
                result[i] = set()
            else:
                result[i] = index.dict[result[i]]
        #print('res[i] = ' + str(result[i]))

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


def process(sp_query):
    res = []
    counter = 0
    for i in range(len(sp_query)):
        elem = sp_query[i]
        if elem != 'AND' and elem != 'OR' and elem != 'NOT' and elem != '(' and elem != ')':
            counter += 1
        else:
            counter = 0
        if counter == 3:
            res.append('AND')
            res.append(res[len(res) - 2])
            counter = 2
        res.append(elem)
    ans = []
    pair = ''
    for elem in res:
        if elem == 'AND' or elem == 'OR' or elem == 'NOT' or elem == '(' or elem == ')':
            ans.append(elem)
        else:
            if len(pair) != 0:
                pair += elem
                ans.append(pair)
                pair = ''
            else:
                pair = elem + ' '
    return ans


def di_search(index, files):
    query = input("Enter your query: ")

    while query != "q":
        result = []
        op_stack = []
        sp_query = query.split(' ')
        sp_query = process(sp_query)
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

        answer = solve(result, files, index)
        for elem in answer:
            print(str(elem) + " -> " + files.files[elem].name)

        query = input("\nEnter your query: ")


def cprocess(sp_query):
    res = []
    counter = 0
    for i in range(len(sp_query)):
        elem = sp_query[i]
        if elem != 'AND' and elem != 'OR' and elem != 'NOT' and elem != '(' and elem != ')' and elem[0] != '\\':
            counter += 1
        else:
            counter = 0
        if counter == 2:
            res.append('\\1')
            counter = 1
        res.append(elem)

    return res


def ci_search(index, files):
    query = input("Enter your query: ")

    while query != "q":
        result = []
        op_stack = []
        sp_query = query.split(' ')
        sp_query = cprocess(sp_query)
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
                    if current[0] != '\\' or current == '(':
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
            elif elem[0] == '\\':
                while len(op_stack) != 0:
                    current = op_stack.pop()
                    if current == 'OR' or current == 'AND' or current == 'NOT' or current == '(':
                        op_stack.append(current)
                        break
                    result.append(current)

                op_stack.append(elem)
            else:
                result.append(elem)
        while len(op_stack) != 0:
            result.append(op_stack.pop())

        answer = csolve(result, files, index)
        for elem in answer:
            print(str(elem) + " -> " + files.files[elem].name)

        query = input("\nEnter your query: ")


def ccoord_op(val1, val2, coord):
    need_1 = set(val1.keys())
    need_2 = set(val2.keys())

    intersection = need_1 & need_2
    rem = []
    for key in intersection:
        coords_1 = sorted(val1[key].coord)
        coords_2 = sorted(val2[key].coord)
        i = 0
        j = 0
        while i < len(coords_1) and j < len(coords_2):
            if abs(coords_1[i] - coords_2[j]) <= coord:
                rem.append(key)
                break
            if coords_1[i] < coords_2[j]:
                i += 1
            else:
                j += 1

    result = {}
    for elem in rem:
        result[elem] = val2[elem]

    return result


def cand_op(val1, val2):
    need_1 = set(sorted(val1.keys()))
    need_2 = set(sorted(val2.keys()))

    intersection = need_1 & need_2
    res = {}
    for key in intersection:
        res[key] = val2[key]
    return res


def cor_op(val1, val2):
    need_1 = set(sorted(val1.keys()))
    need_2 = set(sorted(val2.keys()))

    union = need_1 | need_2
    res = {}
    for key in union:
        if key in val1 and key not in val2:
            res[key] = val1[key]
        elif key in val2 and key not in val1:
            res[key] = val2[key]
        else:
            res[key] = val2[key]
    return res


def cnot_op(val, files):
    ids = files.get_ids()
    val_set = set(val.keys())
    need = ids - val_set
    result = {}
    for key in need:
        result[key] = File(key)
    return result


def csolve(result, files, index):
    for i in range(0, len(result)):
        if result[i] != 'AND' and result[i] != 'OR' and result[i] != 'NOT' and result[i][0] != '\\':
            if result[i] not in index.dict:
                result[i] = {}
            else:
                result[i] = index.dict[result[i]]
        #print('res[i] = ' + str(result[i]))

    res_stack = []
    for elem in result:
        if elem == 'AND':
            val1 = res_stack.pop()
            val2 = res_stack.pop()
            res_stack.append(cand_op(val1, val2))
        elif elem == 'OR':
            val1 = res_stack.pop()
            val2 = res_stack.pop()
            res_stack.append(cor_op(val1, val2))
        elif elem == 'NOT':
            res_stack.append(cnot_op(res_stack.pop(), files))
        elif isinstance(elem, str) and elem[0] == '\\':
            value = ''
            for i in range(1, len(elem)):
                value += elem[i]
            value = int(value)
            val1 = res_stack.pop()
            val2 = res_stack.pop()
            res_stack.append(ccoord_op(val1, val2, value))
        else:
            res_stack.append(elem)

    #print('Stack len: ' + str(len(res_stack)))
    return sorted(res_stack.pop())
