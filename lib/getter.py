class Example:
    __name = "ashish"


    @property
    def get_name(s):
        return s.__name
    @get_name.setter
    def get_name(self,n):
        self.__name = n

obj = Example()
obj.get_name = "hari"
print(obj.get_name)
