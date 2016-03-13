# Pokemon69
Moteur de recherche intelligent de points d'intérêts (POI)

A partir d'une ville et d'un métier, on récupere les données des API de Facebook et Yelp, on les merge, et affiche :)

Lecon : la doc de facebook est horrible, vive yelp qui honore la paypal mafia, python toujours aussi plaisant, on aurait besoin de machine learning par rapport à toutes les variables dispo, peu de data. On s'est fait plaisir :)

# Installation
## For back
```
git clone
pip install Flask
pip install yelp
pip install flask-cors
pip install facebook-sdk
```

Add your Yelp key in yelp.json
Update your Facebook access_token in api.py
`python podium.py`

URL : /search?city=Lyon&job=Artiste

## For front
Change URL of back
`npm install`
`npm start -s`
