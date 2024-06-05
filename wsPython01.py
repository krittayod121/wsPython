def calculate_mhr(age):
    return 220 - age

def calculate_zone2(mhr):
    low = 0.6 * mhr
    up  = 0.7 * mhr
    return low, up

age = int(input("อายุปัจจุบัน : "))
mhr = calculate_mhr(age)
low_zone2, up_zone2 = calculate_zone2(mhr)

print(f"อัตราการเต้นของหัวใจตํ่าสุดที่เหมาะสม: {up_zone2:.2f} ")
print(f"อัตราการเต้นของหัวใจตํ่าสุดที่เหมาะสม: {low_zone2:.2f}")
