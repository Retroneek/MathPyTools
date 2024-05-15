runtime = True
while (runtime):
    runtime_option = True
    values = []
    try:
        terms = int(input("How many terms are in your equation?:"))
        for i in range(terms):
            print('What is your value for degree', terms - i)
            values.append(int(input("")))

        x = int(input("What is your possible zero:"))

        print(values)
        eval_value = values[0]

        for j in range(len(values) - 1):
            eval_value = (eval_value * x) + values[j + 1]

        if (eval_value == 0):
            print("This is a possible zero!")

        else:
            print(eval_value)
            print("This is not a possible zero.")

        while (runtime_option):
            runtime_keyword = input("Do you want to continue? [Y] (Yes)/ [N] (No)")
            if (isinstance(runtime_keyword, str)):
                if (runtime_keyword.upper() == 'Y'):
                    runtime_option = False
                elif (runtime_keyword.upper() == 'N'):
                    runtime_option = False
                    runtime = False
                else:
                    print("Please enter Y or N.")

    except:
        print('insert an actual integer')
