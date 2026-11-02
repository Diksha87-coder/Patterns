#shopping discount calculator
def calculate_discount(amount):
    if amount > 5000:
        discount = amount * 20 / 100
    elif amount >= 3000:
        discount = amount * 15 / 100
    elif amount >= 1000:
        discount = amount * 10 / 100
    else:
        discount = 0

    final_amount = amount - discount

    return discount, final_amount


amount = float(input("Enter shopping amount: "))

discount, final_amount = calculate_discount(amount)

print("Discount:", discount)
print("Final payable amount:", final_amount)


#word frequency counter using function

def word_frequency(text):
    words = text.lower().split()

    frequency = {}

    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    print("Total words:", len(words))
    print("Word frequency:", frequency)

    max_word = max(frequency, key=frequency.get)
    print("Most frequent word:", max_word)

    print("Words appearing only once:")
    for word in frequency:
        if frequency[word] == 1:
            print(word)


text = input("Enter an article: ")
word_frequency(text)