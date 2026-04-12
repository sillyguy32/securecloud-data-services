import random


#  Register
def register(db, username, password, role="client"):
    user = db.create_user(username, password, role)
    print(f"[INFO] User '{user['username']}' registered.")
    return user


#  Login with MFA
def login(db, username, password):
    user = db.authenticate_user(username, password)

    if not user:
        print("[ERROR] Invalid username or password.")
        return None

    print("[INFO] Password verified.")

    #  MFA (multi factor auth) step (one time password)
    otp = generate_otp()
    print(f"[DEBUG] OTP sent: {otp}")  # simulate sending OTP

    user_input = input("Enter OTP: ")

    if user_input != otp:
        print("[ERROR] Invalid OTP.")
        return None

    print("[SUCCESS] Login successful.")
    return user


#  OTP (one time password) generator
def generate_otp():
    return str(random.randint(100000, 999999))