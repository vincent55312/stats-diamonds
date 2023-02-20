import json
import matplotlib.pyplot as plt
import numpy as np


class DiamondDTO:
    def __init__(self, carat, cut, color, clarity, depth, table, price, x, y, z):
        self.carat = carat
        self.cut = cut
        self.color = color
        self.clarity = clarity
        self.depth = depth
        self.table = table
        self.price = price
        self.x = x
        self.y = y
        self.z = z

with open("data.json") as file:
    data = json.load(file)

diamonds = []
for diamond_data in data:
    diamond = DiamondDTO(
        carat=diamond_data["carat"],
        cut=diamond_data["cut"],
        color=diamond_data["color"],
        clarity=diamond_data["clarity"],
        depth=diamond_data["depth"],
        table=diamond_data["table"],
        price=diamond_data["price"],
        x=diamond_data["x"],
        y=diamond_data["y"],
        z=diamond_data["z"]
    )
    diamonds.append(diamond)

price_average = 0
prices = []
for diamond in diamonds:
    price_average += diamond.price
    prices.append(diamond.price)

price_average /= len(diamonds)

prices.sort()
mid = len(prices) // 2
if len(prices) % 2 == 0:
    median_price = (prices[mid-1] + prices[mid]) / 2
else:
    median_price = prices[mid]
print("number diamonds", len(prices))
print("low price", prices[0])
print("big price", prices[len(prices)-1])
print("price average", price_average)
print("median price:", median_price)

# Créer une liste de carats et une liste de prix
carats = [diamond.carat for diamond in diamonds]
prices = [diamond.price for diamond in diamonds]

# Calculer la droite de régression
slope, intercept = np.polyfit(carats, prices, 1)
max_price = max(prices)
max_carat = (max_price - intercept) / slope
line = [max_price if price > max_price else price for price in (slope * np.array([0, max_carat]) + intercept)]

# Créer le graphique avec la droite de régression allant jusqu'au prix maximum
plt.scatter(carats, prices, s=1)
plt.plot([0, max_carat], line, color='red')
plt.xlabel('Carats')
plt.ylabel('Price')
plt.show()