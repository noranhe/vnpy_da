CStockRspInfoField = {
    "ErrorID": "int",
    "ErrorMsg": "string",
}

CStockReqUserLoginField = {
    "UserId": "string",
    "UserPwd": "string",
    "UserType": "string",
    "MacAddress": "string",
    "ComputerName": "string",
    "SoftwareName": "string",
    "SoftwareVersion": "string",
    "AuthorCode": "string",
    "ErrorDescription": "string",
}

CStockRspAccountField = {
    "UserId": "string",
    "UserName": "string",
    "UserType": "string",
    "LoginPwd": "string",
    "AccountNo": "string",
    "TradePwd": "string",
    "IsSimulation": "string",
    "FrontendIp": "string",
    "FrontendPort": "string",
    "CurrencyNo": "string",
    "UserState": "string",
    "SelAll": "string",
    "Strategy": "string",
    "Inner": "string",
    "YingSun": "string",
    "ChaoDan": "string",
    "Option": "string",
    "CmeMarket": "string",
    "CmeCOMEXMarket": "string",
    "CmeNYMEXMarket": "string",
    "CmeCBTMarket": "string",
    "IceUSMarket": "string",
    "IceECMarket": "string",
    "IceEFMarket": "string",
    "CanTradeStockHK": "string",
    "CanTradeStockAM": "string",
    "MultiLogin": "string",
    "SellStockHK": "string",
    "SellStockAM": "string",
    "CanTradeStockKRX": "string",
    "HkexMarket": "string",
    "IdNumber": "string",
    "HkexMarketFee": "string",
    "IsProfessional": "string",
    "IsOverSea": "string",
    "IsFirstLogin": "string",
    "UserMobile": "string",
    "HasSetQA": "string",
    "CanTradeStockSGXQ": "string",
    "ExistMac": "string",
    "RatioINE": "string",
    "EurexMarket": "string",
    "HkexIsOverMaxTerminal": "string",
    "HkexOverMoney": "string",
    "CanTradeStockAU": "string",
    "NyFlag": "string",
}

CStockReqUserLogoutField = {
    "UserId": "string",
    "AccountNo": "string",
    "ErrorDescription": "string",
}

CStockReqOrderInsertField = {
    "UserId": "string",
    "AccountNo": "string",
    "LocalNo": "string",
    "ExchangeCode": "string",
    "ContractCode": "string",
    "BidAskFlag": "string",
    "OpenCloseFlag": "string",
    "OrderQty": "string",
    "OrderPrice": "string",
    "OrderType": "string",
    "TriggerPrice": "string",
    "TIF": "string",
    "StrategyId": "string",
    "MaxShow": "string",
    "MinQty": "string",
    "ErrorDescription": "string",
}

CStockRspOrderInsertField = {
    "UserId": "string",
    "AccountNo": "string",
    "SystemNo": "string",
    "LocalNo": "string",
    "OrderNo": "string",
    "ExchangeCode": "string",
    "ContractCode": "string",
    "BidAskFlag": "string",
    "OrderQty": "string",
    "OrderPrice": "string",
    "OrderType": "string",
    "OrderDate": "string",
    "OrderTime": "string",
    "ErrorCode": "string",
    "OrderState": "string",
    "TriggerPrice": "string",
    "TIF": "string",
    "OpenCloseFlag": "string",
    "StrategyId": "string",
    "MaxShow": "string",
    "MinQty": "string",
    "ExchangeTime": "string",
}

CStockReqOrderModifyField = {
    "SystemNo": "string",
    "UserId": "string",
    "LocalNo": "string",
    "AccountNo": "string",
    "OrderNo": "string",
    "ExchangeCode": "string",
    "ContractCode": "string",
    "BidAskFlag": "string",
    "OrderQty": "string",
    "OrderPrice": "string",
    "ModifyQty": "string",
    "ModifyPrice": "string",
    "OrderType": "string",
    "TriggerPrice": "string",
    "ModifyTriggerPrice": "string",
    "TIF": "string",
    "ErrorDescription": "string",
}

CStockRspOrderModifyField = CStockRspOrderInsertField

CStockReqOrderCancelField = {
    "UserId": "string",
    "LocalNo": "string",
    "AccountNo": "string",
    "SystemNo": "string",
    "OrderNo": "string",
    "ExchangeCode": "string",
    "ContractCode": "string",
    "BidAskFlag": "string",
    "OrderQty": "string",
    "OrderPrice": "string",
    "OrderType": "string",
    "ErrorDescription": "string",
}

CStockRspOrderCancelField = {
    "UserId": "string",
    "AccountNo": "string",
    "SystemNo": "string",
    "LocalNo": "string",
    "OrderNo": "string",
    "CancelNo": "string",
    "ExchangeCode": "string",
    "ContractCode": "string",
    "BidAskFlag": "string",
    "OrderQty": "string",
    "OrderPrice": "string",
    "FilledQty": "string",
    "CancelledQty": "string",
    "OrderType": "string",
    "CancelledDate": "string",
    "CancelledTime": "string",
    "ErrorCode": "string",
}

CStockReqPasswordUpdateField = {
    "UserId": "string",
    "OldPassword": "string",
    "NewPassword": "string",
    "ErrorDescription": "string",
}

CStockRspPasswordUpdateField = {
    "UserId": "string",
    "OldPassword": "string",
    "NewPassword": "string",
}

CStockQryOrderField = {
    "UserId": "string",
    "AccountNo": "string",
    "IsSimulation": "string",
    "OrderNo": "string",
    "OrderDateTime": "string",
    "ErrorDescription": "string",
}

CStockRspOrderField = {
    "UserId": "string",
    "AccountNo": "string",
    "SystemNo": "string",
    "LocalNo": "string",
    "OrderNo": "string",
    "ExchangeCode": "string",
    "ContractCode": "string",
    "BidAskFlag": "string",
    "OrderQty": "string",
    "OrderPrice": "string",
    "FilledQty": "string",
    "FilledPrice": "string",
    "OrderType": "string",
    "OrderDate": "string",
    "OrderTime": "string",
    "ErrorCode": "string",
    "OrderState": "string",
    "CancelUserId": "string",
    "TriggerPrice": "string",
    "TIF": "string",
    "OpenCloseFlag": "string",
    "StrategyId": "string",
    "MaxShow": "string",
    "MinQty": "string",
    "ExchangeTime": "string",
    "CancelTime": "string",
}

CStockQryTradeField = {
    "UserId": "string",
    "ErrorDescription": "string",
    "lastFilledNo": "string",
}

CStockRspTradeField = {
    "UserId": "string",
    "AccountNo": "string",
    "FilledNo": "string",
    "OrderNo": "string",
    "SystemNo": "string",
    "LocalNo": "string",
    "ExchangeCode": "string",
    "TreatyCode": "string",
    "BuySale": "string",
    "FilledNumber": "string",
    "FilledPrice": "string",
    "FilledDate": "string",
    "FilledTime": "string",
    "Commsion": "string",
    "OrderNumber": "string",
    "OrderPrice": "string",
    "DeliveryDate": "string",
    "FilledType": "string",
    "OrderType": "string",
    "ValidDate": "string",
    "AddReduce": "string",
    "ExchangeTime": "string",
    "SubClientNo": "string",
    "FillBrokerList": "string",
    "ErrorDescription": "string",
}

CStockQryInstrumentField = {
    "PageIndex": "int",
    "ExchangeNo": "string",
    "ModifyDay": "string",
    "ErrorDescription": "string",
}

CStockRspInstrumentField = {
    "ExchangeNo": "string",
    "ExchangeName": "string",
    "CommodityNo": "string",
    "CommodityName": "string",
    "CommodityType": "string",
    "CurrencyNo": "string",
    "CurrencyName": "string",
    "ProductDot": "double",
    "UpperTick": "double",
    "SettlePrice": "double",
    "TradeMonth": "string",
    "DotNum": "int",
    "LowerTick": "int",
    "DotNumCarry": "int",
    "UpperTickCarry": "double",
    "FirstNoticeDay": "string",
    "FreezenPercent": "double",
    "FreezenMoney": "double",
    "FeeMoney": "double",
    "FeePercent": "double",
    "PriceStrike": "double",
    "ProductDotStrike": "double",
    "UpperTickStrike": "double",
    "LastTradeDay": "string",
    "LastUpdateDay": "string",
    "CriticalPrice": "double",
    "CriticalMinChangedPrice": "double",
    "ExchangeSub": "string",
    "OptionType": "string",
    "OptionMonth": "string",
    "OptionStrikePrice": "string",
    "OptionCommodityNo": "string",
    "OptionContractNo": "string",
    "MortgagePercent": "string",
    "UpperTickCode": "string",
    "LotSize": "string",
    "FlatTime": "string",
    "CommodityFNameEN": "string",
    "CanSell": "string",
    "SellRate": "double",
    "SellMax": "double",
    "StrikeRate": "double",
    "StrikePrice": "double",
    "ReceivePrice": "double",
    "ExpireDate": "string",
    "SellRateKeep": "double",
    "StrikeCommodityNo": "string",
    "CallPutFlag": "string",
    "Publisher": "string",
}

CStockQryExchangeField = {
    "ProductGroupID": "string",
    "ErrorDescription": "string",
}

CStockRspExchangeField = {
    "ExchangeNo": "string",
    "ExchangeName": "string",
    "SettleType": "string",
    "NameEN": "string",
}

CStockQryCapitalField = {
    "Unused": "char",
    "ErrorDescription": "string",
}

CStockRspCapitalField = {
    "UserId": "string",
    "Deposit": "string",
    "Withdraw": "string",
    "TodayTradableFund": "string",
    "TodayInitialBalance": "string",
    "TodayRealtimeBalance": "string",
    "FrozenFund": "string",
    "Commission": "string",
    "InitialMargin": "string",
    "YdTradableFund": "string",
    "YdInitialBalance": "string",
    "YdFinalBalance": "string",
    "ProfitLoss": "string",
    "CurrencyNo": "string",
    "CurrencyRate": "double",
    "LMEUnexpiredPL": "double",
    "LMEUnaccountPL": "double",
    "MaintenanceMargin": "double",
    "Premium": "double",
    "CreditAmount": "double",
    "IntialFund": "double",
    "FundAccountNo": "string",
    "MortgageInMoney": "double",
    "MarginLimit": "double",
    "BorrowInMoney": "double",
    "T1DeliveryMoney": "double",
    "T2DeliveryMoney": "double",
    "T3DeliveryMoney": "double",
    "TNDeliveryMoney": "double",
    "TradeLimit": "double",
    "CanCashOutMoneyAmount": "double",
    "DepositInterest": "double",
    "LoanInterest": "double",
    "CrossCurrencyMaxMoneyAmt": "double",
    "SellShortFrozenMoney": "double",
    "SellShortInterest": "double",
    "ShortPosAddtionalMargin": "double",
    "ErrorDescription": "string",
}

CStockQryPositionField = {
    "ErrorDescription": "string",
}

CStockRspPositionField = {
    "ClientNo": "string",
    "ExchangeCode": "string",
    "ProductCode": "string",
    "LongShortPosFlag": "string",
    "PosCostPrice": "double",
    "CanSellShares": "int",
    "TodayBuyShares": "int",
    "FrosenShares": "int",
    "TotalBuyMoney": "double",
    "TotalSellMoney": "double",
    "TotalBuyShares": "int",
    "TotalSellShares": "int",
    "FirstPosDate": "string",
    "ClosePosPL": "double",
    "T1DeliveryShares": "int",
    "T2DeliveryShares": "int",
    "T3DeliveryShares": "int",
    "NotDeliveryShares": "int",
    "DeliveredShares": "int",
    "SellShortShares": "int",
    "SellShortMoney": "double",
    "SSPosAvgCostPrice": "double",
}

CStockQryTickField = {
    "Unused": "char",
    "ErrorDescription": "string",
}

CStockRspTickField = {
    "UpperTickCode": "string",
    "PriceFrom": "string",
    "UpperTick": "string",
    "ProductDot": "string",
    "DotNum": "string",
    "LowerTick": "string",
}

CStockQryCurrencyField = {
    "Unused": "char",
    "ErrorDescription": "string",
}

CStockRspCurrencyField = {
    "CurrencyNo": "string",
    "IsBase": "int",
    "ChangeRate": "double",
    "CurrencyName": "string",
    "CurrencyNameEN": "string",
}

CStockQryVersionField = {
    "UserId": "string",
    "UserPwd": "string",
    "ErrorDescription": "string",
}

CStockRspVersionField = {
    "Version": "string",
    "MustUpdate": "string",
    "MustVersion": "string",
    "VersionContent_CN": "string",
    "VersionContent_US": "string",
}

CStockRtnOrderField = {
    "LocalOrderNo": "string",
    "ExchangeNo": "string",
    "TreatyCode": "string",
    "OrderNo": "string",
    "OrderNumber": "int",
    "FilledNumber": "int",
    "FilledAdvPrice": "double",
    "BuyHoldNumber": "int",
    "BuyHoldOpenPrice": "double",
    "BuyHoldPrice": "double",
    "SaleHoldNumber": "int",
    "SaleHoldOpenPrice": "double",
    "SaleHoldPrice": "double",
    "IsCanceled": "string",
    "FilledTotalFee": "double",
    "Status": "int",
    "AccountNo": "string",
    "HoldType": "string",
    "HoldMarginBuy": "double",
    "HoldMarginSale": "double",
    "CurrPrice": "double",
    "FloatProfit": "double",
}

CStockRtnCapitalField = {
    "ClientNo": "string",
    "AccountNo": "string",
    "CurrencyNo": "string",
    "Available": "double",
    "YAvailable": "double",
    "CanCashOut": "double",
    "Money": "double",
    "ExpiredProfit": "double",
    "FrozenDeposit": "double",
    "Fee": "double",
    "Deposit": "double",
    "KeepDeposit": "double",
    "Status": "int",
    "InMoney": "double",
    "OutMoney": "double",
    "UnexpiredProfit": "double",
    "TodayTotal": "double",
    "UnaccountProfit": "double",
    "Royalty": "double",
    "ExchangeNo": "string",
    "TreatyCode": "string",
    "OrderNo": "string",
    "OrderNumber": "int",
    "FilledNumber": "int",
    "FilledAdvPrice": "double",
    "BuyHoldNumber": "int",
    "BuyHoldOpenPrice": "double",
    "BuyHoldPrice": "double",
    "SaleHoldNumber": "int",
    "SaleHoldOpenPrice": "double",
    "SaleHoldPrice": "double",
    "IsCanceled": "string",
    "FilledTotalFee": "double",
    "Credit": "double",
    "MarginLimit": "double",
    "BorrowValue": "double",
    "MortgageMoney": "double",
    "T1": "double",
    "T2": "double",
    "T3": "double",
    "TN": "double",
    "TradeLimit": "double",
    "FCrossMax": "double",
    "SellFreezenMoney": "double",
    "SellInterest": "double",
    "SellNeedAddMargin": "double",
}

CStockRtnPositionField = CStockRspPositionField

CStockRtnTradeField = CStockRspTradeField

CStockReqGetQuestionField = {
    "Unused": "int",
    "ErrorDescription": "string",
}

CStockRspQuestionField = {
    "QuestionType": "string",
    "QuestionId": "string",
    "QuestionCN": "string",
    "QuestionEN": "string",
}

CStockReqSafeVerifyField = {
    "UserId": "string",
    "UserPwd": "string",
    "Type": "string",
    "Question": "string",
    "Answer": "string",
    "MobileNumber": "string",
    "VerifyCode": "string",
    "SaveMac": "string",
    "MacAddress": "string",
    "ErrorDescription": "string",
}

CStockReqSetVerifyQAField = {
    "UserId": "string",
    "UserPwd": "string",
    "Type": "string",
    "Question": "string",
    "Answer": "string",
    "MobileNumber": "string",
    "VerifyCode": "string",
    "SaveMac": "string",
    "ErrorDescription": "string",
}

CStockReqVerifyCodeField = {
    "UserId": "string",
    "UserPwd": "string",
    "Type": "string",
    "Question": "string",
    "Answer": "string",
    "MobileNumber": "string",
    "VerifyCode": "string",
    "ErrorDescription": "string",
}

