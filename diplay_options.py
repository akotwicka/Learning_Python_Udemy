def DisplayOptions(options):
    for index, opt in enumerate(options):
        print(index, " - ", opt)
    print('Select option above or press enter to exit:')
    a = input()
    return a

options = ['load data', 'export data', 'analyze & predict']
choice = 'x'

while choice:
    choice = DisplayOptions(options)
    if choice:
        try:
            choice_num = int(choice)
            if (choice_num > 0) and (choice_num <= len(options)):
                print(choice_num, " - ", options[choice_num-1])
            else:
                print("Wrong choice!")
        except:
            print("Selected option must be a number")
    else:
        print("The end.")