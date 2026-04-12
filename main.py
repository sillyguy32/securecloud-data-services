from database import SecureCloudDatabase
from auth import register, login
try:
    from encryption import encrypt_data, decrypt_data
    encryption_available = True
except ImportError:
    encryption_available = False


def main():
    print("=====  SecureCloud Data Services =====\n")

    
    db = SecureCloudDatabase()

    print(" Creating user...")
    user = register(db,"rayan", "123456", "client")
    print("User created:", user["username"], "with role:", user["role"])

    print("\n Authenticating user...")
    auth_user = login(db,"rayan", "123456")

    if not auth_user:
        print(" Login failed")
        return

    print(" Login successful")


    print("\n Uploading file...")

    raw_data = "VERY_SECRET_CLIENT_DATA"

    if encryption_available:
        encrypted_data = encrypt_data(raw_data)
        print(" Data encrypted")
    else:
        encrypted_data = raw_data
        print(" Encryption module not found, storing raw data")

    file = db.store_file(auth_user["id"], encrypted_data)
    print(" File stored with ID:", file["id"])


    print("\n Retrieving user files...")

    files = db.get_user_files(auth_user["id"])

    for f in files:  # loop through files and print content
        data = f["data"] 

        if encryption_available:
            data = decrypt_data(data)

        print(f"File {f['id']} content:", data)


    print("\n Creating backup...")
    backup = db.create_backup()
    print(" Backup created at:", backup["timestamp"])


    print("\n System Logs:")

    logs = db.get_logs()
    for log in logs:
        print(log)
      
    print("\n SYSTEM RUN COMPLETED SUCCESSFULLY!")


if __name__ == "__main__":
    main()
