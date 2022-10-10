class Employee:
    raise_amt = 1.04

    def __int__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)


class Developer(Employee):
    super().__int__()


dev1 = Developer('Sazzad', 'Hussain', 50000)
dev2 = Developer('Alpha', 'Beta', 30000)

print(dev1.email)
print(dev2.email)