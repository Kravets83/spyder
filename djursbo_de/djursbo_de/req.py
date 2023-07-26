import requests


req = requests.get('https://djursbo.dk/selskabs-og-afdelingshjemmesider/djursbo/afdelinger/tendrupvej-ballesvej/?StepBack=true')

print(req.text)