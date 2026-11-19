# LeetCode 2288. Apply Discount to Prices
# Language: Python

class Solution:
    def discountPrices(self, sentence, discount):
        words = sentence.split()
        result = []

        for word in words:
            if word.startswith("$") and word[1:].isdigit():
                price = int(word[1:])
                discounted = price * (100 - discount) / 100
                result.append(f"${discounted:.2f}")
            else:
                result.append(word)

        return " ".join(result)
