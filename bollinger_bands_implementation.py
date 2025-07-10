import backtrader as bt
from datetime import datetime
import yfinance as yf

class BollingerBandsStrategy(bt.Strategy):

    params = (
        ('period', 20),
        ('std', 2),
        ('size', 20)
    )

    def __init__(self):
        self.bollinger = bt.indicators.BollingerBands(period=self.p.period, 
                                                      devfactor=self.p.std)
        
    def next(self):

        # if we do not have any open positions
        if not self.position:
            # open short position if needed
            if self.data.close[0] > self.bollinger.lines.top:
                self.sell(size=self.p.size)
            # open long positions if needed
            if self.data.close[0] < self.bollinger.lines.bot:
                self.buy(size=self.p.size)
        else:
            # we have opened long positions - we have to check whether to close the postion
            if self.position.size > 0:
                # close it when the price crosses the middle line
                self.sell(exectype=bt.Order.Limit, price=self.bollinger.lines.mid[0],
                          size=self.p.size)
            # close the short postion (with the help of buy)
            else:
                self.buy(exectype=bt.Order.Limit, price=self.bollinger.lines.mid[0],
                          size=self.p.size)

if __name__ == '__main__':

    cerebro = bt.Cerebro()

    # Download data
    df = yf.download('IBM', start='2010-01-01', end='2020-01-01')
    df.columns = [col[0] if isinstance(col, tuple) else col for col in df.columns]

    # Pass dataname
    stock_data = bt.feeds.PandasData(dataname=df)

    # we have to add the data to Cerebro
    cerebro.adddata(stock_data)
    cerebro.addstrategy(BollingerBandsStrategy)

    cerebro.addobserver(bt.observers.Value)
    cerebro.addanalyzer(bt.analyzers.SharpeRatio, riskfreerate= 0)
    cerebro.addanalyzer(bt.analyzers.Returns)
    cerebro.addanalyzer(bt.analyzers.DrawDown)
    cerebro.broker.set_cash(10000)
    print('initial capital: $%.2f' % cerebro.broker.getvalue())

    results = cerebro.run()
    
    print('Sharpe ratio: %.2f' % results[0].analyzers.sharperatio.get_analysis()['sharperatio'])
    print('Return: %.2f%%' % results[0].analyzers.returns.get_analysis()['rnorm100'])
    print('Max Drawdown: %.2f%%' % results[0].analyzers.drawdown.get_analysis()['max']['drawdown'])
    print('Capital: $%.2f' % cerebro.broker.getvalue())

