import pandas as pd


def number_norm(data, name, new_name):

    df = data.copy()

    try:
        df.insert(loc=0, column=new_name, value=df[name])
    except ValueError:
        if df[new_name][0] == df[name][0]:
            pass
        else:
            print('Выбери другое имя нового столбца!')
            return

    def number_change(n):
        try:
            r = ''
            for i in n:
                if i.isdigit():
                    r += str(i)
        except TypeError:
            return None
        else:
            r1 = None
            if len(r) > 10:
                r = r[0:11]
                if r[0] == '7':
                    r1 = r
                elif r[0] == '8':
                    r1 = '7' + r[1:]
        return r1

    print(df.shape)
    df[new_name] = df[new_name].map(number_change)
    df_dropna = df.dropna(subset=[new_name], ignore_index=True)
    print(df_dropna.info())
    print(df_dropna)
    return df_dropna


piranya = pd.read_csv('пиранья.csv', dtype=str)
print(piranya.head(5))
piranya.info()
piranya['Телефон'].isnull().value_counts()
piranya_mod = number_norm(data=piranya, name='Телефон', new_name='number')
piranya_mod.to_excel('Пиранья обработанно.xlsx')
