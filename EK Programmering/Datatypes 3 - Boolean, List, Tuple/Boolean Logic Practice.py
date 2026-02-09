#Write a Python program that:

#1. Creates three boolean variables:
#• is_logged_in
#• has_admin_rights
#• account_locked

#2. Sets them to values that would represent a normal user who is logged in but whose account is locked.

#3. Use logical operators to check if the user should be granted access (logged in AND has admin rights AND NOT locked)

#4. Prints "Access Granted" or "Access Denied" based on the result

# 1. Boolean variables
is_logged_in = True
has_admin_rights = False
account_locked = True

# 2 & 3. Access control logic
if is_logged_in and has_admin_rights and not account_locked:
    print("Access Granted")
else:
    print("Access Denied")

# Bonus challenge: Security alert
if is_logged_in and account_locked:
    print("Security Alert")
