import requests
response = requests.post('http://localhost:3030/family-benchmark_rich_background/sparql', data={
    'query': 'SELECT ?s  { ?s <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.benchmark.org/family#Brother>}'})
# Adding brackets
results = {'<'+i['s']['value']+'>' for i in response.json()['results']['bindings']}
print(results)