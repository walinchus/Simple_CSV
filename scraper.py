import scraperwiki
import csv
data = scraperwiki.scrape('https://www.sos.state.co.us/pubs/charities/reports/2016/tables/Table2-PaidSolicitorSummary2016.csv')
reader = csv.DictReader(data.splitlines())
 
for row in reader:
     for key, value in row.iteritems():
         print key
         print value
print row['Paid Solicitor']
scraperwiki.sqlite.save(['Paid Solicitor'], row)
