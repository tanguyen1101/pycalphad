import calphad.libcalphadcpp as lcp

# Load thermodynamic database
maindb = lcp.Database("crfeni_mie.tdb")
if maindb == None:
	sys.exit("Failed to load database")

# Set equilibrium conditions
conds = lcp.evalconditions()
conds.statevars['T'] = 300
conds.statevars['P'] = 101325
conds.statevars['N'] = 1
conds.elements.append("FE")
conds.elements.append("NI")
conds.elements.append("CR")
conds.elements.append("VA")
conds.xfrac["NI"] = .08
conds.xfrac["CR"] = .18
conds.phases["HCP_A3"] = lcp.PhaseStatus.ENTERED
conds.phases["BCC_A2"] = lcp.PhaseStatus.ENTERED
conds.phases["FCC_A1"] = lcp.PhaseStatus.ENTERED
conds.phases["LIQUID"] = lcp.PhaseStatus.ENTERED
conds.phases["SIGMA"] = lcp.PhaseStatus.ENTERED

# Build the minimization engine
eqfact = lcp.EquilibriumFactory()
if eqfact == None:
	sys.exit("Failed to build EquilibriumFactory")

# Construct equilibrium
myeq = eqfact.create(maindb, conds)

# Show result
print myeq


