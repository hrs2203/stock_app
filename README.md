# DB schema

## models
- User
  - user ID
  - User name
  - Email
  - password

- Company
  - company Id
  - company Name
  - company type
  - unit stock price

- Stock Detail
  - Foreign key -> owning company
  - Foreign key -> owning user
  - qty  

- Transaction
  - Foreign key -> user Id
  - Foreign key -> company Id

- Notice Board
  - stores stock that are for sale
  - stock company name
  - stock qty avail for sale
  - unit stock price


## Stock API used
- received format
  - JSON
- Alpha Vantage
  - limitation, 5 req per min, 500 per day


## Features
- TOP GAINERS
- TOP LOSERS
- TOP ACTIVE

- GLOBAL INDICES
  - WEEKLY, MONTHLY DAILY

- EVENTS: (ONLY COMPANIES CAN CREATE)

- COMPANY:

- USER:
  -PORTFOLIO
  -WATCHLIST
  -FRIENDS/CONNECTIONS
  -CHATBOX
  
-EXTRA FEATURES:
  -IF YOU HAD INVESTED
  -CURRENCY CONVERTER(FOREX)
  -FIND BROKER  
