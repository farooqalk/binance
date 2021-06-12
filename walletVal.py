from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from time import sleep
import colorama, json
from colorama import Fore
from colorama import Style
import os, sys, re
colorama.init()

cashCurrencies= {
"USD" : "/html/body/div[4]/div/div[3]/div[2]/div[2]/button[1]",
"ARS" : "/html/body/div[4]/div/div[3]/div[2]/div[2]/button[2]",
"AED" : "/html/body/div[4]/div/div[3]/div[2]/div[2]/button[3]",
"AUD" : "/html/body/div[4]/div/div[3]/div[2]/div[2]/button[4]",
"BRL" : "/html/body/div[4]/div/div[3]/div[2]/div[2]/button[5]",
"BGN" : "/html/body/div[4]/div/div[3]/div[2]/div[2]/button[6]",
"BOB" : "/html/body/div[4]/div/div[3]/div[2]/div[2]/button[7]",
"BDT" : "/html/body/div[4]/div/div[3]/div[2]/div[2]/button[8]",
"CHF" : "/html/body/div[4]/div/div[3]/div[2]/div[2]/button[9]",
"CNY" : "/html/body/div[4]/div/div[3]/div[2]/div[2]/button[10]",
"COP" : "/html/body/div[4]/div/div[3]/div[2]/div[2]/button[11]",
"COL" : "/html/body/div[4]/div/div[3]/div[2]/div[2]/button[11]",
"CAD" : "/html/body/div[4]/div/div[3]/div[2]/div[2]/button[12]",
"CZK" : "/html/body/div[4]/div/div[3]/div[2]/div[2]/button[13]",
"DKK" : "/html/body/div[4]/div/div[3]/div[2]/div[2]/button[14]",
"EUR" : "/html/body/div[4]/div/div[3]/div[2]/div[2]/button[15]",
"EGP" : "/html/body/div[4]/div/div[3]/div[2]/div[2]/button[16]",
"GBP" : "/html/body/div[4]/div/div[3]/div[2]/div[2]/button[17]",
"HUF" : "/html/body/div[4]/div/div[3]/div[2]/div[2]/button[18]",
"HRK" : "/html/body/div[4]/div/div[3]/div[2]/div[2]/button[19]",
"HKD" : "/html/body/div[4]/div/div[3]/div[2]/div[2]/button[20]",
"INR" : "/html/body/div[4]/div/div[3]/div[2]/div[2]/button[21]",
"ILS" : "/html/body/div[4]/div/div[3]/div[2]/div[2]/button[22]",
"IDR" : "/html/body/div[4]/div/div[3]/div[2]/div[2]/button[23]",
"JPY" : "/html/body/div[4]/div/div[3]/div[2]/div[2]/button[24]",
"KES" : "/html/body/div[4]/div/div[3]/div[2]/div[2]/button[25]",
"KRW" : "/html/body/div[4]/div/div[3]/div[2]/div[2]/button[26]",
"KZT" : "/html/body/div[4]/div/div[3]/div[2]/div[2]/button[27]",
"MYR" : "/html/body/div[4]/div/div[3]/div[2]/div[2]/button[28]",
"MAD" : "/html/body/div[4]/div/div[3]/div[2]/div[2]/button[29]",
"MXN" : "/html/body/div[4]/div/div[3]/div[2]/div[2]/button[30]",
"NOK" : "/html/body/div[4]/div/div[3]/div[2]/div[2]/button[31]",
"NGN" : "/html/body/div[4]/div/div[3]/div[2]/div[2]/button[32]",
"NZD" : "/html/body/div[4]/div/div[3]/div[2]/div[2]/button[33]",
"PEN" : "/html/body/div[4]/div/div[3]/div[2]/div[2]/button[34]",
"PHP" : "/html/body/div[4]/div/div[3]/div[2]/div[2]/button[35]",
"PKR" : "/html/body/div[4]/div/div[3]/div[2]/div[2]/button[36]",
"PLN" : "/html/body/div[4]/div/div[3]/div[2]/div[2]/button[37]",
"RUB" : "/html/body/div[4]/div/div[3]/div[2]/div[2]/button[38]",
"RON" : "/html/body/div[4]/div/div[3]/div[2]/div[2]/button[39]",
"SAR" : "/html/body/div[4]/div/div[3]/div[2]/div[2]/button[40]",
"SGD" : "/html/body/div[4]/div/div[3]/div[2]/div[2]/button[41]",
"SEK" : "/html/body/div[4]/div/div[3]/div[2]/div[2]/button[42]",
"TWD" : "/html/body/div[4]/div/div[3]/div[2]/div[2]/button[43]",
"THB" : "/html/body/div[4]/div/div[3]/div[2]/div[2]/button[44]",
"TRY" : "/html/body/div[4]/div/div[3]/div[2]/div[2]/button[45]",
"UAH" : "/html/body/div[4]/div/div[3]/div[2]/div[2]/button[46]",
"UGX" : "/html/body/div[4]/div/div[3]/div[2]/div[2]/button[47]",
"VND" : "/html/body/div[4]/div/div[3]/div[2]/div[2]/button[48]",
"VES" : "/html/body/div[4]/div/div[3]/div[2]/div[2]/button[49]",
"ZAR" : "/html/body/div[4]/div/div[3]/div[2]/div[2]/button[50]"
}

coin = ""#Mandatory
compareCrypto = ""#Optional
perfCurrency = ""#Mandatory
coinAmount = ""
coinAmountFloat = 0.0
'''
https://stackoverflow.com/questions/47061662/selenium-tests-fail-against-headless-chrome

Solution 2 & 3 Combined

'''
try:#tries to set crypto coin
    arg1 = str(sys.argv[1])#Get coin as argument
    coin = arg1
    coin = re.sub("[^0-9a-zA-Z]",        # Anything except 0..9, a..z and A..Z
       "",                    # replaced with nothing
       coin) 
except:
    print(Fore.YELLOW + "No Crypto Arg!" + Style.RESET_ALL)
    while (coin == "") :
        coin = str(input('Coin Symbol: '))#Take Coin As Input



try:#Get cash currency
    arg2 = str(sys.argv[2])
    perfCurrency = arg2
    perfCurrency = re.sub("[^0-9a-zA-Z]",        # Anything except 0..9, a..z and A..Z
       "",                    # replaced with nothing
       perfCurrency).upper()
    while(not(perfCurrency.upper() in cashCurrencies)):
        print(Fore.YELLOW + "Cash Currency Not Found!" + Style.RESET_ALL)
        perfCurrency = str(input('Currency: ')).upper()#Take Coin As Input

except:
    print(Fore.YELLOW + "No Cash Currency Arg!" + Style.RESET_ALL)
    while(not(perfCurrency.upper() in cashCurrencies)):
        perfCurrency = str(input('Currency: ')).upper()#Take Coin As Input


try:
    with open((str(os.getcwd())+'\\userInfo\\wallet.json')) as f:
        data = json.load(f)

        try:#Checks if user has crypto in local wallet (\\userInfo\\wallet.json)
            coinAmount = data[(coin.upper())]
            try:
                coinAmountFloat = float(coinAmount)
                print( str("Holding ") + str(coinAmount) + str(f" {coin.upper()}"))
            except:
                print(Fore.RED + "Data Is Not a Decimal/Integer!" + Style.RESET_ALL)
                
                exit()
                exit()
                quit()
                sys.exit()

        except:
            print(Fore.RED + f"Crypto ({coin}) Not Found In Wallet" + Style.RESET_ALL)
            exit()
except:
    print(Fore.RED + "Couldn't Load Wallet. Create file in directory /userInfo/wallet.json" + Style.RESET_ALL)
    exit(0)


#TODO implement an optional feature that allows the user to specify a crypto such as BNB, USDT, BUSD OR BTC to compare to the {coin} variable
try:#Get compareCrypto
    arg3 = str(sys.argv[2])
    compareCrypto = arg3
    compareCrypto = re.sub("[^0-9a-zA-Z]",        # Anything except 0..9, a..z and A..Z
       "",                    # replaced with nothing
       compareCrypto).upper()

except:
    1==1
    '''
    print(Fore.YELLOW + "No Cash Currency Arg!" + Style.RESET_ALL)
    while(not(perfCurrency.upper() in cashCurrencies)):
        perfCurrency = str(input('Currency: ')).upper()#Take Coin As Input'''

    
coin = coin.upper()
os.system(f'title={coin}')#clears logs
print(Fore.LIGHTMAGENTA_EX + "Instantiating Connection" + Style.RESET_ALL)
chrome_options = Options()

#workingDir = os.getcwd()#Get Working directory
#os.system(f"cmd /c set PATH=%PATH%;{workingDir}")
#Edit Path: set PATH=%PATH%;%FOO%
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--allow-insecure-localhost")
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(executable_path="chromedriver.exe", options=chrome_options)
driver.maximize_window()
driver.get("https://www.binance.com/en")


print(Fore.GREEN + "Connected To Binance.com" + Style.RESET_ALL)
sleep(3)
if(not(perfCurrency == "usd")):
    try:
        driver.find_element_by_xpath('/html/body/div[1]/div/header/div[4]/div[2]/div[2]').click()#Click Currency Selector
        
    except:
        sleep(2)
        driver.find_element_by_xpath('/html/body/div[1]/div/header/div[4]/div[2]/div[2]').click()#Click Currency Selector

sleep(2)

try:
    driver.find_element_by_xpath(cashCurrencies[perfCurrency]).click()#Select Prefered Currency
    print(Fore.GREEN + f"Currency: {perfCurrency}" + Style.RESET_ALL)
except:
    sleep(2)
    driver.find_element_by_xpath(cashCurrencies[perfCurrency]).click()#Select Prefered Currency

sleep(2)

try:
    driver.get(f"https://www.binance.com/en/trade/{coin}_USDT?layout=pro&type=spot")
    print(Fore.GREEN + f"Crypto: {coin.upper()}" + Style.RESET_ALL)
except:
    print(Fore.RED + f"Crypto: {coin.upper()} Webpage Not Found" + Style.RESET_ALL)
    sleep(2)
    driver.get(f"https://www.binance.com/en/trade/{coin}_BTC?layout=pro&type=spot")

print(Fore.GREEN + "Connection Established" + Style.RESET_ALL)


sleep(2)
os.system('cls')#clears logs

retries = 0
while True:
    
    try:
        
        coinText = re.findall("\d+\.\d+", str(driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div[1]/div/div/div[1]/div/div[2]/div[2]').text))
        coinFloat = float(str(coinText[0]))
        print(str(perfCurrency) + " " + str(float(coinFloat) * (coinAmountFloat)))
    except:
        retries += 1
        print(Fore.YELLOW + f"Crypto: {coin.upper()} Not Found (Retrying {retries})" + Style.RESET_ALL)
        #print(Fore.RED + f"Crypto: {coin.upper()} Not Found" + Style.RESET_ALL)
        try:
            driver.get(f"https://www.binance.com/en/trade/{coin}_BTC?layout=pro&type=spot")
            sleep(3)
            coinText = re.findall("\d+\.\d+", str(driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div[1]/div/div/div[1]/div/div[2]/div[2]').text))
            coinFloat = float(str(coinText[0]))
            print(str(perfCurrency) + " " + str(float(coinFloat) * (coinAmountFloat)))
        except:
            retries+=1
            print(Fore.YELLOW + f"Crypto: {coin.upper()} Not Found (Retrying {retries})" + Style.RESET_ALL)
            driver.get(f"https://www.binance.com/en/trade/{coin}_BNB?layout=pro&type=spot")
            sleep(3)
            try:
                #print(f"{coin}: " + driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div[1]/div/div/div[1]/div/div[2]/div[2]').text)
                coinText = re.findall("\d+\.\d+", str(driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div[1]/div/div/div[1]/div/div[2]/div[2]').text))
                coinFloat = float(str(coinText[0]))
                print(str(perfCurrency) + " " + str(float(coinFloat) * (coinAmountFloat)))
            except:
                print(Fore.RED + f"Crypto: {coin.upper()} Not Found (Failed {retries}/{retries})" + Style.RESET_ALL)
                break
    sleep(0.5)
