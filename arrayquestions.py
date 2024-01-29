# Question no. 1

arr = [3, 2, 5, 7, 10]
target = 9

def twoSum(arr, target):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if target - arr[i] == arr[j]:
                return [i,j]
            else:
                print("NO. Not Found")
            
print(twoSum(arr, target))
twoSum(arr, target)



# Question no. 2  best time for buying and sell shares
def bestTime(prices):
    if len(prices) < 2:
        print("Price data is insufficient...")
        return 0  # or return some default value

    min_price = prices[0]
    max_profit = 0

    for price in prices[1:]:
        min_price = min(min_price, price)
        print(min_price)
        max_profit = max(max_profit, price - min_price)

    return max_profit

prices = [7, 1, 5, 3, 6, 4]
print(bestTime(prices), "max profit")


# Question no. 3  duplicates
nums = [1, 2, 3, 1]

def check_duplicate(nums):
    if len(set(nums)) == len(nums):
        return False
    
    else:
        return True
    

print(check_duplicate(nums))




# Q4. Valid Anagram
    
s = "anagram"
t = "nagaram"

def is_anagrams(s, t):
    if sorted(s) == sorted(t):
        return True
    else:
        return False
    
print(is_anagrams(s,t))



# Question no. 5 palindrome

s = "A man, a plan, a canal: Panama"

def isPalindrome(s):
    cleaned_string = ''.join(char.lower() for char in s if char.isalnum())

    return cleaned_string == cleaned_string[::-1]

print(isPalindrome(s))


  
        
