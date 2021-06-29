class distributore_automatico():

    dict_products = {"cola": 1, "tea" : 1.5, "water": 0.35}
    totMoney = 0
    secretPasswd = "5G;xsB*XZ3zZh4D"

    def __init__(self, amount, balance, password = "", dict_quantity = {}) -> None:
        self.dict_quantity = distributore_automatico.dict_products.fromkeys(self.dict_products, 1)
        self.amount = amount
        self.balance = balance
        self.password = password

    def insert_credit(self):
        self.balance += self.amount # al tot += self.balance che sarebbe tutti i soldi inseriti.
        distributore_automatico.totMoney += self.amount
        self.amount = 0


    def exists(self, product) -> bool:
        if product not in self.dict_quantity.keys() or self.dict_quantity[product] == 0:  #Prodotto esaurito o non esistente
            return False
        return True

    def ask_price(self, ask):
        if self.exists(ask) == False:
            return None
        else:
            return distributore_automatico.dict_products[ask]

    def get_product(self, product):
        if self.exists(product) == False:
            return None
        else:
            if self.balance < distributore_automatico.dict_products[product]:
                return None # credito < prezzo
            self.dict_quantity[product] -= 1
            distributore_automatico.totMoney += distributore_automatico.dict_products[product]
            self.balance -= distributore_automatico.dict_products[product]
            distributore_automatico.totMoney -= distributore_automatico.dict_products[product]
            self.balance = round(self.balance, 2)
        return True
    
    def get_rest(self):
        if distributore_automatico.totMoney == 0:
            return None # passato prima l`omino a prendersi i soldi
        if self.balance == 0:
            return None
        else:
            rest = self.balance
            self.balance = 0
            return round(rest, 2)

    def add_product(self, product_toadd, quantity): #Solo operatore
        if self.password != distributore_automatico.secretPasswd:
            return None
        if product_toadd in self.dict_quantity.keys():
            self.dict_quantity[product_toadd] += quantity
        else:
            self.dict_quantity[product_toadd] = quantity

    def get_money(self): #Solo operatore
        if self.password != distributore_automatico.secretPasswd:
            return None
        money = distributore_automatico.totMoney
        distributore_automatico.totMoney = 0
        return round(money, 2)

if __name__ == "__main__":
    obj = distributore_automatico(1.20, 0)
    obj.insert_credit()
    obj.get_product("cola")
    # print(obj.balance)
    obj_operator = distributore_automatico(0, 0, "5G;xsB*XZ3zZh4D")
    print(obj_operator.get_money())
    print(obj.get_rest())
    # obj_operator.add_product("diocnae", 4)
    # print(obj_operator.dict_quantity)
    # obj.insert_credit()
    # print(obj.balance, obj.amount)   
    # obj.insert_credit()
    # print(obj.balance)
    # print(obj.get_product("cola"))
    # print(obj.balance)
    # print(obj.get_rest())
    # print(obj.balance)