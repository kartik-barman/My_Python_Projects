
print("======================================")
print("           Email Validation           ")
print("======================================")

Email = input("Enter your Valid Email Id : ")

email_length = len(Email)

print(email_length)
if email_length >= 6:
  if Email[0].isalpha():
      if ("@" in Email) and (Email.count("@") == 1):
          print("5")
      else:
          print("Email should be used to atleast 1 @")
  else:
      print("Email should be begin alphabet")
else:
    print("Email should be used 8 words")
