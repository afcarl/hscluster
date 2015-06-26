from nytnlp.common import spacy

# For more accurate timing, force spacy to load
spacy('foo bar', entity=True, tag=True, parse=False)


class Entity():
    def __init__(self, name, label):
        self.name = name.strip().lower()
        self.label = label

    def __eq__(self, other):
        return self.name == other.name and self.label == other.label

    def __hash__(self):
        return hash('_'.join([self.name, self.label]))

    def __repr__(self):
        return '{} ({})'.format(self.name, self.label)


class Document():
    def __init__(self, id, body, tokens):
        self.id = id
        self.body = body
        self.tokens = tokens

        res = spacy(body, entity=True, tag=True, parse=False)
        self.entities = [Entity(e.string, e.label_) for e in res.ents]

    def __repr__(self):
        if hasattr(self, 'cluster'):
            return '{}_{}'.format(self.cluster, self.id)
        return '{}'.format(self.id)