def calculate_price(price, cash_coupon, percent_coupon):
    result1 = 0
    result2 = 0
    TAX = 0.06

    if cash_coupon == 5:
        if percent_coupon == 10 or percent_coupon == 0.10:
            result1 = (price - cash_coupon)
            result1 = result1 - (result1 * 0.10)
        if percent_coupon == 15 or percent_coupon == 0.15:
            result1 = (price - cash_coupon)
            result1 = result1 - (result1 * 0.15)
        if percent_coupon == 20 or percent_coupon == 0.2:
            result1 = (price - cash_coupon)
            result1 = result1 - (result1 * 0.2)
    if cash_coupon == 10:
        if percent_coupon == 10 or percent_coupon == 0.10:
            result1 = (price - cash_coupon)
            result1 = result1 - (result1 * 0.10)
        if percent_coupon == 15 or percent_coupon == 0.15:
            result1 = (price - cash_coupon)
            result1 = result1 - (result1 * 0.15)
        if percent_coupon == 20 or percent_coupon == 0.2:
            result1 = (price - cash_coupon)
            result1 = result1 - (result1 * 0.2)

    if result1 < 10.00:
        result2 = result1 + 5.95
    elif 10 <= result1 < 30:
        result2 = result1 + 7.95
    elif 30 <= result1 < 50:
        result2 = result1 + 11.95
    elif result1 >= 50:
        result2 = result1 + 0

    finalResult = result2 + (result2 * TAX)

    return finalResult


if __name__ == '__main__':
    pass