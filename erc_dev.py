#!/usr/bin/env python3
import requests

#from sys import argv
import sys
import argparse

def get_currency_json(input_currency_code="USD"):
    url = f"https://api.exchangerate-api.com/v4/latest/{input_currency_code}"
    # making our request
    response = requests.get(url)
    data = response.json()
    return data

def convert_currency(input_amount, input_currency_code, output_currency_code):
    data = get_currency_json(input_currency_code)
    # get exchange rate
    rate = data["rates"][output_currency_code]
    fInput_amount = float(input_amount)
    converted_amount = fInput_amount*rate
    print(f"Your {input_amount}{input_currency_code} is equal to "\
    f" {converted_amount}{output_currency_code} at an exchange rate of {rate}")

def get_currency_codes():
    data = get_currency_json()
    rates=data["rates"]
    codes = []
    for key,value in rates.items():
        codes.append(key)
    print("the available currency codes are")
    print(" ".join(codes))

# custom help message 
def printHelp(error_message="I'll try to give you a helpful error message if I can"):
    print("Help for Tommy's Exchange Rate Calculator")
    print(f"{error_message}")
    print("usage: erc  [input_amount][input_currency_code][output_currency_code]")
    print("usage: erc [option]")
    print("available options")
    print("help: prints this message")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    # convert currency option
    options=False
    parser.add_argument("-c", "--convert", action="append", nargs="+", type=str,
                        help="converts currencies: [input amount]"
                                "[input currency][output currency]")
    parser.add_argument("-o", "--options",action="store_true", 
                        help="displays available currencies")
    args = parser.parse_args()

    if args.convert != None:
        args.convert = args.convert[0]
        try:
            input_amount = args.convert[0]
            input_currency_code = args.convert[1]
            output_currency_code = args.convert[2]
            convert_currency( input_amount, input_currency_code, output_currency_code)
        except ValueError:
            printHelp("Mismatched Argument Positions")
        except KeyError:
            printHelp("Incorrect Currency Code")
    elif args.options==True:
       get_currency_codes() 
    elif args.convert ==None:
        printHelp()
