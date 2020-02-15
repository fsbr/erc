#!/usr/bin/env python3
import requests
import sys
import argparse

def get_currency_json(input_currency_code="USD"):
    url = f"https://api.exchangerate-api.com/v4/latest/{input_currency_code}"
    # making our request
    response = requests.get(url)
    data = response.json()
    return data

#def convert_currency(input_amount, input_currency_code, output_currency_code):
def convert(input_amount, input_currency_code, output_currency_code):

    if input_currency_code == "RMB":
        input_currency_code = "CNY"

    data = get_currency_json(input_currency_code)

    # get exchange rate
    rate = data["rates"][output_currency_code]
    converted_amount = input_amount*rate

    converted_amount = "%.2f" % converted_amount
    display_rate = "%.3f" % rate

    print(f"Your {input_amount} {input_currency_code} is equal to "
            f" {converted_amount} {output_currency_code} "
            f"at an exchange rate of {display_rate}")

#def get_currency_codes():
def options():
    data = get_currency_json()
    rates=data["rates"]
    codes = []
    for key,value in rates.items():
        codes.append(key)
    print("Available currency codes:")
    print(" ".join(codes))

# custom help message 
def print_help():
    print("Welcome to Tommy's Exchange Rate Calculator")
    print("erc options - shows available currency codes")
    print("erc convert - converts currency")
    print("Use erc -h to ask for help!")
    print("ex: erc convert 10 USD CNY")


if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()
    
    # put subparsers for the covert, help, and options commands here
    subparsers = parser.add_subparsers(dest="subparser")

    #convert command
    parser_convert = subparsers.add_parser("convert")
    required = parser_convert.add_argument_group("arguments for currency conv")
    required.add_argument("input_amount", type=float)
    required.add_argument("input_currency_code")
    required.add_argument("output_currency_code")
   
    # options command 
    parser_get_currency_codes = subparsers.add_parser("options")

    kwargs = vars(parser.parse_args())
    try:
        globals()[kwargs.pop("subparser")](**kwargs)
    except KeyError:
        print_help()
