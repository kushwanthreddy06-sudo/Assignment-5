from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Create Bayesian Network
model = BayesianNetwork([
    ('Disease', 'Fever'),
    ('Disease', 'Cough')
])

# CPD for Disease
cpd_disease = TabularCPD(
    variable='Disease',
    variable_card=2,
    values=[[0.7], [0.3]]
)

# CPD for Fever
cpd_fever = TabularCPD(
    variable='Fever',
    variable_card=2,
    values=[
        [0.9, 0.2],
        [0.1, 0.8]
    ],
    evidence=['Disease'],
    evidence_card=[2]
)

# CPD for Cough
cpd_cough = TabularCPD(
    variable='Cough',
    variable_card=2,
    values=[
        [0.8, 0.3],
        [0.2, 0.7]
    ],
    evidence=['Disease'],
    evidence_card=[2]
)

# Add CPDs
model.add_cpds(
    cpd_disease,
    cpd_fever,
    cpd_cough
)

# Check Model
print(model.check_model())

# Inference
infer = VariableElimination(model)

result = infer.query(
    variables=['Disease'],
    evidence={
        'Fever': 1,
        'Cough': 1
    }
)

print(result)
