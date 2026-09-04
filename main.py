import pandas as pd


def add_expense():
    main_list = []
    a = ''
    while a != 'q':
        a = input("Enter the reason(Enter q to quit): ")
        if a == 'q':
            break
        b = int(input("Enter the amount spent: "))
        c = (input("Enter the date: "))

        main_list.append({'Date':c,'Reason':a,'Amount':b})

        df = pd.DataFrame(main_list)
        print(df)
        #pandas part
        filename= 'user_database.xlsx'
        df_existing = pd.read_excel(filename)
        newdata = pd.DataFrame(main_list)
        df_updated = pd.concat([df_existing, newdata], ignore_index=True)
        df_updated.to_excel(filename, index=False)
        t = 0
        for i in range(7):
            z = df_updated.loc[i,'Amount']
            t = t+z
        print(f'Total expense: {t}')
        print("\nData captured successfully in DataFrame:")

add_expense()