#!/usr/bin/python

#a1 = 0
#a2 = 0
   
PM_H = 500.4
PM_M = 35.5
PM_L = 0.0
 
AQI_H = 500.0
AQI_M = 101.0
AQI_L = 0.0   

#H1 = 3.68
#M1 = 2.37
#L1 = 3.48

#H2 = 0.0 
#M2 = 0.0
#L2 = 0.0
 
numberOfAntAttributes = 2
#float matchingDegree[3]
#matchingDegree = [1.51, 1.51, 1.51]
#matchingDegree = array.array('f', [1,0,0])  
#trainedMatchingDegree = array.array('f', [1,0,0]) 
#float trainedMatchingDegree[3]; 
#trainedMatchingDegree = [1.51, 1.51, 1.51]
relativeWeight = 1.0 
#totalWeight = 0
#consequentBeliefDegree = array.array('f', [1,0,0,0,1,0,0,0,1])   
#consequentBeliefDegree=[] 
#consequentBeliefDegree = [9]   
  
# Differential Evolution
cbd_0 = 1.0
cbd_1 = 0.0
cbd_2 = 0.0
cbd_3 = 0.0
cbd_4 = 1.0
cbd_5 = 0.0
cbd_6 = 0.0
cbd_7 = 0.0
cbd_8 = 1.0

# Differential Evolution

#beliefDegreeChangeLevel = 0 
#float activationWeight[9]
#activationWeight = array.array('f', [1,0,0])
#activationWeight = [1.51, 1.51, 1.51]
#ruleWiseBeliefDegreeSum = array.array('f', [1,0,0,1,0,0,1,0,0])
#float ruleWiseBeliefDegreeSum[9];  
#ruleWiseBeliefDegreeSum = [1.51, 1.51, 1.51]
#string line
#string cnn_mild
#string cnn_nominal
#string cnn_severe
#counter = 0
#normalized_cnn_severe_degree = 1
#normalized_cnn_mild_degree = 1
#normalized_cnn_nominal_degree = 1
#cnn_pm25 = 1
#aggregatedBeliefDegreeH = 1
#aggregatedBeliefDegreeM = 1
#aggregatedBeliefDegreeL = 1
#finalAggregatedBeliefDegreeH = 1.0
#finalAggregatedBeliefDegreeM = 1.0 
#finalAggregatedBeliefDegreeL = 1.0
#brbH = 0
#brbM = 0
#brbL = 0
#aqi = 1
aqi1 = 1.0
aqi2 = 1.0 
aqi3 = 1.0
aqi4 = 1.0 
aqi5 = 1.0
#aqi6 = 1.0       
 
def ruleBase():             
    global consequentBeliefDegree
    consequentBeliefDegree = [cbd_0, cbd_1, cbd_2, cbd_3, cbd_4, cbd_5, cbd_6, cbd_7, cbd_8]

def transformInput1(i): 
    global H1
    global M1
    global L1
    
    if (i >= PM_H): 
        H1 = 1 
        M1 = 0
        L1 = 0

    elif (i == PM_M):
        H1 = 0 
        M1 = 1
        L1 = 0

    elif (i <= PM_L):
        H1 = 0
        M1 = 0
        L1 = 1
       
    elif (i <= PM_H) and (i >= PM_M):
        M1 = (PM_H-i)/(PM_H-PM_M)
        H1 = 1 - M1
        L1 = 0.0 

    elif (i <= PM_M) and (i >= PM_L):
        L1 = (PM_M-i)/(PM_M-PM_L)
        M1 = 1 - L1  
        H1 = 0.0
    
    #print("H1 is ")
    #print(H1)      
       
def takeInput(): 
    temp_a1 = input("Insert value for PM2.5 (between 0 and 500.4 µg/m3): ")   
    a1 = float(temp_a1)   
    transformInput1(a1) 
    #transformInput2(a2)  
     
#def showTransformedInput():
    #cout<< endl << "Transformed Input is as follow." << endl
    #cout<< "PM2.5 = {(H, " << H1 << "); (M, " << M1 << "); (L, " << L1 << ")}" << endl
    #cout<< "AQI = {(H, " << H2 << "); (M, " << M2 << "); (L, " << L2 << ")}" << endl  

   
def calculateMatchingDegreeBrbCnn():
    increment = 0   
    global matchingDegree 
    matchingDegree = [1.51, 1.51, 1.51]
    
    global trainedMatchingDegree
    trainedMatchingDegree = [1.51, 1.51, 1.51]

    ti1 = [H1, M1, L1] 
    #print("ti1[0] is ")
    #print(ti1[0])
    #ti2 = array.array('f', [normalized_cnn_severe_degree, normalized_cnn_mild_degree, normalized_cnn_nominal_degree])
    ti2 = [normalized_cnn_severe_degree, normalized_cnn_mild_degree, normalized_cnn_nominal_degree]
    #print("ti2[0] is ")
    #print(ti1[0]) 
    #print("\n ti2[1] is ") 
    #print(ti1[1])
    #print("\n ti2[2] is ")  
    #print(ti1[2])   
       
    for c in range(3): 
        #print(ti1[c])
        matchingDegree[increment] = (ti1[c] ** relativeWeight) * (ti2[c] ** relativeWeight) 
        trainedMatchingDegree[increment] = (ti1[c] ** relativeWeight) + (ti2[c] ** relativeWeight)
        #print("matchingDegree value is ")
        #print(matchingDegree[increment])
        #print("trainedMatchingDegree value is ")
        #print(trainedMatchingDegree[increment])
        increment +=1  
    
def showMatchingDegree():
    track = 1 
    #cout << endl << "Matching degrees of the rules are as follow." << endl; 
    for counter in range(9):
        track+=1   
  
def showActivationWeight():  
    trace = 1       
    totalWeight = 0 #to be fixed 10.2.2019
    totalActivationWeight = 0  
    global activationWeight 
    activationWeight = [1.51, 1.41, 1.45]       
    temp_activationWeight = [1.57, 1.81, 1.92]  
    for x in range(3):  
        totalWeight += matchingDegree[x]         
     
    for counter in range(3):           
        inter = trainedMatchingDegree[counter] 
        temp_activationWeight[counter] = inter/totalWeight  
        
    for naw in range(3):
        totalActivationWeight += temp_activationWeight[naw]        
    
    for fin in range(3):
        activationWeight[fin] = temp_activationWeight[fin]/totalActivationWeight
        #print("activationWeight[fin] is ")
        #print(activationWeight[fin])   
  
def takeCnnOutput():
    
    global normalized_cnn_severe_degree 
    global normalized_cnn_mild_degree
    global normalized_cnn_nominal_degree
    
    parser = 0
    f = open("cnn_prediction.txt", "r") #cnn output
    #f = open("cnn_prediction1.txt", "r") #severe 408      
    #f = open("cnn_prediction2.txt", "r") #nominal 36
    #f = open("cnn_prediction3.txt", "r") #mild 117
    if f.mode == 'r':
        #print("reading cnn_prediction.txt file \n") 
        f1 = f.readlines()  
        for line in f1:  
            if parser == 0: 
                cnn_mild = line
                #print(cnn_mild)
            elif parser == 1:
                cnn_nominal = line
                #print(cnn_nominal) 
            else: 
                cnn_severe = line
                #print(cnn_severe) 
            parser +=1    
        f.close()    
    else:
        print("Unable to open the file.");
            
    a = float(cnn_mild)
    b = float(cnn_nominal) 
    c = float(cnn_severe)     
    
    mild_degree = a/100    
    nominal_degree = b/100 
    severe_degree = c/100
    
    sum_degree = severe_degree + mild_degree + nominal_degree
  
    normalized_cnn_severe_degree = severe_degree/sum_degree
    normalized_cnn_mild_degree = mild_degree/sum_degree      
    normalized_cnn_nominal_degree = nominal_degree/sum_degree       
    
    if ((normalized_cnn_severe_degree > normalized_cnn_mild_degree) and (normalized_cnn_severe_degree > normalized_cnn_nominal_degree)):
        cnn_pm25 = (150.5 + 349.9*normalized_cnn_severe_degree) + ((150.4*normalized_cnn_mild_degree)/2)
        print ("PM2.5 computed by CNN: ",cnn_pm25," µg/m3")  

    elif ((normalized_cnn_nominal_degree > normalized_cnn_mild_degree) and (normalized_cnn_nominal_degree > normalized_cnn_severe_degree)):       
        cnn_pm25 = (35.4*(1 - normalized_cnn_nominal_degree)) + ((150.4*normalized_cnn_mild_degree)/2)            
        print ("PM2.5 computed by CNN: ",cnn_pm25," µg/m3")   

    elif ((normalized_cnn_mild_degree > normalized_cnn_severe_degree) and (normalized_cnn_mild_degree > normalized_cnn_nominal_degree)):    
        if normalized_cnn_severe_degree > normalized_cnn_nominal_degree: 
            cnn_pm25 = (35.5 + 114.9*normalized_cnn_mild_degree) + ((500.4*normalized_cnn_severe_degree)/2)
            print ("PM2.5 computed by CNN: ",cnn_pm25," µg/m3")  
            
        elif (normalized_cnn_nominal_degree > normalized_cnn_severe_degree): 
            cnn_pm25 = (35.5 + 114.9*normalized_cnn_mild_degree) + ((35.4*normalized_cnn_nominal_degree)/2)     
            print ("PM2.5 computed by CNN: ",cnn_pm25," µg/m3")
      
    #cout << endl << "CNN-generated Belief Degree for Severe Pollution: " << normalized_cnn_severe_degree << endl;       
    #cout << "CNN-generated Belief Degree for Mild Pollution: " << normalized_cnn_mild_degree << endl;   
    #cout << "CNN-generated Belief Degree for Nominal Pollution: " << normalized_cnn_nominal_degree << endl;     
 
def updateBeliefDegree():
    update = 0
    sumAntAttr1 = 1
    sumAntAttr2 = 1  
    
    if (H1 + M1 + L1) < 1:
        sumAntAttr1 = H1 + M1 + L1
        update = 1 
     
    if (normalized_cnn_severe_degree + normalized_cnn_mild_degree + normalized_cnn_nominal_degree) < 1:
        sumAntAttr2 = normalized_cnn_severe_degree + normalized_cnn_mild_degree + normalized_cnn_nominal_degree
        update = 1 
     
    if update == 1:
        beliefDegreeChangeLevel = (sumAntAttr1 + sumAntAttr2)/numberOfAntAttributes 
        #cout << "Belief Degree Level = " << beliefDegreeChangeLevel << endl
        for go in range(9):
            consequentBeliefDegree[go] = beliefDegreeChangeLevel * consequentBeliefDegree[go]
            #cout << "Updated Consequent Belief Degree : " << consequentBeliefDegree[go] << endl         
    else: 
        print ("No upgradation of belief degree required.") 
 
def aggregateER_BrbCnn():  
    parse = 0
    move1 = 0 
    move2 = 1  
    move3 = 2 
    action1 = 0
    action2 = 1
    action3 = 2 
    
    global ruleWiseBeliefDegreeSum 
    ruleWiseBeliefDegreeSum = [1.51, 1.51, 1.51]
    
    part11 = 1.51
    part12 = 1.51
    part13 = 1.51
    
    part1 = 1.0
    part2 = 1.0
    value = 1.0
    meu = 1.0
    
    numeratorH1 = 1.0
    numeratorH2 = 1.0
    numeratorH = 1.0
    denominatorH1 = 1.0
    denominatorH = 1.0
    
    numeratorM1 = 1.0
    numeratorM = 1.0
    
    numeratorL1 = 1.0
    numeratorL = 1.0
     
    utilityScoreH = 1.0
    utilityScoreM = 0.5
    utilityScoreL = 0.0
    crispValue = 1.0
    degreeOfIncompleteness = 1.0
    utilityMax = 1.0 
    utilityMin = 1.0
    utilityAvg = 1.0
     
    for t in range(3): 
        parse = t * 3   
        ruleWiseBeliefDegreeSum[t] = consequentBeliefDegree[parse] + consequentBeliefDegree[parse+1] + consequentBeliefDegree[parse+2]
 
    for rule in range(3):  
        part11 *= (activationWeight[rule] * consequentBeliefDegree[move1] + 1 - (activationWeight[rule] * ruleWiseBeliefDegreeSum[rule]))         
        move1 += 3 
  
    for rule in range(3):
        part12 *= (activationWeight[rule] * consequentBeliefDegree[move2] + 1 - (activationWeight[rule] * ruleWiseBeliefDegreeSum[rule]))        
        move2 += 3 
 
    for rule in range(3):
        part13 *= (activationWeight[rule] * consequentBeliefDegree[move3] + 1 - (activationWeight[rule] * ruleWiseBeliefDegreeSum[rule]))        
        move3 += 3

    part1 = (part11 + part12 + part13)
    
    for rule in range(3):
        part2 *= (1 - (activationWeight[rule] * ruleWiseBeliefDegreeSum[rule])) 
    
    value = part1 - part2 # to be noted 10.2
    
    meu = 1/value #to be noted 10.2 
 
    for rule in range(3):
        numeratorH1 *= (activationWeight[rule] * consequentBeliefDegree[action1] + 1 - (activationWeight[rule] * ruleWiseBeliefDegreeSum[rule]))        
        action1 += 3

    for rule in range(3):
        numeratorH2 *= (1 - (activationWeight[rule] * ruleWiseBeliefDegreeSum[rule]))              
      
    numeratorH = meu * (numeratorH1 - numeratorH2) 
    
    for rule in range(3): 
        denominatorH1 *= (1 - activationWeight[rule])        
 
    denominatorH = 1 - (meu * denominatorH1)
    
    aggregatedBeliefDegreeH = (numeratorH/denominatorH)
    #cout << endl << "ER Aggregated Belief Degree for Severe Pollution: " << aggregatedBeliefDegreeH << endl
    
    for rule in range(3):
        numeratorM1 *= (activationWeight[rule] * consequentBeliefDegree[action2] + 1 - (activationWeight[rule] * ruleWiseBeliefDegreeSum[rule]))        
        action2 += 3 

    numeratorM = meu * (numeratorM1 - numeratorH2) 
    aggregatedBeliefDegreeM = (numeratorM/denominatorH)  
    #cout << "ER Aggregated Belief Degree for Mild Pollution: " << aggregatedBeliefDegreeM << endl
    
    for rule in range(3):
        numeratorL1 *= (activationWeight[rule] * consequentBeliefDegree[action3] + 1 - (activationWeight[rule] * ruleWiseBeliefDegreeSum[rule]))        
        action3 += 3
     
    numeratorL = meu * (numeratorL1 - numeratorH2)
    aggregatedBeliefDegreeL = (numeratorL/denominatorH) 
    #cout << "ER Aggregated Belief Degree for Nominal Pollution: " << aggregatedBeliefDegreeL << endl;    
    
    if (aggregatedBeliefDegreeH + aggregatedBeliefDegreeM + aggregatedBeliefDegreeL) == 1:
        crispValue = (aggregatedBeliefDegreeH * utilityScoreH) + (aggregatedBeliefDegreeM * utilityScoreM) + (aggregatedBeliefDegreeL * utilityScoreL)
        #cout << "Crisp or numerical value is: " << crispValue << endl;        
        brbH = aggregatedBeliefDegreeH
        brbM = aggregatedBeliefDegreeM
        brbL = aggregatedBeliefDegreeL       
        
        print ("\n BRB-CNN integrated Belief Degree for Hazardous AQI: ",aggregatedBeliefDegreeH,"\n")
        print ("\n BRB-CNN integrated Belief Degree for Unhealthy AQI: ",aggregatedBeliefDegreeM,"\n")
        print ("\n BRB-CNN integrated Belief Degree for Good AQI: ",aggregatedBeliefDegreeL,"\n")
        #cout << "brbH: " << brbH << " brbM: " << brbM << " brbL: " << brbL <<endl;    
 
    else:         
        degreeOfIncompleteness = 1 - (aggregatedBeliefDegreeH + aggregatedBeliefDegreeM + aggregatedBeliefDegreeL)
        #cout << "Usassigned Degree of Belief: " << degreeOfIncompleteness << endl; 
        
        utilityMax = ((aggregatedBeliefDegreeH + degreeOfIncompleteness) * utilityScoreH + (aggregatedBeliefDegreeM*utilityScoreM) + (aggregatedBeliefDegreeL*utilityScoreL))
        
        utilityMin = (aggregatedBeliefDegreeH*utilityScoreH) + (aggregatedBeliefDegreeM*utilityScoreM) + (aggregatedBeliefDegreeL + degreeOfIncompleteness) * utilityScoreL
        
        utilityAvg = (utilityMax + utilityMin)/2 
        
        #cout << "Maximum expected utility: " << utilityMax << endl
        #cout << "Minimum expected utility: " << utilityMin << endl; 
        #cout << "Average expected utility: " << utilityAvg << endl; 
        print ("BRB-CNN integrated Belief Degrees considering degree of Incompleteness: ")  
        
        finalAggregatedBeliefDegreeH = aggregatedBeliefDegreeH/(aggregatedBeliefDegreeH + aggregatedBeliefDegreeM + aggregatedBeliefDegreeL)  
         
        finalAggregatedBeliefDegreeM = aggregatedBeliefDegreeM/(aggregatedBeliefDegreeH + aggregatedBeliefDegreeM + aggregatedBeliefDegreeL)
        
        finalAggregatedBeliefDegreeL = aggregatedBeliefDegreeL/(aggregatedBeliefDegreeH + aggregatedBeliefDegreeM + aggregatedBeliefDegreeL)
                
        
        #cout << endl << "BRB-CNN integrated Belief Degree for Hazardous AQI: " << finalAggregatedBeliefDegreeH << endl; 
        #cout << "BRB-CNN integrated Belief Degree for Unhealthy AQI: " << finalAggregatedBeliefDegreeM << endl; 
        #cout << "BRB-CNN integrated Belief Degree for Good AQI: " << finalAggregatedBeliefDegreeL << endl << endl; 
          
        brbH = finalAggregatedBeliefDegreeH
        brbM = finalAggregatedBeliefDegreeM 
        brbL = finalAggregatedBeliefDegreeL    
           
        #cout << "brbH: " << brbH << " brbM: " << brbM << " brbL: " << brbL <<endl
        if (finalAggregatedBeliefDegreeH > finalAggregatedBeliefDegreeM) and (finalAggregatedBeliefDegreeH > finalAggregatedBeliefDegreeL):
            aqi = (201 + 299*finalAggregatedBeliefDegreeH) + ((200*finalAggregatedBeliefDegreeM)/2)
            print ("AQI predicted by BRB-CNN:",aqi)    
            
        elif (finalAggregatedBeliefDegreeL > finalAggregatedBeliefDegreeM) and (finalAggregatedBeliefDegreeL > finalAggregatedBeliefDegreeH): 
            aqi = (100*(1 - finalAggregatedBeliefDegreeL)) + ((200*finalAggregatedBeliefDegreeM)/2) 
            print ("AQI predicted by BRB-CNN:",aqi)
  
        elif (finalAggregatedBeliefDegreeM > finalAggregatedBeliefDegreeH) and (finalAggregatedBeliefDegreeM > finalAggregatedBeliefDegreeL):
            if finalAggregatedBeliefDegreeH > finalAggregatedBeliefDegreeL:
                aqi = (101 + 99*finalAggregatedBeliefDegreeM) + ((500*finalAggregatedBeliefDegreeH)/2)
                print ("AQI predicted by BRB-CNN: ",aqi)
      
            elif (finalAggregatedBeliefDegreeL > finalAggregatedBeliefDegreeH):   
                aqi = (101 + 99*finalAggregatedBeliefDegreeM) + ((100*finalAggregatedBeliefDegreeL)/2)
                print ("AQI predicted by BRB-CNN:",aqi)  
          
        if aqi >= 301:
            aqi6 = (aqi- 301)/199.0  

        elif (aqi >= 201)and (aqi <= 300):
            aqi6 = (aqi- 201)/99.0   

        elif (aqi >= 151)and (aqi <= 200):
            aqi6 = (aqi- 151)/49.0 

        elif((aqi >= 101)and (aqi <= 150)): 
            aqi6 = (aqi- 101)/49.0   

        elif((aqi >= 51)and (aqi <= 100)): 
            aqi6 = (aqi- 51)/49.0 

        elif(aqi <= 50):  
            aqi6 = (aqi/49.0)  
 
        #cout << "aqi6: " << aqi6 << endl  
        print ("BRB-CNN integrated Belief Degree for Hazardous AQI:",finalAggregatedBeliefDegreeH*aqi6)   
        print ("BRB-CNN integrated Belief Degree for Very Unhealthy AQI:",finalAggregatedBeliefDegreeH*(1-aqi6)) 
        print ("BRB-CNN integrated Belief Degree for Unhealthy AQI: ",finalAggregatedBeliefDegreeM*aqi6)
        print ("BRB-CNN integrated Belief Degree for Unhealthy (Sensitive Groups) AQI:",finalAggregatedBeliefDegreeM*(1-aqi6)) 
        print ("BRB-CNN integrated Belief Degree for Moderate AQI:",finalAggregatedBeliefDegreeL*aqi6) 
        print ("BRB-CNN integrated Belief Degree for Good AQI:",finalAggregatedBeliefDegreeL*(1-aqi6))  
   
def main():  
    ruleBase()   
    takeInput()  
    #showTransformedInput()      
    takeCnnOutput() 
    calculateMatchingDegreeBrbCnn() 
    #showMatchingDegree() 
    showActivationWeight()   
    updateBeliefDegree()    
    aggregateER_BrbCnn()

main() 