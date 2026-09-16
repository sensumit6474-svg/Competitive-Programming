n = int(input("Enter number of products: "))

prices = list(map(float, input("Enter product prices: ").split()))

prices.sort()

print("Prices in ascending order:")
print(prices)