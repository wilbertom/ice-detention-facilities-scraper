from pyquery import PyQuery
facilities_table = PyQuery(url="http://www.ice.gov/detention-facilities/")('#lined')('tbody')('tr')

for tr in facilities_table:
    tr = PyQuery(tr)
    f_name = tr('td')('a')[0].text
    f_state = tr('td')[1].text
    print f_name + ',' + f_state
    
