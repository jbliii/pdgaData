#scrape tournament pages at pdga.com

from bs4 import BeautifulSoup
import requests

f = open('pdga_tournaments.csv','w')
f.write('Date,Year,Name,href,Class,Tier,Location' + '\n')

print('Getting data...')

for y in range(1985,2017):
    for m in range(1,13):
            url = "http://www.pdga.com/tour/events/" + str(y) + '/' + str(m)
            page = requests.get(url)
            print(str(m)+'/'+str(y))

            soup = BeautifulSoup(page.text, 'html.parser')

            tables = soup.findAll('table', class_="views-table cols-6")
            for table in tables:
                tournaments = table.findAll('tr')[1:]

                for t in tournaments:
                    t_date = t.find('td', class_="views-field views-field-DateRange").text.replace(',','').replace('\n','')
                    t_name = t.find('td', class_="views-field views-field-OfficialName").a.text.replace(',','')
                    t_href = t.find('td', class_="views-field views-field-OfficialName").a['href'].replace('\n','')
                    t_class = t.find('td', class_="views-field views-field-Classification").text.replace(',','').replace('\n','')
                    t_tier = t.find('td', class_="views-field views-field-Tier").text.replace(',','').replace('\n','')
                    t_location = t.find('td', class_="views-field views-field-Location").text.replace(',','').replace('\n','')
                    f.write(t_date + ',' + str(y) + ',' + t_name + ',' + t_href + ',' + t_class + ',' + t_tier + ',' + t_location + '\n')

f.close()
