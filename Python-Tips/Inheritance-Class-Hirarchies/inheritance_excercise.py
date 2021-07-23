# Start off by creating the Result class
class Result():
    '''Class to add the result of the students'''
    results ={"A":88,
              "B":71,
              "C":84,
              "D":95,
              "E":60,
              "F":89}
    # method to add new student with his/her mark
    def add_rslt(self, student = '', marks = 0):
        self.results[student] = marks

class Student(Result):
    '''Class to print the result of the students'''
    def sho_rslt(self, student):
        print(student, 'got', self.results[student], 'marks')


if __name__ == '__main__':
    std = Student()
    std.add_rslt("G", 85)
    std.add_rslt('H', 67)
    lst = ["A","B","D","F","H"]
    for i in lst:
        std.sho_rslt(i)
        #