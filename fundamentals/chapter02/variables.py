message = "Hello Python world!"
# print(mesage) gives error
print(message)

# String formatting

name = "ada lovelance"
#case formatting string methods()
print(name.title()) # returns Ada Lovelance title->Title Case
print(name.upper()) # returns ADA LOVELANCE upper->UPPER CASE
print(name.lower()) # returns ADA LOVELANCE lower->lower case

# Using variables in string
first_name = "albert"
last_name = "einstein"

full_name = f"{first_name} {last_name}" 
# f is for 'fromat'
# f"..{variable}..." is a format string

full_name = full_name.title() #title case the name

message = f"Hello, {full_name}"
print(message)

