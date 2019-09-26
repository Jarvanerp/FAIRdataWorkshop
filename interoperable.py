import rdflib

g=rdflib.Graph()
k=rdflib.Graph()

g.parse('uniprotP01892.ttl', format='n3')
k.parse('Q96NZ1.rdf', format='xml')


same_subject = []
same_predicate = []
same_object = []

same_subject_predicate = []
same_predcate_object = []
same_triple = []

for s,p,o in g:
    for s1, p1, o1 in k:
        if s == s1:
            same_subject.append(s)
        if p == p1:
            same_predicate.append(p)
        if o == o1:
            same_object.append(o)
        if s == s and p == p1:
            same_subject_predicate.append([[s, p], o, o1])
        if o == o1 and p == p1:
            same_predcate_object.append([s, s1,[p, o]])
        if o == o1 and p == p1 and s == s1:
            same_triple.append([s, p , o])

# print('same subject')
# print(same_subject)
# print('\n\nsame predicate')
# print(same_predicate)
# print('\n\nsame object')
# print(same_object)

# print('\n\nsame predicate object')
# print(same_predcate_object)
# print('\n\nsame subject predicate')
# print(same_subject_predicate)

print(same_predcate_object)