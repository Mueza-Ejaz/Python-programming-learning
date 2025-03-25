
# Recursion Python Mein – Simple Aur Beginner Level Explanation
# Recursion ka matlab hota hai "Ek function ka khud ko call karna". Matlab, ek function apne andar hi dubara call hota hai jab tak ek
# stopping condition na mil jaye.

# Recursion Ka Basic Concept:
# - Recursion do cheezon par depend karta hai

# 1- Base Case: Ye ek stopping condition hoti hai jo recursion ko rok deti hai, warna program infinite loop mein chala jata hai.

# 2- Recursive Case: Ye woh condition hoti hai jisme function khud ko call karta hai aur problem ko chhoti chhoti parts mein todta hai.

# Example 1: Counting Numbers Using Recursion
# Agar hum 1 se n tak numbers print karna chahein, to recursion ka use kar sakte hain.

def count(n):
    if n == 0:  # Base case (jab 0 ho jaye to ruk jao)
        return
    count(n - 1)  # Recursive call (chhoti problem)
    print(n)  # Ye tab execute hoga jab recursion wapas aaye ga

count(5)

# output:
1  
2  
3  
4  
5  
