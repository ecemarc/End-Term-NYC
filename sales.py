import os
import pandas as pd


# utility function to convert float or integer to usd-formatted string (for printing)
def to_usd(my_price):
    # return "${0:,.2f}".format(my_price)
    return f"${my_price:,.2f}"

#
# INFO INPUTS
#


CSV_FILENAME = "rollingsales.csv"

csv_filepath = os.path.join("data", CSV_FILENAME)

df = pd.read_csv(csv_filepath)

sales = df.to_dict("record")

valid_zip = []  # creating list of zip codes to be selected
for index, row in df.iterrows():  # creating variables for easy access
    zip = (row["ZIP CODE"])
    sales_price = (row[" SALE PRICE "])
    sq = (row["GROSS SQUARE FEET"])
    valid_zip.append(row["ZIP CODE"])


print(type(zip))
print(type(row["ZIP CODE"]))

if int(sq) != 0 and float(sales_price) != 0:
    price_per_sq = float(sales_price)/int(sq)  # calculating price for sq feet
else:
    print("PRICE PER SQUARE FOOT NOT AVAILABLE")

print(df.iloc[0])


# def sorted_by_neighbourhood(a):
#     return a["neighbourhood"]

selected_zip = []

if __name__ == "__main__":  # revisited rock-paper and input module
    while True:
        user_input = input("Please enter the data you would like to sort by: ")
        if user_input == "DONE" or user_input == "done" or user_input == "Done":  # exiting when DONE
            break
        if int(user_input) in df["ZIP CODE"]:
            selected_zip.append(int(user_input))
        else:
            print("INVALID ZIP")

        # elif int(user_input) in valid_zip:
        #     selected_zip.append(user_input)
        # elif int(user_input) not in valid_zip:
        #     print("INVALID ZIP")


for user_input in selected_zip:
    print(row["ADDRESS"])
