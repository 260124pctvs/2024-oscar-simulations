import random 
from tqdm import tqdm 
from math import log
winners = []
top_choices = []
for x in tqdm(range(10000)):

  #simulate academy
  academy = range(1,9500)
  derp = [random.randint(-24,24),random.randint(-21,24),random.randint(-24,24),random.randint(-24,24),random.randint(-24,24),random.randint(-24,24),random.randint(-24,24),random.randint(-24,24),random.randint(-24,24),random.randint(-16,24)]
  picture_votes = []
  for voter in academy:
    american_fiction = ["American Fiction",8+log(33.1+derp[0]) + random.random()]
    anatomy_of_a_fall = ["Anatomy of a Fall",8+log(22.3+derp[1]) + random.random()]
    barbie = ["Barbie",8+log(39.5+derp[2]) + random.random()]
    the_holdovers = ["The Holdovers",8+log(50.5+derp[3]) + random.random()]
    killers_of_the_flower_moon = ["Killers of the Flower Moon",8+log(43.4+derp[4]) + random.random()]
    maestro = ["Maestro",8+log(26.5+derp[5]) + random.random()]
    oppenheimer = ["Oppenheimer",8+log(82.1+derp[6]) + random.random()]
    past_lives = ["Past Lives",8+log(29+derp[7]) + random.random()]
    poor_things = ["Poor Things",8+log(41+derp[8]) + random.random()]
    the_zone_of_interest = ["The Zone of Interest",8+log(16.5+derp[9]) + random.random()]
    rank = []
    rankalg = 10
    while rankalg > 0:	
      floor = 0
      amf = american_fiction[1] + floor
      floor = amf
      ana = floor + anatomy_of_a_fall[1]
      floor = ana
      bar = floor + barbie[1]
      floor = bar
      hol = floor + the_holdovers[1]
      floor = hol
      kil = floor + killers_of_the_flower_moon[1]
      floor = kil
      mae = floor + maestro[1]
      floor = mae
      opp = floor + oppenheimer[1]
      floor = opp
      pas = floor + past_lives[1]
      floor = pas
      pot = floor + poor_things[1]
      floor = pot
      zon = floor + the_zone_of_interest[1]
      floor = zon
      
      vote = random.uniform(0,floor)
      if vote < amf:
        rank.append(american_fiction[0])
        american_fiction[1] = 0
      elif vote < ana:
        rank.append(anatomy_of_a_fall[0])
        anatomy_of_a_fall[1] = 0
      elif vote < bar:
        rank.append(barbie[0])
        barbie[1] = 0
      elif vote < hol:
        rank.append(the_holdovers[0])
        the_holdovers[1] = 0
      elif vote < mae:
        rank.append(maestro[0])
        maestro[1] = 0
      elif vote < opp:
        rank.append(oppenheimer[0])
        oppenheimer[1] = 0
      elif vote < pot:
        rank.append(poor_things[0])
        poor_things[1] = 0
      elif vote < pas:
        rank.append(past_lives[0])
        past_lives[1] = 0
      elif vote < zon:
        rank.append(the_zone_of_interest[0])
        the_zone_of_interest[1] = 0
      rankalg = rankalg - 1
    picture_votes.append(rank)	
    top_choices.append(rank[0])	
  k = 1
  #picture_votes2 = picture_votes
  #+while k < 100:
  #	print picture_votes2.pop()
  #	k = k + 1


  #run algo
  nowinner = True
  eliminated = []
  while nowinner:
    amfcount = 0
    anacount = 0
    barcount = 0
    holcount = 0
    kilcount = 0
    maecount = 0
    oppcount = 0
    potcount = 0
    pascount = 0
    zoncount = 0
    for j in picture_votes:
      #print j[0]
      if len(j) > 0:
        if j[0] == "American Fiction":
          amfcount = amfcount + 1
        elif j[0] == "Anatomy of a Fall":
          anacount = anacount + 1
        elif j[0] == "Barbie":
          barcount = barcount + 1
        elif j[0] == "The Holdovers":
          holcount = holcount + 1
        elif j[0] == "Killers of the Flower Moon":
          kilcount = kilcount + 1
        elif j[0] == "Maestro":
          maecount = maecount + 1
        elif j[0] == "Oppenheimer":
          oppcount = oppcount + 1
        elif j[0] == "Poor Things":
          potcount = potcount + 1
        elif j[0] == "Past Lives":
          pascount = pascount + 1
        elif j[0] == "The Zone of Interest":
          zoncount = zoncount + 1
    maximum = max(amfcount,anacount,barcount,holcount,kilcount,maecount,oppcount,potcount,pascount,zoncount)
    list_movies = [amfcount,anacount,barcount,holcount,kilcount,maecount,oppcount,potcount,pascount,zoncount]
    for i in eliminated:
      if i == "American Fiction":
        list_movies[0] = 200000
      elif i == "Anatomy of a Fall":
        list_movies[1] = 200000
      elif i == "Barbie":
        list_movies[2] = 200000
      elif i == "The Holdovers":
        list_movies[3] = 200000
      elif i == "Killers of the Flower Moon":
        list_movies[4] = 200000
      elif i == "Maestro":
        list_movies[5] = 200000
      elif i == "Oppenheimer":
        list_movies[6] = 200000
      elif i == "Poor Things":
        list_movies[7] = 200000
      elif i == "Past Lives":
        list_movies[8] = 200000
      elif i == "The Zone of Interest":
        list_movies[9] = 200000
    minimum = min(list_movies)
    eliminate = ""
    #print maximum
    #print minimum
    if maximum > 50:
      if amfcount == maximum:
        winners.append("American Fiction")
      elif anacount == maximum:
        winners.append("Anatomy of a Fall")
      elif barcount == maximum:
        winners.append("Barbie")
      elif holcount == maximum:
        winners.append("The Holdovers")
      elif kilcount == maximum:
        winners.append("Killers of the Flower Moon")
      elif maecount == maximum:
        winners.append("Maestro")
      elif oppcount == maximum:
        winners.append("Oppenheimer")
      elif potcount == maximum:
        winners.append("Poor Things")
      elif pascount == maximum:
        winners.append("Past Lives")
      elif zoncount == maximum:
        winners.append("The Zone of Interest")
      nowinner = False
    else:	
      if amfcount == minimum:
        eliminate = "American Fiction"
        eliminated.append(eliminate)
      elif anacount == minimum:
        eliminate = "Anatomy of a Fall"
        eliminated.append(eliminate)
      elif barcount == minimum:
        eliminate = "Barbie"
        eliminated.append(eliminate)
      elif holcount == minimum:
        eliminate = "The Holdovers"
        eliminated.append(eliminate)	
      elif kilcount == minimum:
        eliminate = "Killers of the Flower Moon"
        eliminated.append(eliminate)
      elif maecount == minimum:
        eliminate = "Maestro"
        eliminated.append(eliminate)
      elif oppcount == minimum:
        eliminate = "Oppenheimer"
        eliminated.append(eliminate)
      elif potcount == minimum:
        eliminate = "Poor Things"
        eliminated.append(eliminate)
      elif pascount == minimum:
        eliminate = "Past Lives"
        eliminated.append(eliminate)
      elif zoncount == minimum:
        eliminate = "The Zone of Interest"
        eliminated.append(eliminate)
      for e in picture_votes:
        if eliminate in e:
          e.remove(eliminate)
        if len(e) == 0:
          del e

print("American Fiction " + str(winners.count("American Fiction")))
print("Anatomy of a Fall " + str(winners.count("Anatomy of a Fall")))
print("Barbie " + str(winners.count("Barbie")))
print("The Holdovers " + str(winners.count("The Holdovers")))
print("Killers of the Flower Moon " + str(winners.count("Killers of the Flower Moon")))
print("Maestro " + str(winners.count("Maestro")))
print("Oppenheimer " + str(winners.count("Oppenheimer")))
print("Poor Things " + str(winners.count("Poor Things")))
print("Past Lives " + str(winners.count("Past Lives")))
print("The Zone of Interest " + str(winners.count("The Zone of Interest")))


print("first choices")
print("American Fiction " + str(top_choices.count("American Fiction")/950000.0)+"%")
print("Anatomy of a Fall " + str(top_choices.count("Anatomy of a Fall")/950000.0)+"%")
print("Barbie " + str(top_choices.count("Barbie")/950000.0)+"%")
print("The Holdovers " + str(top_choices.count("The Holdovers")/950000.0)+"%")
print("Killers of the Flower Moon " + str(top_choices.count("Killers of the Flower Moon")/950000.0)+"%")
print("Maestro " + str(top_choices.count("Maestro")/950000.0)+"%")
print("Oppenheimer " + str(top_choices.count("Oppenheimer")/950000.0)+"%")
print("Poor Things " + str(top_choices.count("Poor Things")/950000.0)+"%")
print("Past Lives " + str(top_choices.count("Past Lives")/950000.0)+"%")
print("The Zone of Interest " + str(top_choices.count("The Zone of Interest")/950000.0)+"%")
