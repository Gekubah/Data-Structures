#script of available cars and their prices in dollars
#import numpy as np
C={
   'Volvo':82000,
   'Ford':72000,
   'Toyota':88000,
   'Audi':85000,
   'BMW':100000,
   'Volkswagen':90000,
   'Mercedes-Benz':92000,
   'Renault':91000,
   'Peugeot':120000,
   'Honda':95000,
   'Hyundai':98000,
   'Hummer':200000,
   'Jaguar':300000,
   'Jeep':99000,
   'land Rover':87000,
  'Lexus':130000,
  'Nissan':97000,
  'Porsche':135000,
  'Rolls-Royce':300000,
  'Suzuki':89000,
  'Spyker':125000,
  'Reynard':115000,
  'Rezvani':155000,
  'Pantha':250000,
  'Pagani':320000,
  'Opel':300000,
  'Lloyd':290000,
  'Lombardi':288000,
  'Lamborghini':165000,
  }


#input for car name
carName=input('which car is of interest to you:')
if carName in C:
    carPrice=C[carName]
    print(f'the price of {carName} is {carPrice}.')
    
else: 
    print('this car is not available')

   


   
   
    

  
 