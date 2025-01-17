CFutureRspInfoField = {
    "ErrorID": "int",
    "ErrorMsg": "string",
}

CFutureReqUserLoginField = {
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

CFutureRspAccountField = {
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

CFutureReqUserLogoutField = {
    "UserId": "string",
    "AccountNo": "string",
    "ErrorDescription": "string",
}

CFutureReqOrderInsertField = {
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
    "Tag50": "string",
    "ErrorDescription": "string",
    "IsProgram": "int",
    "OrgOrderLocationID": "string",
}

CFutureRspOrderInsertField = {
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
    "OrdSourceType": "string",
    "Tag50": "string",
}

CFutureReqOrderModifyField = {
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
    "Tag50": "string",
    "ErrorDescription": "string",
    "OrgOrderLocationID": "string",
}

CFutureRspOrderModifyField = CFutureRspOrderInsertField

CFutureReqOrderCancelField = {
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
    "Tag50": "string",
    "ErrorDescription": "string",
    "OrgOrderLocationID": "string",
}

CFutureRspOrderCancelField = {
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
    "OrdSourceType": "string",
    "Tag50": "string",
}

CFutureReqPasswordUpdateField = {
    "UserId": "string",
    "OldPassword": "string",
    "NewPassword": "string",
    "ErrorDescription": "string",
}

CFutureRspPasswordUpdateField = {
    "UserId": "string",
    "OldPassword": "string",
    "NewPassword": "string",
}

CFutureQryOrderField = {
    "UserId": "string",
    "AccountNo": "string",
    "IsSimulation": "string",
    "OrderNo": "string",
    "OrderDateTime": "string",
    "ErrorDescription": "string",
}

CFutureRspOrderField = {
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

CFutureQryTradeField = {
    "UserId": "string",
    "ErrorDescription": "string",
    "lastFilledNo": "string",
    "maxItemNumOnePage": "string",
}

CFutureRspTradeField = {
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
    "ErrorDescription": "string",
}

CFutureQryInstrumentField = {
    "PageIndex": "int",
    "ExchangeNo": "string",
    "CommodityNo": "string",
    "CommodityType": "string",
    "ContractNo": "string",
    "ErrorDescription": "string",
}

CFutureRspInstrumentField = {
    "CommodityCode": "string",
    "ExchangeNo": "string",
    "ContractNo": "string",
    "ContractFName": "string",
    "CommodityNo": "string",
    "CommodityFName": "string",
    "CommodityType": "string",
    "CommodityFCurrencyNo": "string",
    "CurrencyFName": "string",
    "ProductDot": "double",
    "UpperTick": "double",
    "ExchangeName": "string",
    "LastSettlePrice": "double",
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
    "ContractFNameEN": "string",
    "CommodityFNameEN": "string",
    "OptionStyle": "string",
}

CFutureQryExchangeField = {
    "ProductGroupID": "string",
    "ErrorDescription": "string",
}

CFutureRspExchangeField = {
    "ExchangeNo": "string",
    "ExchangeName": "string",
    "SettleType": "string",
    "NameEN": "string",
}

CFutureQryCapitalField = {
    "Unused": "char",
    "ErrorDescription": "string",
}

CFutureRspCapitalField = {
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
    "TradeLimit": "double",
    "CanCashOutMoneyAmount": "double",
    "DepositInterest": "double",
    "LoanInterest": "double",
    "ErrorDescription": "string",
}

CFutureQryPositionField = {
    "ErrorDescription": "string",
}

CFutureRspPositionField = {
    "MatchDate": "string",
    "MatchNo": "string",
    "ClientNo": "string",
    "ExchangeNo": "string",
    "CommodityNo": "string",
    "ContractNo": "string",
    "Direct": "string",
    "HoldVol": "int",
    "HoldPrice": "double",
    "CurrencyNo": "string",
    "ForciblyPrice": "double",
    "Account": "string",
    "HoldType": "string",
    "DeliveryDate": "string",
    "ExchangeName": "string",
    "CurrencyName": "string",
    "ContCode": "string",
    "HoldMargin": "double",
}

CFutureQryTickField = {
    "Unused": "char",
    "ErrorDescription": "string",
}

CFutureRspTickField = {
    "UpperTickCode": "string",
    "PriceFrom": "string",
    "UpperTick": "string",
    "ProductDot": "string",
    "DotNum": "string",
    "LowerTick": "string",
}

CFutureQryCurrencyField = {
    "Unused": "char",
    "ErrorDescription": "string",
}

CFutureRspCurrencyField = {
    "CurrencyNo": "string",
    "IsBase": "int",
    "ChangeRate": "double",
    "CurrencyName": "string",
    "CurrencyNameEN": "string",
}

CFutureQryCommodityField = {
    "UpdateDate": "string",
    "ExchangeNo": "string",
    "ErrorDescription": "string",
}

CFutureRspCommodityField = {
    "CommodityNo": "string",
    "ExchangeNo": "string",
    "CommodityType": "string",
    "Name": "string",
    "Enabled": "string",
    "RegDate": "string",
    "CurrencyNo": "string",
    "ProductDot": "double",
    "LowerTick": "double",
    "UpperTick": "double",
    "DotNum": "int",
    "StrikeCommodityId": "int",
    "OptionStyle": "string",
    "ExchangeNo2": "string",
    "IsSFuture": "string",
}

CFutureQryExchangeTimeField = {
    "Unused": "char",
    "ErrorDescription": "string",
}

CFutureQryCommodityTimeField = {
    "ExchangeNo": "string",
    "CommodityNo": "string",
    "ErrorDescription": "string",
}

CFutureRspExchangeTimeField = {
    "Year": "string",
    "SummerBegin": "string",
    "WinterBegin": "string",
    "ExchangeNo": "string",
    "Name": "string",
}

CFutureRspCommodityTimeField = {
    "CrossTrade": "string",
    "Stage": "string",
    "Summer": "string",
    "Opendate": "string",
    "Closingdate": "string",
    "CommodityNo": "string",
    "ComName": "string",
    "ExchangeNo": "string",
    "ExName": "string",
}

CFutureQryVersionField = {
    "UserId": "string",
    "UserPwd": "string",
    "ErrorDescription": "string",
}

CFutureRspVersionField = {
    "Version": "string",
    "MustUpdate": "string",
    "MustVersion": "string",
    "VersionContent_CN": "string",
    "VersionContent_US": "string",
}

CFutureRtnOrderField = {
    "LocalNo": "string",
    "ExchangeCode": "string",
    "ContractCode": "string",
    "OrderNo": "string",
    "OrderQty": "int",
    "FilledQty": "int",
    "FilledAvgPrice": "double",
    "LongPositionQty": "int",
    "LongPosAveragePrx": "double",
    "CNLongPosAveragePrx": "double",
    "ShortPositionQty": "int",
    "ShortPosAveragePrx": "double",
    "CNShortPosAveragePrx": "double",
    "IsCanceled": "string",
    "FilledTotalFee": "double",
    "SequenceNo": "int",
    "AccountNo": "string",
    "PositionType": "string",
    "LongPosMargin": "double",
    "ShortPosMargin": "double",
    "CurrPrice": "double",
    "ProfitLoss": "double",
}

CFutureRtnCapitalField = {
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

CFutureRtnPositionField = CFutureRtnOrderField

CFutureRtnTradeField = CFutureRspTradeField

CFutureReqGetQuestionField = {
    "Unused": "int",
    "ErrorDescription": "string",
}

CFutureRspQuestionField = {
    "QuestionType": "string",
    "QuestionId": "string",
    "QuestionCN": "string",
    "QuestionEN": "string",
}

CFutureReqSafeVerifyField = {
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

CFutureReqSetVerifyQAField = {
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

CFutureReqVerifyCodeField = {
    "UserId": "string",
    "UserPwd": "string",
    "Type": "string",
    "Question": "string",
    "Answer": "string",
    "MobileNumber": "string",
    "VerifyCode": "string",
    "ErrorDescription": "string",
}

CFutureQryTotalPositionField = {
    "AccountNo": "string",
    "ErrorDescription": "string",
}

CFutureRspTotalPositionField = CFutureRtnOrderField

CFutureQryStrategyField = {
    "ExchangeNo": "string",
    "ErrorDescription": "string",
}

CFutureRspStrategyField = {
    "CommodityCode": "string",
    "ExchangeNo": "string",
    "ContractNo": "string",
    "ContractFName": "string",
    "CommodityNo": "string",
    "CommodityFName": "string",
    "CommodityType": "string",
    "CommodityFCurrencyNo": "string",
    "CurrencyFName": "string",
    "ProductDot": "double",
    "UpperTick": "double",
    "ExchangeName": "string",
    "LastSettlePrice": "double",
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
    "ContractFNameEN": "string",
    "CommodityFNameEN": "string",
    "OptionStyle": "string",
}

CFutureQryStrategyDetailField = {
    "StartegyCommodityNo": "string",
    "ErrorDescription": "string",
}

CFutureRspStrategyDetailField = {
    "StartegyCommodityNo": "string",
    "StartegyContractNo": "string",
    "Price": "string",
    "LegNum": "int",
    "LastTradeDate": "string",
    "SeqId": "int",
    "CommodityNo": "string",
    "ContractNo": "string",
    "Direct": "string",
    "Quantity": "int",
    "Model": "string",
    "ModifyDate": "string",
    "OrderMethod": "string",
    "PriceTolerance": "double",
    "PriceParam": "double",
    "SuportQuantity": "int",
    "MinMove": "int",
    "TimerOrder": "int",
    "TimerOrderBeyondNum": "string",
    "TimerOrderPrice": "int",
    "TimerOrderPriceBeyondNum": "string",
    "TimerOrderPriceTriggerNum": "string",
    "ZhiSunOrder": "int",
    "ZhiSunOrderBeyondNum": "string",
    "TimerPingCang": "int",
    "TimerPingCangBeyondNum": "string",
    "SafeDeep": "int",
    "MainRange": "int",
}

