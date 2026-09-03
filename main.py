import pandas as pd

main_list = []
a = input("Enter the reason: ")
b = int(input("Enter the prize: "))
c = (input("Enter the date: "))

main_list.append([a,b,c])

#pandas part
filename= 'user_database.xlsx'
df_existing = pd.read_excel(filename)
newdata = pd.DataFrame(main_list)
df_updated = pd.concat([df_existing, newdata], ignore_index=True)
df_updated.to_excel(filename, index=False)

print("\nData captured successfully in DataFrame:")
