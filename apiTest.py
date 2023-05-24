import requests
import pandas as pd

dataDict = {}
response = requests.get("https://datausa.io/api/data?drilldowns=Nation&measures=Population")
jresponse = response.json()
if response.status_code == 200:
    dataInfo = jresponse["data"]
    sourceInfo = jresponse["source"][0]["annotations"]["source_name"]

    df = pd.DataFrame(dataInfo,
                      columns=['ID Nation', 'Nation', 'ID Year', 'Year', 'Population', 'Slug Nation', 'YoY Growth%'])
    # Calculate the Year-on-Year population growth
    df_sorted = df.sort_values('ID Year', ascending=True)
    df_sorted['YoY Growth%'] = (df_sorted.select_dtypes(include=['int', 'float']).pct_change()['Population'])

    # Finding the peak growth percentage year and calculating the time duration
    peakGrowth = df_sorted.loc[df_sorted['YoY Growth%'].idxmax()]
    start_year = df_sorted['ID Year'].min()
    end_year = df_sorted['ID Year'].max()
    years = end_year - start_year

    # Finding the lowest growth percentage year
    lowestGrowth = df_sorted.loc[df_sorted['YoY Growth%'].idxmin()]

    print("According to", sourceInfo + ", in " + str(years) + " years from " + str(start_year) + " to " + str(
        end_year) + ", peak population growth was {:.2%}".format(peakGrowth['YoY Growth%']), "in " + peakGrowth['Year'],
          "and the lowest population increase was {:.2%}".format(lowestGrowth['YoY Growth%']), "in",
          lowestGrowth['Year'])
