# 3) Write a program to solve a fractional Knapsack problem using a greedy method
class Item:
    def _init_(self, value, weight):
        self.value = value
        self.weight = weight

    def fractionalKnapsack(W, arr):
        arr.sort(key=lambda x: (x.value / x.weight), reverse=True)
        finalvalue = 0.0
        for item in arr:
            print(finalvalue)
            if item.weight <= W:
                W -= item.weight
                finalvalue += item.value
            else:
                finalvalue += item.value * W / item.weight
                break
        return finalvalue


if _name_ == "_main_":
    W = 50
    arr = [Item(60, 10), Item(100, 20), Item(120, 30)]
    max_val = Item.fractionalKnapsack(W, arr)
    print(max_val)
