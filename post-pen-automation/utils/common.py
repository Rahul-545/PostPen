from faker import Faker
import random

fake = Faker()

def generate_random_email():
    return f"{fake.user_name()}{random.randint(100,999)}@test.com"

def generate_random_password(length=12):
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*'
    return ''.join(random.choice(chars) for _ in range(length))