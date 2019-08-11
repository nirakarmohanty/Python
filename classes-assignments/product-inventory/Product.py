
class Product():
    price=0
    id=0
    quantity=0
    def __init__(self,price,id,quantity):
        print('Product Class')
        self.id=id
        self.price=price
        self.quantity=quantity

    def calculateTotalPrice(self):
        self.price=self.price

    def calculateQuantity(self,quantity):
        self.quantity=self.quantity+quantity

    def getTotalPriceOfProduct(self):
        return self.price

    def getTotalQuantityOfProduct(self):
        return self.quantity


object = Product(120,12,100)
object.calculateTotalPrice()
result=object.getTotalPriceOfProduct()
print(result)
