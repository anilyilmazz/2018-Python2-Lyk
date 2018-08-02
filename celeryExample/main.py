from celeryExample.background import multiple,parse_date

multiple.delay(10,10)
parse_date.delay("merhaba dunya")

