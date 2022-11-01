def remove_char(s1,s2):
    dict={ord(s2):None}
    print(s1.translate(dict))
s1=input("give string:")
s2=input("give character to remove:")
remove_char(s1,s2)
