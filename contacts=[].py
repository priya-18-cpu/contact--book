contacts=[]

def add_contact():
    contacts.append({
        "name":input("Name:"),
        "phone":input("Phone:"),
        "email":input("Email:"),
        "address":input("Address:")
         })
    print("Added contact!\n")
    
def view_contact():
    for c in contacts:
        print(f"{c['name']}-{c['phone']}")
        print()
        
def search_contact():
    k=input("Search contact by name/phone:") 
    for c in contacts:
        if k in c['name']or k==c['phone']:
            print(c)
            return
        print("Not found.\n")
        
def update_contact():
    k=input("update contact by name/phone:")
    for c in contacts:
        if k in c['name']or k==c['phone']:
           c['name']=input(f"New name[{c['name']}]:")or c['name']
           c['phone']=input(f"New phone[{c['phone']}]:")or c['phone']
           c['email']=input(f"New email[{c['email']}]:")or c['email']
           c['address']=input(f"New address[{c['address']}]:")or c['address']
           print("updated contact!\n")
           return
    print("Not found.\n")
    
def delete_contact():
    k= input("Delete contact by name/phone:")
    for c in contacts:
        if k in c['name'] or k==c['phone']:
            contacts.remove(c)
            print("Deleted contact!\n")
            return
        print("Not found.\n")
while True:
    print("1.Add contact 2.view contact 3.search contact 4.Update contact 5.Delete contact 6.Exit")
    ch=input("Choose:")
    if ch=='1':add_contact()
    elif ch=='2':view_contact()
    elif ch=='3':search_contact()
    elif ch=='4':update_contact()
    elif ch=='5':delete_contact()
    elif ch=='6':break
            
        
                
       
                                                                  
                   
        

                            

               