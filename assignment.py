emails = ["kobby@example.com", "enoch@example.com", "jesse@example.com", "peter@example.com"]
print("Original order:", emails)

emails.sort()
print("Sorted order:", emails)

emails.append("akosua@example.com")
emails.append("clarebel@example.com")

emails.pop(1)

print("Number of people coming to the wedding:", len(emails))

emails.sort()
print(emails)