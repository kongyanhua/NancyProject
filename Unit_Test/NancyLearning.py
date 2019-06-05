__metaclass__=type #

# class Person:
#
#     def SetName(self,name):
#         self.name=name
#     def GetName(self,):
#         return self.name
#     def Great(self):
#         print ("Hello, I am %s." % self.name)
#
# foo=Person()
# foo.SetName('Nancy')
# foo.Great()
# class Secretive:
#     def __inaccessible(self):
#         print ("Bet you can't see me ")
#     def accessible(self):
#         print ("The secret message is ")
#         self.__inaccessible()
# s=Secretive()
# #s.__inaccessible
# s.accessible()
# class Filter:
#     def init(self):
#         self.blocked = []
#     def filter(self, sequence):
#         return [x for x in sequence if x not in self.blocked]
# class SPAMFilter:
#     def init(self):
#         self.blocked='SPAM'
# f=Filter()
# f.init()
# f.filter([1, 2, 3])
# print (f.filter)
# result=issubclass(SPAMFilter, Filter)
# print (result)


class Calculator:
    def calculate(self,expression):
        self.value=eval(expression)
class Talker:
    def talk(self):
        print("Hi ,my value is ",self.value)
class TalkingCalculator(Calculator,Talker):
    pass
tc=TalkingCalculator()
tc.calculate('1+2*4')
tc.talk()

print(hasattr(tc,'talk'))
