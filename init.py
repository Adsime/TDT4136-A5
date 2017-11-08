import assignment5

docs = ["./boards/easy.txt", "./boards/medium.txt", "./boards/hard.txt", "./boards/veryhard.txt"]

for doc in docs:
    # Create a problem using 'doc'
    csp = assignment5.create_sudoku_csp(doc)

    # Try to solve the problem
    res = csp.backtracking_search()

    # Print results
    print "Result for board '" + doc + "'"
    print "Call count: " + csp.backtrack_calls.__str__() + " | Failure count: " + csp.backtrack_fails.__str__() + "\n"
    assignment5.print_sudoku_solution(res)
    print "\n"
