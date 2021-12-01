from Groups import *
from Site import Site
def populate():
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
    disabledGroup_Suvery1 = Group1(site1,site2,site3,site4,site5,site6)

    controlGroup_Survey2 = Group2(site7,site8,site9,site4,site5,site6)
    abledGroup_Survey2 = Group2(site7,site8,site9,site4,site5,site6)
    disabledGroup_Survey2 = Group2(site7,site8,site9,site4,site5,site6)

    controlGroup_Survey3 = Group3(site1,site2,site3,site4,site5,site6,site7,site8,site9,site10,site11,site12)
    abledGroup_Survey3 = Group3(site1,site2,site3,site4,site5,site6,site7,site8,site9,site10,site11,site12)
    disabledGroup_Survey3 = Group3(site1,site2,site3,site4,site5,site6,site7,site8,site9,site10,site11,site12)



if __name__ == '__main__':
    populate()
    print('-----------------Welcome--------------------')
    print('Hello! Welcome and thank you for being part of our research')
    print('Please choose your role: ')
    print('1. Participant')
    print('2. Researcher')
    role = int(input())
    if role == 1:
        print('Please input experiment number: ')
        experimentNumber = int(input())
        print('Please input group number: ')
        groupNumber = int(input())
    elif (role == 2):
        print('Please input password: ')
        password = input()
        if (password == '1234'):
            print('Welcome researcher')
        else:
            print('Wrong password')


