import math
name = input("what is your name(password): ")
if name.upper() != "KENT":
    print("you are not eligble(get out of here)")
while name.upper() == "KENT":
    print("in this calcualter you can calculate ROE ,PER ,ROI ,ROIC ,PB ratio, and ROA (in this order enter the values )")
    ask_recomendation = input("do you want a recomendation(yes or no):")
    def ROE_calculate():
        Annual_net_income = input("annual net income: ")
        equity_of_shareholder = input("sharesholeder's(you) equity: ")
        ROE = int(Annual_net_income) / int(equity_of_shareholder)
        print("ROE = ")
        print(ROE)

    #calculation for PER

    def PER_calculate():
        current_price = input("currrent stock price: ")
        annual_profit = input("annual profit; ")
        PER = int(current_price) / int(annual_profit)
        print("PER = ")
        print(PER)

    #calculation of ROI
    
    def ROI_calculate():
        cost_of_investment = input("cost of investment: ")
        Profit = input("profit: ")
        ROI = (int(Profit) - int(cost_of_investment)) / int(cost_of_investment)
        print("ROI = ")
        print(ROI)

    #calculation of ROIC

    def ROIC_calculate():
        totl_invstd_cap = input("total invested capital: ")
        tax_percentage = input("tax percentage(without percentage sign): ")
        nop = input("net operating profit of invested company (search it up): ")
        roic = int(nop) + int(nop) * (int(tax_percentage) * 100) / int(totl_invstd_cap) * 100
        print(roic)
        print("%")

    #calculation of P/B ratio

    def PB_ratio():
        market_cap = input("market cap: ")
        total_assets = input("total assets: ")
        total_liablities = input("total liability: ")
        PBR = int(market_cap) / (int(total_assets) - int(total_liablities))
        print(PBR)

    #calculation of ROA

    def ROA_calculate():
        net_income = input("net income: ")
        total_assets = input("total assets: ")
        ROA = int(net_income) / int(total_assets)
        print(ROA) 
    
    def ROE_calculate():
        Annual_net_income = input("annual net income: ")
        equity_of_shareholder = input("sharesholeder's(you) equity: ")
        ROE = int(Annual_net_income) / int(equity_of_shareholder)
        print("ROE = ")
        print(ROE)

    #calculation for PER

    def PER_calculate():
        current_price = input("currrent stock price: ")
        annual_profit = input("annual profit; ")
        PER = int(current_price) / int(annual_profit)
        print("PER = ")
        print(PER)

    #calculation of ROI
    
    def ROI_calculate():
        cost_of_investment = input("cost of investment: ")
        Profit = input("profit: ")
        ROI = (int(Profit) - int(cost_of_investment)) / cost_of_investment
        print("ROI = ")
        print(ROI)

    #calculation of ROIC

    def ROIC_calculate():
        totl_invstd_cap = input("total invested capital: ")
        tax_percentage = input("tax percentage(without percentage sign): ")
        nop = input("net operating profit of invested company (search it up): ")
        roic = int(nop) + int(nop) * (int(tax_percentage) * 100) / int(totl_invstd_cap) * 100
        print(roic)
        print("%")

    #calculation of P/B ratio
    
    def PB_ratio():
        market_cap = input("market cap: ")
        total_assets = input("total assets: ")
        total_liablities = input("total liability: ")
        PBR = int(market_cap) / (int(total_assets) - int(total_liablities))
        print(PBR)

    #calculation of ROA

    def ROA_calculate():
        net_income = input("net income: ")
        total_assets = input("total assets: ")
        ROA = int(net_income) / int(total_assets)
        print(ROA) 
    
    print(" ")
    print("calculating ROE")
    print(" ")
    ROE_calculate()
    print(" ")
    print("moving on to PER")
    print(" ")
    PER_calculate()
    print(" ")
    print("moving on to ROI")
    print(" ")
    ROI_calculate()
    print(" ")
    print("moving on to ROIC")
    print(" ")
    ROIC_calculate()
    print(" ")
    print("moving on to P/B ratio")
    print(" ")
    PB_ratio()
    print(" ")
    print("last one, ROA")
    print(" ")
    ROA_calculate()
    print("the companies stats: ")
    print(" ")
    print("ROE = ")
    print(ROE_calculate)

    #recomendation

    recomendation = 30
    if ask_recomendation.upper == "YES":
        if ROE_calculate <= 15 :
           print("source may not be good")
           print(" ")
        elif not ROE_calculate <= 15:
           print("ROE good")
        elif PER_calculate <= 20:
           print("source may not be good")
           print(" ")
           recomendation = recomendation - PER_calculate / 4
        elif not PER_calculate <= 15:
           print("PER good")
        elif ROI_calculate <= 5:
           print("source may not be good")
           print(" ")
           recomendation = recomendation - ROI_calculate
        elif not ROI_calculate <= 5 :
            print("ROI good")
        elif ROIC_calculate <= 9 :
           print("source may not be good")
           print(" ")
           recomendation = recomendation - ROIC_calculate / (9 / 5)
        elif not ROIC_calculate <= 9:
            print("ROIC good")
        elif PB_ratio <= 1:
           print("source may be good")
           print(" ")
           recomendation = recomendation - PB_ratio * 5
        elif not PB_ratio <= 1:
            print("P/B ratio good")
        elif ROA_calculate <= 10:
           print("source may not be good")
           print(" ")
           recomendation = recomendation - ROA_calculate / 2
        elif not ROA_calculate <= 10:
            print("ROA good")
        if recomendation == 30 or 29:
            print("source may be good(emphasizing 'may')")

    print("thank you " + name + ". (you can ignore this⬇️, if you aren't using this again)")
    