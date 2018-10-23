class Greeting:
    def ÅQinitÅQ(self):
        self.msg="hello"
        self.target="paiza"
    def say_hello(self):
        print(self.msg+" "+self.target)
class Hello(Greeting):
    def say_hello(self):
        self.target="python"
        print(self.msg+" "+self.target)
Hello().say_hello() 