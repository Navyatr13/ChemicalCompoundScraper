import spacy
from scispacy.linking import EntityLinker

nlp = spacy.load("en_core_sci_sm")
nlp.add_pipe("scispacy_linker", config={"linker_name": "umls"})

def extract_entities(text):
    """
    Extract chemical entities from a text using scispaCy.
    """
    doc = nlp(text)
    entities = []
    for ent in doc.ents:
        linked_entities = [link[0] for link in ent._.kb_ents]
        entities.append({
            "text": ent.text,
            "label": ent.label_,
            "linked_entities": linked_entities
        })
    return entities
