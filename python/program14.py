import csv
field_name=['No','company','car model']
car=[
    {'No':1,'company':'ferrari','car model': 'GH'},
    {'No':2,'company':'Bmw','car model': 'X5'},
    {'No':3,'company':'Maruti suzuki','car model': 'swift'},
    {'No':4,'company':'Audi','car model': 'Rs7'},
    {'No':5,'company':'Toyota','car model': 'Fortuner'}
]
with open('car.csv','w',newline='') as csvfile:
          write=csv.DictWriter(csvfile,fieldnames=field_name)
          write.writeheader()
          write.writerows(car)
with open('car.csv',newline='') as csvfile:
        d=csv.reader(csvfile)
        for r in d:
                print(','.join(r))