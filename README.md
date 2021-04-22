# CountryInsights

This API offers to get geleral info about different countries by typing the city that is located there.
You can get Name of Country, Native Name, Capital, Numeric Code, Actual Population, 
Languages (Name, ISO-639-1, ISO-639-2), Currencies (Name, Code, Symbol) and All Cities.

Project built on Django Rest Framework with using open-source external API's to to build project's database.

## How to deploy:
```
- Download Repository
git clone https://github.com/DiamondWrist/CountryInsights.git

- Install Requirements
pip install -r requirements.txt
```

****OPTIONAL****:
If you want to work with your own local backend you need to update database with actual info. 
I built custom terminal command to make this process a bit easier. 

```
python manage.py initcountry
```

Then, you have to uncomment ****api_url variable in madgicx_geo.py**** with local API address.
(My External API work on Heroku)

After installing all requirement packages you can run madgicx_geo.py file to get info on the desired country.

## EXAMPLE:

```
python madgicx_geo.py city1, city2, ...
```
```
Request and Response Example:

% python madgicx_geo.py Vilnius

Request City: Vilnius
-------------------------------
Country: Lithuania
Native Name: Lietuva
Numeric Code: 440
Population: 2872294 people
Capital: Vilnius

Language(-es): 
 - Name: Lithuanian
 - Native Name: lietuvių kalba
 - ISO-639-1: lt
 - ISO-639-2: lit

Currency(-ies): 
 - Name: Euro
 - Code: EUR
 - Symbol: €

Cities: 
Alytus,Anciskiai,Antakalnis,Garliava,Ignalina,Jonava,Jurbarkas,Juskonys,Kaunas,Kretinga,Mastaiciai,
Palanga,Panevezys,Sakiai,Salcininkai,Trakai,Ukmerge,Uzliedziai,Venta,Vievis,Vilniaus Apskritis,Vilnius,Visaginas
```

