#1
print("hello world")

#2
def greet():
    print("こんにちは")
greet()

#3
def greet(name):
    print(f"私の名前は{name}です")
greet("綾子")

#4
def get_greet():
    return "おはようございます"
get_greet()
print(get_greet())

#5
def add(a, b):
    return a + b
result = add(1, 6)
print(result)