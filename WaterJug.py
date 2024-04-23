def pour(juga,jugb):
max1, max2, fill = 5,7,4
print("%d \t %d" % (juga,jugb))
if jugb == fill:
return
elif jugb == max2:
pour(0, juga)
elif juga != 0 and jugb == 0:
pour(0, juga)
elif juga == fill :
pour(juga,0)
elif juga<max1:
pour(max1, jugb)
elif juga< (max2- jugb):
pour(0,(juga + jugb))
else :
pour(juga-(max2-jugb),(max2-jugb)+jugb)
print("Jug A \t Jug B")
pour(0,0)