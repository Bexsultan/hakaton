class MoneyFmt:

    def __init__(self,amount):
        self.amount = amount

    def update(self, amount2):
        self.amount = amount2

    def repr(self):
        return float(self.amount)

    def __str__(self):
        if self.amount >= 0:
            return '${:,.2f}'.format(self.amount)
        else:
            return '-${:,.2f}'.format(self.amount)
