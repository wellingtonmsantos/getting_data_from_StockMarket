from bs4 import BeautifulSoup
import pandas as pd
import requests
from datetime import datetime

today = str(datetime.today())
today_as_list = today[0:9]

session = requests.Session()
response = session.get("https://www.fundamentus.com.br/resultado.php",
                       headers={'User-Agent': 'Mozilla/5.0'})

soup = BeautifulSoup(response.text, "html.parser")

header = soup.find("tr")
headers = []

for i in header.find_all("th"):
    title = i.text
    headers.append(title)

table = soup.find("tbody").find_all("tr")

new_list = []
for ii in table:
    data = ii.text
    percentage_off = data.replace("%", '').replace(".", "")
    new_list.append(percentage_off.split())

df = pd.DataFrame(new_list, columns=headers)
df['date'] = today_as_list

export_csv = df.to_csv(r'C:\Users\wellm\Desktop\Projeto-Get-Stock-Data\dataset.csv', header=True, index=False)
