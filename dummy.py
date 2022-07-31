class student:
    def __init__(self, name, add, marks):
        print("{} scored {} marks.".format(name, marks))
        self.name = name
        self.add = add
        self.marks = marks

    def result(self):
        print("{} achieved {} marks".format(self.name, self.marks))

    def address(self):
        print("{} lives at {}".format(self.name, self.add))


class achiever(student):
    def __init__(self, name, add, marks, division):
        self.name = name
        self.add = add
        self.marks = marks
        print("{} is a achiever with a good marks and {} division.".format(name, division))
        super().__init__(self.name, self.add, self.marks)
        self.division = division

    def outcome(self):
        # super().__init__(name, add, marks)
        print("As {} got {} marks, so his division is {}.".format(self.name, self.marks, self.division))
        # print("As n got m marks, so his division is {}.".format(self.division))


class hallfame(student):
    def __init__(self, name, address, mark):
        print("{} is hall of famer for achieving {} marks and is living in {}.".format(name, mark, address))
        super().__init__(name, address, mark)


class success(achiever, hallfame):
    def __init__(self, name, add, marks, div):
        print("{} achieved {} division.".format(name, div))
        # Calling the constructor of both the parent class in the order of their inheritance
        super().__init__(name, add, marks,
                         div)  # calls init method of base class 1(achiever) which also calls its parent class student
        super(achiever, self).__init__(name, add,
                                       marks)  # calls init method of base class 2(hallfame) which also calls its parent class student
        # self.div = div


suc = success("Irfan", "Mumbai", 45, "first")
print('')
ach = achiever("qasim", 'delhi', 30, "second")
ach.outcome()
print('*' * 50)
ach.result()  # accessing methods of the super class using object of the subclass
print('*' * 50)
ach.address()