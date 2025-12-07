import json
import hashlib

def checkSignup(username, email, password, confirm_password):
    if not all([username, email, password, confirm_password]):
        return "Please fill in all the fields"
    
    if len(username) < 5:
        return "Username must be at least 5 characters long"
    
    if len(password) < 6:
        return "Password must be at least 6 characters long"
    
    if password != confirm_password:
        return "Passwords don't match"
    
    if "@" not in email or "." not in email:
        return "Invalid email address"
    
    # Check if any exsiting users or email
    users = getUsers()
    for user in users:
        if user['username'].lower() == username.lower():
            return "That username is already taken, try a different one"
        if user['email'].lower() == email.lower():
            return "That email is already registered, try logging in instead"
    return None

def getUsers():
    with open("users.json", 'r') as f:
        return json.load(f)

def addUser(username, email, password):
    users = getUsers()
    
    #Hash password
    hashed = hashlib.sha256(password.encode()).hexdigest()
    users.append({
        'username': username,
        'email': email,
        'password': hashed
    })
    
    with open("users.json", 'w') as f:
        json.dump(users, f, indent=2)

def checkLogin(username, password):
    users = getUsers()
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    
    for user in users:
        if user['username'].lower() == username.lower():
            if user['password'] == hashed_password:
                return None  
            else:
                return "Incorrect password"
    return "Username not found"
