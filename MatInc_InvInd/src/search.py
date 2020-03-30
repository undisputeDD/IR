def search(dictionary):
    query = input("Enter your query: ")

    while query != "q":
        sp_query = query.split(' ')
        for elem in sp_query:
            print(elem)
        query = input("Enter your query: ")
