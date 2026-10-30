# add (a), add (b), remove (), add (c), remove (), remove (), 
# add (d), add (e), add (f), remove (), add (g), add (h), 
# remove (), remove (), remove (), add (i), remove (), size().


# Back --> Front
*     run 1 : = = = = = = = =
*     run 2 : = = = = = = = a
*     run 3 : = = = = = = b a
*     run 4 : = = = = = = b =
*     run 5 : = = = = = c b =
*     run 6 : = = = = = c = =
*     run 7 : = = = = = = = =
*     run 8 : = = = = d = = =
*     run 9 : = = = e d = = =
*     run 10 : = = f e d = = =
*     run 11 : = = f e = = = =
*     run 12 : = g f e = = = = 
*     run 13 : h g f e = = = =
*     run 14 : h g f = = = = =
*     run 15 : h g = = = = = =
*     run 16 : h = = = = = = =
*     run 17 : = = = = = = = =
*     run 18 : = = = = = = = i
*     run 19 : = = = = = = = =
0

methods, 
add_member
remove_member

attributes
frontQueue endQueue lengthQueue