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
    data = get_currency_json(input_currency_code)

    # get exchange rate
    rate = data["rates"][output_currency_code]
    converted_amount = input_amount*rate
    converted_amount = "%.2f" % converted_amount
    display_rate = "%.3f" % rate

    print(f"Your {input_amount} {input_currency_code} is equal to "
    f" {converted_amount} {output_currency_code} at an exchange rate of {display_rate}")

#def get_currency_codes():
def options():
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
    
    # put subparsers for the covert, help, and options commands here
    subparsers = parser.add_subparsers(dest="subparser")

    # what goes in the quotes is the name of the command
    parser_convert = subparsers.add_parser("convert")
    required = parser_convert.add_argument_group("arguments for currency conv")
    required.add_argument("input_amount", type=float)
    required.add_argument("input_currency_code")
    required.add_argument("output_currency_code")
    
    parser_get_currency_codes = subparsers.add_parser("options")

    # run each function by popping out fo the kwargs list
    kwargs = vars(parser.parse_args())
    globals()[kwargs.pop('subparser')](**kwargs)
