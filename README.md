# 🔐 One-Time Pad (OTP) Encoder/Decoder

This Python script demonstrates a basic implementation of the **One-Time Pad encryption** algorithm — a theoretically unbreakable cipher when the key is truly random and used only once.

## 🧠 How It Works
- Takes a plaintext message (`m`) and a key (`k`) of the same length
- XORs each byte of the message with the corresponding byte of the key
- Base64-encodes the output for easy display and storage
- Decryption reverses the process with the same key

## ⚠️ Key Rule
The key **must be the exact same length** as the message to maintain perfect secrecy.

## ✅ Example Usage
```python
m = "SkylerLovesSusie"
k = "SecretMessagelbn"

enc = otp(m, k)
print(f"Encrypted: {enc}")

dec = otpd(enc, k)
print(f"Decrypted: {dec}")
