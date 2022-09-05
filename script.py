'''
Hacking The Fender
The Fender, a notorious computer hacker and general villain of the people, has compromised several top-secret passwords including your own. 
Your mission, should you choose to accept it, is threefold. 
You must acquire access to The Fender‘s systems, you must update his "passwords.txt" file to scramble the secret data. 
The last thing you need to do is add the signature of Slash Null, a different hacker whose nefarious deeds could be very conveniently halted by 
The Fender if they viewed Slash Null as a threat.
'''
import csv
import json
# create an empty list
compromised_users = []
# opem the csv file and save to a password_file variable
with open("passwords.csv") as password_file:
    # make a dictionairy from the file and save in password_csv for use
    password_csv = csv.DictReader(password_file)
    # iterate through each row and save the username into the empty list created earlier
    for password_row in password_csv:
        compromised_users.append(password_row["Username"])

# open a new writable "w" file to save the compromised users to from the 
# compromised_users list we created above from the passwords.csv file
with open("compromised_users.txt","w") as compromised_user_file:
    # iterate over each username and save to the file
    for user in compromised_users:
        compromised_user_file.write(user)

# create json file from boss_message dictionairy
with open('boss_message.json','w') as boss_message:
    boss_message_dict = {
    'recipient':'The Boss',
    'message':'Mission Success'
    }
    json.dump(boss_message_dict, boss_message)
    
with open('new_passwords.csv','w') as new_passwords_obj:
    slash_null_sig = """
    / )( \   / __) /  \(_  _)            
) \/ (  ( (_ \(  O ) )(              
\____/   \___/ \__/ (__)             
 _  _   __    ___  __ _  ____  ____  
/ )( \ / _\  / __)(  / )(  __)(    \ 
) __ (/    \( (__  )  (  ) _)  ) D ( 
\_)(_/\_/\_/ \___)(__\_)(____)(____/ 
        ____  __     __   ____  _  _ 
 ___   / ___)(  )   / _\ / ___)/ )( \
(___)  \___ \/ (_/\/    \\___ \) __ (
    (____/\____/\_/\_/(____/\_)(_/
__ _  _  _  __    __                
(  ( \/ )( \(  )  (  )               
/    /) \/ (/ (_/\/ (_/\             
\_)__)\____/\____/\____/"""
    new_passwords_obj.write(slash_null_sig)