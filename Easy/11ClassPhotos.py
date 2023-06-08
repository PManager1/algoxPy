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
    redAr.sort(reverse=True)
    blueAr.sort(reverse=True)

    print("sorted red and blue ",  redAr, blueAr )
    if ( redAr[0] > blueAr[0]) :
        back = redAr;
        ahead = blueAr;
    else:
        back = blueAr;
        ahead = redAr;

    for i, val in enumerate(back):
        print("back [i],ahead[i]",back [i],ahead[i])
        if( back [i] > ahead[i] ): continue
        else:
            return False;
    return True;






redShirt = [5,8,1,3,4];
blueShirt = [6,9,2,4,5];
res = classPhoto(redShirt,blueShirt)
print("res = ", res);
# Very easy.