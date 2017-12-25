import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
br = float(input("Satılacak Ürün Miktarını Giriniz: "))
sm = float(input("Sabit Maliyeti Giriniz: "))
dg = float(input("Diğer Giderleri Giriniz: "))
bdm = float(input("Birim Değişken Maliyeti Giriniz: "))


bsf = (sm+dg+(bdm*br))/br
print ("-"*35)
print ("Başabaş Noktasındaki Birim Satış Fiyatınız = ",bsf,"TL")


dfs = pd.DataFrame({'Değerler':[br,sm,dg,bdm,bsf]}, index=('Ürün Miktarı(br)',
                    'Sabit Maliyet(₺)','Diğer Giderler(₺)','Birim Değişken Maliyet(₺)',
                    'Birim Satış Fiyatı(₺)'))
print ("-"*35)
print(dfs)


fig = plt.figure()    
df = pd.DataFrame({'Etiket':['Ürün Miktarı(br)','Sabit Maliyet(₺)','Diğer Giderler(₺)',
                             'Birim Değişken Maliyet(₺)','Birim Satış Fiyatı(₺)'],
                            'Değerler':[br,sm,dg,bdm,bsf]}, index=[1,2,3,4,5])

sns.barplot(x='Etiket', y='Değerler', data=df,palette='rainbow')
fig.tight_layout()