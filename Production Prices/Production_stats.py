import pandas as pd

df = pd.read_csv('crop_production.csv')
df = df.dropna()
crop = 'Wheat'

Quest = ['Wheat',]
data = pd.DataFrame(columns=['Year','Production'])


for x in range(2000,2015):
    crop_year = x
    data_yearly = df[(df["Crop_Year"]) == crop_year]
    data_crop = data_yearly[(data_yearly["Crop"]) == crop]
    crop_production = data_crop[['Crop_Year','Production']]
    crop_mean = crop_production['Production'].mean()

    
    data.loc[x] = crop_year, crop_mean
    
    #data.append({'crop_year':crop_year,'crop_mean':crop_mean},ignore_index=True)
    #result = pd.DataFrame(crop_mean)
    #print(crop_production.head(10))
    #result.to_csv('arhar.csv')    
    #data_production.to_csv('arhar.csv', header=False, index=False)
    
    data.to_csv("{}.csv".format(crop),header=True, index=False)
    
print(data)   
