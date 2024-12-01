class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class UserList:
    def __init__(self, filename):
        self.userlist = []
        self.filename = filename

    def read_user_file(self):
        try:
            with open(self.filename, 'r') as file:
                for line in file:
                    username, password = line.strip().split(',')
                    self.userlist.append(User(username, password))
        except FileNotFoundError:
            print("File not found. Starting with an empty user list.")

    def write_user_file(self):
        with open(self.filename, 'w') as file:
            for user in self.userlist:
                file.write(f"{user.username},{user.password}\n")

    def display_user_list(self):
        print(f"{'Username':<15} {'Password':<15}")
        print(f"{'-'*15} {'-'*15}")
        for user in self.userlist:
            print(f"{user.username:<15} {user.password:<15}")

    def find_username(self, username):
        for index, user in enumerate(self.userlist):
            if user.username == username:
                return index
        return -1

    def change_password(self, username, password):
        index = self.find_username(username)
        if index != -1:
            self.userlist[index].password = password

    def add_user(self, username, password):
        if self.find_username(username) == -1:
            self.userlist.append(User(username, password))

    def delete_user(self, username):
        index = self.find_username(username)
        if index != -1:
            del self.userlist[index]

    def strength(self, password):
        score = 0
        if len(password) >= 8:
            score += 1
        if any(char.isupper() for char in password):
            score += 1
        if any(char.islower() for char in password):
            score += 1
        if any(char.isdigit() for char in password):
            score += 1
        if any(char in "~!@#$%^&*()_+|-={}[]:;<>?/" for char in password):
            score += 1
        return score

def main():
    user_list = UserList('Final_Project_Passwords.txt')
    user_list.read_user_file()

    while True:
        print("\nMenu:")
        print("1) Add a New User")
        print("2) Delete an Existing User")
        print("3) Change Password on an Existing User")
        print("4) Display All Users")
        print("5) Save Changes to File")
        print("6) Quit")
        selection = input("Enter Selection: ")

        if selection == '1':
            username = input("Enter User ID: ")
            if user_list.find_username(username) != -1:
                print("Username Already Exists")
            else:
                while True:
                    password = input("Enter Password: ")
                    strength = user_list.strength(password)
                    if strength < 5:
                        print(f"This password is weak - {strength}")
                    else:
                        user_list.add_user(username, password)
                        print("User Added")
                        break

        elif selection == '2':
            username = input("Enter User ID: ")
            if user_list.find_username(username) == -1:
                print("Username Not Found")
            else:
                user_list.delete_user(username)
                print("User Deleted")

        elif selection == '3':
            username = input("Enter User ID: ")
            if user_list.find_username(username) == -1:
                print("Username Not Found")
            else:
                while True:
                    password = input("Enter New Password: ")
                    strength = user_list.strength(password)
                    if strength < 5:
                        print(f"This password is weak - {strength}")
                    else:
                        user_list.change_password(username, password)
                        print("Password Changed")
                        break

        elif selection == '4':
            user_list.display_user_list()

        elif selection == '5':
            user_list.write_user_file()
            print("Changes Saved")

        elif selection == '6':
            break

        else:
            print("Invalid Selection")

if __name__ == "__main__":
    main()
