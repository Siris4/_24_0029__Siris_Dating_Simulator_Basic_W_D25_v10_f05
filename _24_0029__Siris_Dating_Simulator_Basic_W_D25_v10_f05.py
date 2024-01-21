while True:

    print('=============================================')
    print('Welcome to Siris\'s Date-Matching Incubator')
    print('=============================================')

    print('Please answer some questions about yourself!')
    user_name = input("What is your name? ")
    print(' ')
    user_age = int(input("How old are you? "))
    print(' ')

    girl_age1 = input("Do you want a girl that is the same age as you? y / n: ")
    print(' ')
    girl_proximity2 = input("Do you want your girl to live in San Diego? y / n: ")
    print(' ')
    girl_degree3 = input("Do you want your girl to have a college degree? y / n: ")
    print(' ')
    girl_smoking4 = input("Is it okay if your girl is a smoker? y / n: ")
    print(' ')
    girl_drinking5 = input("Is it okay if your girl is a drinker? y / n: ")
    print(' ')
    girl_kids6 = input("Do you want the girl to prefer kids? y / n: ")
    print(' ')
    girl_pets7 = input("Do you want your girl to have any pets? y / n: ")
    print(' ')
    girl_marriage8 = input("Do you want her to be looking for marriage? y / n: ")
    print(' ')

    # creating list
    user_answers = [girl_age1, girl_proximity2, girl_degree3, girl_smoking4, girl_drinking5, girl_kids6, girl_pets7, girl_marriage8]
    # List created

    # below, the list is for: [age, proximity, degree, smoking, drinking, kids, pets, marriage]
    # use list of girls below as key in dictionary as extra credit point. dating_pool

    sarah_date = ['y', 'n', 'y', 'n', 'y', 'n', 'y', 'y']
    jennifer_date = ['n', 'y', 'n', 'y', 'y', 'n', 'n', 'n']
    katelyn_date = ['n', 'y', 'y', 'y', 'y', 'y', 'n', 'n']
    cindy_date = ['n', 'y', 'n', 'n', 'y', 'n', 'n', 'n']
    lynn_date = ['y', 'y', 'y', 'n', 'y', 'y', 'n', 'y']

    dating_pool = {"Sarah": sarah_date, "Jennifer": jennifer_date, "Katelyn": katelyn_date, "Cindy": cindy_date, "Lynn": lynn_date}

    sarah_compat = 0
    for x in range(8):
        if user_answers[x] == dating_pool["Sarah"][x]:
            sarah_compat += 1
    print('Compatibility % with Sarah: ')
    Compatibility = (sarah_compat / 8.00) * 100
    print("%.2f" % Compatibility)

    # Similar blocks for Jennifer, Katelyn, Cindy, and Lynn...
9nput("Would you like one of your other friends to try dating on this app? y/n ")
    print(' ')

    if user_input == 'n':
        print('Thanks for stopping by ' + user_name + '!!!')
        break
