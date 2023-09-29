#!/usr/bin/env python3
# Created By: Tony Tran
# Date: Sept. 29, 2023
# This is program calculates the subtotal, tax, and total price of a Pizza.

import constants


def main():
    diameter = float(input("Pizza's Diameter: "))
    HST = constants.HST
    LABOUR = constants.LABOUR
    RENTAL = constants.RENTAL
    INGREDIENTS = constants.INGREDIENTS
    subtotal = format(LABOUR + RENTAL + (INGREDIENTS * diameter))
    tax = format(HST * float(subtotal))
    total = round(float(format(float(subtotal) + float(tax))), 2)
    print(f"Total cost of the Pizza is {total}")


if __name__ == "__main__":
    main()
