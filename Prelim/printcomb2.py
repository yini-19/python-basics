for i in range(10):
    for j in range(10):
        for k in range(10):
            for l in range(10): 
                if i < k or (i == k and j < l):             
                    print(i, end="")
                    print(j, end=" ")
                    print(k, end="")
                    print(l, end=", ")
                