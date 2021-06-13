import readability_v_ks

#SpaCy is from this file if need to use class this is where and how to import as above as well
nlp = readability_v_ks.spacy.load('en_core_web_sm')
nlp.add_pipe('readability')

print('')
print('For the sentence:')
print('I am some really difficult text to read because I use obnoxiously large words.')
doc = nlp("I am some really difficult text to read because I use obnoxiously large words.")
print(doc._.flesch_kincaid_grade_level)
print(doc._.flesch_kincaid_reading_ease)
print(doc._.dale_chall)
print(doc._.smog)
print(doc._.coleman_liau_index)
print(doc._.automated_readability_index)
print(doc._.forcast)
print('')

print('For the sentence:')
print("The heart's upper chambers (atria) beat out of coordination with the lower chambers (ventricles).\
	This condition may have no symptoms, but when symptoms do appear they include palpitations, shortness of breath, and fatigue.\
	Treatments include drugs, electrical shock (cardioversion), and minimally invasive surgery (ablation).)")
doc = nlp("The heart's upper chambers (atria) beat out of coordination with the lower chambers (ventricles).\
	This condition may have no symptoms, but when symptoms do appear they include palpitations, shortness of breath, and fatigue.\
	Treatments include drugs, electrical shock (cardioversion), and minimally invasive surgery (ablation).)")
print(doc._.flesch_kincaid_grade_level)
print(doc._.flesch_kincaid_reading_ease)
print(doc._.dale_chall)
print(doc._.smog)
print(doc._.coleman_liau_index)
print(doc._.automated_readability_index)
print(doc._.forcast)