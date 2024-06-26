# Passing data from Parent function to child function
def countVowel(word,i,n,res):
    if i==n:
        print("Vowels count is:",res)
        return 
    v="aeiouAEIOU"
    if word[i] in v:
        res+=1
    countVowel(word,i+1,n,res)
word="abcdeefuigh"
n=len(word)
countVowel(word,0,n,0)

# Passing data from child function to Parent function
def countVowel1(word,i,n,res):
    if i==n:
        return 0
    nextcountvowels=countVowel1(word,i+1,n,res)
    v="aeiouAEIOU"
    if word[i] in v:
        nextcountvowels+=1
    return nextcountvowels
word="abcdeefuigh"
n=len(word)
print("Vowels count is: ",countVowel1(word,0,n,0))