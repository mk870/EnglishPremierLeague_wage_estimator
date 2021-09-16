
from flask import Flask,render_template,request,url_for
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

@app.route('/home',methods=['GET','POST'])

def home():
  with open('soccer.pkl','rb') as f:
    model = pickle.load(f)

  if request.method == 'POST':
    Age = int(request.form['age'])
    Height = float(request.form['height'])
    Weight = float(request.form['weight'])
    Skill = int(request.form['skill'])
    International_rating = int(request.form['International_rating'])
    Rating = int(request.form['Rating'])
    Ball_control = int(request.form['ball_control'])
    Agility = int(request.form['agility'])
    Stamina = int(request.form['stamina'])
    Mentality = int(request.form['mentality'])
    Physic = int(request.form['physic'])
    Value = int(request.form['value'])
    On_loan = (request.form['On_loan'])
    if(On_loan == 'yes'):
      On_loan = 1
    else:
      On_loan = 0
    Remaining_contract_years = float(request.form['Remaining_contract_years'])
    Years_in_the_club = float(request.form['years_in_the_club'])

    Team_Arsenal = (request.form['team'])
    if (Team_Arsenal == 'Arsenal'):
      Team_Arsenal = 1
    else:
      Team_Arsenal = 0

    Team_AstonVilla = (request.form['team'])
    if (Team_AstonVilla == 'Aston villa'):
      Team_AstonVilla = 1
    else:
      Team_AstonVilla = 0

    Team_Brighton = (request.form['team'])
    if (Team_Brighton == 'Brighton & Hove Albion'):
      Team_Brighton = 1
    else:
      Team_Brighton = 0

    Team_Burnley = (request.form['team'])
    if (Team_Burnley == 'Burnley'):
      Team_Burnley = 1
    else:
      Team_Burnley = 0

    Team_Chelsea = (request.form['team'])
    if (Team_Chelsea == 'Chelsea'):
      Team_Chelsea = 1
    else:
      Team_Chelsea = 0

    Team_CrystalPalace = (request.form['team'])
    if (Team_CrystalPalace == 'Crystal palace'):
      Team_CrystalPalace = 1
    else:
      Team_CrystalPalace = 0

    Team_Everton = (request.form['team'])
    if (Team_Everton == 'Everton'):
      Team_Everton = 1
    else:
      Team_Everton = 0

    Team_Fulham = (request.form['team'])
    if (Team_Fulham == 'Fulham'):
      Team_Fulham = 1
    else:
      Team_Fulham = 0

    Team_LeedsUnited = (request.form['team'])
    if (Team_LeedsUnited == 'Leeds United'):
      Team_LeedsUnited = 1
    else:
      Team_LeedsUnited = 0

    Team_LeciesterCity = (request.form['team'])
    if (Team_LeciesterCity == 'Leicester City'):
      Team_LeciesterCity = 1
    else:
      Team_LeciesterCity = 0

    Team_Liverpool = (request.form['team'])
    if (Team_Liverpool == 'Liverpool'):
      Team_Liverpool = 1
    else:
      Team_Liverpool = 0

    Team_ManchesterCity = (request.form['team'])
    if (Team_ManchesterCity == 'manchestercity'):
      Team_ManchesterCity = 1
    else:
      Team_ManchesterCity = 0

    Team_ManchesterUnited = (request.form['team'])
    if (Team_ManchesterUnited == 'manchesterunited'):
      Team_ManchesterUnited = 1
    else:
      Team_ManchesterUnited = 0

    Team_NewcastleUnited = (request.form['team'])
    if (Team_NewcastleUnited == 'Newcastle United'):
      Team_NewcastleUnited = 1
    else:
      Team_NewcastleUnited = 0

    Team_SheffieldUnited = (request.form['team'])
    if (Team_SheffieldUnited == 'Sheffield United'):
      Team_SheffieldUnited = 1
    else:
      Team_SheffieldUnited = 0

    Team_Southampton = (request.form['team'])
    if (Team_Southampton == 'Southampton'):
      Team_Southampton = 1
    else:
      Team_Southampton = 0

    Team_TottenhamHotspur = (request.form['team'])
    if (Team_TottenhamHotspur == 'Tottenham'):
      Team_TottenhamHotspur = 1
    else:
      Team_TottenhamHotspur = 0

    Team_WestBromwichAlbion = (request.form['team'])
    if (Team_WestBromwichAlbion == 'West brom'):
      Team_WestBromwichAlbion = 1
    else:
      Team_WestBromwichAlbion = 0

    Team_WestHamUnited = (request.form['team'])
    if (Team_WestHamUnited == 'West ham'):
      Team_WestHamUnited = 1
    else:
      Team_WestHamUnited = 0

    Team_WolverhamptonWanderers = (request.form['team'])
    if (Team_WolverhamptonWanderers =='Wolverhampton'):
      Team_WolverhamptonWanderers = 1
    else:
      Team_WolverhamptonWanderers = 0 

    Position_CAM = (request.form['Position'])
    if (Position_CAM == '1'):
      Position_CAM = 1
    else:
      Position_CAM = 0

    Position_CB = (request.form['Position'])
    if (Position_CB == '2'):
      Position_CB = 1
    else:
      Position_CB = 0
    
    Position_CDM = (request.form['Position'])
    if (Position_CDM == '3'):
      Position_CDM = 1
    else:
      Position_CDM = 0

    Position_CF = (request.form['Position'])
    if (Position_CF == '4'):
      Position_CF = 1
    else:
      Position_CF = 0
    
    Position_CM = (request.form['Position'])
    if (Position_CM == '5'):
      Position_CM = 1
    else:
      Position_CM = 0
    
    Position_GK = (request.form['Position'])
    if (Position_GK == '6'):
      Position_GK = 1
    else:
      Position_GK = 0
    
    Position_LB = (request.form['Position'])
    if (Position_LB == '7'):
      Position_LB = 1
    else:
      Position_LB = 0

    Position_LM = (request.form['Position'])
    if (Position_LM == '8'):
      Position_LM = 1
    else:
      Position_LM = 0

    Position_LW = (request.form['Position'])
    if (Position_LW == '9'):
      Position_LW = 1
    else:
      Position_LW = 0
    
    Position_LWB = (request.form['Position'])
    if (Position_LWB == '10'):
      Position_LWB = 1
    else:
      Position_LWB = 0
    
    Position_RB = (request.form['Position'])
    if (Position_RB == '11'):
      Position_RB = 1
    else:
      Position_RB = 0
    
    Position_RM = (request.form['Position'])
    if (Position_RM == '12'):
      Position_RM = 1
    else:
      Position_RM = 0

    Position_RW = (request.form['Position'])
    if (Position_RW == '13'):
      Position_RW = 1
    else:
      Position_RW = 0
    
    Position_RWB = (request.form['Position'])
    if (Position_RWB == '14'):
      Position_RWB = 1
    else:
      Position_RWB = 0

    Position_ST = (request.form['Position'])
    if (Position_ST == '15'):
      Position_ST = 1
    else:
      Position_ST = 0
    arr = np.array([[Age,Height,Weight,Skill,International_rating,Rating,Ball_control,Agility,Stamina,Mentality,Physic,Value,On_loan,Remaining_contract_years,Years_in_the_club,Team_Arsenal,Team_AstonVilla,Team_Brighton,Team_Burnley,Team_Chelsea,Team_CrystalPalace,Team_Everton,Team_Fulham,Team_LeedsUnited,Team_LeciesterCity,Team_Liverpool,Team_ManchesterCity,Team_ManchesterUnited,Team_NewcastleUnited,Team_SheffieldUnited,Team_Southampton,Team_TottenhamHotspur,Team_WestBromwichAlbion,Team_WestHamUnited,Team_WolverhamptonWanderers,Position_CAM,Position_CB,Position_CDM,Position_CF,Position_CM,Position_GK,Position_LB,Position_LM,Position_LW,Position_LWB,Position_RB,Position_RM,Position_RW,Position_RWB,Position_ST]])

    prediction=model.predict(arr)
    output = np.round_(prediction,2)
    return render_template('index.html',prediction_text="This player earns {} Euros per week".format(output))
  else:
    return render_template('index.html')

if __name__== "__main__":
  app.run(debug = True)