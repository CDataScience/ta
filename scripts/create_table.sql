CREATE TABLE IF NOT EXISTS stock_history (
    date DATE,
    open FLOAT,
    high FLOAT,
    low FLOAT,
    close FLOAT,
    volume INTEGER,
    dividends FLOAT,
    stock_splits FLOAT
);