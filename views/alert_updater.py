# import alerts
from models.alert import Alert

# Instantiate and get all alerts
alerts = Alert.all()

# loop through all alerts
for alert in alerts:
    # tell it what price to find
    alert.load_item_price()
    # notify if the price is reached
    alert.notify_price_reached()

# Do something if there are no alerts found
if not alerts:
    print("There's no alerts")
