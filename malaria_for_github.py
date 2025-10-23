import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv
import sys

continents = {"Asia" : ["Bangladesh", "Benin", "China","Guinea-Bissau","India","Indonesia","Iran","Cameroon",
                        "Middle East & North Africa","Myanmar","Pakistan","Thailand","Yemen",
                        "Afghanistan","Armenia","Azerbaijan","Bahrain","Bhutan","Cambodia","Eswatini","Israel","Japan","Jordan",
                        "Kazakhstan","Kuwait","Kyrgyzstan","Laos","Lebanon","Malaysia","Mongolia","Marshall Islands","Nepal",
                        "North Korea","Brunei","Vietnam","Uzbekistan","United Arab Emirates","Turkmenistan","Timor","Thailand",
                        "Taiwan","Syria","Sri Lanka","South Korea","Singapore","Russia","Qatar","Philippines","Palestine",
                        "Oman","Iraq","Saudi Arabia","Tajikistan","Maldives"],
              "Africa" : ["Algeria","Angola","Burkina Faso","Burundi","Central African Republic","Chad","Cote d'Ivoire",
                        "Democratic Republic of Congo","Ethiopia","Gambia","Ghana","Guinea","Kenya","Liberia","Madagascar","Malawi",
                        "Mali","Mozambique","Niger","Nigeria","Rwanda","Senegal","Sierra Leone","Somalia","South Sudan","Sudan",
                        "Tanzania","Uganda","Zambia","Zimbabwe","Cape Verde","Djibouti","Egypt",
                        "Equatorial Guinea","Eritrea","Gambia","Kiribati","Lesotho","Libya","Mali","Montenegro","Morocco","Mozambique",
                        "Mauritania","Mauritius","Botswana","Uganda","Tunisia","Togo","Seychelles","Sao Tome and Principe","Congo",
                        "Namibia","Gabon","South Africa"],
              "South America" : ["Brazil","Colombia","Argentina","Bolivia","Chile","Ecuador","Guyana","Venezuela",
                                 "Uruguay","Suriname","Peru","Paraguay"],
              "Europe" : ["Albania","Andorra","Austria","Belarus","Belgium","Cyprus","Croatia","Czechia","Denmark","England","Estonia",
                          "Finland","France","Georgia","Germany","Greece","Greenland","Hungary","Iceland","Ireland","Italy",
                          "Lithuania","Luxembourg","Latvia","Moldova","Malta","Monaco","Netherlands","North Macedonia",
                          "Northern Ireland","Norway","Bosnia and Herzegovina","Wales","Ukraine","Turkey","Switzerland","Sweden", 
                          "Spain","Slovenia","Slovakia","Serbia","Scotland","San Marino","Romania","Portugal","Poland","Bulgaria",
                          "United Kingdom"],
              "Oceania" : ["Australia","Fiji","Micronesia","Nauru","New Zealand","Vanuatu","Tuvalu","Tonga","Tokelau",
                           "Solomon Islands","Samoa","Palau","Niue","Papua New Guinea","Cook Islands"],
              "North America" : ["United States Virgin Islands","Bahamas","Barbados","Bermuda","Canada","Puerto Rico","Mexico",
                                 "Northern Mariana Islands","American Samoa","Guam","United States","Haiti","Dominican Republic",
                                 "Saint Vincent and the Grenadines","Saint Kitts and Nevis","Saint Lucia","Grenada"],
              "Central America" : ["Belize","Costa Rica","Dominica","El Salvador","Guatemala","Honduras","Nicaragua",
                                   "Trinidad and Tobago","Cuba","Panama","Jamaica","Antigua and Barbuda"]}

def get_continent(country):
    global continents
    if country in continents["Asia"]:
        return "Asia"
    elif country in continents["Africa"]:
        return "Africa"
    elif country in continents["South America"]:
        return "South America"
    elif country in continents["North America"]:
        return "North America"
    elif country in continents["Central America"]:
        return "Central America"
    elif country in continents["Europe"]:
        return "Europe"
    elif country in continents["Oceania"]:
        return "Oceania"

df = pd.read_csv(r"C:\Users\kgasv\OneDrive\Documentos\Python files\global-malaria.csv")
print(">>>>> HEAD <<<<<")
print(df.head())
#print(df[df["1990"].isnull()])
#print(df[df["1991"].isnull()])
#print(df[df["1992"].isnull()])
#print(df[df["1993"].isnull()])
#print(df[df["1994"].isnull()])
#print(df[df["1995"].isnull()])
#print(df[df["1996"].isnull()])
#print(df[df["1997"].isnull()])
#print(df[df["1998"].isnull()])
#print(df[df["1999"].isnull()])
#print(df[df["2000"].isnull()])
#print(df[df["2001"].isnull()])
#print(df[df["2002"].isnull()])
#print(df[df["2003"].isnull()])
#print(df[df["2004"].isnull()])
#print(df[df["2005"].isnull()])
#print(df[df["2006"].isnull()])
#print(df[df["2007"].isnull()])
#print(df[df["2008"].isnull()])
#print(df[df["2009"].isnull()])
#print(df[df["2010"].isnull()])
#print(df[df["2011"].isnull()])
#print(df[df["2012"].isnull()])
#print(df[df["2013"].isnull()])
#print(df[df["2014"].isnull()])
#print(df[df["2015"].isnull()])
#print(df[df["2016"].isnull()])
#print(df[df["2017"].isnull()])
#print(df[df["2018"].isnull()])
#print(df[df["2019"].isnull()])
#todo I found no null values anywhere in the dataset

df["Continent"] = df["Region"].apply(get_continent)
print(df[df["Continent"].notnull()][["Region","Continent"]])

print(">>>>> SHAPE <<<<<")
print(df.shape)
print(">>>>> ONLY COUNTRIES <<<<<")
print(df.dropna().shape)
# todo the original dataset includes regions that are not countries, but collections of them; for my analysis, I only want countries

# Identify the fields which are not countries and label them as such
print(df[df["Continent"].isnull()])
df["Continent"] = df["Continent"].fillna("Not a Country")

# Create another dataframe with only regions that correspond to countries, excluding rows with values like 'World', 'North America'
df_countries = df[~df["Continent"].isin(["Not a Country"])]

# Shorten long names for better readability in the terminal
df_countries = df_countries.replace("Democratic Republic of Congo", "DRC")
df_countries = df_countries.replace("Saint Vincent and the Grenadines","SVG")
df_countries = df_countries.replace("Saint Kitts and Nevis","SKN")
print(df_countries.shape)

print(">>>>>Average cases per continent per year<<<<<")
avg_continent = df_countries.groupby(['Continent'])[['1990','1991','1992','1993','1994','1995','1996','1997','1998','1999',
                                                     '2000','2001','2002','2003','2004','2005','2006','2007','2008','2009',
                                                     '2010','2011','2012','2013','2014','2015','2016','2017','2018','2019']].mean()
print(avg_continent)

print(">>>>>Averages across all years per continent<<<<<")
print(avg_continent.mean(axis=1))

# Top 10 countries from 1990 to 1995
print("1990---------------------------")
print(df_countries.nlargest(10,"1990")[["Region","1990","Continent"]])
print("1991---------------------------")
print(df_countries.nlargest(10,"1991")[["Region","1991","Continent"]])
print("1992---------------------------")
print(df_countries.nlargest(10,"1992")[["Region","1992","Continent"]])
print("1993---------------------------")
print(df_countries.nlargest(10,"1993")[["Region","1993","Continent"]])
print("1994---------------------------")
print(df_countries.nlargest(10,"1994")[["Region","1994","Continent"]])
print("1995---------------------------")
print(df_countries.nlargest(10,"1995")[["Region","1995","Continent"]])

# Find the top 10 values per year in 5-year intervals
print("================================")
print("TOP 10 COUNTRIES WITH THE MOST CASES OF MALARIA PER CONTINENT PER YEAR")
dicc_top10_continents = {
        "Rank":[1,2,3,4,5,6,7,8,9,10],
        "1990":df_countries.nlargest(10,"1990")["Continent"].reset_index(drop=True),
        "1995":df_countries.nlargest(10,"1995")["Continent"].reset_index(drop=True),
        "2000":df_countries.nlargest(10,"2000")["Continent"].reset_index(drop=True),
        "2005":df_countries.nlargest(10,"2005")["Continent"].reset_index(drop=True),
        "2010":df_countries.nlargest(10,"2010")["Continent"].reset_index(drop=True),
        "2015":df_countries.nlargest(10,"2015")["Continent"].reset_index(drop=True),
        "2019":df_countries.nlargest(10,"2019")["Continent"].reset_index(drop=True)
}
df_top10_continents = pd.DataFrame(dicc_top10_continents)
print(df_top10_continents)
#todo It is overwhelmingly African countries which occupy the top 10 positions in the selected years
print("================================")
print("TOP 10 COUNTRIES WITH THE MOST CASES OF MALARIA PER YEAR")
dicc_top10_countries = {
        "Rank":[1,2,3,4,5,6,7,8,9,10],
        "1990":df_countries.nlargest(10,"1990")["Region"].reset_index(drop=True),
        "1995":df_countries.nlargest(10,"1995")["Region"].reset_index(drop=True),
        "2000":df_countries.nlargest(10,"2000")["Region"].reset_index(drop=True),
        "2005":df_countries.nlargest(10,"2005")["Region"].reset_index(drop=True),
        "2010":df_countries.nlargest(10,"2010")["Region"].reset_index(drop=True),
        "2015":df_countries.nlargest(10,"2015")["Region"].reset_index(drop=True),
        "2019":df_countries.nlargest(10,"2019")["Region"].reset_index(drop=True)
}
df_top10_countries = pd.DataFrame(dicc_top10_countries)
print(df_top10_countries)

print("================================")
print("TOP 10 COUNTRIES WITH THE LEAST CASES OF MALARIA PER YEAR")
dicc_low10_countries = {
        "Rank":[1,2,3,4,5,6,7,8,9,10],
        "1990":df_countries.nsmallest(10,"1990")["Region"].reset_index(drop=True),
        "1995":df_countries.nsmallest(10,"1995")["Region"].reset_index(drop=True),
        "2000":df_countries.nsmallest(10,"2000")["Region"].reset_index(drop=True),
        "2005":df_countries.nsmallest(10,"2005")["Region"].reset_index(drop=True),
        "2010":df_countries.nsmallest(10,"2010")["Region"].reset_index(drop=True),
        "2015":df_countries.nsmallest(10,"2015")["Region"].reset_index(drop=True),
        "2019":df_countries.nsmallest(10,"2019")["Region"].reset_index(drop=True)
}
df_low10_countries = pd.DataFrame(dicc_low10_countries)
print(df_low10_countries)

print("\n\n\n>>>>>>>>>>SOUTH AMERICA<<<<<<<<<<\n\n")
print("================================")
print("TOP 5 COUNTRIES WITH THE LEAST CASES OF MALARIA IN SOUTH AMERICA")
dicc_low5_southamerica = {
    "Rank":[1,2,3,4,5],
    "1990":df_countries[df_countries["Continent"] == "South America"].nsmallest(5,"1990")["Region"].reset_index(drop=True),
    "1995":df_countries[df_countries["Continent"] == "South America"].nsmallest(5,"1995")["Region"].reset_index(drop=True),
    "2000":df_countries[df_countries["Continent"] == "South America"].nsmallest(5,"2000")["Region"].reset_index(drop=True),
    "2005":df_countries[df_countries["Continent"] == "South America"].nsmallest(5,"2005")["Region"].reset_index(drop=True),
    "2010":df_countries[df_countries["Continent"] == "South America"].nsmallest(5,"2010")["Region"].reset_index(drop=True),
    "2015":df_countries[df_countries["Continent"] == "South America"].nsmallest(5,"2015")["Region"].reset_index(drop=True),
    "2019":df_countries[df_countries["Continent"] == "South America"].nsmallest(5,"2019")["Region"].reset_index(drop=True)
}
df_low5_southamerica = pd.DataFrame(dicc_low5_southamerica)
print(df_low5_southamerica)
print("================================")
print("TOP 5 COUNTRIES WITH THE MOST CASES OF MALARIA IN SOUTH AMERICA")
dicc_top5_southamerica = {
    "Rank":[1,2,3,4,5],
    "1990":df_countries[df_countries["Continent"] == "South America"].nlargest(5,"1990")["Region"].reset_index(drop=True),
    "1995":df_countries[df_countries["Continent"] == "South America"].nlargest(5,"1995")["Region"].reset_index(drop=True),
    "2000":df_countries[df_countries["Continent"] == "South America"].nlargest(5,"2000")["Region"].reset_index(drop=True),
    "2005":df_countries[df_countries["Continent"] == "South America"].nlargest(5,"2005")["Region"].reset_index(drop=True),
    "2010":df_countries[df_countries["Continent"] == "South America"].nlargest(5,"2010")["Region"].reset_index(drop=True),
    "2015":df_countries[df_countries["Continent"] == "South America"].nlargest(5,"2015")["Region"].reset_index(drop=True),
    "2019":df_countries[df_countries["Continent"] == "South America"].nlargest(5,"2019")["Region"].reset_index(drop=True)
}
df_top5_southamerica = pd.DataFrame(dicc_top5_southamerica)
print(df_top5_southamerica)

print("\n\n>>>>>2000-2010<<<<<\n")
print("================================")
print("RANKING OF COUNTRIES FOR MALARIA CASES IN SOUTH AMERICA FROM 2000 TO 2010")
dicc_southamerica = {
    "2000":df_countries[df_countries["Continent"] == "South America"].sort_values(by="2000",ascending=False)["Region"].reset_index(drop=True),
    "2001":df_countries[df_countries["Continent"] == "South America"].sort_values(by="2001",ascending=False)["Region"].reset_index(drop=True),
    "2002":df_countries[df_countries["Continent"] == "South America"].sort_values(by="2002",ascending=False)["Region"].reset_index(drop=True),
    "2003":df_countries[df_countries["Continent"] == "South America"].sort_values(by="2003",ascending=False)["Region"].reset_index(drop=True),
    "2004":df_countries[df_countries["Continent"] == "South America"].sort_values(by="2004",ascending=False)["Region"].reset_index(drop=True),
    "2005":df_countries[df_countries["Continent"] == "South America"].sort_values(by="2005",ascending=False)["Region"].reset_index(drop=True),
    "2006":df_countries[df_countries["Continent"] == "South America"].sort_values(by="2006",ascending=False)["Region"].reset_index(drop=True),
    "2007":df_countries[df_countries["Continent"] == "South America"].sort_values(by="2007",ascending=False)["Region"].reset_index(drop=True),
    "2008":df_countries[df_countries["Continent"] == "South America"].sort_values(by="2008",ascending=False)["Region"].reset_index(drop=True),
    "2009":df_countries[df_countries["Continent"] == "South America"].sort_values(by="2009",ascending=False)["Region"].reset_index(drop=True),
    "2010":df_countries[df_countries["Continent"] == "South America"].sort_values(by="2010",ascending=False)["Region"].reset_index(drop=True)
}
df_southamerica = pd.DataFrame(dicc_southamerica)
print(df_southamerica)

print("================================")
print("RISK CATEGORIES: COUNTRIES FOR MALARIA CASES IN SOUTH AMERICA FROM 2000 TO 2010")
southamerica_malaria_risk = {
    "Argentina":"Low",
    "Bolivia":"High",
    "Brazil":"High",
    "Chile":"Min",
    "Colombia":"High",
    "Ecuador":"High",
    "Guyana":"Max",
    "Paraguay":"Min", #? declared malaria-free by the WHO in 2018
    "Peru":"High",
    "Suriname":"Moderate",
    "Uruguay":"Min",
    "Venezuela":"Max"
}
def country_risk(country):
    global southamerica_malaria_risk
    try:
        lvl_risk = southamerica_malaria_risk[country]
    except:
        lvl_risk = "NULL" 
    return lvl_risk

dicc_southamerica_risk = {
    "2000":df_southamerica["2000"].apply(country_risk),
    "2001":df_southamerica["2001"].apply(country_risk),
    "2002":df_southamerica["2002"].apply(country_risk),
    "2003":df_southamerica["2003"].apply(country_risk),
    "2004":df_southamerica["2004"].apply(country_risk),
    "2005":df_southamerica["2005"].apply(country_risk),
    "2006":df_southamerica["2006"].apply(country_risk),
    "2007":df_southamerica["2007"].apply(country_risk),
    "2008":df_southamerica["2008"].apply(country_risk),
    "2009":df_southamerica["2009"].apply(country_risk),
    "2010":df_southamerica["2010"].apply(country_risk)
}
df_southamerica_risk = pd.DataFrame(dicc_southamerica_risk)
print(df_southamerica_risk)

'''
There is a missmatch between countries with maximum malaria-risk such as Venezuela and Guyana, which NEVER occupy the top 2 possitions and only start dominating
the top 5 after 2005

Brazil and Colombia have historically had stronger public health programs, with substantial vector control, surveillance, and reporting infrastructure.
Venezuela, in contrast, experienced inconsistent investment in its health system, especially after the early 2000s.

Brazil and Colombia both have robust national disease surveillance networks that cooperate with PAHO and WHO.
Venezuela's data reporting became increasingly irregular after the mid-2000s — partly due to political centralization and resource shortages.
Venezuela, in the early years of Chavez, had the Misión Barrio Adentro, but this focused on urban and primary care, not vector-borne disease control 
in RURAL regions.
In 2006, economic shifts and CENTRALIZATION of public health governance caused malaria control programs to decline (shortages of insecticides, DIAGNOSTIC 
kits, and trained personnel)

Even if malaria risk was high, stronger control programs in Brazil and Colombia might have resulted in better containment 
but HIGHER REPORTING, while weaker systems in Venezuela might have meant UNDERREPORTING or delayed detection.

Ecuador launched a comprehensive malaria control strategy supported by the Global Fund and the Pan American Health Organization (PAHO).
Focus shifted to community-based vector control, insecticide-treated bed nets (ITNs), and rapid DIAGNOSTIC testing.
Indoor residual spraying campaigns were expanded, especially in the Amazon.

Health system STRENGTHENING under Rafael Correa (post-2006)
The Constitution of 2008 recognized healthcare as a universal right.
The government massively increased public health spending, especially in preventive and rural healthcare.
The MINISTRY of PUBLIC HEALTH integrated malaria surveillance into primary healthcare networks, improving early DETECTION and reporting.
Health decentralization allowed provincial and local health authorities to act faster in outbreak RESPONSE.
'''

#Top 5 countries with most malaria cases per continent from 1995 to 2015 in 2-year intervals
print("================================")
print("AFRICA")
df_top10_2010_Africa = df_countries[df_countries["Continent"] == "Africa"].nlargest(5,"2010")[["Region","2010"]]
print(df_top10_2010_Africa)
print("================================")
print("ASIA")
df_top10_2010_Asia = df_countries[df_countries["Continent"] == "Asia"].nlargest(5,"2010")[["Region","2010"]]
print(df_top10_2010_Asia)
print("================================")
print("EUROPE")
df_top10_2010_Europe = df_countries[df_countries["Continent"] == "Europe"].nlargest(5,"2010")[["Region","2010"]]
print(df_top10_2010_Europe)
print("================================")
print("SOUTH AMERICA")
df_top10_2010_SouthAmerica = df_countries[df_countries["Continent"] == "South America"].nlargest(5,"2010")[["Region","2010"]]
print(df_top10_2010_SouthAmerica)
print("================================")
print("NORTH AMERICA")
df_top10_2010_NorthAmerica = df_countries[df_countries["Continent"] == "North America"].nlargest(5,"2010")[["Region","2010"]]
print(df_top10_2010_NorthAmerica)
print("================================")
print("CENTRAL AMERICA")
df_top10_2010_CentralAmerica = df_countries[df_countries["Continent"] == "Central America"].nlargest(5,"2010")[["Region","2010"]]
print(df_top10_2010_CentralAmerica)
print("================================")
print("OCEANIA")
df_top10_2010_Oceania = df_countries[df_countries["Continent"] == "Oceania"].nlargest(5,"2010")[["Region","2010"]]
print(df_top10_2010_Oceania)



years = ["2000", "2003", "2006", "2009", "2012", "2015"] #? list of years for the following aggregates
#Total cases per continent in 2010
print("================================")
print(">>>>>>>>>> SUM OF CASES <<<<<<<<<<")
sum_cases = df_countries.groupby("Continent")[years].sum().reset_index()
print(sum_cases)
#Average cases per continent in 2010
print("================================")
print(">>>>>>>>>> AVERAGE CASES <<<<<<<<<<")
df_mean = df_countries.groupby("Continent")[years].mean().reset_index()
print(df_mean)
#DataFrames of average cases per continent 2000 - 2015 in 3-year intervals
df_mean = df_mean.rename(columns={year: f"{year}_Mean" for year in years})

#? Start matplotlib
df_plot = df_mean.melt(id_vars="Continent", 
                       var_name="Year", 
                       value_name="Mean_Cases")

df_plot["Year"] = df_plot["Year"].str.replace("_Mean", "").astype(int)

plt.figure(figsize=(10,6))

for continent in df_plot["Continent"].unique():
    subset = df_plot[df_plot["Continent"] == continent]
    plt.plot(subset["Year"], subset["Mean_Cases"], marker="o", label=continent)

plt.title("Average Malaria Cases by Continent (2000-2015)")
plt.xlabel("Year")
plt.ylabel("Average Number of Cases")
plt.legend(title="Continent")
plt.grid(True)
plt.tight_layout()
plt.show()

# What was the year with the most cases?
all_years = []
for i in range(2020-1990):
    num = 1990+i
    all_years.append(str(num))

max_cases_year = {"Year":[],"Cases":[],"Country":[]}
df_max_cases_year = pd.DataFrame(max_cases_year)
for num in all_years:
    cases = df_countries[df_countries[num] == df_countries[num].max()][["Region",num]]
    cases_country = cases["Region"].values[0]
    cases_num = cases[num].values[0]
    temp_df = pd.DataFrame({"Year":[num],"Cases":[cases_num],"Country":[cases_country]})
    df_max_cases_year = pd.concat([df_max_cases_year,temp_df])

print(">>>>>>>>>> YEAR WITH THE MOST CASES <<<<<<<<<<")
print(df_max_cases_year[df_max_cases_year["Cases"] == df_max_cases_year["Cases"].max()])
# todo The year with the most cases was 2008, with 280604 cases of malaria in Nigeria

# What position does Bangladesh occupy throughout the years?
print(">>>>> WORLD RANKING OF BANGLADESH THROUGHOUT THE YEARS <<<<<")
df_Bangladesh = pd.DataFrame({"Year":[],"Position":[]})
for year in all_years:
    df_ordered = df_countries.sort_values(year, ascending=False).reset_index()
    position = df_ordered[df_ordered["Region"] == "Bangladesh"].index.values[0]
    df_temp = pd.DataFrame({"Year":[year],"Position":[int(position)+1]})
    df_Bangladesh = pd.concat([df_Bangladesh,df_temp])
print(df_Bangladesh)

print(">>>>> CASES OF MALARIA IN BANGLADESH <<<<<")
print(df_countries[df_countries["Region"] == "Bangladesh"][["Region","1990","2000","2010","2019"]])

# todo This shows me the rank of Bangladesh worldwide per year. I can create a bar chart with it, showing the evolution of
# todo its position. 
'''
Bangladesh dropped from position 5 worldwide to position 52. What could have caused this massive improvement in the fight against
malaria? In 1990, Bangladesh had 36419 cases of malaria, and in 2019 only 110. According to the WHO, it is a High Risk country
(>100), but undeniably its improvement has been immense.


Healthcare System
Expanded primary care: The government built thousands of community clinics and health centers across rural areas (especially 
from the late 1990s).
Trained health workers: The deployment of Community Health Care Providers (CHCPs) and Health Assistants ensured that malaria 
diagnosis and treatment reached even remote villages.
Improved access to diagnostics and treatment: Widespread distribution of Rapid Diagnostic Tests (RDTs) and artemisinin-based 
combination therapies (ACTs) after 2005 significantly reduced transmission.

Result: Earlier detection and faster treatment = fewer severe cases = fewer total infections.


Malaria Control Programmes
1998: Launch of the National Malaria Control Programme (NMCP) under the Ministry of Health.
2007: Bangladesh joined the Global Fund to Fight AIDS, Tuberculosis, and Malaria (GFATM) — this was pivotal. The funding 
supported:
Free insecticide-treated bed nets (ITNs and LLINs).
Indoor residual spraying in endemic districts.
Data-driven surveillance systems.

By 2019, the Global Fund and WHO reported a 90% drop in malaria cases compared to 2000.


Political continuity and partnerships
Successive Bangladeshi governments — regardless of political party — maintained malaria eradication as a priority in national 
health strategies.
Unlike in some countries, malaria programs didn't collapse during government transitions.
Partnerships with NGOs (like BRAC, one of the largest in the world) played a huge role in implementing prevention and education 
campaigns.

This combination of political commitment + NGO collaboration created consistent policy follow-through — something relatively 
rare in developing nations.


Socioeconomic progress
Rising incomes, better housing, and rural electrification reduced exposure to mosquitoes.
Mobile technology allowed better health communication and monitoring.
Migration patterns changed — fewer people working deep in forested, high-risk areas thanks to economic diversification.


Regional cooperation
Bangladesh worked with India and Myanmar under the WHO South-East Asia Regional Office (SEARO) initiative to coordinate 
cross-border malaria control.
This reduced reinfection in border zones — historically a major challenge.


Public Policy
The Health and Population Sector Programme (1998-2003) and subsequent Health, Nutrition and Population Sector Programme (HNPSP, 
2003-2011) were government-led reforms that expanded healthcare coverage.
Politicians like health ministers and local MPs often backed public health funding and infrastructure in rural constituencies.
The government's Vision 2021 (adopted in 2009) explicitly aimed for a malaria-free Bangladesh by 2030, shaping budgets and donor 
negotiations.
'''


print(">>>>> RANKING OF BANGLADESH THROUGHOUT THE YEARS AMONG ASIAN COUNTRIES <<<<<")
df_Bangladesh_in_Asia = pd.DataFrame({"Year":[],"Position":[]})
for year in all_years:
    df_ordered = df_countries[df_countries["Continent"] == "Asia"].sort_values(year, ascending=False).reset_index()
    position = df_ordered[df_ordered["Region"] == "Bangladesh"].index.values[0]
    df_temp = pd.DataFrame({"Year":[year],"Position":[int(position)+1]})
    df_Bangladesh_in_Asia = pd.concat([df_Bangladesh_in_Asia,df_temp])

print(df_Bangladesh_in_Asia)

# todo Bangladesh passed from position 5 in 1990 to position 52 in 2019, showing a massive improvement in malaria prevention

df_countries.to_csv('malaria_countries.csv')
df_mean.to_csv('malaria_continent_averages.csv')
sum_cases.to_csv('malaria_sum_cases.csv')
df_Bangladesh_in_Asia.to_csv('malaria_bangladesh_position_asia.csv')
df_Bangladesh.to_csv('malaria_bangladesh_position.csv')