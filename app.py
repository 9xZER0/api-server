from fastapi import FastAPI

app = FastAPI()

# Home page
@app.get("/")
def home():
    return {
        "messages" : "Welcome To Secure World"
    }

# Login User
@app.post("/verify_user")
def login():
    return {
        "messages" : "Success"
    }

# Signup User
@app.post("/create_user")
def signup():
    return{
        "message" : "User Created"
    }

# Reset User Password
@app.post("/reset_password")
def forgot():
    return {
        "message" : "Reset Successful"
    }

# Logout User
@app.get('/logout')
def logout():
    return {
        "message" : "Logout Successful"
    }