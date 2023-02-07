import spacy

nlp = spacy.load("en_core_web_trf")
ruler = nlp.add_pipe("entity_ruler")
patterns = [{"label": "ORG", "pattern": "MyCorp Inc."}, {"label": "FUCK", "pattern": "王博伟"}]
ruler.add_patterns(patterns)

doc = nlp("MyCorp Inc. is a company in the U.S, which is owned by 王博伟")
print([(ent.text, ent.label_) for ent in doc.ents])
