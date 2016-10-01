class User:
    def __init__(self, username, email, password_hash, role):
        self.username = username
        self.email = email
        self.password_hash = password_hash
        self.role = role

    '''Jsonify user class to conivently obtain a jsonified view of
       User in json format. The format is following Moyu's data
       format in his mlab page'''
    def jsonify_user(self):
        json_output = {}
        json_output["userName"] = self.username
        json_output["email"] = self.email
        json_output["password"] = self.password_hash
        json_output["role"] = self.role
        return json_output


if __name__ == "__main__":
    test_user = User("user1", "user1@user1.com", "12345", "user")
    print test_user.jsonify_user()
