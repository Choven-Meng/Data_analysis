#question: For a given animal find frequency of all the attributes 
#DATA
#class_id  animal_id    attributes
#   1        21         walk, talk, sleep
#   1        22         eat, sleep
#   1        21         cry,laugh, sleep
#   1        21         dance, cook, walk

from collections import Counter
cluster_attribites=pd.DataFrame({'attribute_frequency' : data.groupby('animal_id').apply(
    lambda x: str(Counter([item for sublist in [i.split(',') for i in list(data['attributes'])] for item in sublist])))}).reset_index()
    
#output:    animal_id	       attribute_frequency
#         0	  21	            Counter({' sleep': 3, 'walk': 1, ' talk': 1, '...
#         1	  22	            Counter({' sleep': 3, 'walk': 1, ' talk': 1, '...
