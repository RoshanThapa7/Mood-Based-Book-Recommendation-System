from graphviz import Digraph

dot = Digraph()

dot.node('A', 'User Interaction')
dot.node('B', 'Mood Detection System')
dot.node('C', 'Web Integration')
dot.node('D', 'Book Recommendation System')
dot.node('E', 'Database & Storage')

dot.edges(['AB', 'BC', 'CD', 'DE'])

dot.render('block_diagram', format='png', view=True)
