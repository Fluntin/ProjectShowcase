import os

def is_weekday(date):
    # Check if a date is a weekday

    # Input: date -> datetime object
    # Output: if date is a weekday True
    #         if date is a weekend False

    weekno = date.weekday()
    weekday = bool

    if weekno < 5:
        weekday = True
    else:
        weekday = False

    return weekday

def show_main_menu():
    # Prints out the main menu

    # Input: None
    # Output: None

    print("1 -> Fundamental analysis")
    print("2 -> Technical analysis")
    print("3 -> Ranking according to beta value")
    print("4 -> Exit")
    print('\n')
    print("Choose: ")

def show_fundamental_menu(stock_list):
    # Displays names of all companies in stock_list.
    # Allows the user to select a specific company.
    # Writes out fundamental data for the selected company.

    # Input: list -> [Stock1, Stock2, Stock3...]
    # Output: None

    while True:
        print('')
        print('-----Fundamental menu-----')

        try:
            for i, stock in enumerate(stock_list, start=1):
                print(f"{i} -> {stock.company_name}")
            print(len(stock_list) + 1, '-> Go to Main menu')

            print('')
            val = int(input("What stock would you like to get the fundamental analysis for?"))
            print('')

            if val < len(stock_list) + 1:
                print('')
                print(f"-----Fundamental analysis for {stock_list[val - 1].company_name}-----")
                print(f"Company's Debt to Equity is: {stock_list[val - 1].debt_to_equity}")
                print(f"Company's Price to Earnings ratio: {stock_list[val - 1].pe}")
                print(f"Company's Price to Sales ratio: {stock_list[val - 1].ps}")
            elif val == len(stock_list) + 1:
                break
            else:
                print('Try again')

        except ValueError:
            os.system('cls')

        print('')
        print('')

def show_technical_menu(stock_list):
    # Displays names of all companies in stock_list.
    # Allows the user to select a specific company.
    # Writes out Technical analysis data for the selected company.

    # Input: list -> [Stock1, Stock2, Stock3...]
    # Output: None

    while True:

        print('')
        print('-----Technical analysis-----')

        try:
            for i, stock in enumerate(stock_list, start=1):
                print(f"{i} -> {stock.company_name}")
            print(len(stock_list) + 1, '-> Go to Main menu')

            print('')
            val = int(input("What stock would you like to get the technical analysis for?"))
            print('')

            if val < len(stock_list) + 1:
                print('')
                print(f"-----Technical analysis for {stock_list[val - 1].company_name}-----")
                print(f"Course development for last 30 days: {stock_list[val - 1].course_development}")
                print(f"Highest value for last 30 days: {stock_list[val - 1].course_highest}")
                print(f"Lowest value for last 30 days: {stock_list[val - 1].course_lowest}")
                print(f"Beta value: {stock_list[val - 1].betha}")

            elif val == len(stock_list) + 1:
                break

            else:
                print('Try again')

        except ValueError:
            os.system('cls')

    print('')
    print('')

def show_betha_ranking(stock_list):
    # Sorts companies from stock_list according to the beta value

    # Input: list -> [Stock1, Stock2, Stock3...]
    # Output: None

    print('')
    print('---Ranking according to Beta value---')
    betha = dict()

    for stock in stock_list:
        betha[stock.company_name] = round(float(stock.betha), 3)

    sorted_betha = sorted(betha.items(), key=lambda x: x[1], reverse=True)

    for i, (company_name, beta_value) in enumerate(sorted_betha, start=1):
        print(f"{i} -> {company_name}: {beta_value}")