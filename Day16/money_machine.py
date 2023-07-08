
class MoneyMachine:

    currency = '$'

    COIN_VALUES = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }

    def __init__(self):
        self.profit = 0;
        self.money_received = 0;

    def report(self):
        print(f"Money: {self.currency}{self.profit}")

    def process_coins(self):
        print("Please insert the coins");

        for coin in self.COINS_VALUES: # type: ignore
            self.money_received += int(input(f"enter the {coin}?")) * COIN_VALUES[coin];

        return self.money_received

    def make_payment(self,cost):
        
        self.process_coins()

        if(self.money_received >= cost):
            change = round(self.money_received - cost, 2)
            print(f"Here is {self.currency}{change} in change.")
            self.profit += cost
            self.money_received = 0
            return True
        else:
            print("Sorry that's not enough money. Money refunded.")
            self.money_received = 0
            return False
