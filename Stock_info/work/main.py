import os
from stock import Stock
from data_operations import choose_online_vs_offline, sort_betha
from menu_operations import show_main_menu, show_fundamental_menu, show_teknisk_menu, want_gui
from gui_operations import gui_menu

def main():
    stock_list = choose_online_vs_offline()
    gui = want_gui()

    if not gui:
        while True:
            print('') 
            print('-----Main menu-----')

            try:
                show_main_menu()
                val = int(input())

                if val == 1:
                    os.system('cls')
                    show_fundamental_menu(stock_list) 

                elif val == 2:
                    os.system('cls')
                    show_teknisk_menu(stock_list)

                elif val == 3:
                    os.system('cls')
                    sort_betha(stock_list)

                elif val == 4:
                    os.system('cls')
                    print('Thank you for using the program and have a nice day.')
                    break

                else:
                    os.system('cls')

            except ValueError:
                os.system('cls')

    else:
        gui_menu(stock_list)

if __name__ == "__main__":
    os.system('cls')   
    main()