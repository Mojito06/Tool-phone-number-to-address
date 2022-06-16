import requests
import sys
import json
import time
import os

phonenb = sys.argv[1]

black="\033[0;30m"
red="\033[0;31m"
green="\033[0;32m"
bgreen="\033[1;32m"
yellow="\033[0;33m"
blue="\033[0;34m"
purple="\033[0;35m"
cyan="\033[0;36m"
bcyan="\033[1;36m"
white="\033[0;37m"
nc="\033[00m"

version="1.6"

ask = green + '[' + white + '?' + green + '] '+ yellow
success = yellow + '[' + white + '√' + yellow + '] '+green
error = blue + '[' + white + '!' + blue + '] '+red
info= yellow + '[' + white + '+' + yellow + '] '+ cyan
info2= green + '[' + white + '•' + green + '] '+ purple

logo=f'''
{red}  _____       __   _
{cyan} |  __ \     |  \ | |                _                   | |
{yellow} | |__) |   _|   \| |__   __ __  __ | |_   _____ _ __
{blue} |  ___/ | | | |\ \ |  | |  |  \/  \| '_ \|  __/| /__|
{red} | |   | |_| | | \  |  |_|  | |  |  | |_| |  _| | |
{yellow} |_|    \__, |_|  \_|\_____/|_|__|__|____ |____\|_|
{green}         __/ |                          {cyan}[v1.0]
{cyan}        |___/                   {red}[By Frnk & Mojito]
'''

def slowprint(n):
    for word in n + '\n':
        sys.stdout.write(word)
        sys.stdout.flush()
        time.sleep(0.0000000000000000000000000000001)

slowprint(logo)

url = 'https://www.ovhtelecom.fr/engine/api/connectivity/eligibility/search/buildingsByLine'
myobj = {'lineNumber': phonenb,'status':'active'}

phonenb = sys.argv[1]
x = requests.post(url, data = myobj)
#print(x.text)

y = requests.get('https://api.sfr.fr/service-eligibility/api/rest/v1/eligibilityByNDI?ndi='+phonenb+'&byMap=false&lineType=ACTIVE_INACTIVE_IF_NONE')


p = json.loads(y.text)

try:
    print("recherche effectué sur "+phonenb[0]+phonenb[1]+'.'+phonenb[2]+phonenb[3]+'.'+phonenb[4]+phonenb[5]+'.'+phonenb[6]+phonenb[7]+'.'+phonenb[8]+phonenb[9]+"\n")
    print("Numéro trouvé \n \n ID : " + str(p['id']) + "\n Data-ID : "+str(p['data']['id']+"\n"))
    print(" Adresse : "+ str(p['data']['eligibilityLookup']['installationAddresses'][0]['installationCBL']['technicalAddress']['streetNumber'] + ' '+ str(p['data']['eligibilityLookup']['installationAddresses'][0]['installationCBL']['technicalAddress']['streetName'])))
    print(" Ville : "+ str(p['data']['eligibilityLookup']['installationAddresses'][0]['installationCBL']['technicalAddress']['zipCodesAndCities'][0]['cities'][0]))
    print(" ZipCode : "+ str(p['data']['eligibilityLookup']['installationAddresses'][0]['installationCBL']['technicalAddress']['zipCodesAndCities'][0]['zipCode'])+"\n")
    print(" Propriétaire : "+ str(p['data']['eligibilityLookup']['installationAddresses'][0]['installationDSL']['adslLines'][0]['adslComplement']['holder']))
except:
    try:
        print("recherche effectué sur "+phonenb[0]+phonenb[1]+'.'+phonenb[2]+phonenb[3]+'.'+phonenb[4]+phonenb[5]+'.'+phonenb[6]+phonenb[7]+'.'+phonenb[8]+phonenb[9]+"\n")
        print("Numéro trouvé \n \n ID : " + str(p['id']) + "\n Data-ID : "+str(p['data']['id']+"\n"))
        print(" Adresse : "+ str(p['data']['eligibilityLookup']['installationAddresses'][0]['installationDSL']['technicalAddress']['streetNumber'] + ' '+ str(p['data']['eligibilityLookup']['installationAddresses'][0]['installationCBL']['technicalAddress']['streetName'])))
        print(" Ville : "+ str(p['data']['eligibilityLookup']['installationAddresses'][0]['installationDSL']['technicalAddress']['zipCodesAndCities'][0]['cities'][0]))
        print(" ZipCode : "+ str(p['data']['eligibilityLookup']['installationAddresses'][0]['installationDSL']['technicalAddress']['zipCodesAndCities'][0]['zipCode'])+"\n")
        print(" Propriétaire : "+ str(p['data']['eligibilityLookup']['installationAddresses'][0]['installationDSL']['adslLines'][0]['adslComplement']['holder']))
    except:
        try:
            print("recherche effectué sur "+phonenb[0]+phonenb[1]+'.'+phonenb[2]+phonenb[3]+'.'+phonenb[4]+phonenb[5]+'.'+phonenb[6]+phonenb[7]+'.'+phonenb[8]+phonenb[9]+"\n")
            print("Numéro trouvé \n \n ID : " + str(p['id']) + "\n Data-ID : "+str(p['data']['id']+"\n"))
            print(" Adresse : "+ str(p['data']['eligibilityLookup']['installationAddresses'][0]['installationTHD']['technicalAddress']['streetNumber'] + ' '+ str(p['data']['eligibilityLookup']['installationAddresses'][0]['installationCBL']['technicalAddress']['streetName'])))
            print(" Ville : "+ str(p['data']['eligibilityLookup']['installationAddresses'][0]['installationTHD']['technicalAddress']['zipCodesAndCities'][0]['cities'][0]))
            print(" ZipCode : "+ str(p['data']['eligibilityLookup']['installationAddresses'][0]['installationTHD']['technicalAddress']['zipCode'])+"\n")
            print(" Propriétaire : "+ str(p['data']['eligibilityLookup']['installationAddresses'][0]['installationDSL']['adslLines'][0]['adslComplement']['holder']))
        except:
            pass
os.system('explorer "http://www.google.com/maps/search/'+str(p['data']['eligibilityLookup']['installationAddresses'][0]['installationCBL']['technicalAddress']['streetNumber']) + ' '+ str(p['data']['eligibilityLookup']['installationAddresses'][0]['installationCBL']['technicalAddress']['streetName']))
#print(json.dumps(parsed, indent=4, sort_keys=True))
#print(y.text)
