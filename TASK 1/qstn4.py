sample = {'physics':88 ,  'maths':75,  'chemistry':72, 'Basic electrical':89 }

key_max = max(sample.keys(), key=(lambda k: sample[k]))
key_min = min(sample.keys(), key=(lambda k: sample[k]))

print('Maximum Value: ',sample[key_max])
print('Minimum Value: ',sample[key_min])       
           


