import random

def generate_class_c_ip():
    first_octet = random.randint(192, 223)
    second_octet = random.choice([x for x in range(256) if x != 168])
    third_octet = random.randint(0, 255)
    fourth_octet = random.randint(1, 254) # 0 is reserved base, 255 is reserved broadcast

    return f"{first_octet}.{second_octet}.{third_octet}.{fourth_octet}"

random_ip = generate_class_c_ip()
print("Random Class C Public IP address:", random_ip)
