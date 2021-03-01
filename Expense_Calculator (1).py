#main method program starts here
if __name__ == '__main__' :
    ''' Declaring empty dictionaries and variables'''
    budget_dict = {}
    total=0
    balance=0
    ## Initlization of custom functions
    def validate_name(name):
        '''this function return the given input contains only aplhabets accepts only one attribute'''
        return name.isalpha()
    def validate_number(number):
        '''this function return the given input contains only numbers in floating point datatype ,accepts only one attribute'''
        return float(number)
    def returnSum(myDict):
        '''this function return the given dictionary and sums up the values of all the keys available in the dictionary'''
        sum = 0
        for i in myDict: 
            sum = sum + float(myDict[i])
        return sum
    def summary():
        '''this functions prints the output '''
        print('-'*50)
        print('-'*15 ,'Expenses Calculator','-'*14)
        print("-" * 50)
        print("Item name".ljust(40, ' '), "Amount", "/-")
        print("-" * 50)
        print("budget".ljust(40, ' '), round(float(budget),2), "/-")
        print("-" * 50)
        for x,y in budget_dict.items():
            print(x.ljust(40,' '),":",y,"/-")
        print("-" * 50)
        print("Total".ljust(40, ' '), round(returnSum(budget_dict),2), "/-")
        print("Balance".ljust(40, ' '), round(budget,2) - round(returnSum(budget_dict),2), "/-")
    #loop for continous loop    
    while(True):
        try:
            #takes input for budget and strips ths empty spaces
            print('To Quit press q or 0 on keyboard')
            budget = float(input('Enter your Salary :').strip())
            if budget < 0:
                continue
            if budget == 'q' or budget == 'Q' or budget == '0':
                break
            break
        except ValueError:
            print('Please type number ')
    if budget > total:
        while(True):
            try:
                #takes input for name of expenditure and strip the empty spaces
                expenditure_name = str(input('Enter the expenditure_name:').strip())
                #when input match loop is exited
                if expenditure_name == 'q' or expenditure_name == 'Q' or expenditure_name == '0':
                    summary()
                    break
                else:
                    if validate_name(expenditure_name):
                        expenditure_amount = input('Enter the amount for {}:'.format(expenditure_name)).strip()
                        check_amount = returnSum(budget_dict) + round(float(expenditure_amount),2)
                        #checks for whether amounts reaches to its threshold
                        if check_amount > budget:
                                print('Insufficient Balance....!')
                                summary()
                                break
                        if validate_number(expenditure_amount) :   
                            
                            #if the both amount and name passes through the validation they are added to the dictionary
                            if expenditure_name in budget_dict:
                                value = budget_dict[expenditure_name]
                                result = value + float(expenditure_amount)
                                budget_dict[expenditure_name] = round(float(result),2)
                            else:
                                budget_dict[expenditure_name] = round(float(expenditure_amount),2)

                        else:
                            print('Please type positive numbers only')
                    else:
                        print('Please type character only')  
            except ValueError:
                print('Please type character only')
    else:
        print('Insufficient Balance.....!')
