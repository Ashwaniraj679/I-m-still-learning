unique_id = 2002060940
count = 0


with open('output.txt','w') as file:
    while count < 25:
        i = 1
        while i < 20001:
            for x in range(20000):
                file.write(f'<record from="{i}" to="graphics/pictures/person/{unique_id}/portrait"/>\n')
                i +=1
                unique_id +=1
            count += 1
    
print("XML files created successfully.")
