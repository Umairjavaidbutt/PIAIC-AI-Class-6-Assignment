class String():
  def __init__(self):
    self.string = ""
  def get_String(self):
    self.string = input("Enter statement: ")
  def print_String(self):
    print(self.string.upper())
        
string = String()        
string.get_String()
string.print_String()
