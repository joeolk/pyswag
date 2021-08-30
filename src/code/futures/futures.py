# THIS IS FOR FRANCIS!
from datetime import datetime, timedelta
import yfinance as yf


def get_high_low(args):
    """

    """

    end_date = datetime.now().date() - timedelta(1)
    start_date = end_date - timedelta(2)

    if args.start_date:
        end_date = args.end_date
        start_date = args.start_date

    data = yf.download(args.ticker_symbol, start=start_date, end=end_date)

    most_recent_day_high = data.iloc[-1]['High']
    most_recent_day_low = data.iloc[-1]['Low']

    return [f"High: {most_recent_day_high}", f"Low: {most_recent_day_low}"]
