import hashlib
import os
import hmac


def hash_password(password: str, salt: str = None) -> dict:
    """
    Hash a password using SHA-256 with optional salt.

    Returns:
        dict: {
            "salt": salt used,
            "hash": hashed password
        }
    """

    # Generate salt if not provided
    if salt is None:
        salt = os.urandom(16).hex()

    # Combine password + salt
    salted_password = password + salt

    # Hash using SHA-256
    hashed = hashlib.sha256(salted_password.encode()).hexdigest()

    return {
        "salt": salt,
        "hash": hashed
    }


def verify_password(password: str, salt: str, hashed_password: str) -> bool:
    """
    Verify if a password matches the stored hash.
    """

    new_hash = hashlib.sha256((password + salt).encode()).hexdigest()

    return hmac.compare_digest(new_hash, hashed_password)


if __name__ == "__main__":
    # Example usage
    result = hash_password("mypassword123")

    print("Salt:", result["salt"])
    print("Hash:", result["hash"])

    # Verify
    is_valid = verify_password("mypassword123", result["salt"], result["hash"])
    print("Password valid?", is_valid)
