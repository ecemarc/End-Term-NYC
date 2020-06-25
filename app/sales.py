# TEAM BEST
import pandas as pd
import os


# utility function to convert float or integer to usd-formatted string (for printing)
def to_usd(my_price):
    # return "${0:,.2f}".format(my_price)
    return f"${my_price:,.2f}"


def get_data():
    pass


def do_query(csv_file):

    #
    # INFO INPUTS
    #
    # ********************************eventually we will change to use csv_file that is given to this function*****************
    CSV_FILENAME = "rollingsales.csv"

    csv_filepath = os.path.join(os.path.dirname(
        __file__), "..",  "data", CSV_FILENAME)

    df = pd.read_csv(csv_filepath)

    sales = df.to_dict("record")

    valid_zip = []  # creating list of zip codes to be selected
    for index, row in df.iterrows():  # creating variables for easy access
        zip = (row["ZIP CODE"])
        sales_price = (row[" SALE PRICE "])
        sq = (row["GROSS SQUARE FEET"])
        valid_zip.append(row["ZIP CODE"])

    # print(type(zip))
    # print(type(row["ZIP CODE"]))
    # print(type(row["TAX CLASS AT PRESENT"]))

    if int(sq) != 0 and float(sales_price) != 0:
        # calculating price for sq feet
        price_per_sq = float(sales_price)/int(sq)
    else:
        print("PRICE PER SQUARE FOOT NOT AVAILABLE")

    print(df.iloc[0])

    # def sorted_by_neighbourhood(a):
    #     return a["neighbourhood"]
    nan_value = float("NaN")
    selected_zips = []
    selected_tc = []
    selected_items_sales_price = []
    while True:
        user_input = input(
            "Please choose if you would like to query by ZIP, Tax Class at Present(enter TC), Building Class at Pesent(enter BC): ")
        if user_input == "zip" or user_input == "ZIP" or user_input == "ZIP" or user_input == "tc" or user_input == "TC" or user_input == " bc" or user_input == "BC":
            if user_input == "zip" or user_input == "ZIP":
                user_input_zip = input(
                    "Please enter the zip code(s) you are interested in: ")
                if int(user_input_zip) in df["ZIP CODE"]:
                    print(df[df["ZIP CODE"] == int(user_input_zip)])
                    selected_items = df[df["ZIP CODE"] == int(user_input_zip)]
                    selected_items[" SALE PRICE "] = pd.to_numeric(
                        selected_items[" SALE PRICE "], errors='coerce')
                    selected_items["GROSS SQUARE FEET"] = pd.to_numeric(
                        selected_items["GROSS SQUARE FEET"], errors='coerce')
                    print(selected_items.dtypes)
                    selected_items_sf_price = selected_items_sales[" SALE PRICE "] / \
                        selected_items_feet["GROSS SQUARE FEET"]
                    user_input_calc = input(
                        "Would you like to learn square foot pricing for this zip? : ")
                    if user_input_calc == "YES" or user_input_calc == "yes":
                        print(selected_items_sf_price)
                    else:
                        break

                elif user_input_zip == "DONE" or user_input_zip == "done" or user_input_zip == "Done":  # exiting when DONE
                    break
                else:
                    print("INVALID ZIP")
            if user_input == "tc" or user_input == "TC":
                user_input_tc = input(
                    "Please enter the Tax Class Codes you are interested in: ")
                if str(user_input_tc) in str(df["TAX CLASS AT PRESENT"]):
                    print(df[df["TAX CLASS AT PRESENT"] == str(user_input_tc)])
                elif user_input == "DONE" or user_input == "done" or user_input == "Done":  # exiting when DONE
                    break
                else:
                    print("INVALID TAX CODE")
            if user_input == "bc" or user_input == "BC":
                user_input_bc = input(
                    "Please enter the Building Class Codes you are interested in: ")
                if str(user_input_bc) in str(df["BUILDING CLASS AT PRESENT"]):
                    print(df[df["BUILDING CLASS AT PRESENT"]
                             == str(user_input_bc)])
                elif user_input == "DONE" or user_input == "done" or user_input == "Done":  # exiting when DONE
                    break
                else:
                    print("INVALID BUILDING CODE")
        else:
            break


def store_locally():
    pass


if __name__ == "__main__":  # revisited rock-paper and input module
    # get_data

    do_query("A")  # passing just dummy string for now

    # store_locally

    # export_to_gspread

    # send_email
