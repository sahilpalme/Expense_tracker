import pandas as pd


def add_expense():
    main_list = []
    a = ''
    while True:
        a = input("Enter the reason(Enter q to quit): ")
        if a == 'q':
            break
        else:
            b = int(input("Enter the amount spent: "))
            c = (input("Enter the date: "))
            main_list.append({'Date':c,'Reason':a,'Amount':b})

        #pandas part
    filename= 'user_database.xlsx'
    df_existing = pd.read_excel(filename)
    newdata = pd.DataFrame(main_list)
    df_updated = pd.concat([df_existing, newdata], ignore_index=True)
    df_updated.to_excel(filename, index=False)
    print("\nData captured successfully in DataFrame:")


def total_expense():
    df = pd.read_excel('user_database.xlsx')
    t = df['Amount'].sum()
    print(f'Total expense: {t}')


add_expense()
total_expense()