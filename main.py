if __name__ == "__main__":
    wsa = 0 #Window seat acumulator
    msa = 0 #Middle seat acumulator
    asa = 0 #Aisle seat acumulator

    max_cols = 0
    # input_array = [ [3,4], [4,5], [2,3], [3,4] ]
    input_array = [ [3,2], [4,3], [2,3], [3,4] ] #Example input array
    # passegers = int(input("Type the amount of passegers > "))
    passegers = 30 #Example amount

    al = len(input_array)
    for i in range(al):
        arrRows = input_array[i][0]
        for j in range(input_array[i][1]):
            if (j+1) > max_cols:
                max_cols = j+1
            if i == 0 or i == (al - 1):
                if arrRows > 2:
                    wsa += 1
                    asa += 1
                    msa += arrRows - 2
                else:
                    wsa += 1
                    asa += 1
            else:
                if arrRows > 2:
                    asa += 2
                    msa += arrRows - 2
                else:
                    asa += 2

    if passegers > asa:
        passegers -= asa
        if passegers > wsa:
            passegers -= wsa
            if passegers > msa:
                passegers -= msa
            else:
                msa = passegers
        else:
            wsa = passegers
            msa = 0
    else:
        asa = passegers
        wsa = 0
        msa = 0 

    # print(f"Window Seats: {wsa}")
    # print(f"Middle Seats: {msa}")
    # print(f"Aisle Seats: {asa}")
    # print(f"Max Cols: {max_cols}")
    
    pacounter = 1
    pwcounter = 1 + asa
    pmcounter = 1 + wsa + asa
    result_arr = []
    for row in input_array:
        result_arr.append([])

    # result_arr = [ [], [], [], [] ]

    for col in range(max_cols):
        for row in range(al):
            arrRows = input_array[row][0]
            auxColArr = []
            if col >= input_array[row][1]:
                continue
            if row == 0:
                if arrRows > 2:
                    if wsa > 0:
                        auxColArr.append(pwcounter)
                        pwcounter += 1
                        wsa -= 1
                    else:
                        auxColArr.append(0)
                    for i in range(arrRows - 2):
                        if msa > 0:
                            auxColArr.append(pmcounter)
                            pmcounter += 1
                            msa -= 1
                        else:
                            auxColArr.append(0)   
                    if asa > 0:
                        auxColArr.append(pacounter)
                        pacounter += 1
                        asa -= 1
                    else:
                        auxColArr.append(0)    
                else:
                    if wsa > 0:
                        auxColArr.append(pwcounter)
                        pwcounter += 1
                        wsa -= 1
                    else:
                        auxColArr.append(0)    
                    if asa > 0:
                        auxColArr.append(pacounter)
                        pacounter += 1
                        asa -= 1
                    else:
                        auxColArr.append(0)    
            elif row == (al - 1):
                if arrRows > 2:
                    if asa > 0:
                        auxColArr.append(pacounter)
                        pacounter += 1
                        asa -= 1
                    else:
                        auxColArr.append(0)    
                    for i in range(arrRows - 2):
                        if msa > 0:
                            auxColArr.append(pmcounter)
                            pmcounter += 1
                            msa -= 1
                        else:
                            auxColArr.append(0)   
                    if wsa > 0:
                        auxColArr.append(pwcounter)
                        pwcounter += 1
                        wsa -= 1
                    else:
                        auxColArr.append(0)
                else:
                    if asa > 0:
                        auxColArr.append(pacounter)
                        pacounter += 1
                        asa -= 1
                    else:
                        auxColArr.append(0)
                    if wsa > 0:
                        auxColArr.append(pwcounter)
                        pwcounter += 1
                        wsa -= 1
                    else:
                        auxColArr.append(0)    
            else:
                if arrRows > 2:
                    if asa > 0:
                        auxColArr.append(pacounter)
                        pacounter += 1
                        asa -= 1
                    else:
                        auxColArr.append(0)    
                    for i in range(arrRows - 2):
                        if msa > 0:
                            auxColArr.append(pmcounter)
                            pmcounter += 1
                            msa -= 1
                        else:
                            auxColArr.append(0)    
                    if asa > 0:
                        auxColArr.append(pacounter)
                        pacounter += 1
                        asa -= 1        
                    else:
                        auxColArr.append(0)    
                else:
                    if asa > 0:
                        auxColArr.append(pacounter)
                        pacounter += 1
                        asa -= 1
                    else:    
                        auxColArr.append(0)    
                    if asa > 0:
                        auxColArr.append(pacounter)
                        pacounter += 1
                        asa -= 1
                    else:
                        auxColArr.append(0)    
            result_arr[row].append(auxColArr)            
    print("Every seat row is represented by a list where each sublist represent each column")
    for i in range(len(result_arr)):
        print(f"Seats Row {i+1}")
        print(result_arr[i])
