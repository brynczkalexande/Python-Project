counter = 0
answer = 'y'
while answer == 'Y' or answer == 'y':
  smallest = 10
  highest = 0
  total = 0
  for i in range(5):
    score = float(input("Enter a score" ))
    while score < 0 or score > 10:
      print 'Invalid score. Try again.'
      score = float(input("Enter a score"))
    if score < smallest:
      smallest = score
    if score > highest:
      highest = score
    total += score
    print "The smallest score is", smallest, "The greatest score is", highest
      
  average = (total - highest - smallest)/3
  print average
  counter = counter + 1
  answer = input("Do you want to have another entry?")
  print  'The number of entries is', counter
  overallaverage = 0
  overallaverage += average
  findaverage = 0
  findaverage = overallaverage / counter
  print 'The overall average is', findaverage