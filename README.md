# WAD_2_Group_6B_Project
SUPA Triple Rumble Tournament
Use Python 3.9.13

Open source used: 
  1. AdminLTE        https://github.com/ColorlibHQ/AdminLTE
  2. jquery          https://github.com/jquery/jquery
  3. bootstrap       https://github.com/twbs/bootstrap
  
Instruction Website:
  1. Simpleui        https://fengyuanchen.github.io/simpleui/

How to run the code (Mac OS):
  1. Access into the $cd .../WAD_2_Group_6B_Project/Tournament/
  2. $pip install -r requirement.txt
  3. $python3 manage.py makemigrations
  4. $python3 manage.py migrate
  5. $python3 population_script.py
  6. if 'DEBUG=True', then need execute '$python3 manage.py collectstatic'. Else, just skip this step.
  7. $python3 manage.py runserver

How to run the code (Windows OS):
  1.  check python version==3.9.13
  2.  create environment
  3.  activate environment
  4.  pip install -r requirement.txt
  5.  $python manage.py makemigrations
  6.  $python manage.py migrate
  7.  $python population_script.py
  8.  if 'DEBUG=True', then need execute '$python3 manage.py collectstatic'. Else, just skip this step.
  9.  $python manage.py runserver
