# Length of String
str="Sarthak"

length=len(str)

# Strings are immutable
# Means string methd don't change original string but always return new string



#Convert to upper and lower case
strUpper=str.upper()
strLower=str.lower()

print(strUpper)
print(strLower)



# Replace the occurenences of chars
str="sarthak"
strReplace=str.replace("s","k")
print(strReplace)

# Split the string
# Returns a list
strSplit=str.split("a")
print(strSplit)

# To Make first letter capital and 
# make all other letters small
print(str.capitalize())


# Count number of occuerences
print(str.count("a"))


# To check if it ends with that string
print(str.endswith("ak"))


# To find the first occurence and return the index
# If does not find gives -1
print(str.find("ak"))


# If contains only A-Z and a-z
print(str.isalpha())

# If contains only A-Z and a-z and 0-9
print(str.isalnum())