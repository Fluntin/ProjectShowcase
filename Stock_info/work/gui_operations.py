import tkinter as tk

def create_stock_selection_gui(stock_list, show_fundamental_callback, show_technical_callback, show_betha_callback):
    # Create a GUI for selecting a stock

    # Input: stock_list -> list of Stock objects
    #        show_fundamental_callback -> function to call when showing fundamental analysis
    #        show_technical_callback -> function to call when showing technical analysis
    #        show_betha_callback -> function to call when showing beta ranking

    my_w = tk.Tk()
    my_w.geometry("750x500")  # Size of the window
    my_w.title("Stock Analysis")  # Adding a title

    options = tk.StringVar(my_w)
    options.set("Select Stock")  # default value

    l1 = tk.Label(my_w, text='Select One', width=10)
    l1.grid(row=2, column=1)

    company_names = [stock.company_name for stock in stock_list]

    om1 = tk.OptionMenu(my_w, options, *company_names)
    om1.grid(row=2, column=2)

    b1 = tk.Button(my_w, text='Show Fundamental', command=show_fundamental_callback)
    b1.grid(row=2, column=3)

    b2 = tk.Button(my_w, text='Show Technical', command=show_technical_callback)
    b2.grid(row=3, column=3)

    b3 = tk.Button(my_w, text='Show Betha Ranking', command=show_betha_callback)
    b3.grid(row=4, column=3)

    my_w.mainloop()