"""
Simulate a retail store's inventory updates over a single business day using only assignment operators (+=, -=, *=).
Requirements:
Start with a variable stock = 50.A morning customer buys 12 items (decrease stock).
A delivery truck arrives and doubles the remaining stock (multiply stock).
An evening shipment arrives, adding 15 more items (increase stock).
Print the value of stock after each individual operation to track the history."""

stock = 50

while True:
    operation = input("enter : customer, truck, shipment : ")
    if operation == "customer":
        stock -= 12
        print(f" current stock : {stock} " )
    elif operation == "truck":
        stock *= 2
        print(f" current stock : {stock} " )
    elif operation == "shipment":
        stock += 15
        print(f" current stock : {stock} " )
    else:
        break

print(f" final stock : {stock} " )