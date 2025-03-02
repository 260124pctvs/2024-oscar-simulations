import random 
from tqdm import tqdm 
from math import log
winners = []
top_choices = []
for x in tqdm(range(10000)):

  #simulate academy
  academy = range(1,9500)
  derp = [random.randint(-24,24),random.randint(-24,24),random.randint(-24,24),random.randint(-24,24),random.randint(-24,24),random.randint(-24,24),random.randint(1,24),random.randint(-15,24),random.randint(-23,24),random.randint(-24,24)]
  picture_votes = []
  for voter in academy:
    anora = ["Anora",8+log(188.8+derp[0]) + random.random()]
    a_complete_unknown = ["A Complete Unknown",8+log(38.2+derp[1]) + random.random()]
    the_brutalist = ["The Brutalist",8+log(43+derp[2]) + random.random()]
    conclave = ["Conclave",8+log(85.2+derp[3]) + random.random()]
    dune_part_two = ["Dune: Part Two",8+log(26.2+derp[4]) + random.random()]
    emilia_perez = ["Emilia Perez",8+log(34.4+derp[5]) + random.random()]
    im_still_here = ["I'm Still Here",8+log(0+derp[6]) + random.random()]
    nickel_boys = ["Nickel Boys",8+log(15.2+derp[7]) + random.random()]
    the_substance = ["The Substance",8+log(23.2+derp[8]) + random.random()]
    wicked = ["Wicked",8+log(29.6+derp[9]) + random.random()]
    rank = []
    rankalg = 10
    while rankalg > 0:	
      floor = 0
      ano = anora[1] + floor
      floor = ano
      acu = floor + a_complete_unknown[1]
      floor = acu
      bru = floor + the_brutalist[1]
      floor = bru
      con = floor + conclave[1]
      floor = con
      dun = floor + dune_part_two[1]
      floor = dun
      emi = floor + emilia_perez[1]
      floor = emi
      opp = floor + im_still_here[1]
      floor = opp
      nic = floor + nickel_boys[1]
      floor = nic
      sub = floor + the_substance[1]
      floor = sub
      wic = floor + wicked[1]
      floor = wic
      
      vote = random.uniform(0,floor)
      if vote < ano:
        rank.append(anora[0])
        anora[1] = 0
      elif vote < acu:
        rank.append(a_complete_unknown[0])
        a_complete_unknown[1] = 0
      elif vote < bru:
        rank.append(the_brutalist[0])
        the_brutalist[1] = 0
      elif vote < con:
        rank.append(conclave[0])
        conclave[1] = 0
      elif vote < emi:
        rank.append(emilia_perez[0])
        emilia_perez[1] = 0
      elif vote < opp:
        rank.append(im_still_here[0])
        im_still_here[1] = 0
      elif vote < sub:
        rank.append(the_substance[0])
        the_substance[1] = 0
      elif vote < nic:
        rank.append(nickel_boys[0])
        nickel_boys[1] = 0
      elif vote < wic:
        rank.append(wicked[0])
        wicked[1] = 0
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
    anocount = 0
    acucount = 0
    brucount = 0
    concount = 0
    duncount = 0
    emicount = 0
    oppcount = 0
    subcount = 0
    niccount = 0
    wiccount = 0
    for j in picture_votes:
      #print j[0]
      if len(j) > 0:
        if j[0] == "Anora":
          anocount = anocount + 1
        elif j[0] == "A Complete Unknown":
          acucount = acucount + 1
        elif j[0] == "The Brutalist":
          brucount = brucount + 1
        elif j[0] == "Conclave":
          concount = concount + 1
        elif j[0] == "Dune: Part Two":
          duncount = duncount + 1
        elif j[0] == "Emilia Perez":
          emicount = emicount + 1
        elif j[0] == "I'm Still Here":
          oppcount = oppcount + 1
        elif j[0] == "The Substance":
          subcount = subcount + 1
        elif j[0] == "Nickel Boys":
          niccount = niccount + 1
        elif j[0] == "Wicked":
          wiccount = wiccount + 1
    maximum = max(anocount,acucount,brucount,concount,duncount,emicount,oppcount,subcount,niccount,wiccount)
    list_movies = [anocount,acucount,brucount,concount,duncount,emicount,oppcount,subcount,niccount,wiccount]
    for i in eliminated:
      if i == "Anora":
        list_movies[0] = 200000
      elif i == "A Complete Unknown":
        list_movies[1] = 200000
      elif i == "The Brutalist":
        list_movies[2] = 200000
      elif i == "Conclave":
        list_movies[3] = 200000
      elif i == "Dune: Part Two":
        list_movies[4] = 200000
      elif i == "Emilia Perez":
        list_movies[5] = 200000
      elif i == "I'm Still Here":
        list_movies[6] = 200000
      elif i == "The Substance":
        list_movies[7] = 200000
      elif i == "Nickel Boys":
        list_movies[8] = 200000
      elif i == "Wicked":
        list_movies[9] = 200000
    minimum = min(list_movies)
    eliminate = ""
    #print maximum
    #print minimum
    if maximum > 50:
      if anocount == maximum:
        winners.append("Anora")
      elif acucount == maximum:
        winners.append("A Complete Unknown")
      elif brucount == maximum:
        winners.append("The Brutalist")
      elif concount == maximum:
        winners.append("Conclave")
      elif duncount == maximum:
        winners.append("Dune: Part Two")
      elif emicount == maximum:
        winners.append("Emilia Perez")
      elif oppcount == maximum:
        winners.append("I'm Still Here")
      elif subcount == maximum:
        winners.append("The Substance")
      elif niccount == maximum:
        winners.append("Nickel Boys")
      elif wiccount == maximum:
        winners.append("Wicked")
      nowinner = False
    else:	
      if anocount == minimum:
        eliminate = "Anora"
        eliminated.append(eliminate)
      elif acucount == minimum:
        eliminate = "A Complete Unknown"
        eliminated.append(eliminate)
      elif brucount == minimum:
        eliminate = "The Brutalist"
        eliminated.append(eliminate)
      elif concount == minimum:
        eliminate = "Conclave"
        eliminated.append(eliminate)	
      elif duncount == minimum:
        eliminate = "Dune: Part Two"
        eliminated.append(eliminate)
      elif emicount == minimum:
        eliminate = "Emilia Perez"
        eliminated.append(eliminate)
      elif oppcount == minimum:
        eliminate = "I'm Still Here"
        eliminated.append(eliminate)
      elif subcount == minimum:
        eliminate = "The Substance"
        eliminated.append(eliminate)
      elif niccount == minimum:
        eliminate = "Nickel Boys"
        eliminated.append(eliminate)
      elif wiccount == minimum:
        eliminate = "Wicked"
        eliminated.append(eliminate)
      for e in picture_votes:
        if eliminate in e:
          e.remove(eliminate)
        if len(e) == 0:
          del e

print("Anora " + str(winners.count("Anora")))
print("A Complete Unknown " + str(winners.count("A Complete Unknown")))
print("The Brutalist " + str(winners.count("The Brutalist")))
print("Conclave " + str(winners.count("Conclave")))
print("Dune: Part Two " + str(winners.count("Dune: Part Two")))
print("Emilia Perez " + str(winners.count("Emilia Perez")))
print("I'm Still Here " + str(winners.count("I'm Still Here")))
print("The Substance " + str(winners.count("The Substance")))
print("Nickel Boys " + str(winners.count("Nickel Boys")))
print("Wicked " + str(winners.count("Wicked")))


print("first choices")
print("Anora " + str(top_choices.count("Anora")/950000.0)+"%")
print("A Complete Unknown " + str(top_choices.count("A Complete Unknown")/950000.0)+"%")
print("The Brutalist " + str(top_choices.count("The Brutalist")/950000.0)+"%")
print("Conclave " + str(top_choices.count("Conclave")/950000.0)+"%")
print("Dune: Part Two " + str(top_choices.count("Dune: Part Two")/950000.0)+"%")
print("Emilia Perez " + str(top_choices.count("Emilia Perez")/950000.0)+"%")
print("I'm Still Here " + str(top_choices.count("I'm Still Here")/950000.0)+"%")
print("The Substance " + str(top_choices.count("The Substance")/950000.0)+"%")
print("Nickel Boys " + str(top_choices.count("Nickel Boys")/950000.0)+"%")
print("Wicked " + str(top_choices.count("Wicked")/950000.0)+"%")