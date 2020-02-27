class reverse():
    def get_string(self):
        self.string = input("Enter string to be reversed: ")
        s = self.string.split(" ")
        s = s[::-1]
        print(" ".join(s))

string = reverse()
string.get_string()
