import os
import pandas as pd

_data_dir='/data_dir'

class StockDataUtil():
    
    @staticmethod
    def get_fin():
        """ファンダメンタル情報 ('stock_fin.csv.gz')

        Result_は実績、Forecast_は予測

        Returns:
            pandas.DataFrame: [description]

        Notes:

            変数名	説明	型	例
            base_date	日付	object	2016/01/04
            Local Code	銘柄コード	int64	2753
            Result_FinancialStatement AccountingStandard	会計基準　単独:NonConsolidated、連結国内:ConsolidatedJP、連結SEC:ConsolidatedUS、連結IFRS:ConsolidatedIFRS	object	ConsolidatedJP
            Result_FinancialStatement FiscalPeriodEnd	決算期	object	2015/12
            Result_FinancialStatement ReportType	決算種別　第1四半期:Q1、中間決算:Q2、第3四半期:Q3、本決算:Annual	object	Q3
            Result_FinancialStatement FiscalYear	決算年度。本決算の決算期末が属する年。	float64	2016
            Result_FinancialStatement ModifyDate	更新日	object	2016/01/04
            Result_FinancialStatement CompanyType	会社区分 一般事業会社:GB、銀行:BK、証券会社:SE、損保会社:IN ※上記に該当しない場合は空文字を設定してます。	object	GB
            Result_FinancialStatement ChangeOfFiscalYearEnd	決算期変更フラグ 決算期変更あり:true、決算期変更なし:false	object	FALSE
            Result_FinancialStatement NetSales	売上高（単位：百万円） 会社区分によって項目名の読替えを行ういます。 銀行：経常収益、証券：営業収益、損保：経常収益 ※未開示の場合は空文字を設定してます。	float64	22354
            Result_FinancialStatement OperatingIncome	営業利益（単位：百万円） ※未開示の場合は空文字を設定してます。	float64	2391
            Result_FinancialStatement OrdinaryIncome	経常利益（単位：百万円） 会計基準が連結SECの場合は、項目名を「税引前利益」に読み替えます。 ※未開示の場合は空文字を設定してます。	float64	2466
            Result_FinancialStatement NetIncome	当期純利益（単位：百万円） ※未開示の場合は空文字を設定してます。	float64	1645
            Result_FinancialStatement TotalAssets	総資産（単位：百万円） ※未開示の場合は空文字を設定してます。	float64	21251
            Result_FinancialStatement NetAssets	純資産（単位：百万円） ※未開示の場合は空文字を設定してます。	float64	16962
            Result_FinancialStatement CashFlowsFromOperatingActivities	営業キャッシュフロー（単位：百万円） ※未開示の場合は空文字を設定してます。	float64	12404
            Result_FinancialStatement CashFlowsFromFinancingActivities	財務キャッシュフロー（単位：百万円） ※未開示の場合は空文字を設定してます。	float64	-98
            Result_FinancialStatement CashFlowsFromInvestingActivities	投資キャッシュフロー（単位：百万円） ※未開示の場合は空文字を設定してます。	float64	-1307
            Forecast_FinancialStatement AccountingStandard	予想: 会計基準　単独:NonConsolidated、連結国内:ConsolidatedJP、連結SEC:ConsolidatedUS、連結IFRS:ConsolidatedIFRS	object	ConsolidatedJP
            Forecast_FinancialStatement FiscalPeriodEnd	来期予想情報:　決算期	object	2016/03
            Forecast_FinancialStatement ReportType	来期予想情報:　決算種別　第1四半期:Q1、中間決算:Q2、第3四半期:Q3、本決算:Annual	object	Annual
            Forecast_FinancialStatement FiscalYear	来期予想情報:　決算年度。本決算の決算期末が属する年。	float64	2016
            Forecast_FinancialStatement ModifyDate	来期予想情報:　更新日	object	2016/01/04
            Forecast_FinancialStatement CompanyType	来期予想情報:　会社区分 一般事業会社:GB、銀行:BK、証券会社:SE、損保会社:IN ※上記に該当しない場合は空文字を設定してます。	object	GB
            Forecast_FinancialStatement ChangeOfFiscalYearEnd	来期予想情報:　決算期変更フラグ 決算期変更あり:true、決算期変更なし:false	object	FALSE
            Forecast_FinancialStatement NetSales	来期予想情報:　売上高（単位：百万円） 会社区分によって項目名の読替えを行います。 銀行：経常収益、証券：営業収益、損保：経常収益 ※未開示の場合は空文字を設定してます。	float64	30500
            Forecast_FinancialStatement OperatingIncome	来期予想情報:　営業利益（単位：百万円） ※未開示の場合は空文字を設定してます。	float64	3110
            Forecast_FinancialStatement OrdinaryIncome	来期予想情報:　経常利益（単位：百万円） 会計基準が連結SECの場合は、項目名を「税引前利益」に読み替えます。 ※未開示の場合は空文字を設定してます。	float64	3200
            Forecast_FinancialStatement NetIncome	来期予想情報:　当期純利益（単位：百万円） ※未開示の場合は空文字を設定してます。	float64	2130
            Result_Dividend FiscalPeriodEnd	配当情報:　決算期	object	2015/11
            Result_Dividend ReportType	配当情報:　決算種別　第1四半期:Q1、中間決算:Q2、第3四半期:Q3、本決算:Annual	object	Annual
            Result_Dividend FiscalYear	配当情報:　決算年度。本決算の決算期末が属する年。	float64	2015
            Result_Dividend ModifyDate	配当情報:　更新日	object	2016/01/07
            Result_Dividend RecordDate	配当情報:　配当基準日	object	2015/11/30
            Result_Dividend DividendPayableDate	配当情報:　配当支払開始日　※予想の場合は空文字を設定してます。	object	2016/02/29
            Result_Dividend QuarterlyDividendPerShare	配当情報:　一株当たり四半期配当金（単位：円）　※未開示の場合は空文字を設定してます。	float64	8
            Result_Dividend AnnualDividendPerShare	配当情報:　一株当たり年間配当金累計（単位：円）※未開示の場合は空文字を設定してます。	float64	15
            Forecast_Dividend FiscalPeriodEnd	予想配当情報:　決算期	object	2016/03
            Forecast_Dividend ReportType	予想配当情報:　決算種別　第1四半期:Q1、中間決算:Q2、第3四半期:Q3、本決算:Annual	object	Annual
            Forecast_Dividend FiscalYear	予想配当情報:　決算年度。本決算の決算期末が属する年。	float64	2016
            Forecast_Dividend ModifyDate	予想配当情報:　更新日	object	2016/01/04
            Forecast_Dividend RecordDate	予想配当情報:　配当基準日	object	2016/03/31
            Forecast_Dividend QuarterlyDividendPerShare	予想配当情報:　一株当たり四半期配当金（単位：円）　※未開示の場合は空文字を設定してます。	float64	45
            Forecast_Dividend AnnualDividendPerShare	予想配当情報:　一株当たり年間配当金累計（単位：円）※未開示の場合は空文字を設定してます。	float64	90
        """        
        path = os.path.join(_data_dir, 'stock_fin.csv.gz')
        return pd.read_csv(path)
    
    @staticmethod
    def get_stock_fin_price():
        """ファンダメンタル+株価情報 (stock_fin_price.csv.gz)

        stock_fin_priceは、株価情報である<<株価情報 : stock_price, stock_price>>と財務諸表である<<ファンダメンタル情報: stock_fin, stock_fin>>をデータとして扱いやすいように結合したデータです。
        変数名や型などについては、同じであるため記載を省略しています。
        また、データのサイズが非常に大きいため、必要に応じて活用していただきたいと思います。

        Returns:
            pandas.DataFrame: [description]
        """        
        path = os.path.join(_data_dir, 'stock_fin_price.csv.gz')
        return pd.read_csv(path)
    
    @staticmethod
    def get_labels():
        """目的変数 (stock_labels.csv.gz)

        stock_labelsは予測の目的変数のデータであり、各銘柄で決算発表が行われた日の取引所公式終値から、その日の翌営業日以降N（5，10，20）営業日間における最高値及び最安値への変化率を記録したデータです。
        各値の計算式は、 ([基準日付の翌日以降N営業日間における高値/安値] / [基準日付の終値]) - 1 です。
        なお、ラベルの対象期間 (5、10、20営業日の間) に値が付かなかった場合は、ラベルを NaN としております。

        Returns:
            pandas.DataFrame: [description]

        Notes:
            変数名	説明	型	例
            base_date	基準日付（各銘柄で決算短信等の開示がされた日）	object	2016-01-04
            Local Code	銘柄コード	int64	1301
            label_date_5	基準日付から5営業日後の日付。label_high_5算出に使用される終値範囲の基準日	object	2016-01-12
            label_high_5	基準日付の終値から5営業日の間の最高値への変化率	float64	0.00364
            label_low_5	基準日付の終値から5営業日の間の最安値への変化率	float64	-0.04
            label_date_10	基準日付から10営業日後の日付。label_high_10算出に使用される終値範囲の基準日	object	2016-01-19
            label_high_10	基準日付の終値から10営業日の間の最高値への変化率	float64	0.00364
            label_low_10	基準日付の終値から10営業日の間の最安値への変化率	float64	-0.05455
            label_date_20	基準日付から20営業日後の日付。label_high_20算出に使用される終値範囲の基準日	object	2016-02-02
            label_high_20	基準日付の終値から20営業日の間の最高値への変化率	float64	0.00364
            label_low_20	基準日付の終値から20営業日の間の最安値への変化率	float64	-0.08364
        """        
        path = os.path.join(_data_dir, 'stock_labels.csv.gz')
        return pd.read_csv(path)
    
    @staticmethod
    def get_list():
        """銘柄情報('stock_list.csv.gz')

        Returns:
            pandas.DataFrame: [description]

        Notes: 
            変数名	説明	型	例
            prediction_target 予測対象銘柄 bool True 
            Effective Date 銘柄情報の基準日 int64 20201030 
            Local Code 株式銘柄コード int64 1301 
            Name (English) 銘柄名 object KYOKUYO CO.,LTD. 
            Section/Products 市場・商品区分 object First Section (Domestic) 
            33 Sector(Code) 銘柄の33業種区分(コード) int64 50 
            33 Sector(name) 銘柄の33業種区分(名前) object Fishery, Agriculture and Forestry 
            17 Sector(Code) 銘柄の17業種区分(コード) int64 1 
            17 Sector(name) 銘柄の17業種区分(名前) object FOODS 
            Size Code (New Index Series) TOPIXニューインデックスシリーズ規模区分(コード) object 7 
            Size (New Index Series) TOPIXニューインデックスシリーズ規模区分 object TOPIX Small 2 
            IssuedShareEquityQuote AccountingStandard 会計基準 単独:NonConsolidated、連結国内:ConsolidatedJP、連結SEC:ConsolidatedUS、連結IFRS:ConsolidatedIFRS object ConsolidatedJP 
            IssuedShareEquityQuote ModifyDate 更新日 object 2020/11/06 
            IssuedShareEquityQuote IssuedShare 発行済株式数
        """
        path = os.path.join(_data_dir, 'stock_list.csv.gz')
        return pd.read_csv(path)
    
    @staticmethod
    def get_price():
        """株価情報 (stock_price.csv.gz)

        EndOfDayQuote CumulativeAdjustmentFactor（累積調整係数）の利用には注意が必要とのこと。

        Returns:
            pandas.DataFrame: [description]

        Notes:
            変数名	説明	型	例
            Local Code	銘柄コード	int64	1301
            EndOfDayQuote Date	日付	object	2016/01/04
            EndOfDayQuote Open	始値	float64	2800
            EndOfDayQuote High	高値	float64	2820
            EndOfDayQuote Low	安値	float64	2740
            EndOfDayQuote Close	終値。大引け後にセットされる	float64	2750
            EndOfDayQuote ExchangeOfficialClose	取引所公式終値。最終の特別気配または最終気配を含む終値	float64	2750
            EndOfDayQuote Volume	売買高	float64	32000
            EndOfDayQuote CumulativeAdjustmentFactor	累積調整係数	float64	0.1
            EndOfDayQuote PreviousClose	前回の終値	float64	2770
            EndOfDayQuote PreviousCloseDate	前回の終値が発生した日	object	2015/12/30
            EndOfDayQuote PreviousExchangeOfficialClose	前回の取引所公式終値	float64	2770
            EndOfDayQuote PreviousExchangeOfficialCloseDate	前回の取引所公式終値が発生した日	object	2015/12/30
            EndOfDayQuote ChangeFromPreviousClose	騰落幅。前回終値と直近約定値の価格差	float64	-20
            EndOfDayQuote PercentChangeFromPreviousClose	騰落率。前回終値からの直近約定値の上昇率または下落率	float64	-0.722
            EndOfDayQuote VWAP	売買高加重平均価格(VWAP)	float64	2778.25
        """        
        path = os.path.join(_data_dir, 'stock_price.csv.gz')
        return pd.read_csv(path)
    