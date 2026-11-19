# install cryptography - pip install cryptography
 
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization

# Step 1: Generate private key
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)

# Step 2: Generate public key
public_key = private_key.public_key()

print("Public and Private Keys Generated Successfully!")

# Step 3: Message to be signed
message = b"Hello, this is a secure message."

print("\nOriginal Message:", message.decode())

# Step 4: Sign message using private key
signature = private_key.sign(
    message,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)

print("\nDigital Signature Generated Successfully!")

# Step 5: Verify signature using public key
try:
    public_key.verify(
        signature,
        message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    print("Signature Verified Successfully!")
    print("Message is Authentic.")

except Exception:
    print("Signature Verification Failed!")

# Step 6: Test modified message
modified_message = b"This message has been modified."

print("\nTesting Modified Message:")

try:
    public_key.verify(
        signature,
        modified_message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    print("Signature Verified!")

except Exception:
    print("Verification Failed! Message was Modified.")
