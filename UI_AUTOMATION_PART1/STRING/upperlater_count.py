from logging import raiseExceptions, exception

text = "countletterLATER"
upper_latter_count = 0
lower = 0

for i in text:
    if i.isupper():
        upper_latter_count += 1
    elif i.islower():
        lower += 1
print(upper_latter_count)
print(lower)