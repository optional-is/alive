#coding:utf-8
import os
import sys
import csv
import requests
from smtplib import SMTP
import datetime

if __name__ == "__main__":
    # open the csv file with the domains to be checked as the first item on each line, blank items will be skipped
    with open('urls.csv', 'rb') as csvfile:
        creader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in creader:
            try:
                if row[0] != '':
                    # fetch the URL
                    print 'Fetching ' + row[0]
                    r = requests.get(row[0])
                    
                    # check to see the response
                    if r.status_code != 200:
                        # let us know there is a problem!
                        print '------ Problems fetching '+row[0]
                        smtp = SMTP()
                        smtp.connect('smtp.mandrillapp.com', 587)
                        smtp.login(os.environ.get('MANDRILL_USERNAME'), os.environ.get('MANDRILL_APIKEY'))
                    
                        from_addr = "Alive Checker <alive@optional.is>"
                        to_addr = [os.environ.get('TO_EMAIL')]
                    
                        subj = row[0]+" is down!"
                        date = datetime.datetime.now().strftime( "%d/%m/%Y %H:%M" )
                    		
                        message_text = """
                    		%s
                    		
                    		%s
                    		""" % ('\n'.join(row[1:]), "See https://status.heroku.com/" if 'heroku' in ''.join(row[1:]).lower() else '')
                    
                        msg = "From: %s\nTo: %s\nSubject: %s\nDate: %s\n\n%s"  % ( from_addr, ', '.join(to_addr), subj, date, message_text )
                    
                        smtp.sendmail(from_addr, to_addr, msg)
                        smtp.quit()
            except:
                pass