import pandas as pd
import matplotlib.pyplot as plt
def print_dataframe(dataframe, print_column=True, print_rows=True):
    # print column names
    if print_column:
        print(",".join([column for column in dataframe]))

    # print rows one by one
    if print_rows:
        for index, row in dataframe.iterrows():
            print(",".join([str(row[column]) for column in dataframe]))

def question_1():
    print("--------------- question_1 ---------------")
    summer = pd.read_csv('Olympics_dataset1.csv')
    winter=pd.read_csv('Olympics_dataset2.csv')
    winter=winter.iloc[:,0:6]
    total=pd.merge(summer,winter, how='left', left_on=['Team'], right_on=['Team'])
    total.columns=['Country','summer_rubbish','summer_participation','summer_gold','summer_sliver','summer_bronze','summer_total',
                   'winter_participation','winter_gold','winter_sliver','winter_bronze','winter_total']
    total.drop(index=[0,len(total)-1],axis=0,inplace=True)
    print(total.head().to_string())
    return total
    pass

def del_abr(x):
    str=''
    v=list(x)
    for i in range(len(v)):
        if v[i]=='(' or v[i]=='[':
            str=''.join(v[0:i])
            break
    str=str.strip()
    return str
def question_2(x):
    print("--------------- question_2 ---------------")
    total=x.copy()
    total['Country']=total['Country'].apply(lambda x:del_abr(x))
    total.drop(['summer_rubbish','summer_total','winter_total'],inplace=True,axis=1)
    total.set_index(["Country"],inplace=True)
    print(total.head().to_string())
    return total
    pass


def question_3(x):
    print("--------------- question_3 ---------------")
    df=x.copy()
    df.dropna(inplace=True)
    print(df.tail(10).to_string())
    return df
    pass


def question_4(x):
    print("--------------- question_4 ---------------")
    df=x
    df['summer_gold']=df['summer_gold'].apply(lambda x:x.replace(',','') if ',' in x else x)
    cou=df['summer_gold'].astype('int').max()
    cou=str(cou)
    v=df.query('summer_gold == @cou ')
    res=v.index
    for i in res:
        print(i)
    pass


def question_5(x):
    print("--------------- question_5 ---------------")
    df=x.copy()
    df['difference']=abs(df['summer_gold'].astype('int')-df['winter_gold'].astype('int'))
    cou=df['difference'].max()
    cou=str(cou)
    v=df.query('difference == @cou')
    for i in v.index:
        s=v.loc[i]['difference']
        print(f'Country:{i}     Difference:{s}')


def question_6(x1):
    print("--------------- question_6 ---------------")
    df=x1.copy()
    df['summer_gold'] = df['summer_gold'].apply(lambda x: x.replace(',', '') if ',' in x else x)
    df['summer_total'] = df['summer_gold'].astype('int') + df['summer_sliver'].astype('int') + df[
        'summer_bronze'].astype('int')
    df['winter_total'] = df['winter_gold'].astype('int') + df['winter_sliver'].astype('int') + df[
        'winter_bronze'].astype('int')
    df['Total']=df['summer_total'].astype('int')+df['winter_total'].astype('int')
    x=df.sort_values(by='Total',ascending=False)
    x.drop(['winter_total','summer_total'],inplace=True,axis=1)
    print(x.head().to_string())
    print(x.tail().to_string())
    return x
    pass


def question_7(x):
    print("--------------- question_7 ---------------")
    df=x.copy()
    df['summer_total'] = df['summer_gold'].astype('int') + df['summer_sliver'].astype('int') + df[
        'summer_bronze'].astype('int')
    df['winter_total'] = df['winter_gold'].astype('int') + df['winter_sliver'].astype('int') + df[
        'winter_bronze'].astype('int')
    dfn=df[['winter_total','summer_total']]
    dfn=dfn.head(10)
    dfn['summer_total']=dfn['summer_total'].astype('int')
    dfn['winter_total']=dfn['winter_total'].astype('int')
    f=plt.figure(figsize=(16,10))
    dfn.plot(kind='barh',stacked=True,zorder=2,ax=f.gca())
    plt.grid(axis='x',zorder=1)
    ax=f.gca()
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    plt.legend(['Winter games','Summer games'],bbox_to_anchor=(0.39, -0.1,0.2,0.2), loc=3,
               ncol=2,frameon=False)
    plt.title('Medals for Winter and Summer Games',fontsize=20)
    plt.ylabel('')

    plt.show()
    pass


def question_8(x):
    print("--------------- question_8 ---------------")
    df=x.copy()
    df=df.loc[['United States','Australia','Great Britain','Japan','New Zealand']]
    df=df.loc[:,['winter_gold','winter_sliver','winter_bronze']]
    df['winter_gold']=df['winter_gold'].astype('int')
    df['winter_sliver'] = df['winter_sliver'].astype('int')
    df['winter_bronze'] = df['winter_bronze'].astype('int')
    f=plt.figure(figsize=(16,10))
    df.plot.bar(ax=f.gca(),zorder=2)
    plt.xticks(rotation=360)
    plt.grid(axis='y', zorder=1)
    ax = f.gca()
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    plt.legend(['Gold','Sliver','Bronze'], bbox_to_anchor=(0.39, -0.1, 0.2, 0.2), loc=3,
               ncol=3, frameon=False)
    plt.xlabel('')

    plt.title('Winter Games', fontsize=20)
    pass


def question_9(x):
    print("--------------- question_9 ---------------")
    df=x.copy()
    df = df.loc[:, ['summer_gold','summer_sliver','summer_bronze','summer_participation']]
    df['summer_gold']=df['summer_gold'].astype('int')
    df['summer_sliver'] = df['summer_sliver'].astype('int')
    df['summer_bronze'] = df['summer_bronze'].astype('int')
    df['summer_participation']=df['summer_participation'].astype('int')
    df['points']=df['summer_gold']*5+df['summer_sliver']*3+df['summer_bronze']
    df['rate']=df['points']/df['summer_participation'].astype('float')
    df.fillna(0, inplace=True)
    df = df.sort_values(by='rate', ascending=False)
    name=df.head()
    name=name.loc[:,['rate']]
    print(name.to_string())

    pass
def qu_0(x):
    str=''
    if x==0 or x=='0':
        str='unknown'
    else:
        str=x
    return str
def question_10(x):
    print("--------------- question_10 ---------------")
    df=x.copy()
    con = pd.read_csv('Countries-Continents.csv')
    con.set_index(['Country'],inplace=True)
    df['summer_gold'] = df['summer_gold'].astype('int')
    df['summer_sliver'] = df['summer_sliver'].astype('int')
    df['summer_bronze'] = df['summer_bronze'].astype('int')
    df['summer_participation'] = df['summer_participation'].astype('int')
    df['winter_gold'] = df['winter_gold'].astype('int')
    df['winter_sliver'] = df['winter_sliver'].astype('int')
    df['winter_bronze'] = df['winter_bronze'].astype('int')
    df['winter_participation'] = df['winter_participation'].astype('int')
    df['summer_points'] = df['summer_gold'] * 5 + df['summer_sliver'] * 3 + df['summer_bronze']
    df['summer_rate'] = df['summer_points'] / df['summer_participation'].astype('float')
    df['winter_points'] = df['winter_gold'] * 5 + df['winter_sliver'] * 3 + df['winter_bronze']
    df['winter_rate'] = df['winter_points'] / df['winter_participation'].astype('float')
    df = pd.merge(df, con, how='left',left_index=True,right_index=True)
    df.fillna(0,inplace=True)
    df['Continent']=df['Continent'].apply(lambda x:qu_0(x))
    nu=df['Continent'].unique()
    f, ax = plt.subplots(nrows=1, ncols=1)
    colormap=['grey','red','blue','orange','green','pink','brown','purple']
    for i in range(len(nu)):
        zhi=nu[i]
        cl=colormap[i]
        x=df.query('Continent == @zhi')
        sr=x['summer_rate'].tolist()
        wr=x['winter_rate'].tolist()
        la=x.index.tolist()
        ax.scatter(x=sr,y=wr,label=zhi,color=cl)
        for i,txt in enumerate(la):
            ax.annotate(txt,(sr[i],wr[i]))
    plt.grid(zorder=1)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['top'].set_visible(False)
    plt.xlabel('Summer Rate')
    plt.ylabel('Winter Rate')
    plt.legend()
    plt.show()
    pass


if __name__ == "__main__":
    total=question_1()#remove first and last row
    total1=question_2(total)#delete the abbrivation
    total2=question_3(total1)#drop the nan rows
    question_4(total2)
    question_5(total2)
    total3=question_6(total2)# sort the values based on Total column
    question_7(total3)
    question_8(total3)
    question_9(total3)
    question_10(total3)
