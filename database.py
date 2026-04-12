from datetime import datetime
from hashing import hash_password, verify_password

class SecureCloudDatabase:
    """
    Simulated secure database for cloud storage system.
    Handles users, files, logs, and backups.
    """

    def __init__(self):
        self.users = []          # stores user accounts
        self.files = []          # stores encrypted files/data
        self.logs = []           # stores system activity logs
        self.backup = []         # backup storage

    def create_user(self, username: str, password: str, role: str = "client"):
        """
        Create a new user with hashed password.
        """

        hashed_data = hash_password(password)

        user = {
            "id": len(self.users) + 1,
            "username": username,
            "password_hash": hashed_data["hash"],
            "salt": hashed_data["salt"],
            "role": role,
            "created_at": datetime.now().isoformat()
        }

        self.users.append(user)
        self._log_action(user["id"], "USER_CREATED")

        return user

    def authenticate_user(self, username: str, password: str):
        """
        Verify login credentials.
        """

        for user in self.users:
            if user["username"] == username:

                is_valid = verify_password(
                    password,
                    user["salt"],
                    user["password_hash"]
                )

                if is_valid:
                    self._log_action(user["id"], "LOGIN_SUCCESS")
                    return user

                self._log_action(user["id"], "LOGIN_FAILED")
                return None

        return None

    def store_file(self, user_id: int, encrypted_data: str):
        """
        Store encrypted file/data for a user.
        """

        file_entry = {
            "id": len(self.files) + 1,
            "user_id": user_id,
            "data": encrypted_data,
            "created_at": datetime.now().isoformat()
        }

        self.files.append(file_entry)
        self._log_action(user_id, "FILE_STORED")

        return file_entry

    # ==============================
    # 📥 RETRIEVE USER FILES
    # ==============================

    def get_user_files(self, user_id: int):
        """
        Get all files belonging to a user.
        """

        return [f for f in self.files if f["user_id"] == user_id]


    def create_backup(self):
        """
        Copy all data into backup storage.
        """

        self.backup = {
            "timestamp": datetime.now().isoformat(),
            "users": self.users.copy(),
            "files": self.files.copy(),
            "logs": self.logs.copy()
        }

        return self.backup


    def _log_action(self, user_id: int, action: str):
        """
        Internal logging function (not exposed).
        """

        log = {
            "id": len(self.logs) + 1,
            "user_id": user_id,
            "action": action,
            "timestamp": datetime.now().isoformat()
        }

        self.logs.append(log)


    def get_logs(self):
        return self.logs


if __name__ == "__main__":

    db = SecureCloudDatabase()

    user = db.create_user("rayan", "123456", "client")
    print("User created:", user)

    auth = db.authenticate_user("rayan", "123456")
    print("Login success:", auth is not None)

    file = db.store_file(user["id"], "ENCRYPTED_SAMPLE_DATA")
    print("File stored:", file)

    print("User files:", db.get_user_files(user["id"]))

    backup = db.create_backup()
    print("Backup created at:", backup["timestamp"])
