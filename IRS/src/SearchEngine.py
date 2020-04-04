from IRS.src.PostList import PostList
from IRS.src.File import File

class SearcEngine:

    def __init__(self):
        pass

    def query_process_double(self, sp_query):
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

    def query_process_coord(self, sp_query):
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

    def search(self, index, files):
        query = input("Enter your query: ")

        while query != "q":
            result = []
            op_stack = []
            sp_query = query.split(' ')
            '''HERE TO CHANGE TYPES OF SEARCH(DOUBLE WORD OR COORD)'''
            #sp_query = self.query_process_double(sp_query)
            sp_query = self.query_process_coord(sp_query)
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
                elif elem[0] == '\\':
                    while len(op_stack) != 0:
                        current = op_stack.pop()
                        if current == '(' or current == 'OR' or current == 'AND' or current == 'NOT':
                            op_stack.append(current)
                            break
                        result.append(current)

                    op_stack.append(elem)
                else:
                    result.append(elem)
            while len(op_stack) != 0:
                result.append(op_stack.pop())

            answer = self.solve(result, files, index)
            for elem in answer:
               print(str(elem) + " -> " + files[elem - 1])

            query = input("\nEnter your query: ")

    def and_op(self, p_list1, p_list2):
        set_1 = set(p_list1.post_list.keys())
        set_2 = set(p_list2.post_list.keys())

        intersection = set_1 & set_2
        result = PostList()
        for elem in intersection:
            result.post_list[elem] = p_list2.post_list[elem]

        return result

    def or_op(self, p_list1, p_list2):
        set_1 = set(p_list1.post_list.keys())
        set_2 = set(p_list2.post_list.keys())

        union = set_1 | set_2
        result = PostList()
        for elem in union:
            if elem not in set_2:
                result.post_list[elem] = p_list1.post_list[elem]
            else:
                result.post_list[elem] = p_list2.post_list[elem]

        return result

    def not_op(self, p_list, files):
        ids = set(p_list.post_list.keys())
        files_fids = set([i for i in range(1, len(files) + 1)])

        need = files_fids - ids

        result = PostList()
        for elem in need:
            result.post_list[elem] = File(elem)

        return result

    def coord_op(self, p_list1, p_list2, value):
        set_1 = (p_list1.post_list.keys())
        set_2 = (p_list2.post_list.keys())

        intersection = set_1 & set_2
        result = PostList()
        for f_id in intersection:
            list_1 = p_list1.post_list[f_id].coord_list
            list_2 = p_list2.post_list[f_id].coord_list

            i = 0
            j = 0
            while i < len(list_1) and j < len(list_2):
                if abs(list_1[i] - list_2[j]) <= value:
                    result.add_file_coord(f_id, list_2[j])
                    break
                if list_1[i] < list_2[j]:
                    i += 1
                else:
                    j += 1

        return result

    def solve(self, result, files, index):
        for i in range(len(result)):
            if result[i] != 'AND' and result[i] != 'OR' and result[i] != 'NOT' and result[i][0] != '\\':
                if result[i] not in index.index.keys():
                    result[i] = PostList()
                else:
                    result[i] = index.index[result[i]]

        res_stack = []
        for elem in result:
            if elem == 'AND':
                val1 = res_stack.pop()
                val2 = res_stack.pop()
                res_stack.append(self.and_op(val1, val2))
            elif elem == 'OR':
                val1 = res_stack.pop()
                val2 = res_stack.pop()
                res_stack.append(self.or_op(val1, val2))
            elif elem == 'NOT':
                res_stack.append(self.not_op(res_stack.pop(), files))
            elif isinstance(elem, str) and elem[0] == '\\':
                value = ''
                for i in range(1, len(elem)):
                    value += elem[i]
                value = int(value)
                val1 = res_stack.pop()
                val2 = res_stack.pop()
                res_stack.append(self.coord_op(val1, val2, value))
            else:
                res_stack.append(elem)

        #print('Stack len: ' + str(len(res_stack)))
        return sorted(res_stack.pop().post_list.keys())
