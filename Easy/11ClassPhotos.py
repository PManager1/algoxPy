# Two input array has height of studens wth red shirts and secnd with blue shirts.
# there wlll be equal no of studens wering red and blue shirs.
# all heights are positive
#Constratins of the phonto:   all red and blue studnes must be in the same row.
# phoeot must have exact two rows.
# rows shoudl have same no of studetns.
# students in the front row must be shorter than the students at the back. .
#
# Questoin; can we achieve this objective ?  True or False
# 739

def classPhoto(redAr,blueAr):
    print("red and blue before sorting",  redAr, blueAr )
    # find which array have highest the largest height from two arrays. do it by sorting of each arrays.
    # redAr = rredAr.sort(reverse=True)
    # blueAr = bblueAr.sort(reverse=True)

    redAr.sort(reverse=True)
    blueAr.sort(reverse=True)

    print("sorted red and blue ",  redAr, blueAr )
    # print("first element of Red  ",  redAr[0] )
    # if ( r)
    pass




redShirt = [5,8,1,3,4];
blueShirt = [6,4,2,4,5];
classPhoto(redShirt,blueShirt)
# Very easy.