from Groups import *
from Site import Site
from Surveys import *

#3 site-uri responsive
site1 = Site('S1', False, True)
site2 = Site('S2', False, True)
site3 = Site('S3', False, True)

#3 site-uri unresponsive and unaccessbile
site4 = Site('S4', False, False)
site5 = Site('S5', False, False)
site6 = Site('S6', False, False)

#3 site-uri accesible
site7 = Site('S7', True, False)
site8 = Site('S8', True, False)
site9 = Site('S9', True, False)

#3 site-uri responsive and accesible
site10 = Site('S10', True, True)
site11 = Site('S11', True, True)
site12 = Site('S12', True, True)

controlGroup_Survey1 = Group1(site1,site2,site3,site4,site5,site6)
abledGroup_Survey1 = Group1(site1,site2,site3,site4,site5,site6)
disabledGroup_Survey1 = Group1(site1, site2, site3, site4, site5, site6)

controlGroup_Survey2 = Group2(site7,site8,site9,site4,site5,site6)
abledGroup_Survey2 = Group2(site7,site8,site9,site4,site5,site6)
disabledGroup_Survey2 = Group2(site7,site8,site9,site4,site5,site6)

controlGroup_Survey3 = Group3(site1,site2,site3,site4,site5,site6,site7,site8,site9,site10,site11,site12)
abledGroup_Survey3 = Group3(site1,site2,site3,site4,site5,site6,site7,site8,site9,site10,site11,site12)
disabledGroup_Survey3 = Group3(site1,site2,site3,site4,site5,site6,site7,site8,site9,site10,site11,site12)

survey1 = Survey1(controlGroup_Survey1, abledGroup_Survey1, disabledGroup_Survey1)
survey2 = Survey2(controlGroup_Survey2, abledGroup_Survey2, disabledGroup_Survey2)
survey3 = Survey3(controlGroup_Survey3, abledGroup_Survey3, disabledGroup_Survey3)



def survey1Questions():

    print('Welcome to the survey. You have previously been asked to interact with 6 sites. You are not going to be asked to'
          'answer a few questions about them. Be as honest as possible. Responses are anonimous.')
    print('Did you prefer to navigate on the computer or on the mobile device? \n 1. Computer \n 2.Mobile Device')
    prefered = int(input())
    print('Out of the 6 sites you were asked to interact with, which ones do you consider to be responsive? Please input their numbers one by one. When finished input 0')
    responsive = int(input())
    while responsive:
        responsive = int(input())
    print('If you could only interact with one of these 6 sites, which one would you choose?')
    best = int(input())
    print('Briefly explain what you liked about this site')
    likes = input()
    print('Age: ')
    age = int(input())
    print('Region: ')
    region = input()
    print('Last education level \n 1. Highschool 2.Undergraduate 3. Postgraduate 4.PHD 5. Middleschool')
    educationLevel = int(input())
    print('Ocupation: \n 1.Student 2.Unemployed 3.Employed in the IT field 4. Employed in a non-IT field')
    ocupation = int(input())
    print('Do you know what responsive web design means? yes/no')
    knows = input()
    print('Please rate the sites in order of preffereance (1 - least prefered, 2- most preffered')
    site1 = int(input('Site1'))
    site2 = int(input('Site2'))
    site3 = int(input('Site3'))
    site4 = int(input('Site4'))
    site5 = int(input('Site5'))
    site6 = int(input('Site6'))
    print('Thank you for your answers')
    return prefered, best, likes, age, region, educationLevel, ocupation, knows, site1, site2, site3, site4, site5, site6
    #here run menu again

def manipulateInformation(information, group):
    global survey1
    att = getattr(survey1, 'group%d' % group)

    if(information[0] == 1):
        att.preferedPC +=1
    else:
        att.preferedMobile +=1

    bestSite = getattr(att, 'site%d' % information[1])
    att.bestSite.ChosenBest +=1

    bestSite.likes += information[2]

    att.age.append(information[3])

    att.region.append(information[4])

    if(information[5] == 'yes'):
        att.knows += 1

    att.site1.grade += site1
    att.site2.grade += site2
    att.site3.grade += site3
    att.site4.grade += site4
    att.site5.grade += site5
    att.site6.grade += site6


def main():
    print('-----------------Welcome--------------------')
    print('Hello! Welcome and thank you for being part of our research')
    print('Please choose your role: ')
    print('1. Participant')
    print('2. Researcher')
    role = int(input())
    global survey1
    if role == 1:
        print('Please input experiment number: ')
        experimentNumber = int(input())
        print('Please input group number: ')
        groupNumber = int(input())

        if experimentNumber == 1 and groupNumber == 1:
            gatheredInformation = survey1Questions()
            manipulateInformation(gatheredInformation, groupNumber)

            print('Raspunsuri salvate')
            print(survey1.group1.knows)
            print(survey1.group1.site1.grade)
            print(survey1.group1.site2.grade)
            print(survey1.group1.age)


        elif experimentNumber == 1 and groupNumber == 2:
            pass
        elif experimentNumber == 1 and groupNumber == 3:
            pass
        elif experimentNumber == 2 and groupNumber == 1:
            pass
        elif experimentNumber == 2 and groupNumber == 2:
            pass
        elif experimentNumber == 2 and groupNumber == 3:
            pass
        elif experimentNumber == 3 and groupNumber == 1:
            pass
        elif experimentNumber == 3 and groupNumber == 2:
            pass
        elif experimentNumber == 3 and groupNumber == 3:
            pass
    elif (role == 2):
        print('Please input password: ')
        password = input()
        if (password == '1234'):
            print('Welcome researcher')
        else:
            print('Wrong password')


main()