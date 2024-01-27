import datetime as dt
import pandas_datareader as panda
from menu_operations import is_weekday

# Define constants for file paths
KURSER_FILE_PATH = "kurser.txt"
FUNDAMENTA_FILE_PATH = "fundamenta.txt"
GENERAL_INDEX_FILE_PATH = "generalindex.txt"

def get_history_data_online(companies):
    # Calculate start_date and end_date
    # Use Panda to get data for a specific ticker
    # If the date in the range start_date to end_date is a workday, store a date and a closing price in a dictionary -> {Date: Value}

    # Input: companies -> {Company name: Ticker}
    # Output: dictionary -> {Company name: {Date: Value}}

    start_date = dt.datetime.now().date() - dt.timedelta(days=31)
    end_date = dt.datetime.now().date()

    history_data = dict()
    for key in companies:
        raw_data = panda.DataReader(companies[key], 'yahoo', str(start_date), str(end_date))

        index = dict()
        for i in range(0, 31):
            date = start_date + dt.timedelta(days=i)

            if is_weekday(date):
                börskurs = raw_data.loc[date.strftime('%Y-%m-%d'), 'Close']
                index[str(date)] = round(börskurs, 2)

        history_data[key] = index

    return history_data

def get_fundamentals_data_offline(company_list):
    # Get data from : fundamenta.txt -> (Format: Company name, DebtToEquity, Price to Earnings ratio, Price to Sales ratio)
    # Store data as a dictionary

    # Input: company_list -> [Company name1, Company name2, Company name3...]
    # Output: dictionary -> {Company name: [DebtToEquity, Price to Earnings ratio, Price to Sales ratio]}

    txt = open(FUNDAMENTA_FILE_PATH, "r", encoding="utf8")
    content = txt.read()
    content_list = content.split()
    txt.close()

    # Go through each element in a list and find cutoff points
    # Cutoff point = index position of a company name
    # Create a list of positions for cutoff points.
    cut_points = list()
    for i in range(0, len(content_list)):
        if content_list[i] in company_list:
            cut_points.append(i)
    cut_points.append(len(content_list))

    data = dict()
    for i in range(0, len(cut_points) - 1):
        data_list = []

        for j in range(cut_points[i] + 1, cut_points[i + 1]):
            data_list.append(content_list[j])
        data[content_list[cut_points[i]]] = data_list

    return data

def get_fundamentals_data_online(companies):
    # Use Yahoo finance to get fundamental data

    # Input: companies -> {Company name: Ticker}
    # Output: dictionary -> {Company name: [DebtToEquity, Price to Earnings ratio, Price to Sales ratio]}

    fundamentals_data = dict()

    for key in companies:
        data_list = []
        company = panda.get_quote_table(companies[key])

        # Debt-To-Equity
        debt_to_equity = company.get("Debt to Equity (mrq)")
        data_list.append(debt_to_equity if debt_to_equity else "None")

        # Price-to-Earnings
        pe_ratio = company.get("PE Ratio (TTM)")
        data_list.append(pe_ratio if pe_ratio else "None")

        # Price-to-Sales
        ps_ratio = company.get("Price to Sales (TTM)")
        data_list.append(ps_ratio if ps_ratio else "None")

        fundamentals_data[key] = data_list

    return fundamentals_data

def get_omx_offline():
    # Get data from : generalindex.txt -> (Format: Date, Value)
    # Store data as a dictionary

    # Input: None
    # Output: dictionary -> {Date: Value}

    txt = open(GENERAL_INDEX_FILE_PATH, "r", encoding="utf8")
    content = txt.read()
    content_list = content.split()
    txt.close()

    data = dict()
    for i in range(3, len(content_list), 2):
        data[content_list[i]] = content_list[i + 1]

    return data

def get_omx_online():
    # Calculate start_date and end_date
    # Use Panda to get data for a specific ticker
    # If the date in the range start_date to end_date is a workday, store a date and a closing price in a dictionary -> {Date: Value}

    # Input: None
    # Output: dictionary -> {Date: Value}

    start_date = dt.datetime.now().date() - dt.timedelta(days=30)
    end_date = dt.datetime.now().date()

    raw_data = panda.DataReader('^OMXSPI', 'yahoo', str(start_date), str(end_date))

    index = dict()
    for i in range(0, 30):
        date = start_date + dt.timedelta(days=i)

        if is_weekday(date):
            date.strftime('%Y-%m-%d')

            high = raw_data.loc[str(date), 'High']
            low = raw_data.loc[str(date), 'Low']
            börskurs = round((high + low) / 2, 3)

            index[str(date)] = börskurs

    return index