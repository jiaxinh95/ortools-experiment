# Creates the model
model = cp_model.CpModel()
 
# Creates the variables
x = model.NewIntVar(0, 10, 'x')
y = model.NewIntVar(0, 10, 'y')
z = model.NewIntVar(0, 10, 'z')
 
# Create enforcement literals
a = model.NewBoolVar('a')
b = model.NewBoolVar('b')
c = model.NewBoolVar('c')
 
# Creates the constraints
model.Add(x > y).OnlyEnforceIf(a)
model.Add(y > z).OnlyEnforceIf(b)
model.Add(z > x).OnlyEnforceIf(c)
 
# Add assumptions
model.AddAssumptions([a, b, c])
 
# Creates a solver and solves.
solver = cp_model.CpSolver()
status = solver.Solve(model)
 
# Print solution.
print(f'Status = {solver.StatusName(status)}')
if status == cp_model.INFEASIBLE:
    # print infeasible boolean variables index
    print('SufficientAssumptionsForInfeasibility = 'f'{solver.SufficientAssumptionsForInfeasibility()}')
     
    # print infeasible boolean variables
    infeasibles = solver.SufficientAssumptionsForInfeasibility()
    for i in infeasibles:
        print('Infeasible constraint: %d' % model.GetBoolVarFromProtoIndex(i))
