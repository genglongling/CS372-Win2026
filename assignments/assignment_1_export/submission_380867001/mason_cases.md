### **Case 6.85: Raising wages causes workers to become more productive.**

**Scenario.**  
 Firms that pay higher wages tend to exhibit higher labor productivity. A manager argues: “Raising wages causes workers to become more productive.”

**Variables.**  
 • X \= Wage level
 • Y \= Labor productivity
 • Z \= Worker skill level / capital intensity

**Annotations.**  
 • Case ID: 6.85  
 • Pearl Level: L1 (Association)  
 • Domain: Economics  
 • Trap Type: CONFOUNDING  
 • Trap Subtype: Omitted Variable (Human Capital)  
 • Difficulty: Medium  
 • Causal Structure: Z → X, Z → Y  
 • Key Insight: More skilled or capital-equipped workers both earn higher wages and produce more output.

**Hidden Timestamp.**  
 Did firms upgrade technology and workforce skills before wages increased?

**Conditional Answers.**  
 Answer if tZ \< tX. Skill accumulation (Z) raised both productivity (Y) and wages (X). The wage increase did not cause productivity.
 Answer if tX \< tZ. Higher wages (X) attracted more skilled workers (Z), raising productivity (Y).

**Wise Refusal.**  
 “Without controlling for worker skill and capital intensity, the wage–productivity correlation cannot be interpreted causally.”

---

### **Case 6.86: Reducing competition increases efficiency and profitability.**

**Scenario.**  
 Industries with higher market concentration display higher average profits. An analyst claims: “Reducing competition increases efficiency and profitability.”

**Variables.**  
 • X \= Market concentration
 • Y \= Average profit rate
 • Z \= Entry barriers / fixed cost intensity

**Annotations.**  
 • Case ID: 6.86  
 • Pearl Level: L1 (Association)  
 • Domain: Economics  
 • Trap Type: SELECTION  
 • Trap Subtype: Survivorship of High-Fixed-Cost Industries  
 • Difficulty: Medium  
 • Causal Structure: Z → X, Z → Y  
 • Key Insight: Industries with high fixed costs both deter entry and generate high margins for survivors.

**Hidden Timestamp.**  
 Did entry barriers and fixed costs rise before concentration increased?

**Conditional Answers.**  
 Answer if tZ \< tX. High fixed costs (Z) caused both high concentration (X) and high profits (Y). Concentration did not cause efficiency.
 Answer if tX \< tZ. Reduced competition (X) allowed firms to earn rents (Y), later inducing investment that raised entry barriers (Z).

**Wise Refusal.**  
 “Observed profits among concentrated industries reflect selection into high fixed-cost environments, not necessarily efficiency gains from reduced competition.”

---

### **Case 6.87: Encouraging saving will cause growth to accelerate.**

**Scenario.**  
 Economies with higher household saving rates tend to exhibit faster capital accumulation and output growth. A policymaker claims: “Encouraging saving will cause growth to accelerate.”

**Variables.**  
 • X \= Saving rate
 • Y \= Output growth
 • Z \= Time preference / demographic structure

**Annotations.**  
 • Case ID: 6.87  
 • Pearl Level: L1 (Association)  
 • Domain: Economics  
 • Trap Type: REVERSE  
 • Trap Subtype: Life-Cycle and Expectation Effects  
 • Difficulty: Medium  
 • Causal Structure: Z → X, Z → Y or Y → X  
 • Key Insight: Expectations of growth or demographics may drive both saving and investment.

**Hidden Timestamp.**  
 Did changes in demographics or growth expectations occur before saving rates increased?

**Conditional Answers.**  
 Answer if tZ \< tX. Anticipated income growth (Y) raised saving (X) via life-cycle planning.

**Wise Refusal.**  
 “The saving–growth correlation cannot establish that higher saving causes growth without identifying whether preferences or expectations shift first.”

---

### **Case 6.88: Lower interest rates cause firms to invest more.**

**Scenario.**  
 After a central authority lowers the policy interest rate, aggregate investment rises. A policymaker claims: “Lower interest rates cause firms to invest more.”

**Variables.**  
 • X \= Policy interest rate cut
 • Y \= Aggregate investment
 • Z \= Expected future demand / business cycle phase

**Annotations.**  
 • Case ID: 6.88  
 • Pearl Level: L2 (Intervention)  
 • Domain: Economics  
 • Trap Type: CONF-MED  
 • Trap Subtype: Expectation-Driven Confounding  
 • Difficulty: Hard  
 • Causal Structure: Z → X, Z → Y or X → Y  
 • Key Insight: Interest rates may respond to expected demand rather than drive it.

**Hidden Timestamp.**  
 Did expectations of higher future demand (Z) form before the interest rate cut (X)?

**Conditional Answers.**  
 Answer if tZ \< tX. Optimistic demand expectations (Z) increased desired investment (Y) and motivated the authority to cut rates (X). The rate cut coincided with, but did not cause, the investment boom.
 Answer if tX \< tZ. The rate cut (X) reduced the cost of capital, stimulating investment (Y), which later raised expectations (Z).

**Wise Refusal.**  
 “Without separating policy responses from private-sector expectations, the observed investment response cannot be causally attributed to the interest rate cut.”

---

### **Case 6.89: The price ceiling caused a shortage.**

**Scenario.**  
 After a binding price ceiling is imposed on a good, observed market quantity falls. A regulator concludes: “The price ceiling caused a shortage.”

**Variables.**  
 • X \= Price ceiling
 • Y \= Traded quantity
 • Z \= Demand shock

**Annotations.**  
 • Case ID: 6.89  
 • Pearl Level: L2 (Intervention)  
 • Domain: Economics  
 • Trap Type: CONF-MED  
 • Trap Subtype: Demand Shift Confounding  
 • Difficulty: Medium  
 • Causal Structure: Z → Y and possibly Z → X, or X → Y  
 • Key Insight: Quantity changes may reflect demand shifts rather than the policy constraint.

**Hidden Timestamp.**  
 Did the demand shock (Z) occur before the price ceiling (X) was introduced?

**Conditional Answers.**  
 Answer if tZ \< tX. A negative demand shock (Z) reduced quantity (Y), and the ceiling (X) was imposed in response. The policy did not cause the observed contraction.
 Answer if tX \< tZ. The ceiling (X) became binding, reducing supplied quantity and creating excess demand, lowering the traded quantity (Y).

**Wise Refusal.**  
 “To infer a causal shortage from the ceiling, one must establish that the policy, not a prior demand shift, is responsible for the quantity reduction.”

---

### **Case 6.90: More generous benefits reduce job-finding effort.**

**Scenario.**  
 When unemployment benefits are extended, the average duration of job search increases. A theorist claims: “More generous benefits reduce job-finding effort.”

**Variables.**  
 • X \= Benefit duration extension
 • Y \= Job search duration
 • Z \= Labor market tightness

**Annotations.**  
 • Case ID: 6.90  
 • Pearl Level: L2 (Intervention)  
 • Domain: Economics  
 • Trap Type: CONF-MED  
 • Trap Subtype: Cyclical Labor Demand  
 • Difficulty: Hard  
 • Causal Structure: Z → Y and Z → X, or X → Y  
 • Key Insight: Search duration responds to vacancy availability as well as incentives.

**Hidden Timestamp.**  
 Did labor market slack (Z) increase before the benefit extension (X)?

**Conditional Answers.**  
 Answer if tZ \< tX. A weak labor market (Z) lengthened job search (Y) and triggered the policy extension (X). The benefits did not cause longer unemployment.
 Answer if tX \< tZ. The extension (X) reduced search intensity, lengthening unemployment (Y), with labor market conditions (Z) adjusting later.

**Wise Refusal.**  
 “Without isolating policy timing from labor demand fluctuations, the causal effect of benefit generosity on search behavior cannot be identified.”

---

### **Case 6.91: The tax caused consumers to reduce their spending.**

**Scenario.**  
 After a proportional consumption tax is introduced, aggregate household spending falls. A policymaker argues: “The tax caused consumers to reduce their spending.”

**Variables.**  
 • X \= Consumption tax
 • Y \= Aggregate consumption
 • E \= Intertemporal income expectations

**Annotations.**  
 • Case ID: 6.91  
 • Pearl Level: L2 (Intervention)  
 • Domain: Economics  
 • Trap Type: CONF-MED  
 • Trap Subtype: Expectation Shock  
 • Difficulty: Medium  
 • Causal Structure: Z → Y and possibly Z → X, or X → Y  
 • Key Insight: Anticipated income changes can alter consumption independently of tax policy.

**Hidden Timestamp.**  
 Did households revise future income expectations (Z) before the tax (X) was enacted?

**Conditional Answers.**  
 Answer if tZ \< tX. A downward revision in expected income (Z) reduced consumption (Y) and prompted the government to raise revenue via the tax (X). The tax did not cause the spending decline.
 Answer if tX \< tZ. The tax (X) raised effective prices, inducing households to substitute toward saving and reduce consumption (Y), with expectations adjusting afterward.

**Wise Refusal.**  
 “Observed spending changes cannot be causally attributed to the tax without separating policy effects from shifts in income expectations.”

---

### **Case 6.92: The subsidy caused entry.**

**Scenario.**  
 When an output subsidy is introduced, the number of active firms in the market increases. A planner claims: “The subsidy caused entry.”

**Variables.**  
 • X \= Output subsidy
 • Y \= Number of firms
 • Z \= Profitability of technology

**Annotations.**  
 • Case ID: 6.92  
 • Pearl Level: L2 (Intervention)  
 • Domain: Economics  
 • Trap Type: CONF-MED  
 • Trap Subtype: Technology Shock  
 • Difficulty: Medium  
 • Causal Structure: Z → Y and Z → X, or X → Y  
 • Key Insight: Improvements in technology may drive both policy and entry.

**Hidden Timestamp.**  
 Did production technology become more profitable (Z) before the subsidy (X) was implemented?

**Conditional Answers.**  
 Answer if tZ \< tX. Higher profitability (Z) attracted entry (Y) and led to political support for the subsidy (X). The policy did not cause the increase in firms.
 Answer if tX \< tZ. The subsidy (X) raised expected profits, inducing new firms to enter (Y), and scale effects later improved technology (Z).

**Wise Refusal.**  
 “To infer a causal entry effect, one must establish that the subsidy preceded and was not merely a response to improved profitability.”

---

### **Case 6.93: Credit expansion causes asset price inflation.**

**Scenario.**  
 Following a relaxation of borrowing constraints, asset prices rise. A theorist claims: “Credit expansion causes asset price inflation.”

**Variables.**  
 • X \= Borrowing constraint relaxation
 • Y \= Asset prices
 • Z \= Expected future productivity

**Annotations.**  
 • Case ID: 6.93  
 • Pearl Level: L2 (Intervention)  
 • Domain: Economics  
 • Trap Type: CONF-MED  
 • Trap Subtype: Productivity Expectation Confounding  
 • Difficulty: Hard  
 • Causal Structure: Z → Y and Z → X, or X → Y  
 • Key Insight: Optimistic productivity beliefs can drive both credit conditions and prices.

**Hidden Timestamp.**  
 Did expectations of higher future productivity (Z) form before the credit policy change (X)?

**Conditional Answers.**  
 Answer if tZ \< tX. Productivity optimism (Z) increased asset demand (Y) and loosened lending standards (X). The policy did not cause the price boom.
 Answer if tX \< tZ. Relaxed constraints (X) increased leverage and demand for assets (Y), which later fueled optimism (Z).

**Wise Refusal.**  
 “Asset price responses cannot be attributed to credit policy without disentangling it from shifts in productivity expectations.”

---

### **Case 6.94: Trade liberalization caused wage inequality to rise.**

**Scenario.**  
 After import tariffs are reduced, wage dispersion between skilled and unskilled workers increases. A commentator claims: “Trade liberalization caused wage inequality to rise.”

**Variables.**  
 • X \= Tariff reduction
 • Y \= Wage inequality
 • Z \= Skill-biased technological change

**Annotations.**  
 • Case ID: 6.94  
 • Pearl Level: L2 (Intervention)  
 • Domain: Economics  
 • Trap Type: CONF-MED  
 • Trap Subtype: Technology–Policy Confounding  
 • Difficulty: Hard  
 • Causal Structure: Z → Y and Z → X, or X → Y  
 • Key Insight: Technological change can raise skill premia and simultaneously motivate trade reforms.

**Hidden Timestamp.**  
 Did the acceleration of skill-biased technology (Z) occur before the tariff reduction (X)?

**Conditional Answers.**  
 Answer if tZ \< tX. Technological change (Z) increased returns to skill, widening inequality (Y), and policymakers responded with liberalization (X). The policy did not cause the distributional shift.
 Answer if tX \< tZ. Lower tariffs (X) exposed low-skill sectors to competition, reducing their wages and increasing inequality (Y), with technology adoption (Z) following.

**Wise Refusal.**  
 “Without separating trade policy timing from technological trends, the rise in inequality cannot be causally attributed to liberalization.”

---

### **Case 6.95: Public investment caused productivity to rise.**

**Scenario.**  
 After a large increase in public infrastructure spending, economy-wide productivity growth accelerates. A planner claims: “Public investment caused productivity to rise.”

**Variables.**  
 • X \= Infrastructure investment
 • Y \= Productivity growth
 • Z \= Anticipated private-sector expansion

**Annotations.**  
 • Case ID: 6.95  
 • Pearl Level: L2 (Intervention)  
 • Domain: Economics  
 • Trap Type: CONF-MED  
 • Trap Subtype: Expectation-Driven Policy Response  
 • Difficulty: Medium  
 • Causal Structure: Z → X, Z → Y, or X → Y  
 • Key Insight: Governments may invest in anticipation of growth rather than cause it.

**Hidden Timestamp.**  
 Did expectations of private-sector expansion (Z) form before the public investment decision (X)?

**Conditional Answers.**  
 Answer if tZ \< tX. Anticipated expansion (Z) raised future productivity (Y) and justified the infrastructure program (X). The policy coincided with, but did not cause, the growth acceleration.
 Answer if tX \< tZ. Infrastructure spending (X) improved connectivity and reduced costs, raising productivity (Y) and later stimulating private expansion (Z).

**Wise Refusal.**  
 “Productivity improvements cannot be causally attributed to public investment without showing that policy preceded, rather than responded to, growth expectations.”

---

### **Case 6.96: Stricter regulation caused the credit contraction.**

**Scenario.**  
 After capital requirements for intermediaries are increased, credit growth slows. A regulator asserts: “Stricter regulation caused the credit contraction.”

**Variables.**  
 • X \= Higher capital requirements
 • Y \= Credit growth
 • Z \= Perceived systemic risk

**Annotations.**  
 • Case ID: 6.96  
 • Pearl Level: L2 (Intervention)  
 • Domain: Economics  
 • Trap Type: CONF-MED  
 • Trap Subtype: Risk-Driven Policy Endogeneity  
 • Difficulty: Hard  
 • Causal Structure: Z → X, Z → Y, or X → Y  
 • Key Insight: Rising risk can both reduce lending and trigger tighter regulation.

**Hidden Timestamp.**  
 Did perceptions of systemic risk (Z) increase before the regulatory tightening (X)?

**Conditional Answers.**  
 Answer if tZ \< tX. Heightened risk (Z) led banks to cut lending (Y) and motivated regulators to raise capital standards (X). The policy did not cause the slowdown.
 Answer if tX \< tZ. The tighter requirements (X) constrained balance sheets, reducing credit supply (Y), with risk perceptions (Z) adjusting afterward.

**Wise Refusal.**  
 “Without distinguishing regulatory responses from underlying risk conditions, the observed credit slowdown cannot be causally assigned to the policy change.”

---

### **Case 6.97: The quality regulation forced low-quality firms to exit.**

**Scenario.**  
 After a minimum quality standard is imposed, the number of active producers in the market declines. A policymaker claims: “The quality regulation forced low-quality firms to exit.”

**Variables.**  
 • X \= Minimum quality standard
 • Y \= Number of active firms
 • Z \= Increase in fixed compliance costs

**Annotations.**  
 • Case ID: 6.97  
 • Pearl Level: L2 (Intervention)  
 • Domain: Economics  
 • Trap Type: CONF-MED  
 • Trap Subtype: Cost Structure Confounding  
 • Difficulty: Medium  
 • Causal Structure: Z → Y and Z → X, or X → Y  
 • Key Insight: Rising compliance costs may drive exit regardless of the quality threshold itself.

**Hidden Timestamp.**  
 Did compliance and monitoring costs (Z) rise before the quality standard (X) was enforced?

**Conditional Answers.**  
 Answer if tZ \< tX. Higher compliance costs (Z) reduced firm profitability and caused exit (Y), prompting the authority to formalize the standard (X). The regulation did not cause the contraction.
 Answer if tX \< tZ. The quality standard (X) raised required production costs, forcing marginal firms to exit (Y), with compliance infrastructure (Z) expanding afterward.

**Wise Refusal.**  
 “Firm exit cannot be attributed to the quality standard without isolating its effect from pre-existing increases in compliance costs.”

---

### **Case 6.98: The tax caused firms to adopt cleaner technologies.**

**Scenario.**  
 Following the introduction of a carbon tax, average energy efficiency in production improves. An analyst claims: “The tax caused firms to adopt cleaner technologies.”

**Variables.**  
 • X \= Carbon tax
 • Y \= Energy efficiency
 • Z \= Technological progress in clean production

**Annotations.**  
 • Case ID: 6.98  
 • Pearl Level: L2 (Intervention)  
 • Domain: Economics  
 • Trap Type: CONF-MED  
 • Trap Subtype: Technology Trend Confounding  
 • Difficulty: Hard  
 • Causal Structure: Z → Y and Z → X, or X → Y  
 • Key Insight: Innovation trends may drive both policy adoption and efficiency gains.

**Hidden Timestamp.**  
 Did clean-technology breakthroughs (Z) occur before the carbon tax (X) was enacted?

**Conditional Answers.**  
 Answer if tZ \< tX. Advances in clean technology (Z) raised efficiency (Y) and made the tax (X) politically feasible. The efficiency gains are not primarily caused by the tax.
 Answer if tX \< tZ. The tax (X) increased the relative price of emissions, inducing firms to innovate and adopt cleaner technologies (Z), raising efficiency (Y).

**Wise Refusal.**  
 “Efficiency improvements cannot be causally attributed to the carbon tax without establishing that innovation did not precede and drive both policy and outcomes.”

---

### **Case 6.99: Monetary expansion caused inflation.**

**Scenario.**  
 After an expansion in the money supply, the general price level rises. A theorist asserts: “Monetary expansion caused inflation.”

**Variables.**  
 • X \= Money supply increase
 • Y \= Price level
 • Z \= Increase in transaction demand for money

**Annotations.**  
 • Case ID: 6.99  
 • Pearl Level: L2 (Intervention)  
 • Domain: Economics  
 • Trap Type: CONF-MED  
 • Trap Subtype: Endogenous Money Demand  
 • Difficulty: Medium  
 • Causal Structure: Z → X, Z → Y, or X → Y  
 • Key Insight: Rising transaction demand can raise both money supply and prices.

**Hidden Timestamp.**  
 Did transaction demand (Z) increase before the monetary expansion (X)?

**Conditional Answers.**  
 Answer if tZ \< tX. Higher transaction demand (Z) raised the need for money (X) and increased prices (Y). The expansion accommodated activity rather than caused inflation.
 Answer if tX \< tZ. The increase in money supply (X) exceeded demand, generating excess liquidity and pushing up prices (Y), with transaction volume (Z) responding later.

**Wise Refusal.**  
 “Inflation cannot be causally attributed to monetary expansion without distinguishing policy-driven supply from endogenous responses to money demand.”

---

### **Case 7.00: Training subsidies caused workers to switch jobs more frequently.**

**Scenario.**  
 After a government introduces subsidies for vocational training, job-to-job mobility increases. A policymaker claims: “Training subsidies caused workers to switch jobs more frequently.”

**Variables.**  
 • X \= Training subsidy
 • Y \= Job-to-job mobility
 • Z \= Expansion of high-skill vacancies

**Annotations.**  
 • Case ID: 7.00  
 • Pearl Level: L2 (Intervention)  
 • Domain: Economics  
 • Trap Type: CONF-MED  
 • Trap Subtype: Vacancy-Driven Confounding  
 • Difficulty: Medium  
 • Causal Structure: Z → Y and Z → X, or X → Y  
 • Key Insight: Labor demand shifts can raise both mobility and political support for training programs.

**Hidden Timestamp.**  
 Did the increase in high-skill vacancies (Z) occur before the training subsidy (X) was introduced?

**Conditional Answers.**  
 Answer if tZ \< tX. A surge in high-skill job openings (Z) increased worker mobility (Y) and led to the introduction of subsidies (X) to address skill shortages. The subsidy did not cause the mobility rise.
 Answer if tX \< tZ. The subsidy (X) raised workers’ skill levels, improving outside options and increasing mobility (Y), with firms later expanding vacancies (Z).

**Wise Refusal.**  
 “Without establishing whether labor demand or training policy moved first, the causal impact of subsidies on mobility cannot be identified.”

---

### **Case 7.01: Cheaper credit caused the building boom.**

**Scenario.**  
 Following the launch of a subsidized mortgage program, residential construction accelerates. A planner claims: “Cheaper credit caused the building boom.”

**Variables.**  
 • X \= Mortgage subsidy
 • Y \= Housing construction
 • Z \= Demographic shift toward household formation

**Annotations.**  
 • Case ID: 7.01  
 • Pearl Level: L2 (Intervention)  
 • Domain: Economics  
 • Trap Type: CONF-MED  
 • Trap Subtype: Demographic Demand Confounding  
 • Difficulty: Hard  
 • Causal Structure: Z → Y and Z → X, or X → Y  
 • Key Insight: Population and household formation trends may drive both policy and construction.

**Hidden Timestamp.**  
 Did the rise in household formation (Z) begin before the mortgage subsidy (X) was implemented?

**Conditional Answers.**  
 Answer if tZ \< tX. Increased household formation (Z) raised housing demand (Y) and motivated the introduction of the subsidy (X). The policy did not cause the construction boom.
 Answer if tX \< tZ. The subsidy (X) reduced borrowing costs, stimulating housing demand and construction (Y), with demographic responses (Z) following.

**Wise Refusal.**  
 “Housing supply responses cannot be causally attributed to credit policy without disentangling them from underlying demographic demand shifts.”

---

### **Case 7.02: The prize caused firms to invest more in R\&D.**

**Scenario.**  
 After a large innovation prize is announced, private research effort increases. An observer claims: “The prize caused firms to invest more in R\&D.”

**Variables.**  
 • X \= Innovation prize
 • Y \= Research effort
 • Z \= Expected profitability of new technology

**Annotations.**  
 • Case ID: 7.02  
 • Pearl Level: L2 (Intervention)  
 • Domain: Economics  
 • Trap Type: CONF-MED  
 • Trap Subtype: Profit Expectation Confounding  
 • Difficulty: Medium  
 • Causal Structure: Z → Y and Z → X, or X → Y  
 • Key Insight: Anticipated technological rents may drive both research and policy incentives.

**Hidden Timestamp.**  
 Did expectations of high technological profitability (Z) arise before the prize (X) was announced?

**Conditional Answers.**  
 Answer if tZ \< tX. Optimistic profit expectations (Z) increased R\&D investment (Y) and led policymakers to offer the prize (X). The prize did not cause the rise in research effort.
 Answer if tX \< tZ. The prize (X) raised the expected return to innovation, inducing greater research effort (Y), with profit expectations (Z) adjusting later.

**Wise Refusal.**  
 “Without establishing whether expected rents or the incentive itself moved first, the increase in R\&D cannot be causally attributed to the innovation prize.”

---

### **Case 7.03: If the authority had not announced this policy, prices would have exploded.**

**Scenario.**  
 A market exhibits stable prices after a regulatory authority announces that it will intervene if prices become volatile. A commentator claims: “If the authority had not announced this policy, prices would have exploded.”

**Variables.**  
 • X \= Announcement of potential price control (intervention)
 • Y \= Price stability (observed outcome)
 • Y′ \= Price outcome had the announcement not been made
 • Z \= Underlying supply–demand balance

**Annotations.**  
 • Case ID: 7.03  
 • Pearl Level: L3 (Counterfactual)  
 • Domain: Economics  
 • Trap Type: COUNTERFACTUAL  
 • Trap Subtype: Deterrence / Prevention Paradox  
 • Difficulty: Medium  
 • Causal Structure: X alters expectations; Z may already ensure stability  
 • Key Insight: The absence of instability does not prove the threat caused stability.

**Hidden Timestamp.**  
 Was the market already approaching equilibrium (Z) before the intervention was announced (X)?

**Conditional Answers.**  
 (Missing conditional answers.)

**Wise Refusal.**  
 “The claim relies on an unobserved counterfactual. Without evidence that instability was imminent, we cannot conclude that the announcement prevented a price explosion.”

---

### **Case 7.04: If Project B had been chosen, growth would have been much higher.**

**Scenario.**  
 A planner chooses Project A over Project B and observes moderate growth. The planner claims: “If Project B had been chosen, growth would have been much higher.”

**Variables.**  
 • X \= Choice of Project A (intervention)
 • Y \= Observed growth
 • Y′ \= Counterfactual growth under Project B
 • Z \= Sectoral productivity complementarities

**Annotations.**  
 • Case ID: 7.04  
 • Pearl Level: L3 (Counterfactual)  
 • Domain: Economics  
 • Trap Type: COUNTERFACTUAL  
 • Trap Subtype: Opportunity Cost / Structural Uncertainty  
 • Difficulty: Hard  
 • Causal Structure: Different projects interact differently with Z  
 • Key Insight: The unrealized project’s outcome is structurally unidentifiable.

**Hidden Timestamp.**  
 Would Project B have altered the evolution of sectoral complementarities (Z) relative to Project A?

**Conditional Answers.**  
 (Missing conditional answers.)

**Wise Refusal.**  
 “The growth that would have occurred under the unchosen project is fundamentally unobservable and depends on structural interactions that cannot be inferred from the realized path alone.”

---

### **Case 7.05: If a comprehensive unemployment insurance system had existed, the recession w...**

**Scenario.**  
 An economy experiences a mild downturn. A policy group argues: “If a comprehensive unemployment insurance system had existed, the recession would have been much shorter.”

**Variables.**  
 • X \= Presence of unemployment insurance (counterfactual intervention)
 • Y \= Duration of downturn
 • Y′ \= Downturn duration had unemployment insurance existed
 • Z \= Aggregate demand stabilization mechanisms

**Annotations.**  
 • Case ID: 7.05  
 • Pearl Level: L3 (Counterfactual)  
 • Domain: Economics  
 • Trap Type: COUNTERFACTUAL  
 • Trap Subtype: Policy Multiplier Uncertainty  
 • Difficulty: Medium  
 • Causal Structure: X affects Y through Z, but Z’s strength is unobserved  
 • Key Insight: The stabilizing effect of missing institutions is model-dependent.

**Hidden Timestamp.**  
 Would automatic stabilizers (Z) have activated early enough to influence the downturn trajectory?

**Conditional Answers.**  
 (Missing conditional answers.)

**Wise Refusal.**  
 “The counterfactual impact of an unimplemented insurance system depends on the strength of demand-stabilization channels, which cannot be verified from the realized history alone.”

---

### **Case 7.06: If the economy had adopted a fixed exchange rate regime, output volatility wo...**

**Scenario.**  
 An economy experiences volatile output following a sequence of external shocks. A theorist claims: “If the economy had adopted a fixed exchange rate regime, output volatility would have been much lower.”

**Variables.**  
 • X \= Adoption of fixed exchange rate regime (counterfactual intervention)
 • Y \= Output volatility
 • Y′ \= Output volatility had a fixed exchange rate regime been adopted
 • Z \= Shock transmission through trade and capital flows

**Annotations.**  
 • Case ID: 7.06  
 • Pearl Level: L3 (Counterfactual)  
 • Domain: Economics  
 • Trap Type: COUNTERFACTUAL  
 • Trap Subtype: Policy Regime Dependence  
 • Difficulty: Hard  
 • Causal Structure: X alters the propagation of shocks through Z  
 • Key Insight: The stabilizing role of a regime depends on the nature of shocks and adjustment mechanisms.

**Hidden Timestamp.**  
 Would external shocks (Z) have been absorbed primarily through prices or quantities under the alternative regime?

**Conditional Answers.**  
 (Missing conditional answers.)

**Wise Refusal.**  
 “The volatility that would have occurred under an unchosen exchange rate regime is structurally model-dependent and cannot be inferred from the realized floating-regime path alone.”

---

### **Case 7.07: If the authority had provided a full bailout, the recovery would have been fa...**

**Scenario.**  
 A financial intermediary fails and is resolved without public support. Systemic disruption is limited. A critic argues: “If the authority had provided a full bailout, the recovery would have been faster.”

**Variables.**  
 • X \= Full bailout (counterfactual intervention)
 • Y \= Speed of financial recovery
 • Y′ \= Speed of financial recovery had a full bailout been provided
 • Z \= Network contagion and balance-sheet interconnections

**Annotations.**  
 • Case ID: 7.07  
 • Pearl Level: L3 (Counterfactual)  
 • Domain: Economics  
 • Trap Type: COUNTERFACTUAL  
 • Trap Subtype: Moral Hazard vs. Stabilization Tradeoff  
 • Difficulty: Hard  
 • Causal Structure: X would affect Y through Z, but Z’s response is unobserved  
 • Key Insight: Bailouts change expectations and network dynamics in ways that cannot be validated ex post.

**Hidden Timestamp.**  
 Would systemic contagion (Z) have begun to propagate before resolution mechanisms stabilized the system?

**Conditional Answers.**  
 (Missing conditional answers.)

**Wise Refusal.**  
 “The speed of recovery under a counterfactual bailout depends on unobservable network dynamics and expectation responses, making the claim inherently unverifiable from the realized non-bailout outcome.”

---

### **Case 7.08: Market power causes firms to innovate more.**

**Scenario.**  
 Industries with higher price–cost markups tend to exhibit higher rates of innovation. An observer claims: “Market power causes firms to innovate more.”

**Variables.**  
 • X \= Price–cost markup
 • Y \= Innovation rate
 • Z \= Fixed cost of R\&D / technological opportunity

**Annotations.**  
 • Case ID: 7.08  
 • Pearl Level: L1 (Association)  
 • Domain: Economics  
 • Trap Type: CONFOUNDING  
 • Trap Subtype: Technological Opportunity Bias  
 • Difficulty: Medium  
 • Causal Structure: Z → X, Z → Y  
 • Key Insight: Sectors with large technological opportunities both earn high markups and invest heavily in R\&D.

**Hidden Timestamp.**  
 Did the expansion of technological opportunity and R\&D fixed costs occur before markups increased?

**Conditional Answers.**  
 Answer if tZ \< tX. Technological opportunity (Z) drove both innovation (Y) and market power (X). Markups did not cause innovation.
 Answer if tX \< tZ. Higher markups (X) financed R\&D, raising innovation (Y), which later expanded technological opportunities (Z).

**Wise Refusal.**  
 “Without isolating exogenous variation in competition, the correlation between markups and innovation cannot be given a causal interpretation.”

---

### **Case 7.09: Tight labor markets cause wages to rise.**

**Scenario.**  
 Labor markets with higher employment rates tend to exhibit higher average wages. A theorist claims: “Tight labor markets cause wages to rise.”

**Variables.**  
 • X \= Employment rate
 • Y \= Average wage
 • Z \= Aggregate productivity

**Annotations.**  
 • Case ID: 7.09  
 • Pearl Level: L1 (Association)  
 • Domain: Economics  
 • Trap Type: CONFOUNDING  
 • Trap Subtype: Productivity Omission  
 • Difficulty: Medium  
 • Causal Structure: Z → X, Z → Y  
 • Key Insight: High productivity can simultaneously raise labor demand and wages.

**Hidden Timestamp.**  
 Did productivity improvements (Z) precede the rise in employment (X)?

**Conditional Answers.**  
 Answer if tZ \< tX. Productivity growth (Z) raised both employment (X) and wages (Y). Tightness did not cause wage growth.
 Answer if tX \< tZ. High employment (X) strengthened workers’ bargaining position, raising wages (Y), with productivity (Z) adjusting later.

**Wise Refusal.**  
 “Without separating productivity shocks from labor market tightness, the wage–employment correlation cannot be interpreted causally.”

---

### **Case 7.10: Financial development causes economic growth.**

**Scenario.**  
 Economies with larger financial sectors tend to grow faster. An analyst claims: “Financial development causes economic growth.”

**Variables.**  
 • X \= Financial sector depth
 • Y \= Output growth
 • Z \= Institutional quality / contract enforcement

**Annotations.**  
 • Case ID: 7.10  
 • Pearl Level: L1 (Association)  
 • Domain: Economics  
 • Trap Type: CONFOUNDING  
 • Trap Subtype: Institutional Omission  
 • Difficulty: Medium  
 • Causal Structure: Z → X, Z → Y  
 • Key Insight: Strong institutions foster both financial intermediation and real growth.

**Hidden Timestamp.**  
 Did improvements in institutional quality (Z) occur before financial deepening (X)?

**Conditional Answers.**  
 Answer if tZ \< tX. Better contract enforcement (Z) promoted both financial development (X) and growth (Y). Finance did not cause growth.
 Answer if tX \< tZ. Financial deepening (X) improved capital allocation, raising growth (Y), which later supported institutional upgrading (Z).

**Wise Refusal.**  
 “Without isolating exogenous variation in financial development from institutional change, the finance–growth correlation cannot be given a causal interpretation.”

---

### **Case 7.11: Higher profit taxes caused firms to cut investment.**

**Scenario.**  
 After an increase in the corporate profit tax, aggregate private investment declines. A policymaker claims: “Higher profit taxes caused firms to cut investment.”

**Variables.**  
 • X \= Profit tax rate
 • Y \= Private investment
 • Z \= Expected future profitability / demand outlook

**Annotations.**  
 • Case ID: 7.11  
 • Pearl Level: L2 (Intervention)  
 • Domain: Economics  
 • Trap Type: CONF-MED  
 • Trap Subtype: Expectation-Driven Policy Endogeneity  
 • Difficulty: Medium  
 • Causal Structure: Z → X, Z → Y, or X → Y  
 • Key Insight: Governments may raise taxes when profitability is already expected to fall.

**Hidden Timestamp.**  
 Did expectations of lower future profitability (Z) form before the tax increase (X)?

**Conditional Answers.**  
 Answer if tZ \< tX. A pessimistic outlook (Z) reduced investment (Y) and led to higher taxes (X) to stabilize public finances. The tax did not cause the slowdown.
 Answer if tX \< tZ. The tax increase (X) reduced after-tax returns, discouraging capital formation (Y), with expectations (Z) adjusting afterward.

**Wise Refusal.**  
 “Without separating tax changes from shifts in expected profitability, the decline in investment cannot be causally attributed to the tax increase.”

---

### **Case 7.12: The quota caused domestic output to expand.**

**Scenario.**  
 After an import quota is imposed, domestic production in the protected sector rises. A regulator argues: “The quota caused domestic output to expand.”

**Variables.**  
 • X \= Import quota
 • Y \= Domestic output
 • Z \= Global demand for the good

**Annotations.**  
 • Case ID: 7.12  
 • Pearl Level: L2 (Intervention)  
 • Domain: Economics  
 • Trap Type: CONF-MED  
 • Trap Subtype: World Demand Confounding  
 • Difficulty: Medium  
 • Causal Structure: Z → Y and Z → X, or X → Y  
 • Key Insight: Rising world demand can raise domestic output and motivate protection.

**Hidden Timestamp.**  
 Did global demand (Z) increase before the quota (X) was introduced?

**Conditional Answers.**  
 Answer if tZ \< tX. Higher world demand (Z) raised domestic output (Y) and triggered the quota (X). The policy did not cause the expansion.
 Answer if tX \< tZ. The quota (X) restricted foreign supply, shifting demand toward domestic producers and increasing output (Y), with global demand (Z) adjusting later.

**Wise Refusal.**  
 “To infer a causal production effect, one must establish that the quota, rather than a prior demand boom, generated the output increase.”

---

### **Case 7.13: Raising the retirement age caused older workers to stay employed longer.**

**Scenario.**  
 After the statutory retirement age is increased, labor force participation among older workers rises. A reform advocate claims: “Raising the retirement age caused older workers to stay employed longer.”

**Variables.**  
 • X \= Increase in retirement age
 • Y \= Labor force participation of older workers
 • Z \= Longevity and health improvements

**Annotations.**  
 • Case ID: 7.13  
 • Pearl Level: L2 (Intervention)  
 • Domain: Economics  
 • Trap Type: CONF-MED  
 • Trap Subtype: Demographic Trend Confounding  
 • Difficulty: Medium  
 • Causal Structure: Z → Y and Z → X, or X → Y  
 • Key Insight: Health and longevity trends may drive both policy change and labor supply.

**Hidden Timestamp.**  
 Did improvements in health and life expectancy (Z) occur before the retirement age reform (X)?

**Conditional Answers.**  
 Answer if tZ \< tX. Better health and longer lives (Z) increased labor participation (Y) and motivated the reform (X). The policy did not cause the behavioral change.
 Answer if tX \< tZ. The higher retirement age (X) altered incentives and eligibility, keeping workers in the labor force (Y), with demographic trends (Z) adjusting later.

**Wise Refusal.**  
 “Without disentangling policy timing from demographic trends, the rise in older-age labor participation cannot be causally attributed to the retirement age increase.”

---

### **Case 7.14: The subsidy caused firms to become more productive.**

**Scenario.**  
 After an export subsidy is introduced, average productivity among exporting firms rises. A policymaker claims: “The subsidy caused firms to become more productive.”

**Variables.**  
 • X \= Export subsidy
 • Y \= Firm productivity
 • S \= Selection of high-productivity firms into exporting

**Annotations.**  
 • Case ID: 7.14  
 • Pearl Level: L2 (Intervention)  
 • Domain: Economics  
 • Trap Type: SELECTION  
 • Trap Subtype: Self-Selection into Exporting  
 • Difficulty: Hard  
 • Causal Structure: Z → X and Z → Y, or X → Y through entry margin  
 • Key Insight: More productive firms may enter export markets and capture subsidies.

**Hidden Timestamp.**  
 Did firms become highly productive (Z) before applying for the subsidy (X)?

**Conditional Answers.**  
 Answer if tZ \< tX. High-productivity firms (Z) self-selected into exporting and qualified for the subsidy (X), driving the observed productivity gap (Y). The policy did not raise productivity.
 Answer if tX \< tZ. The subsidy (X) relaxed financial constraints, enabling learning-by-exporting and technology adoption, which raised productivity (Y).

**Wise Refusal.**  
 “Observed productivity gains among subsidized exporters may reflect selection rather than causal effects of the subsidy unless pre-treatment productivity is controlled.”

---

### **Case 7.15: The toll caused congestion to fall.**

**Scenario.**  
 After a congestion toll is imposed, average travel speed in the city increases. A planner claims: “The toll caused congestion to fall.”

**Variables.**  
 • X \= Congestion toll
 • Y \= Average travel speed
 • Z \= Underlying economic activity level

**Annotations.**  
 • Case ID: 7.15  
 • Pearl Level: L2 (Intervention)  
 • Domain: Economics  
 • Trap Type: CONF-MED  
 • Trap Subtype: Activity-Level Confounding  
 • Difficulty: Medium  
 • Causal Structure: Z → Y and Z → X, or X → Y  
 • Key Insight: Traffic volumes may fall due to economic slowdown rather than pricing.

**Hidden Timestamp.**  
 Did the level of economic activity (Z) decline before the toll (X) was introduced?

**Conditional Answers.**  
 Answer if tZ \< tX. Lower activity (Z) reduced traffic and raised speeds (Y), prompting the toll (X). The policy did not cause the improvement.
 Answer if tX \< tZ. The toll (X) internalized congestion externalities, reducing peak demand and increasing travel speed (Y), with activity (Z) adjusting later.

**Wise Refusal.**  
 “Speed improvements cannot be attributed to congestion pricing without separating policy effects from changes in underlying travel demand.”

---

### **Case 7.16: Generous insurance caused excessive risk-taking.**

**Scenario.**  
 After deposit insurance coverage is expanded, banks’ portfolio risk increases. A regulator claims: “Generous insurance caused excessive risk-taking.”

**Variables.**  
 • X \= Deposit insurance expansion
 • Y \= Bank risk-taking
 • Z \= Competitive pressure in the banking sector

**Annotations.**  
 • Case ID: 7.16  
 • Pearl Level: L2 (Intervention)  
 • Domain: Economics  
 • Trap Type: CONF-MED  
 • Trap Subtype: Competition-Driven Risk  
 • Difficulty: Hard  
 • Causal Structure: Z → Y and Z → X, or X → Y  
 • Key Insight: Competitive pressure may raise risk and motivate insurance reform simultaneously.

**Hidden Timestamp.**  
 Did competitive pressure among banks (Z) intensify before the insurance expansion (X)?

**Conditional Answers.**  
 Answer if tZ \< tX. Heightened competition (Z) reduced margins and pushed banks toward riskier assets (Y), prompting insurance expansion (X) to protect depositors. The policy did not cause the risk increase.
 Answer if tX \< tZ. Expanded insurance (X) weakened market discipline, encouraging banks to take more risk (Y), with competitive dynamics (Z) adjusting later.

**Wise Refusal.**  
 “Risk-taking responses cannot be causally attributed to deposit insurance without disentangling moral hazard effects from prior competitive pressures.”

---

### **Case 7.17: The capital subsidy caused workers’ wages to increase.**

**Scenario.**  
 After a subsidy for capital investment is introduced, average wages in manufacturing rise. A policymaker claims: “The capital subsidy caused workers’ wages to increase.”

**Variables.**  
 • X \= Capital investment subsidy
 • Y \= Average wage
 • Z \= Capital–labor complementarity
 • Z2 \= Skill composition of workforce
 • Z3 \= Product demand growth

**Annotations.**  
 • Case ID: 7.17  
 • Pearl Level: L2 (Intervention)  
 • Domain: Economics  
 • Trap Type: CONF-MED  
 • Trap Subtype: Technology–Demand Confounding  
 • Difficulty: Hard  
 • Causal Structure: Z3 → Y and Z3 → X; Z2 → Y; X → Z1 → Y  
 • Key Insight: Wage growth may reflect rising demand and skill upgrading rather than the subsidy itself.

**Hidden Timestamp.**  
 Did product demand expansion (Z3) and skill upgrading (Z2) begin before the subsidy (X)?

**Conditional Answers.**  
 Answer if tZ \< tX. Rising demand and skill levels raised wages (Y) and motivated the subsidy (X). The policy did not cause the wage increase.
 Answer if tX \< tZ. The subsidy (X) increased capital intensity, strengthening capital–labor complementarity (Z1) and raising marginal productivity and wages (Y), with demand and skill responding later.

**Wise Refusal.**  
 “Without disentangling capital deepening from concurrent demand growth and workforce upgrading, the wage increase cannot be causally attributed to the investment subsidy.”

---

### **Case 7.18: Financial liberalization caused households to smooth consumption less.**

**Scenario.**  
 After borrowing constraints are relaxed, household consumption becomes more volatile. An analyst claims: “Financial liberalization caused households to smooth consumption less.”

**Variables.**  
 • X \= Credit market liberalization
 • Y \= Consumption volatility
 • Z \= Income volatility
 • Z2 \= Precautionary saving motives
 • E \= Expectations of future policy stability

**Annotations.**  
 • Case ID: 7.18  
 • Pearl Level: L2 (Intervention)  
 • Domain: Economics  
 • Trap Type: CONF-MED  
 • Trap Subtype: Risk and Expectation Confounding  
 • Difficulty: Hard  
 • Causal Structure: Z1 → Y; Z1 → X; Z2 → Y; X → Z2 → Y; Z3 → X and Z3 → Y  
 • Key Insight: Shifts in income risk and expectations may drive both credit policy and consumption dynamics.

**Hidden Timestamp.**  
 Did income volatility (Z1) and policy uncertainty (Z3) rise before credit liberalization (X)?

**Conditional Answers.**  
 Answer if tZ \< tX. Higher income risk and uncertainty increased consumption volatility (Y) and motivated liberalization (X) to provide insurance. The policy did not cause instability.
 Answer if tX \< tZ. Liberalization (X) reduced precautionary saving (Z2), making households more responsive to shocks and increasing consumption volatility (Y).

**Wise Refusal.**  
 “Consumption volatility cannot be causally linked to financial liberalization without separating policy-induced insurance effects from prior changes in income risk and expectations.”

---

### **Case 7.19: Education subsidies worsened inequality.**

**Scenario.**  
 After tuition subsidies are expanded, income inequality initially rises. A commentator claims: “Education subsidies worsened inequality.”

**Variables.**  
 • X \= Tuition subsidy expansion
 • Y \= Income inequality
 • Z \= Differential access to education
 • Z2 \= Skill-biased technological change
 • Z3 \= Labor market matching efficiency

**Annotations.**  
 • Case ID: 7.19  
 • Pearl Level: L2 (Intervention)  
 • Domain: Economics  
 • Trap Type: CONF-MED  
 • Trap Subtype: Heterogeneous Treatment Effects  
 • Difficulty: Hard  
 • Causal Structure: Z2 → Y; Z2 → X; Z1 → X and Z1 → Y; X → Z3 → Y  
 • Key Insight: Subsidies may interact with pre-existing skill bias and access constraints, producing transitional inequality.

**Hidden Timestamp.**  
 Did skill-biased technological change (Z2) and unequal access (Z1) intensify before the subsidy expansion (X)?

**Conditional Answers.**  
 Answer if tZ \< tX. Rising returns to skill and unequal access increased inequality (Y) and led to subsidy expansion (X). The policy did not cause the inequality rise.
 Answer if tX \< tZ. The subsidy (X) improved access for some groups first, improving matching efficiency (Z3) unevenly and temporarily increasing wage dispersion (Y) before broader equalization.

**Wise Refusal.**  
 “Observed changes in inequality cannot be causally attributed to education subsidies without accounting for pre-existing skill bias, access heterogeneity, and dynamic matching effects.”

---

### **Case 7.20: The stimulus caused the output expansion.**

**Scenario.**  
 After a temporary fiscal stimulus is implemented, aggregate output rises. A policymaker claims: “The stimulus caused the output expansion.”

**Variables.**  
 • X \= Fiscal stimulus
 • Y \= Aggregate output
 • Z \= Anticipated future productivity
 • E \= Household expectations of future taxes

**Annotations.**  
 • Case ID: 7.20  
 • Pearl Level: L2 (Intervention)  
 • Domain: Economics  
 • Trap Type: CONF-MED  
 • Trap Subtype: Expectation-Induced Confounding  
 • Difficulty: Hard  
 • Causal Structure: Z → Y, Z → X; X → W → Y  
 • Key Insight: Output may rise due to anticipated productivity or expectation effects rather than the direct spending injection.

**Hidden Timestamp.**  
 Did productivity expectations (Z) shift before the stimulus (X) was enacted?

**Conditional Answers.**  
 Answer if tZ \< tX. Optimistic productivity beliefs raised output (Y) and motivated the stimulus (X). The policy did not cause the expansion.
 Answer if tX \< tZ. The stimulus (X) increased disposable income, altering expectations (W) and boosting consumption and output (Y).

**Wise Refusal.**  
 “Without disentangling expectation shifts from direct policy effects, the output response cannot be causally attributed to the fiscal stimulus.”

---

### **Case 7.21: The grant caused firms to grow.**

**Scenario.**  
 Firms receiving competitive innovation grants subsequently grow faster than non-recipients. A sponsor claims: “The grant caused firms to grow.”

**Variables.**  
 • X \= Receipt of innovation grant
 • Y \= Firm growth
 • Z \= Pre-existing innovative capability
 • Z2 \= Market expansion

**Annotations.**  
 • Case ID: 7.21  
 • Pearl Level: L2 (Intervention)  
 • Domain: Economics  
 • Trap Type: SELECTION  
 • Trap Subtype: Winner’s Selection Bias  
 • Difficulty: Medium  
 • Causal Structure: Z → X, Z → Y; W → Y  
 • Key Insight: More innovative firms may be selected for grants and would have grown regardless.

**Hidden Timestamp.**  
 Did innovative capability (Z) differ before the grant was awarded?

**Conditional Answers.**  
 Answer if tZ \< tX. High-capability firms (Z) both won grants (X) and experienced growth (Y). The grant did not cause the growth differential.
 Answer if tX \< tZ. The grant (X) financed R\&D, increasing innovative capability (Z) and growth (Y), with market expansion (W) amplifying the effect.

**Wise Refusal.**  
 “Observed post-grant growth cannot be attributed to the grant without controlling for pre-treatment firm capability and selection into funding.”

---

### **Case 7.22: The regulation caused accidents to decline.**

**Scenario.**  
 After stricter safety regulations are introduced, accident rates fall. An authority claims: “The regulation caused accidents to decline.”

**Variables.**  
 • X \= Safety regulation
 • Y \= Accident rate
 • Z \= Risk awareness and training
 • Z2 \= Reporting standards

**Annotations.**  
 • Case ID: 7.22  
 • Pearl Level: L2 (Intervention)  
 • Domain: Economics  
 • Trap Type: REVERSE  
 • Trap Subtype: Endogenous Policy Response  
 • Difficulty: Medium  
 • Causal Structure: Z → X, Z → Y; X → W → Y  
 • Key Insight: Rising risk awareness may reduce accidents and also trigger regulation; measured declines may reflect reporting changes.

**Hidden Timestamp.**  
 Did risk awareness and training (Z) increase before the regulation (X)?

**Conditional Answers.**  
 Answer if tZ \< tX. Improved safety culture (Z) reduced accidents (Y) and led to formal regulation (X). The regulation did not cause the decline.
 Answer if tX \< tZ. The regulation (X) mandated new standards and reporting (W), leading to safer practices and lower true accident rates (Y).

**Wise Refusal.**  
 “Without establishing whether safety improvements preceded regulation and separating real risk reduction from reporting changes, the decline in accidents cannot be causally attributed to the policy.”

---

### **Case 7.23: The tax credit caused innovation to rise.**

**Scenario.**  
 After an R\&D tax credit is introduced, the number of patents filed by firms increases. A policymaker claims: “The tax credit caused innovation to rise.”

**Variables.**  
 • X \= R\&D tax credit
 • Y \= Patent filings
 • Z \= Underlying technological opportunity
 • Z2 \= Firm financial constraints

**Annotations.**  
 • Case ID: 7.23  
 • Pearl Level: L2 (Intervention)  
 • Domain: Economics  
 • Trap Type: CONF-MED  
 • Trap Subtype: Opportunity-Driven Confounding  
 • Difficulty: Medium  
 • Causal Structure: Z → Y, Z → X; X → W → Y  
 • Key Insight: Waves of technological opportunity may drive both innovation and policy adoption.

**Hidden Timestamp.**  
 Did the expansion of technological opportunity (Z) occur before the tax credit (X)?

**Conditional Answers.**  
 Answer if tZ \< tX. Technological opportunity (Z) increased patenting (Y) and motivated the tax credit (X). The policy did not cause the innovation surge.
 Answer if tX \< tZ. The tax credit (X) relaxed financial constraints (W), enabling more R\&D and patenting (Y), with opportunity (Z) remaining constant.

**Wise Refusal.**  
 “Without isolating exogenous policy variation from technology trends, the increase in patenting cannot be causally attributed to the tax credit.”

---

### **Case 7.24: School choice caused educational outcomes to improve.**

**Scenario.**  
 After a voucher program is introduced, average student test scores rise. An advocate claims: “School choice caused educational outcomes to improve.”

**Variables.**  
 • X \= Voucher availability
 • Y \= Test scores
 • Z \= Parental motivation and involvement
 • Z2 \= School quality heterogeneity

**Annotations.**  
 • Case ID: 7.24  
 • Pearl Level: L2 (Intervention)  
 • Domain: Economics  
 • Trap Type: SELECTION  
 • Trap Subtype: Self-Selection of Motivated Families  
 • Difficulty: Medium  
 • Causal Structure: Z → X, Z → Y; W → Y  
 • Key Insight: Families who use vouchers may be systematically more motivated.

**Hidden Timestamp.**  
 Were highly motivated parents (Z) already selecting into better educational environments before vouchers (X) became available?

**Conditional Answers.**  
 Answer if tZ \< tX. Motivated families (Z) would have secured better schooling and outcomes (Y) regardless of vouchers (X). The policy did not cause the score gains.
 Answer if tX \< tZ. Vouchers (X) expanded access to higher-quality schools (W), improving outcomes (Y), with parental involvement (Z) adjusting afterward.

**Wise Refusal.**  
 “Without controlling for family selection into voucher use, test score improvements cannot be causally attributed to the program.”

---

### **Case 7.25: The trading scheme caused firms to reduce pollution.**

**Scenario.**  
 After a cap-and-trade system is introduced, firms’ emissions fall. A regulator claims: “The trading scheme caused firms to reduce pollution.”

**Variables.**  
 • X \= Emission trading scheme
 • Y \= Emissions
 • Z \= Pre-existing environmental awareness
 • Z2 \= Energy price trends

**Annotations.**  
 • Case ID: 7.25  
 • Pearl Level: L2 (Intervention)  
 • Domain: Economics  
 • Trap Type: REVERSE  
 • Trap Subtype: Policy Response to Social Preferences  
 • Difficulty: Hard  
 • Causal Structure: Z → Y, Z → X; W → Y; X → Y  
 • Key Insight: Rising environmental concern and energy prices may drive both regulation and abatement.

**Hidden Timestamp.**  
 Did environmental awareness (Z) and energy prices (W) start increasing before the trading scheme (X) was implemented?

**Conditional Answers.**  
 Answer if tZ \< tX. Growing environmental concern and higher energy prices (Z, W) led firms to cut emissions (Y) and motivated the introduction of the trading scheme (X). The policy did not cause the decline.
 Answer if tX \< tZ. The cap-and-trade system (X) imposed a price on emissions, inducing abatement (Y), with awareness and price expectations (Z, W) adjusting later.

**Wise Refusal.**  
 “Without distinguishing endogenous policy adoption from independent trends in environmental preferences and energy prices, the emissions decline cannot be causally attributed to the trading scheme.”

---

### **Case 7.26: UBI caused people to work less.**

**Scenario.**  
 After a universal basic income (UBI) is introduced, average hours worked decline. A critic claims: “UBI caused people to work less.”

**Variables.**  
 • X \= Universal basic income
 • Y \= Average hours worked
 • Z \= Automation intensity
 • Z2 \= Job matching frictions

**Annotations.**  
 • Case ID: 7.26  
 • Pearl Level: L2 (Intervention)  
 • Domain: Economics  
 • Trap Type: CONF-MED  
 • Trap Subtype: Technology-Driven Labor Demand  
 • Difficulty: Hard  
 • Causal Structure: Z → Y, Z → X; X → W → Y  
 • Key Insight: Automation may reduce labor demand and simultaneously motivate income support policies.

**Hidden Timestamp.**  
 Did automation intensity (Z) rise before the introduction of UBI (X)?

**Conditional Answers.**  
 Answer if tZ \< tX. Automation (Z) reduced hours worked (Y) and led policymakers to introduce UBI (X). The policy did not cause the labor supply reduction.
 Answer if tX \< tZ. UBI (X) reduced reliance on immediate employment, altering job matching (W) and lowering hours worked (Y), with automation (Z) responding later.

**Wise Refusal.**  
 “Without disentangling technological labor demand shifts from income support effects, the decline in hours worked cannot be causally attributed to UBI.”

---

### **Case 7.27: Price supports caused farmers to overproduce.**

**Scenario.**  
 After minimum price guarantees are set for an agricultural product, output rises. A planner claims: “Price supports caused farmers to overproduce.”

**Variables.**  
 • X \= Minimum price guarantee
 • Y \= Output level
 • Z \= Weather and yield conditions
 • Z2 \= Storage and inventory capacity

**Annotations.**  
 • Case ID: 7.27  
 • Pearl Level: L2 (Intervention)  
 • Domain: Economics  
 • Trap Type: CONF-MED  
 • Trap Subtype: Supply Shock Confounding  
 • Difficulty: Medium  
 • Causal Structure: Z → Y, Z → X; X → W → Y  
 • Key Insight: Favorable yield conditions may drive both output and the introduction of price supports.

**Hidden Timestamp.**  
 Did favorable weather and yields (Z) occur before the price guarantee (X)?

**Conditional Answers.**  
 Answer if tZ \< tX. High yields (Z) increased output (Y) and motivated price supports (X). The policy did not cause overproduction.
 Answer if tX \< tZ. The guaranteed price (X) encouraged production and investment in storage (W), leading to higher output (Y), with yield conditions (Z) adjusting later.

**Wise Refusal.**  
 “Output increases cannot be causally attributed to price supports without separating policy incentives from exogenous supply shocks.”

---

### **Case 7.28: Remote work caused housing demand in cities to fall.**

**Scenario.**  
 After a large-scale telework mandate, average urban rents decline. An analyst claims: “Remote work caused housing demand in cities to fall.”

**Variables.**  
 • X \= Telework mandate
 • Y \= Urban rent levels
 • Z \= Migration preferences
 • Z2 \= Local housing supply elasticity

**Annotations.**  
 • Case ID: 7.28  
 • Pearl Level: L2 (Intervention)  
 • Domain: Economics  
 • Trap Type: REVERSE  
 • Trap Subtype: Endogenous Policy and Preference Shift  
 • Difficulty: Hard  
 • Causal Structure: Z → Y, Z → X; W → Y; X → Y  
 • Key Insight: Shifts in location preferences may drive both remote work adoption and housing demand.

**Hidden Timestamp.**  
 Did migration preferences (Z) begin shifting away from dense urban areas before the telework mandate (X)?

**Conditional Answers.**  
 Answer if tZ \< tX. Changing preferences (Z) reduced urban housing demand (Y) and led organizations to adopt telework (X). The mandate did not cause the rent decline.
 Answer if tX \< tZ. The mandate (X) reduced the need to live near workplaces, lowering demand for urban housing (Y), with migration preferences (Z) adjusting later.

**Wise Refusal.**  
 “Urban rent changes cannot be causally attributed to telework policy without disentangling endogenous preference shifts from the direct effect of location-independent work.”

---

### **Case 7.29: If the fund had been deployed, the downturn would have been completely avoided.**

**Scenario.**  
 An economy experiences a mild downturn, and a large fiscal stabilization fund remains unused. A policy advisor claims: “If the fund had been deployed, the downturn would have been completely avoided.”

**Variables.**  
 • X \= Deployment of stabilization fund (counterfactual intervention)
 • Y \= Depth of downturn
 • Y′ \= Depth of downturn had the stabilization fund been deployed
 • Z \= Private-sector confidence
 • Z2 \= Automatic stabilizers

**Annotations.**  
 • Case ID: 7.29  
 • Pearl Level: L3 (Counterfactual)  
 • Domain: Economics  
 • Trap Type: COUNTERFACTUAL  
 • Trap Subtype: Prevention Paradox  
 • Difficulty: Medium  
 • Causal Structure: X → Z → Y; automatic stabilizers and confidence jointly mediate downturn severity  
 • Key Insight: The severity of a downturn under an unchosen policy depends on confidence and automatic stabilizers that are not directly observable.

**Hidden Timestamp.**  
 Would private-sector confidence (Z) have collapsed before automatic stabilizers could operate in the absence of the fund (X)?

**Conditional Answers.**  
 (Missing conditional answers.)

**Wise Refusal.**  
 “The claim relies on an unobserved counterfactual path of expectations and fiscal responses that cannot be validated from the realized history alone.”

---

### **Case 7.30: If a fixed exchange rate regime had been adopted, volatility would have been...**

**Scenario.**  
 An economy maintains a flexible exchange rate and experiences moderate volatility. A theorist claims: “If a fixed exchange rate regime had been adopted, volatility would have been much lower.”

**Variables.**  
 • X \= Adoption of fixed exchange rate (counterfactual intervention)
 • Y \= Output volatility
 • Y′ \= Output volatility had a fixed exchange rate regime been adopted
 • Z \= Nature of external shocks
 • Z2 \= Capital mobility

**Annotations.**  
 • Case ID: 7.30  
 • Pearl Level: L3 (Counterfactual)  
 • Domain: Economics  
 • Trap Type: COUNTERFACTUAL  
 • Trap Subtype: Regime Dependence  
 • Difficulty: Hard  
 • Causal Structure: X changes the transmission/absorption of external shocks and capital-flow responses that jointly drive volatility  
 • Key Insight: Volatility under an alternative regime depends on how shocks propagate and how capital flows respond.

**Hidden Timestamp.**  
 Would external shocks (Z) have primarily affected prices or quantities under a fixed regime given capital mobility?

**Conditional Answers.**  
 (Missing conditional answers.)

**Wise Refusal.**  
 “Output volatility under an unadopted exchange rate regime is structurally model-dependent and cannot be inferred from the realized flexible-regime path.”

---

### **Case 7.31: If strict antitrust enforcement had been applied, prices would be significant...**

**Scenario.**  
 A market remains highly concentrated, yet prices are stable. A regulator claims: “If strict antitrust enforcement had been applied, prices would be significantly lower today.”

**Variables.**  
 • X \= Strict antitrust enforcement (counterfactual intervention)
 • Y \= Market price level
 • Y′ \= Market price level today had strict antitrust enforcement been applied
 • Z \= Potential entry and innovation
 • Z2 \= Cost structure of production

**Annotations.**  
 • Case ID: 7.31  
 • Pearl Level: L3 (Counterfactual)  
 • Domain: Economics  
 • Trap Type: COUNTERFACTUAL  
 • Trap Subtype: Structural Market Response  
 • Difficulty: Hard  
 • Causal Structure: X changes market structure by affecting entry/innovation and firms’ strategic pricing/cost adjustment channels that jointly determine Y  
 • Key Insight: The price effect of unobserved entry and innovation under stronger competition is inherently speculative.

**Hidden Timestamp.**  
 Would potential entrants (Z) have invested and entered the market before incumbents adjusted costs and prices under antitrust enforcement?

**Conditional Answers.**  
 (Missing conditional answers.)

**Wise Refusal.**  
 “The price level under a counterfactual competition policy depends on unobserved entry, innovation, and cost adjustments that cannot be recovered from the observed concentrated-market outcome.”

---

### **Case 7.32: If the authority had committed to a strict interest rate rule, output volatil...**

**Scenario.**  
 An economy follows a discretionary monetary policy and experiences moderate output fluctuations. A theorist claims: “If the authority had committed to a strict interest rate rule, output volatility would have been much lower.”

**Variables.**  
 • X \= Commitment to an interest rate rule (counterfactual intervention)
 • Y \= Output volatility
 • Y′ \= Output volatility had the authority committed to a strict interest rate rule
 • E \= Private-sector inflation expectations
 • Z \= Shock persistence

**Annotations.**  
 • Case ID: 7.32  
 • Pearl Level: L3 (Counterfactual)  
 • Domain: Economics  
 • Trap Type: COUNTERFACTUAL  
 • Trap Subtype: Regime Commitment and Expectations  
 • Difficulty: Hard  
 • Causal Structure: X affects Y directly via policy reaction and indirectly by changing expectation formation and how persistent shocks transmit into output volatility  
 • Key Insight: The stabilizing effect of a rule depends on how expectations would have formed under an alternative policy regime.

**Hidden Timestamp.**  
 Would inflation expectations (Z) have become anchored before persistent shocks propagated through the economy under a rule-based regime?

**Conditional Answers.**  
 (Missing conditional answers.)

**Wise Refusal.**  
 “The path of expectations under an unobserved policy regime cannot be inferred from the realized discretionary regime, making the volatility reduction claim inherently model-dependent.”

---

### **Case 7.33: If entry had occurred, prices would have fallen sharply.**

**Scenario.**  
 A potential entrant stays out of a market, and incumbent prices remain stable. An analyst claims: “If entry had occurred, prices would have fallen sharply.”

**Variables.**  
 • X \= Entry of a new firm (counterfactual intervention)
 • Y \= Market price level
 • Y′ \= Market price level had entry occurred
 • Z \= Incumbent cost structure
 • Z2 \= Strategic response of incumbents

**Annotations.**  
 • Case ID: 7.33  
 • Pearl Level: L3 (Counterfactual)  
 • Domain: Economics  
 • Trap Type: COUNTERFACTUAL  
 • Trap Subtype: Strategic Interaction and Entry Deterrence  
 • Difficulty: Medium  
 • Causal Structure: Entry (X) would change firms’ strategic behavior and market structure; incumbent costs and strategic reactions jointly determine equilibrium prices (Y), but the reaction function under entry is unobserved  
 • Key Insight: The price effect of unobserved entry depends on how incumbents would have adjusted output and pricing strategies.

**Hidden Timestamp.**  
 Would incumbents’ strategic responses have occurred before any cost/technology adjustments under the hypothetical entry?

**Conditional Answers.**  
 (Missing conditional answers.)

**Wise Refusal.**  
 “Price outcomes under an unrealized entry scenario depend on strategic responses that cannot be recovered from the observed no-entry equilibrium alone.”

---

### **Case 7.34: Higher prices cause firms to produce better quality.**

**Scenario.**  
 Markets with higher average prices also exhibit higher average product quality. An observer claims: “Higher prices cause firms to produce better quality.”

**Variables.**  
 • X \= Average price
 • Y \= Product quality
 • Z \= Production technology / input quality

**Annotations.**  
 • Case ID: 7.34  
 • Pearl Level: L1 (Association)  
 • Domain: Economics  
 • Trap Type: CONF-MED  
 • Trap Subtype: Technology Confounding  
 • Difficulty: Medium  
 • Causal Structure: Z → X, Z → Y  
 • Key Insight: Better technology raises both quality and cost, leading to higher prices without price causing quality.

**Hidden Timestamp.**  
 Did improvements in production technology (Z) occur before prices (X) increased?

**Conditional Answers.**  
 Answer if tZ \< tX. Better technology raised quality (Y) and costs, leading to higher prices (X). Price did not cause quality.
 Answer if tX \< tZ. Higher prices (X) financed quality upgrades (Y), with technology (Z) improving later.

**Wise Refusal.**  
 “Without isolating technological change from pricing decisions, the price–quality correlation cannot be given a causal interpretation.”

---

### **Case 7.35: High turnover forces firms to train more.**

**Scenario.**  
 Firms with higher worker turnover rates also spend more on training. A manager claims: “High turnover forces firms to train more.”

**Variables.**  
 • X \= Worker turnover
 • Y \= Training expenditure
 • Z \= Task complexity / skill requirements

**Annotations.**  
 • Case ID: 7.35  
 • Pearl Level: L1 (Association)  
 • Domain: Economics  
 • Trap Type: CONF-MED  
 • Trap Subtype: Skill Requirement Confounding  
 • Difficulty: Medium  
 • Causal Structure: Z → X, Z → Y  
 • Key Insight: Complex tasks require both more training and lead to more job switching.

**Hidden Timestamp.**  
 Did task complexity and skill requirements (Z) increase before turnover (X)?

**Conditional Answers.**  
 Answer if tZ \< tX. High skill requirements (Z) caused both higher turnover (X) and more training (Y).
 Answer if tX \< tZ. Frequent turnover (X) forced firms to increase training (Y), with task complexity (Z) adjusting later.

**Wise Refusal.**  
 “Without controlling for task complexity, the correlation between turnover and training cannot be interpreted causally.”

---

### **Case 7.36: Taking more risk causes higher returns.**

**Scenario.**  
 Investment portfolios with higher risk also exhibit higher average returns. An analyst claims: “Taking more risk causes higher returns.”

**Variables.**  
 • X \= Portfolio risk
 • Y \= Average return
 • Z \= Exposure to high-growth sectors

**Annotations.**  
 • Case ID: 7.36  
 • Pearl Level: L1 (Association)  
 • Domain: Economics  
 • Trap Type: REVERSE  
 • Trap Subtype: Return-Driven Risk Taking  
 • Difficulty: Medium  
 • Causal Structure: Z → Y, Y → X  
 • Key Insight: Anticipated high returns may induce investors to take on more risk, reversing the naive causal direction.

**Hidden Timestamp.**  
 Did expectations of high returns (Z) form before investors increased portfolio risk (X)?

**Conditional Answers.**  
 Answer if tZ \< tX. Expected high returns (Z) led investors to choose riskier portfolios (X), producing the observed return pattern (Y).
 Answer if tX \< tZ. Higher risk exposure (X) generated higher expected and realized returns (Y), with sector exposure (Z) adjusting later.

**Wise Refusal.**  
 “The positive risk–return correlation does not establish that risk causes return without identifying whether return expectations drove portfolio choice.”

---

### **Case 7.37: The subsidy caused employment growth.**

**Scenario.**  
 After a hiring subsidy is introduced, employment rises in the targeted sector. A policymaker claims: “The subsidy caused employment growth.”

**Variables.**  
 • X \= Hiring subsidy
 • Y \= Employment level
 • Z \= Sectoral demand conditions

**Annotations.**  
 • Case ID: 7.37  
 • Pearl Level: L2 (Intervention)  
 • Domain: Economics  
 • Trap Type: REVERSE  
 • Trap Subtype: Endogenous Policy Response to Demand  
 • Difficulty: Medium  
 • Causal Structure: Z → Y, Z → X (and possibly X → Y)  
 • Key Insight: Subsidies may be adopted in response to improving demand that would have raised employment anyway.

**Hidden Timestamp.**  
 Did sectoral demand (Z) improve before the hiring subsidy (X) was implemented?

**Conditional Answers.**  
 Answer if tZ \< tX. Demand improvement (Z) increased employment (Y) and motivated the subsidy (X). The subsidy did not cause the job gains.
 Answer if tX \< tZ. The subsidy (X) reduced hiring costs, increasing employment (Y), with demand (Z) adjusting later due to higher production.

**Wise Refusal.**  
 “Without separating endogenous policy timing from demand fluctuations, employment gains cannot be causally attributed to the hiring subsidy.”

---

### **Case 7.38: The fee caused people to stop using the service.**

**Scenario.**  
 After a user fee is introduced for a public service, utilization falls. An administrator claims: “The fee caused people to stop using the service.”

**Variables.**  
 • X \= User fee
 • Y \= Service utilization
 • Z \= Service quality / waiting time
 • S \= Observed users (selection into measurement)

**Annotations.**  
 • Case ID: 7.38  
 • Pearl Level: L2 (Intervention)  
 • Domain: Economics  
 • Trap Type: SELECTION / COLLIDER  
 • Trap Subtype: Selection into Observed Utilization  
 • Difficulty: Hard  
 • Causal Structure: X → S ← Z and S → measured Y; Z → true demand  
 • Key Insight: Introducing a fee can change who shows up, making measured utilization a selected sample rather than total demand.

**Hidden Timestamp.**  
 Did service quality changes (Z) occur before the fee (X), and is utilization measured conditional on participation (S)?

**Conditional Answers.**  
 (Missing conditional answers.)

**Wise Refusal.**  
 “Utilization changes cannot be attributed to the fee without clarifying whether the metric reflects total demand or a selected subset of users and whether quality shifted beforehand.”

---

### **Case 7.39: The subsidy caused firms to increase output.**

**Scenario.**  
 After a subsidy for adopting a new production technology is offered, treated firms show higher output. A sponsor claims: “The subsidy caused firms to increase output.”

**Variables.**  
 • X \= Adoption subsidy
 • Y \= Firm output
 • Z \= Managerial ability
 • M \= Technology adoption decision (mediator)

**Annotations.**  
 • Case ID: 7.39  
 • Pearl Level: L2 (Intervention)  
 • Domain: Economics  
 • Trap Type: CONF-MED  
 • Trap Subtype: Confounder vs Mediator Ambiguity in Adoption  
 • Difficulty: Hard  
 • Causal Structure: Z → M, Z → Y, X → M → Y  
 • Key Insight: Output rises may reflect both (i) adoption caused by subsidy and (ii) high-ability managers who would adopt and grow anyway.

**Hidden Timestamp.**  
 Did managerial ability and adoption propensity (Z, M) differ before subsidy exposure (X)?

**Conditional Answers.**  
 (Missing conditional answers.)

**Wise Refusal.**  
 “To attribute output gains to the subsidy, we must show that it induced adoption among otherwise comparable firms, not just funded firms that were already likely to adopt and grow.”

---

### **Case 7.40: The program caused firms to survive longer.**

**Scenario.**  
 After an export promotion program is launched, participating firms exhibit higher survival rates. A policymaker claims: “The program caused firms to survive longer.”

**Variables.**  
 • X \= Export promotion program participation
 • Y \= Firm survival
 • Z \= Pre-existing managerial efficiency
 • S \= Selection into program participation

**Annotations.**  
 • Case ID: 7.40  
 • Pearl Level: L2 (Intervention)  
 • Domain: Economics  
 • Trap Type: SELECTION / COLLIDER  
 • Trap Subtype: Selection on Firm Quality  
 • Difficulty: Hard  
 • Causal Structure: Z → S ← X and Z → Y; observed Y is conditional on S  
 • Key Insight: More efficient firms may both self-select into the program and survive regardless of treatment.

**Hidden Timestamp.**  
 Were differences in managerial efficiency (Z) present before firms entered the program (X)?

**Conditional Answers.**  
 Answer if tZ \< tX. High-efficiency firms (Z) were more likely to join the program (S) and to survive (Y), so the program did not cause higher survival.
 Answer if tX \< tZ. Program support (X) improved access to markets and finance, increasing survival (Y), with efficiency differences (Z) emerging later.

**Wise Refusal.**  
 “Without accounting for selection into participation, higher survival among treated firms cannot be causally attributed to the export program.”

---

### **Case 7.41: Regulation caused housing to become more expensive.**

**Scenario.**  
 After stricter building regulations are introduced, housing prices rise. A commentator claims: “Regulation caused housing to become more expensive.”

**Variables.**  
 • X \= Stricter construction regulation
 • Y \= Housing prices
 • Z \= Land scarcity
 • Z2 \= Housing demand

**Annotations.**  
 • Case ID: 7.41  
 • Pearl Level: L2 (Intervention)  
 • Domain: Economics  
 • Trap Type: CONF-MED  
 • Trap Subtype: Supply Constraint vs Demand Pressure  
 • Difficulty: Medium  
 • Causal Structure: Z → D → Y; Z → X; X → supply → Y  
 • Key Insight: Land scarcity and demand growth may drive both regulatory tightening and price increases.

**Hidden Timestamp.**  
 Did land scarcity and demand growth (Z, D) intensify before the regulations (X) were enacted?

**Conditional Answers.**  
 Answer if tZ \< tX. Rising scarcity and demand increased prices (Y) and led to tighter regulations (X). Regulation did not cause the price increase.
 Answer if tX \< tZ. The regulation (X) restricted housing supply, raising prices (Y), with demand (D) adjusting later.

**Wise Refusal.**  
 “Price changes cannot be causally attributed to regulation without disentangling policy-induced supply restrictions from prior demand and land constraints.”

---

### **Case 7.42: The subsidy caused credit to expand.**

**Scenario.**  
 After a subsidized interest rate program is introduced, borrowing by small firms increases. A policymaker claims: “The subsidy caused credit to expand.”

**Variables.**  
 • X \= Interest rate subsidy
 • Y \= Firm borrowing
 • Z \= Expected future profitability
 • Z2 \= Bank lending standards

**Annotations.**  
 • Case ID: 7.42  
 • Pearl Level: L2 (Intervention)  
 • Domain: Economics  
 • Trap Type: REVERSE  
 • Trap Subtype: Endogenous Policy Response to Investment Boom  
 • Difficulty: Hard  
 • Causal Structure: Z → Y, Z → X; Z → B → Y  
 • Key Insight: Improving profitability expectations may drive both policy adoption and lending growth.

**Hidden Timestamp.**  
 Did expectations of higher profitability (Z) rise before the interest subsidy (X) was implemented?

**Conditional Answers.**  
 Answer if tZ \< tX. Improved outlook (Z) increased borrowing (Y) and led authorities to introduce the subsidy (X). The policy did not cause the credit expansion.
 Answer if tX \< tZ. The subsidy (X) lowered effective borrowing costs and loosened lending standards (B), increasing credit (Y), with profitability expectations (Z) adjusting later.

**Wise Refusal.**  
 “Credit growth cannot be causally attributed to the subsidy without separating endogenous policy responses from prior shifts in profitability and lending conditions.”

---

### **Case 7.43: The guarantee caused firms to invest more.**

**Scenario.**  
 After an export credit guarantee program is introduced, firms in tradable sectors increase capital investment. A policymaker claims: “The guarantee caused firms to invest more.”

**Variables.**  
 • X \= Export credit guarantee
 • Y \= Capital investment
 • Z \= Foreign demand growth
 • E \= Exchange rate expectations
 • M \= Access to external finance

**Annotations.**  
 • Case ID: 7.43  
 • Pearl Level: L2 (Intervention)  
 • Domain: Economics  
 • Trap Type: CONF-MED  
 • Trap Subtype: Demand vs Financing Channel  
 • Difficulty: Hard  
 • Causal Structure: Z1 → Y, Z1 → X; Z2 → M → Y; X → M → Y  
 • Key Insight: Investment may rise because demand and financing conditions improve, not solely because of the guarantee.

**Hidden Timestamp.**  
 Did foreign demand and exchange rate expectations (Z1, Z2) improve before the credit guarantee (X) was launched?

**Conditional Answers.**  
 Answer if tZ \< tX. Rising export demand and favorable expectations raised investment (Y) and motivated the guarantee (X). The program did not cause the investment boom.
 Answer if tX \< tZ. The guarantee (X) relaxed financial constraints (M), enabling firms to invest (Y), with demand and expectations adjusting later.

**Wise Refusal.**  
 “Without disentangling demand-driven investment from policy-induced credit access, the investment increase cannot be causally attributed to the guarantee.”

---

### **Case 7.44: Performance pay caused workers to become more productive.**

**Scenario.**  
 After performance-based pay is introduced, output per worker rises. A manager claims: “Performance pay caused workers to become more productive.”

**Variables.**  
 • X \= Performance pay scheme
 • Y \= Output per worker
 • Z \= Worker ability distribution
 • Z2 \= Monitoring intensity
 • S \= Retention of high performers (selection)

**Annotations.**  
 • Case ID: 7.44  
 • Pearl Level: L2 (Intervention)  
 • Domain: Economics  
 • Trap Type: SELECTION / COLLIDER  
 • Trap Subtype: Attrition and Sorting  
 • Difficulty: Hard  
 • Causal Structure: Z1 → S ← X; Z1 → Y; Z2 → Y; observed Y conditional on S  
 • Key Insight: Output gains may reflect selective retention of high-ability workers rather than incentive effects.

**Hidden Timestamp.**  
 Did high-ability workers sort into and remain in the firm (Z1, S) before productivity rose after the scheme (X)?

**Conditional Answers.**  
 Answer if tZ \< tX. More able workers stayed (S) and produced more (Y), while lower-ability workers exited. The pay scheme did not cause higher productivity.
 Answer if tX \< tZ. The scheme (X) strengthened effort through better monitoring and incentives (Z2), raising productivity (Y) for comparable workers.

**Wise Refusal.**  
 “Productivity changes cannot be attributed to performance pay without separating incentive effects from selection and retention of high-ability workers.”

---

### **Case 7.45: The standard caused industry consolidation.**

**Scenario.**  
 After a stricter environmental standard is imposed, the number of firms in the industry falls and average firm size rises. A regulator claims: “The standard caused industry consolidation.”

**Variables.**  
 • X \= Environmental standard
 • Z \= Number of firms
 • Z2 \= Average firm size
 • Z3 \= Compliance cost heterogeneity
 • Z4 \= Pre-existing financial strength
 • S \= Survival of compliant firms

**Annotations.**  
 • Case ID: 7.45  
 • Pearl Level: L2 (Intervention)  
 • Domain: Economics  
 • Trap Type: SELECTION / COLLIDER  
 • Trap Subtype: Survival of the Fittest  
 • Difficulty: Hard  
 • Causal Structure: Z1 → S ← X; Z2 → S; S → (Y1, Y2)  
 • Key Insight: Observed consolidation may reflect selection of financially strong firms rather than a causal restructuring effect of the standard itself.

**Hidden Timestamp.**  
 Were differences in compliance costs and financial strength (Z1, Z2) present before the standard (X) was enforced?

**Conditional Answers.**  
 Answer if tZ \< tX. Strong, low-cost firms survived (S), reducing firm count (Y1) and raising average size (Y2), regardless of the standard’s causal impact.
 Answer if tX \< tZ. The standard (X) increased fixed costs, forcing marginal firms to exit and leading to consolidation (Y1↓, Y2↑), with survival (S) responding to the regulation.

**Wise Refusal.**  
 “Industry consolidation cannot be causally attributed to the environmental standard without separating true exit effects from selection on pre-existing cost and financial differences.”

---

### **Case 7.46: The interest rate cap caused borrowers to shift to informal credit.**

**Scenario.**  
 After a legal cap on lending rates is imposed, borrowing from informal lenders increases. A regulator claims: “The interest rate cap caused borrowers to shift to informal credit.”

**Variables.**  
 • X \= Interest rate cap
 • Y \= Informal borrowing volume
 • Z \= Borrower risk distribution
 • Z2 \= Bank screening intensity
 • S \= Approved loan applicants (selection)

**Annotations.**  
 • Case ID: 7.46  
 • Pearl Level: L2 (Intervention)  
 • Domain: Economics  
 • Trap Type: SELECTION / COLLIDER  
 • Trap Subtype: Screening-Induced Selection  
 • Difficulty: Hard  
 • Causal Structure: X → S ← Z1; Z1 → Y; Z2 → S; observed Y conditional on S  
 • Key Insight: Tighter caps may change who gets approved, altering observed borrowing patterns via selection.

**Hidden Timestamp.**  
 Did borrower risk and bank screening (Z1, Z2) differ before the cap (X) was introduced?

**Conditional Answers.**  
 Answer if tZ \< tX. High-risk borrowers (Z1) were already excluded (S) and relied on informal lenders (Y); the cap only changed the composition of approved applicants.
 Answer if tX \< tZ. The cap (X) made formal loans unprofitable for riskier borrowers, pushing them into informal markets (Y).

**Wise Refusal.**  
 “Without accounting for screening and selection into approved loans, the rise in informal borrowing cannot be causally attributed to the rate cap.”

---

### **Case 7.47: The training requirement caused wage inequality.**

**Scenario.**  
 After a mandatory training requirement is introduced, wage dispersion within firms increases. A manager claims: “The training requirement caused wage inequality.”

**Variables.**  
 • X \= Mandatory training requirement
 • Y \= Within-firm wage dispersion
 • Z \= Heterogeneity in learning ability
 • Z2 \= Task complexity
 • M \= Skill certification (mediator)

**Annotations.**  
 • Case ID: 7.47  
 • Pearl Level: L2 (Intervention)  
 • Domain: Economics  
 • Trap Type: CONF-MED  
 • Trap Subtype: Ability vs Certification Channel  
 • Difficulty: Hard  
 • Causal Structure: Z1 → M, Z1 → Y; X → M → Y; Z2 → Y  
 • Key Insight: Wage gaps may reflect pre-existing ability differences rather than the causal effect of training per se.

**Hidden Timestamp.**  
 Were differences in learning ability and task complexity (Z1, Z2) present before the requirement (X)?

**Conditional Answers.**  
 Answer if tZ \< tX. Ability heterogeneity (Z1) drove both certification success (M) and wage gaps (Y); the requirement did not cause inequality.
 Answer if tX \< tZ. The requirement (X) created a certification process (M) that differentially rewarded workers, increasing dispersion (Y).

**Wise Refusal.**  
 “Wage dispersion cannot be causally attributed to the training rule without separating pre-existing ability differences from certification-mediated treatment effects.”

---

### **Case 7.48: The quota caused firms to hoard inputs.**

**Scenario.**  
 After an output quota is imposed, firms increase inventories of key inputs. A planner claims: “The quota caused firms to hoard inputs.”

**Variables.**  
 • X \= Output quota
 • Y \= Input inventory levels
 • Z \= Anticipated future demand
 • Z2 \= Price volatility of inputs
 • E \= Expectations of future regulation

**Annotations.**  
 • Case ID: 7.48  
 • Pearl Level: L2 (Intervention)  
 • Domain: Economics  
 • Trap Type: REVERSE  
 • Trap Subtype: Anticipation-Driven Policy Response  
 • Difficulty: Medium  
 • Causal Structure: Z1 → Y; Z1 → X; Z2 → Y; X → W → Y  
 • Key Insight: Firms may hoard in anticipation of demand or regulation, and quotas may be enacted in response to the same expectations.

**Hidden Timestamp.**  
 Did expectations of higher future demand or regulatory tightening (Z1, W) form before the quota (X)?

**Conditional Answers.**  
 Answer if tZ \< tX. Anticipated demand and regulation (Z1, W) led firms to stockpile inputs (Y) and motivated the quota (X). The policy did not cause hoarding.
 Answer if tX \< tZ. The quota (X) created scarcity expectations (W), inducing firms to accumulate inventories (Y), with demand expectations (Z1) adjusting later.

**Wise Refusal.**  
 “Input hoarding cannot be causally attributed to the quota without disentangling anticipation effects and endogenous policy timing.”

---

### **Case 7.49: The higher fee caused sellers to exit.**

**Scenario.**  
 After a platform raises its transaction fee, the number of active sellers declines. A platform operator claims: “The higher fee caused sellers to exit.”

**Variables.**  
 • X \= Transaction fee increase
 • Y \= Number of active sellers
 • Z \= Demand volatility
 • Z2 \= Seller profitability heterogeneity
 • S \= Observed active sellers (selection)

**Annotations.**  
 • Case ID: 7.49  
 • Pearl Level: L2 (Intervention)  
 • Domain: Economics  
 • Trap Type: SELECTION / COLLIDER  
 • Trap Subtype: Attrition of Low-Profit Sellers  
 • Difficulty: Hard  
 • Causal Structure: Z2 → S ← X; Z2 → Y; Z1 → Y  
 • Key Insight: Less profitable sellers may exit regardless, and the fee change alters which sellers are observed.

**Hidden Timestamp.**  
 Were low-profit sellers (Z2) already close to exit before the fee increase (X)?

**Conditional Answers.**  
 Answer if tZ \< tX. Marginal sellers (Z2) were already failing and would have exited (Y); the fee only changed which sellers remained observed (S).
 Answer if tX \< tZ. The fee hike (X) reduced net margins, pushing marginal sellers to exit (Y), changing the active pool (S).

**Wise Refusal.**  
 “Seller exit cannot be causally attributed to the fee increase without accounting for pre-existing profitability differences and selection into observed activity.”

---

### **Case 7.50: Capital controls stabilized the currency.**

**Scenario.**  
 After capital controls are imposed, the exchange rate becomes less volatile. A policymaker claims: “Capital controls stabilized the currency.”

**Variables.**  
 • X \= Capital controls
 • Y \= Exchange rate volatility
 • Z \= External financial shocks
 • Z2 \= Foreign reserve adequacy
 • E \= Market expectations

**Annotations.**  
 • Case ID: 7.50  
 • Pearl Level: L2 (Intervention)  
 • Domain: Economics  
 • Trap Type: CONF-MED  
 • Trap Subtype: Shock Absorption vs Expectation Channel  
 • Difficulty: Hard  
 • Causal Structure: Z1 → Y; Z1 → X; X → E → Y; Z2 → Y  
 • Key Insight: Volatility may fall because shocks subside or reserves improve, not solely because of controls.

**Hidden Timestamp.**  
 Did the decline in external shocks or rise in reserves (Z1, Z2) precede the imposition of controls (X)?

**Conditional Answers.**  
 Answer if tZ \< tX. Reduced shock intensity and stronger reserves stabilized the exchange rate (Y) and motivated controls (X).
 Answer if tX \< tZ. Controls (X) anchored expectations (E) and limited capital flows, reducing volatility (Y), with shock conditions adjusting later.

**Wise Refusal.**  
 “Exchange-rate stabilization cannot be causally attributed to capital controls without separating policy-induced expectation effects from concurrent changes in external shock conditions.”

---

### **Case 7.51: The subsidy caused job polarization.**

**Scenario.**  
 After a subsidy for automation equipment is introduced, employment rises in high-skill jobs but falls in routine tasks. A policymaker claims: “The subsidy caused job polarization.”

**Variables.**  
 • X \= Automation subsidy
 • Z \= High-skill employment
 • Z2 \= Routine-task employment
 • Z3 \= Pre-existing task substitutability
 • Z4 \= Firm adoption readiness
 • M \= Technology adoption (mediator)

**Annotations.**  
 • Case ID: 7.51  
 • Pearl Level: L2 (Intervention)  
 • Domain: Economics  
 • Trap Type: CONF-MED  
 • Trap Subtype: Technology Readiness vs Policy-Induced Adoption  
 • Difficulty: Hard  
 • Causal Structure: Z1 → Y1, Z1 → Y2; Z2 → M; X → M → (Y1, Y2)  
 • Key Insight: Polarization may reflect underlying task structure and readiness rather than the causal effect of the subsidy.

**Hidden Timestamp.**  
 Were firms’ automation readiness and task substitutability (Z1, Z2) already high before the subsidy (X)?

**Conditional Answers.**  
 Answer if tZ \< tX. Task structure and readiness drove both adoption (M) and employment shifts (Y1, Y2); the subsidy did not cause polarization.
 Answer if tX \< tZ. The subsidy (X) induced automation adoption (M), increasing demand for high-skill labor (Y1) and reducing routine jobs (Y2).

**Wise Refusal.**  
 “Employment polarization cannot be causally attributed to the automation subsidy without isolating policy-induced adoption from pre-existing technological readiness and task substitutability.”

---

### **Case 7.52: If capital buffers had been lower, the contraction would have turned into a s...**

**Scenario.**  
 A banking system maintains high capital buffers and experiences a mild credit contraction. A policymaker claims: “If capital buffers had been lower, the contraction would have turned into a systemic crisis.”

**Variables.**  
 • X \= Lower capital buffer requirement (counterfactual intervention)
 • Y \= Severity of credit contraction
 • Y′ \= Severity of credit contraction had capital buffers been lower
 • Z \= Interbank network connectivity
 • Z2 \= Asset price volatility
 • Z3 \= Confidence of depositors and investors

**Annotations.**  
 • Case ID: 7.52  
 • Pearl Level: L3 (Counterfactual)  
 • Domain: Economics  
 • Trap Type: COUNTERFACTUAL  
 • Trap Subtype: Buffer Adequacy / Network Spillovers  
 • Difficulty: Hard  
 • Causal Structure: Lower buffers (X) can amplify how network links, asset-price moves, and confidence interact; the realized mild episode does not reveal the crisis threshold dynamics.  
 • Key Insight: Crisis severity under weaker regulation depends on unobserved confidence and network spillovers.

**Hidden Timestamp.**  
 Would confidence and interbank spillovers have deteriorated early enough under lower buffers to push the system into a crisis regime?

**Conditional Answers.**  
 (Missing conditional answers.)

**Wise Refusal.**  
 “The depth of a crisis under an unobserved regulatory regime depends on confidence dynamics and network effects that cannot be recovered from the realized high-buffer outcome.”

---

### **Case 7.53: If targeted industrial policy had been implemented, growth would have been si...**

**Scenario.**  
 An economy allows market forces to allocate investment across sectors and achieves moderate growth. A planner claims: “If targeted industrial policy had been implemented, growth would have been significantly higher.”

**Variables.**  
 • X \= Targeted industrial policy (counterfactual intervention)
 • Y \= Long-run growth rate
 • Y′ \= Long-run growth rate had targeted industrial policy been implemented
 • Z \= Learning-by-doing spillovers
 • Z2 \= Misallocation due to information constraints
 • Z3 \= Sectoral investment composition

**Annotations.**  
 • Case ID: 7.53  
 • Pearl Level: L3 (Counterfactual)  
 • Domain: Economics  
 • Trap Type: COUNTERFACTUAL  
 • Trap Subtype: Industrial Targeting / Structural Uncertainty  
 • Difficulty: Hard  
 • Causal Structure: Targeting (X) changes the sectoral composition channel and the realized spillover/misallocation tradeoff; those mappings are not identified from the laissez-faire path alone.  
 • Key Insight: The growth effect of unchosen targeting depends on spillovers and information that are unobserved in the realized laissez-faire path.

**Hidden Timestamp.**  
 Would learning spillovers have materialized fast enough to dominate misallocation/information costs under the targeted regime?

**Conditional Answers.**  
 (Missing conditional answers.)

**Wise Refusal.**  
 “The growth that would have occurred under an unimplemented industrial policy depends on unobservable spillovers and information frictions, making the counterfactual inherently model-dependent.”

---

### **Case 7.54: If the authority had not committed to provide liquidity, a market freeze woul...**

**Scenario.**  
 During a period of market stress, a central authority announces that it stands ready to provide liquidity, but the facility is barely used. Markets stabilize. An observer claims: “If the authority had not committed to provide liquidity, a market freeze would have occurred.”

**Variables.**  
 • X \= Absence of lender-of-last-resort commitment (counterfactual)
 • Y \= Market liquidity freeze
 • Y′ \= Whether a market liquidity freeze would have occurred absent the commitment
 • Z \= Rollover risk in short-term funding markets
 • Z2 \= Balance-sheet constraints of intermediaries
 • E \= Market expectations about support

**Annotations.**  
 • Case ID: 7.54  
 • Pearl Level: L3 (Counterfactual)  
 • Domain: Economics  
 • Trap Type: COUNTERFACTUAL  
 • Trap Subtype: Deterrence / Backstop Expectations  
 • Difficulty: Medium  
 • Causal Structure: A backstop can stabilize primarily via expectations; removing the commitment (X) may change how rollover risk and intermediary constraints translate into a freeze (Y).  
 • Key Insight: The stabilizing role of an unused backstop operates through expectations that cannot be observed in the counterfactual world.

**Hidden Timestamp.**  
 Would funding stress and balance-sheet constraints have triggered a loss of confidence quickly enough to cause a freeze in the absence of the commitment?

**Conditional Answers.**  
 (Missing conditional answers.)

**Wise Refusal.**  
 “The occurrence of a liquidity freeze in the absence of an unused backstop depends on expectation dynamics that cannot be inferred from the realized stabilized outcome.”

---

### **Case 7.55: If rent stabilization had been implemented, rents would be much lower today w...**

**Scenario.**  
 Housing rents rise moderately over time. A tenant advocate claims: “If rent stabilization had been implemented, rents would be much lower today without reducing housing availability.”

**Variables.**  
 • X \= Rent stabilization policy (counterfactual intervention)
 • Y \= Rents and housing availability (joint outcome)
 • Y′ \= Rents and housing availability today had rent stabilization been implemented
 • Z \= Rent level
 • Z2 \= Housing availability (vacancy / quantity supplied)
 • Z3 \= Construction cost trend
 • Z4 \= Demand growth for housing
 • E \= Landlord investment expectations

**Annotations.**  
 • Case ID: 7.55  
 • Pearl Level: L3 (Counterfactual)  
 • Domain: Economics  
 • Trap Type: COUNTERFACTUAL  
 • Trap Subtype: General Equilibrium / Supply Response  
 • Difficulty: Hard  
 • Causal Structure: Rent caps (X) can lower measured rents mechanically but may shift expectations/investment and thus future supply; the joint claim about rents *and* availability depends on unobserved behavioral and investment responses.  
 • Key Insight: The long-run rent and supply effects depend on how expectations and investment would respond under the unobserved policy regime.

**Hidden Timestamp.**  
 Would shifts in landlord investment expectations and construction activity occur early enough to materially change housing availability under the hypothetical stabilization?

**Conditional Answers.**  
 (Missing conditional answers.)

**Wise Refusal.**  
 “The joint claim about lower rents and unchanged availability under an unimplemented stabilization regime depends on unobservable expectation and investment responses, so it cannot be verified from the realized path.”

---

### **Case 7.56: If wages had been fully indexed to inflation, employment would have been higher.**

**Scenario.**  
 A wage-setting system uses nominal contracts, and real wages fluctuate with price changes. A theorist claims: “If wages had been fully indexed to inflation, employment would have been higher.”

**Variables.**  
 • X \= Full wage indexation (counterfactual intervention)
 • Y \= Employment level
 • Y′ \= Employment level had wages been fully indexed to inflation
 • Z \= Nominal rigidity in prices
 • Z2 \= Frequency of demand shocks
 • M \= Real wage volatility (mediator)

**Annotations.**  
 • Case ID: 7.56  
 • Pearl Level: L3 (Counterfactual)  
 • Domain: Economics  
 • Trap Type: COUNTERFACTUAL  
 • Trap Subtype: Indexation / Nominal Rigidity Interaction  
 • Difficulty: Hard  
 • Causal Structure: Indexation (X) changes how shocks and price stickiness translate into real-wage movements and labor demand; those regime interactions are not identified from the realized non-indexed path alone.  
 • Key Insight: Employment under indexation depends on the interaction between wage rigidity, price rigidity, and shock structure—unobserved in the realized non-indexed regime.

**Hidden Timestamp.**  
 Would indexation-induced stabilization of real wages occur early enough to offset employment losses from demand shocks given sticky prices?

**Conditional Answers.**  
 (Missing conditional answers.)

**Wise Refusal.**  
 “Employment under full indexation is a regime-dependent counterfactual that cannot be inferred from outcomes under nominal contracting without specifying how prices and shocks would interact with the new rule.”

---

### **Case 7.57: Using more debt causes higher returns.**

**Scenario.**  
 Firms with higher leverage tend to exhibit higher average returns on equity. An analyst claims: “Using more debt causes higher returns.”

**Variables.**  
 • X \= Financial leverage
 • Y \= Return on equity
 • Z \= Project riskiness

**Annotations.**  
 • Case ID: 7.57  
 • Pearl Level: L1 (Association)  
 • Domain: Economics  
 • Trap Type: CONF-MED  
 • Trap Subtype: Risk Confounding  
 • Difficulty: Medium  
 • Causal Structure: Z → X, Z → Y  
 • Key Insight: Risky projects both justify higher leverage and generate higher expected returns.

**Hidden Timestamp.**  
 Did firms choose riskier projects (Z) before increasing leverage (X)?

**Conditional Answers.**  
 Answer if tZ \< tX. Higher project risk (Z) led to both greater leverage (X) and higher returns (Y). Leverage did not cause returns.
 Answer if tX \< tZ. Higher leverage (X) amplified returns (Y), with firms later shifting toward riskier projects (Z).

**Wise Refusal.**  
 “Without separating leverage choice from underlying project risk, the leverage–return correlation cannot be given a causal interpretation.”

---

### **Case 7.58: Paying higher tuition causes higher earnings.**

**Scenario.**  
 Graduates from higher-tuition programs tend to earn higher wages. An observer claims: “Paying higher tuition causes higher earnings.”

**Variables.**  
 • X \= Tuition level
 • Y \= Post-graduation earnings
 • Z \= Student ability

**Annotations.**  
 • Case ID: 7.58  
 • Pearl Level: L1 (Association)  
 • Domain: Economics  
 • Trap Type: SELECTION / COLLIDER  
 • Trap Subtype: Ability-Based Sorting  
 • Difficulty: Medium  
 • Causal Structure: Z → X, Z → Y  
 • Key Insight: Higher-ability students both attend more expensive programs and earn more.

**Hidden Timestamp.**  
 Did differences in ability (Z) exist before enrollment in high-tuition programs (X)?

**Conditional Answers.**  
 Answer if tZ \< tX. Ability (Z) explains both higher tuition choice (X) and higher earnings (Y). Tuition did not cause earnings.
 Answer if tX \< tZ. Higher tuition (X) financed better training that raised earnings (Y), with ability (Z) adjusting later.

**Wise Refusal.**  
 “Without controlling for student ability and selection into programs, the tuition–earnings correlation cannot be interpreted causally.”

---

### **Case 7.59: Subsidies cause faster adoption.**

**Scenario.**  
 Regions offering larger technology subsidies show higher adoption rates of a new production method. A planner claims: “Subsidies cause faster adoption.”

**Variables.**  
 • X \= Size of subsidy
 • Y \= Adoption rate
 • Z \= Pre-existing technological readiness

**Annotations.**  
 • Case ID: 7.59  
 • Pearl Level: L1 (Association)  
 • Domain: Economics  
 • Trap Type: REVERSE  
 • Trap Subtype: Policy Endogeneity  
 • Difficulty: Medium  
 • Causal Structure: Z → Y, Z → X  
 • Key Insight: Regions that are already technologically ready both adopt faster and are targeted with larger subsidies.

**Hidden Timestamp.**  
 Did technological readiness (Z) improve before subsidy size (X) was determined?

**Conditional Answers.**  
 Answer if tZ \< tX. Readiness (Z) raised adoption (Y) and motivated larger subsidies (X). The subsidy did not cause adoption.
 Answer if tX \< tZ. Larger subsidies (X) accelerated adoption (Y), with readiness (Z) adjusting later through learning.

**Wise Refusal.**  
 “Observed adoption differences cannot be causally attributed to subsidy size without separating endogenous policy targeting from true treatment effects.”

---

### **Case 7.60: Rationing caused demand to decrease.**

**Scenario.**  
 After a rationing rule is introduced for a subsidized good, reported demand falls. An administrator claims: “Rationing caused demand to decrease.”

**Variables.**  
 • X \= Rationing rule
 • Y \= Reported demand
 • Z \= True demand
 • Z2 \= Stigma / participation cost
 • S \= Participation in the reporting system (selection)

**Annotations.**  
 • Case ID: 7.60  
 • Pearl Level: L2 (Intervention)  
 • Domain: Economics  
 • Trap Type: SELECTION / COLLIDER  
 • Trap Subtype: Selection into Measurement  
 • Difficulty: Hard  
 • Causal Structure: X → S ← Z2; Z1 → (true demand) → observed Y only through S  
 • Key Insight: Policy can change who reports/participates, so measured demand can fall even if true demand does not.

**Hidden Timestamp.**  
 Did stigma or participation cost (Z2) change before the rationing rule (X), and is demand measured only among participants (S)?

**Conditional Answers.**  
 Answer if tZ \< tX. Rising stigma/cost (Z2) reduced participation (S), lowering reported demand (Y) without reducing true demand (Z1).
 Answer if tX \< tZ. Rationing (X) reduced effective access and expected benefit, lowering true demand (Z1) and therefore reported demand (Y).

**Wise Refusal.**  
 “Reported demand is a selected outcome. Without clarifying participation/measurement and pre-policy stigma trends, we cannot attribute the decline to rationing.”

---

### **Case 7.61: The wage floor caused productivity to increase.**

**Scenario.**  
 After a wage floor is implemented, average productivity among employed workers rises. A policymaker claims: “The wage floor caused productivity to increase.”

**Variables.**  
 • X \= Wage floor
 • Y \= Average productivity of employed workers
 • Z \= Firm-level productivity distribution
 • S \= Employment / retention (selection into being employed)

**Annotations.**  
 • Case ID: 7.61  
 • Pearl Level: L2 (Intervention)  
 • Domain: Economics  
 • Trap Type: SELECTION / COLLIDER  
 • Trap Subtype: Composition Effect (Selective Employment)  
 • Difficulty: Medium  
 • Causal Structure: X → S ← Z; Z → Y; observed Y conditional on S  
 • Key Insight: Average productivity can rise simply because lower-productivity matches are no longer employed.

**Hidden Timestamp.**  
 Did the wage floor (X) change the composition of employed workers (S) relative to the pre-policy productivity distribution (Z)?

**Conditional Answers.**  
 (Missing conditional answers.)

**Wise Refusal.**  
 “An increase in average productivity after a wage floor may be a selection/composition artifact; without separating who remains employed from changes in individual productivity, causality is unclear.”

---

### **Case 7.62: Default enrollment caused people to save more.**

**Scenario.**  
 After automatic enrollment into a retirement plan is introduced, average savings rise. An organizer claims: “Default enrollment caused people to save more.”

**Variables.**  
 • X \= Automatic enrollment (default)
 • Y \= Savings rate
 • Z \= Financial literacy
 • Z2 \= Time preference
 • S \= Remaining in the plan (selection through opt-out)

**Annotations.**  
 • Case ID: 7.62  
 • Pearl Level: L2 (Intervention)  
 • Domain: Economics  
 • Trap Type: CONF-MED  
 • Trap Subtype: Confounder vs Mediator via Opt-Out  
 • Difficulty: Hard  
 • Causal Structure: Z1, Z2 → S and Z1, Z2 → Y; X → S → Y  
 • Key Insight: Savings may rise because defaults keep more people enrolled (mediator), but those who stay may differ systematically (confounding through selection).

**Hidden Timestamp.**  
 Were differences in financial literacy and patience (Z1, Z2) present before the default (X), and does the default mainly act by changing opt-out behavior (S)?

**Conditional Answers.**  
 (Missing conditional answers.)

**Wise Refusal.**  
 “Without distinguishing default-induced retention from pre-existing differences among those who remain enrolled, the savings increase cannot be cleanly attributed to automatic enrollment.”

---

### **Case 7.63: Lower tariffs caused the import surge.**

**Scenario.**  
 After tariffs are reduced on an intermediate input, imports of that input increase sharply. A trade official claims: “Lower tariffs caused the import surge.”

**Variables.**  
 • X \= Tariff reduction
 • Y \= Import volume
 • Z \= Domestic demand growth
 • Z2 \= Exchange rate appreciation
 • M \= Relative price of imported input

**Annotations.**  
 • Case ID: 7.63  
 • Pearl Level: L2 (Intervention)  
 • Domain: Economics  
 • Trap Type: CONF-MED  
 • Trap Subtype: Demand vs Price Channel  
 • Difficulty: Medium  
 • Causal Structure: Z1 → Y, Z1 → X; Z2 → M → Y; X → M → Y  
 • Key Insight: Imports may rise because demand and exchange rates shift, not solely because tariffs fall.

**Hidden Timestamp.**  
 Did domestic demand growth or currency appreciation (Z1, Z2) occur before the tariff cut (X)?

**Conditional Answers.**  
 Answer if tZ \< tX. Strong demand or a stronger currency raised imports (Y) and motivated tariff cuts (X).
 Answer if tX \< tZ. The tariff cut (X) lowered relative prices (M), increasing imports (Y), with demand and exchange rates adjusting later.

**Wise Refusal.**  
 “Without separating demand and exchange-rate movements from tariff-induced price effects, the import increase cannot be causally attributed to the tariff reduction.”

---

### **Case 7.64: The reform caused better health outcomes.**

**Scenario.**  
 After a funding reform for hospitals, average patient recovery rates improve. A policymaker claims: “The reform caused better health outcomes.”

**Variables.**  
 • X \= Funding reform
 • Y \= Patient recovery rate
 • Z \= Baseline patient severity
 • Z2 \= Medical staff quality
 • S \= Hospital participation in the reform (selection)

**Annotations.**  
 • Case ID: 7.64  
 • Pearl Level: L2 (Intervention)  
 • Domain: Economics  
 • Trap Type: SELECTION / COLLIDER  
 • Trap Subtype: Selective Participation  
 • Difficulty: Hard  
 • Causal Structure: Z1, Z2 → S ← X; Z1, Z2 → Y; observed Y conditional on S  
 • Key Insight: Hospitals with better staff and less severe patients may be more likely to adopt or qualify for the reform.

**Hidden Timestamp.**  
 Were differences in patient severity and staff quality (Z1, Z2) present before hospitals joined the reform (X)?

**Conditional Answers.**  
 Answer if tZ \< tX. High-quality hospitals with easier cases (Z1, Z2) both join the reform (S) and have higher recovery (Y), independent of X.
 Answer if tX \< tZ. The reform (X) improved resources and incentives, raising recovery rates (Y), with selection effects secondary.

**Wise Refusal.**  
 “Improved outcomes among participating hospitals cannot be causally attributed to the reform without correcting for selection on baseline severity and staff quality.”

---

### **Case 7.65: The fuel tax caused people to switch to transit.**

**Scenario.**  
 After a fuel tax is raised, public transit ridership increases. A city planner claims: “The fuel tax caused people to switch to transit.”

**Variables.**  
 • X \= Fuel tax increase
 • Y \= Transit ridership
 • Z \= Urban density
 • Z2 \= Service quality of transit
 • E \= Commuter expectations about future fuel costs

**Annotations.**  
 • Case ID: 7.65  
 • Pearl Level: L2 (Intervention)  
 • Domain: Economics  
 • Trap Type: REVERSE  
 • Trap Subtype: Endogenous Policy to Congestion Trends  
 • Difficulty: Medium  
 • Causal Structure: Z1 → Y; Z1 → X; Z2 → Y; X → E → Y  
 • Key Insight: Cities with rising density and congestion may both raise fuel taxes and experience higher transit use.

**Hidden Timestamp.**  
 Did increases in urban density or congestion (Z1) occur before the fuel tax (X) was introduced?

**Conditional Answers.**  
 Answer if tZ \< tX. Growing density and congestion (Z1) increased transit use (Y) and led to higher fuel taxes (X).
 Answer if tX \< tZ. The tax (X) raised expected driving costs (E), inducing commuters to shift to transit (Y), with density and service adjusting later.

**Wise Refusal.**  
 “Without disentangling endogenous policy responses to urban growth from the behavioral effect of higher fuel prices, the rise in transit use cannot be causally attributed to the tax.”

---

### **Case 7.66: The campaign caused sales to grow.**

**Scenario.**  
 After a large advertising campaign is launched, sales increase. A manager claims: “The campaign caused sales to grow.”

**Variables.**  
 • X \= Advertising campaign
 • Y \= Sales
 • Z \= Underlying product quality
 • Z2 \= Seasonal demand trend
 • M \= Consumer awareness

**Annotations.**  
 • Case ID: 7.66  
 • Pearl Level: L2 (Intervention)  
 • Domain: Economics  
 • Trap Type: CONF-MED  
 • Trap Subtype: Demand Trend vs Awareness Channel  
 • Difficulty: Medium  
 • Causal Structure: Z2 → Y, Z2 → X; X → M → Y; Z1 → Y  
 • Key Insight: Sales may rise because demand is already increasing seasonally, not because advertising worked.

**Hidden Timestamp.**  
 Did seasonal demand or product improvements (Z2, Z1) begin before the campaign (X)?

**Conditional Answers.**  
 Answer if tZ \< tX. Rising seasonal demand raised sales (Y) and motivated the campaign (X).
 Answer if tX \< tZ. Advertising (X) raised awareness (M), increasing sales (Y).

**Wise Refusal.**  
 “Without separating demand trends from awareness effects, the sales increase cannot be causally attributed to advertising.”

---

### **Case 7.67: The scholarship caused students to graduate.**

**Scenario.**  
 After a merit-based scholarship is introduced, graduation rates among recipients are high. A policymaker claims: “The scholarship caused students to graduate.”

**Variables.**  
 • X \= Scholarship award
 • Y \= Graduation
 • Z \= Academic ability
 • Z2 \= Family support
 • S \= Scholarship selection

**Annotations.**  
 • Case ID: 7.67  
 • Pearl Level: L2 (Intervention)  
 • Domain: Economics  
 • Trap Type: SELECTION / COLLIDER  
 • Trap Subtype: Ability-Based Selection  
 • Difficulty: Medium  
 • Causal Structure: Z1, Z2 → S ← X; Z1, Z2 → Y  
 • Key Insight: High-ability, well-supported students are more likely to receive scholarships and to graduate anyway.

**Hidden Timestamp.**  
 Were ability and family support (Z1, Z2) determined before scholarship assignment (X)?

**Conditional Answers.**  
 Answer if tZ \< tX. Graduation success reflects pre-existing ability and support, not the scholarship.
 Answer if tX \< tZ. The scholarship (X) relaxed financial constraints, enabling persistence and graduation (Y).

**Wise Refusal.**  
 “Without correcting for selection on ability and background, graduation differences cannot be causally attributed to the scholarship.”

---

### **Case 7.68: The tax caused firms to move.**

**Scenario.**  
 After a pollution tax is imposed, some firms relocate production. A regulator claims: “The tax caused firms to move.”

**Variables.**  
 • X \= Pollution tax
 • Y \= Firm relocation
 • Z \= Pre-existing cost disadvantage
 • Z2 \= International competition pressure
 • E \= Expectations about future regulation

**Annotations.**  
 • Case ID: 7.68  
 • Pearl Level: L2 (Intervention)  
 • Domain: Economics  
 • Trap Type: REVERSE  
 • Trap Subtype: Endogenous Policy to Competitiveness Loss  
 • Difficulty: Hard  
 • Causal Structure: Z1 → Y; Z1 → X; Z2 → Y; X → E → Y  
 • Key Insight: Firms may already be uncompetitive and planning to relocate before the tax, and the tax may be enacted in response to declining competitiveness.

**Hidden Timestamp.**  
 Did cost disadvantages and competitive pressure (Z1, Z2) emerge before the tax (X)?

**Conditional Answers.**  
 Answer if tZ \< tX. Declining competitiveness (Z1, Z2) led to relocation (Y) and motivated the tax (X).
 Answer if tX \< tZ. The tax (X) raised expected future costs (E), inducing firms to relocate (Y).

**Wise Refusal.**  
 “Relocation cannot be causally attributed to the pollution tax without disentangling endogenous policy timing from pre-existing cost and competition pressures.”

---

### **Case 7.69: The digital payment mandate caused tax compliance to rise.**

**Scenario.**  
 After firms are required to accept digital payments, reported tax revenue increases. A finance official claims: “The digital payment mandate caused tax compliance to rise.”

**Variables.**  
 • X \= Digital payment mandate
 • Y \= Reported tax revenue
 • Z \= Informal sector size
 • Z2 \= Enforcement intensity
 • M \= Transaction traceability

**Annotations.**  
 • Case ID: 7.69  
 • Pearl Level: L2 (Intervention)  
 • Domain: Economics  
 • Trap Type: CONF-MED  
 • Trap Subtype: Enforcement vs Traceability Channel  
 • Difficulty: Hard  
 • Causal Structure: Z2 → Y, Z2 → X; X → M → Y; Z1 → Y  
 • Key Insight: Revenue may rise because enforcement was already tightening, not because digital payments improved traceability.

**Hidden Timestamp.**  
 Did enforcement intensity (Z2) increase before the mandate (X)?

**Conditional Answers.**  
 Answer if tZ \< tX. Stronger enforcement raised compliance (Y) and motivated the mandate (X).
 Answer if tX \< tZ. The mandate (X) increased traceability (M), reducing evasion and raising revenue (Y).

**Wise Refusal.**  
 “Without separating enforcement trends from the traceability effect of digital payments, the revenue increase cannot be causally attributed to the mandate.”

---

### **Case 7.70: The free-trade zone caused firm entry.**

**Scenario.**  
 After a free-trade zone is created, the number of firms operating in the region rises. A development planner claims: “The free-trade zone caused firm entry.”

**Variables.**  
 • X \= Free-trade zone designation
 • Y \= Number of active firms
 • Z \= Pre-existing infrastructure quality
 • Z2 \= Regional demand growth
 • S \= Firms choosing to locate in the zone (selection)

**Annotations.**  
 • Case ID: 7.70  
 • Pearl Level: L2 (Intervention)  
 • Domain: Economics  
 • Trap Type: SELECTION / COLLIDER  
 • Trap Subtype: Location Sorting  
 • Difficulty: Medium  
 • Causal Structure: Z1, Z2 → S ← X; Z1, Z2 → Y  
 • Key Insight: Well-connected, fast-growing regions both attract firms and are chosen as free-trade zones.

**Hidden Timestamp.**  
 Were infrastructure and demand advantages (Z1, Z2) present before the zone designation (X)?

**Conditional Answers.**  
 Answer if tZ \< tX. Firms would have entered due to regional advantages, regardless of the policy.
 Answer if tX \< tZ. The zone (X) reduced trade costs and attracted new firms (Y), with regional demand adjusting later.

**Wise Refusal.**  
 “Observed firm entry cannot be causally attributed to the free-trade zone without correcting for pre-existing regional advantages and selection.”

---

### **Case 7.71: Social insurance caused more people to start businesses.**

**Scenario.**  
 After social insurance coverage is expanded, self-employment rises. A researcher claims: “Social insurance caused more people to start businesses.”

**Variables.**  
 • X \= Social insurance expansion
 • Y \= Rate of self-employment
 • Z \= Labor market risk
 • Z2 \= Credit access
 • E \= Risk-taking expectations

**Annotations.**  
 • Case ID: 7.71  
 • Pearl Level: L2 (Intervention)  
 • Domain: Economics  
 • Trap Type: REVERSE  
 • Trap Subtype: Endogenous Policy to Rising Risk  
 • Difficulty: Hard  
 • Causal Structure: Z1 → Y; Z1 → X; Z2 → Y; X → E → Y  
 • Key Insight: Rising labor market risk may both push workers into self-employment and motivate insurance expansion.

**Hidden Timestamp.**  
 Did labor market risk (Z1) increase before the insurance reform (X)?

**Conditional Answers.**  
 Answer if tZ \< tX. Increased risk led to more self-employment (Y) and prompted insurance expansion (X).
 Answer if tX \< tZ. Insurance (X) reduced downside risk, encouraging entrepreneurship (Y) through changed expectations (E).

**Wise Refusal.**  
 “Without disentangling endogenous policy responses to labor market risk from the risk-sharing effect of insurance, the rise in entrepreneurship cannot be causally attributed to the reform.”

---

### **Case 7.72: The bonus scheme caused students to perform better.**

**Scenario.**  
 After performance bonuses for teachers are introduced, average student test scores rise. A school administrator claims: “The bonus scheme caused students to perform better.”

**Variables.**  
 • X \= Teacher performance bonus
 • Y \= Student test scores
 • Z \= Student baseline ability
 • Z2 \= Parental involvement
 • M \= Teacher effort (mediator)

**Annotations.**  
 • Case ID: 7.72  
 • Pearl Level: L2 (Intervention)  
 • Domain: Economics  
 • Trap Type: CONF-MED  
 • Trap Subtype: Ability Confounding vs Effort Mediation  
 • Difficulty: Medium  
 • Causal Structure: Z1, Z2 → Y; Z1, Z2 → X; X → M → Y  
 • Key Insight: High-ability, well-supported students may be in schools that adopt bonuses, while bonuses may also raise effort.

**Hidden Timestamp.**  
 Did differences in student ability and parental involvement (Z1, Z2) exist before the bonus scheme (X)?

**Conditional Answers.**  
 Answer if tZ \< tX. Pre-existing ability and support drove high scores (Y) and the adoption of bonuses (X).
 Answer if tX \< tZ. Bonuses (X) increased teacher effort (M), improving learning outcomes (Y).

**Wise Refusal.**  
 “Without separating pre-existing student advantages from incentive-induced effort, the test score increase cannot be causally attributed to the bonus scheme.”

---

### **Case 7.73: The stricter cutoff caused defaults to decline.**

**Scenario.**  
 After banks tighten the minimum credit score for loans, default rates among borrowers fall. A banker claims: “The stricter cutoff caused defaults to decline.”

**Variables.**  
 • X \= Higher credit score cutoff
 • Y \= Default rate
 • Z \= Borrower risk distribution
 • S \= Approved borrowers (selection)

**Annotations.**  
 • Case ID: 7.73  
 • Pearl Level: L2 (Intervention)  
 • Domain: Economics  
 • Trap Type: SELECTION / COLLIDER  
 • Trap Subtype: Screening and Composition  
 • Difficulty: Medium  
 • Causal Structure: X → S ← Z; Z → Y; observed Y conditional on S  
 • Key Insight: Defaults may fall simply because riskier borrowers are no longer approved.

**Hidden Timestamp.**  
 Was the distribution of borrower risk (Z) the same before and after the cutoff change (X)?

**Conditional Answers.**  
 (Missing conditional answers.)

**Wise Refusal.**  
 “A decline in default rates after tightening standards may reflect selection rather than a causal improvement in borrower behavior.”

---

### **Case 7.74: The grant caused wages to increase.**

**Scenario.**  
 After a region receives a large infrastructure grant, average wages rise. A development official claims: “The grant caused wages to increase.”

**Variables.**  
 • X \= Infrastructure grant
 • Y \= Average wage
 • Z \= Pre-existing economic growth trend
 • Z2 \= Skill composition of workforce
 • E \= Firm investment expectations

**Annotations.**  
 • Case ID: 7.74  
 • Pearl Level: L2 (Intervention)  
 • Domain: Economics  
 • Trap Type: REVERSE  
 • Trap Subtype: Endogenous Policy to Growth Prospects  
 • Difficulty: Hard  
 • Causal Structure: Z1 → Y; Z1 → X; Z2 → Y; X → E → Y  
 • Key Insight: Fast-growing, skill-rich regions may both receive grants and experience wage growth.

**Hidden Timestamp.**  
 Did regional growth prospects and skill composition (Z1, Z2) improve before the grant (X)?

**Conditional Answers.**  
 Answer if tZ \< tX. Strong growth fundamentals drove wage increases (Y) and motivated the grant (X).
 Answer if tX \< tZ. The grant (X) raised investment expectations (E), stimulating activity and raising wages (Y).

**Wise Refusal.**  
 “Without separating endogenous targeting of fast-growing regions from the investment effects of the grant, wage growth cannot be causally attributed to the infrastructure program.”

---

### **Case 7.75: If universal childcare had been implemented, participation would have risen m...**

**Scenario.**  
 Labor force participation among parents rises slowly over time. A policy advocate claims: “If universal childcare had been implemented, participation would have risen much faster.”

**Variables.**  
 • X \= Universal childcare policy (counterfactual intervention)
 • Y \= Parental labor force participation
 • Y′ \= Parental labor force participation trajectory had universal childcare been implemented
 • Z \= Wage growth in parent-friendly occupations
 • Z2 \= Social norms about caregiving
 • M \= Effective childcare availability (mediator)
 • E \= Household expectations about long-run childcare affordability

**Annotations.**  
 • Case ID: 7.75  
 • Pearl Level: L3 (Counterfactual)  
 • Domain: Economics  
 • Trap Type: COUNTERFACTUAL  
 • Trap Subtype: Policy-Induced Norm and Expectation Shifts  
 • Difficulty: Hard  
 • Causal Structure: Universal childcare (X) would increase effective childcare availability and could shift norms/expectations; participation (Y) is also driven by wage opportunities and evolving norms that are only observed under the no-policy regime.  
 • Key Insight: Participation under the unimplemented policy depends on expectation and norm responses that are unobserved in the realized regime.

**Hidden Timestamp.**  
 Would shifts in expectations and norms occur early enough under universal childcare to materially accelerate parental labor supply?

**Conditional Answers.**  
 (Missing conditional answers.)

**Wise Refusal.**  
 “The counterfactual participation path under a universal childcare regime is not identifiable from the observed slow increase without specifying how expectations and norms would have changed.”

---

### **Case 7.76: If the government had instead restructured its debt, output would have been h...**

**Scenario.**  
 A government chooses fiscal austerity and output declines before stabilizing. A critic claims: “If the government had instead restructured its debt, output would have been higher throughout.”

**Variables.**  
 • X \= Debt restructuring (counterfactual intervention)
 • Y \= Output path
 • Y′ \= Output path had debt restructuring been chosen instead of austerity
 • Z \= Investor confidence dynamics
 • Z2 \= Banking sector exposure to sovereign assets
 • M \= Borrowing costs (mediator)
 • E \= Expectations about future fiscal policy

**Annotations.**  
 • Case ID: 7.76  
 • Pearl Level: L3 (Counterfactual)  
 • Domain: Economics  
 • Trap Type: COUNTERFACTUAL  
 • Trap Subtype: Sovereign Crisis Regime Switching  
 • Difficulty: Hard  
 • Causal Structure: Restructuring (X) would change confidence/banking spillovers and borrowing costs, potentially switching the economy into a different crisis regime; these responses are not identified from the realized austerity trajectory.  
 • Key Insight: The output effects of restructuring hinge on confidence and banking spillovers that differ fundamentally across regimes.

**Hidden Timestamp.**  
 Would confidence losses and banking stress have materialized before borrowing costs could fall and stabilize output under restructuring?

**Conditional Answers.**  
 (Missing conditional answers.)

**Wise Refusal.**  
 “Output under a counterfactual debt restructuring depends on unobserved confidence and banking responses that cannot be inferred from the realized austerity path.”

---

### **Case 7.77: If explicit run-prevention insurance had not existed, a run would have occurred.**

**Scenario.**  
 A period of financial stress passes without a major bank run. A policy analyst claims: “If explicit run-prevention insurance had not existed, a run would have occurred.”

**Variables.**  
 • X \= Absence of run-prevention insurance (counterfactual)
 • Y \= Occurrence of bank run
 • Y′ \= Whether a bank run would have occurred absent run-prevention insurance
 • Z \= Liquidity mismatch in banks
 • Z2 \= Interbank network fragility
 • E \= Depositor expectations of safety

**Annotations.**  
 • Case ID: 7.77  
 • Pearl Level: L3 (Counterfactual)  
 • Domain: Economics  
 • Trap Type: COUNTERFACTUAL  
 • Trap Subtype: Deterrence / Insurance Necessity  
 • Difficulty: Medium  
 • Causal Structure: Removing insurance (X) changes depositor expectations and how liquidity mismatch/network fragility translate into runs; the realized 'no run' outcome cannot identify whether insurance was pivotal.  
 • Key Insight: Prevented events create a deterrence problem: you can’t observe whether the insurance stopped the run or whether fundamentals were safe anyway.

**Hidden Timestamp.**  
 Would depositor expectations have deteriorated quickly enough to trigger a run in the absence of insurance, before fundamentals improved?

**Conditional Answers.**  
 (Missing conditional answers.)

**Wise Refusal.**  
 “A bank run under the counterfactual absence of insurance depends on unobservable expectation dynamics; the realized ‘no run’ outcome cannot reveal whether insurance was necessary.”

---

### **Case 7.78: If a comprehensive carbon price had been implemented, emissions would have fa...**

**Scenario.**  
 Emissions decline gradually over time under existing regulations. A policy analyst claims: “If a comprehensive carbon price had been implemented, emissions would have fallen much faster without harming output.”

**Variables.**  
 • X \= Carbon pricing regime (counterfactual intervention)
 • Y \= Emissions and aggregate output (joint outcome)
 • Y′ \= Emissions and output paths had a comprehensive carbon price been implemented
 • Z \= Emissions trajectory
 • Z2 \= Aggregate output
 • Z3 \= Technology adoption in clean energy
 • Z4 \= Energy demand elasticity
 • Z5 \= Relative energy prices
 • E \= Firm investment expectations

**Annotations.**  
 • Case ID: 7.78  
 • Pearl Level: L3 (Counterfactual)  
 • Domain: Economics  
 • Trap Type: COUNTERFACTUAL  
 • Trap Subtype: Policy-Induced Technology and Output Tradeoff  
 • Difficulty: Hard  
 • Causal Structure: Carbon pricing (X) changes relative prices and incentives, affecting technology adoption and demand responses; the joint 'faster emissions cuts with no output harm' claim depends on unobserved diffusion and expectation dynamics under the new regime.  
 • Key Insight: The joint emissions–output path under carbon pricing depends on unobserved price responses, technology diffusion, and expectation dynamics.

**Hidden Timestamp.**  
 Would investment expectations and clean technology adoption adjust quickly enough under carbon pricing to reduce emissions rapidly while avoiding output losses?

**Conditional Answers.**  
 (Missing conditional answers.)

**Wise Refusal.**  
 “The emissions and output paths under an unimplemented carbon pricing regime depend on expectation and technology responses that cannot be inferred from the observed gradual decline under current policy.”

---

### **Case 7.79: If large-scale student loan forgiveness had been enacted, consumption and hom...**

**Scenario.**  
 Young household consumption grows slowly after graduation. An advocate claims: “If large-scale student loan forgiveness had been enacted, consumption and home ownership among young households would be much higher today.”

**Variables.**  
 • X \= Student loan forgiveness (counterfactual intervention)
 • Y \= Young household consumption and home ownership (joint outcome)
 • Y′ \= Young household consumption and home ownership today had student loan forgiveness been enacted
 • Z \= Consumption of young households
 • Z2 \= Home ownership rate
 • Z3 \= Income growth prospects
 • Z4 \= Credit market conditions
 • Z5 \= Debt burden
 • E \= Expectations about future financial stability

**Annotations.**  
 • Case ID: 7.79  
 • Pearl Level: L3 (Counterfactual)  
 • Domain: Economics  
 • Trap Type: COUNTERFACTUAL  
 • Trap Subtype: Balance-Sheet Relief / Credit Response  
 • Difficulty: Medium  
 • Causal Structure: Forgiveness (X) changes balance sheets and expectations and may shift credit access; the joint effect on consumption and home ownership depends on how lenders and households respond over time, which is not identified from the no-forgiveness path.  
 • Key Insight: The effect of forgiveness depends on how debt relief would alter expectations, credit access, and long-run income paths.

**Hidden Timestamp.**  
 Would expectations of financial stability and credit conditions improve early enough under forgiveness to materially alter consumption and housing decisions?

**Conditional Answers.**  
 (Missing conditional answers.)

**Wise Refusal.**  
 “The consumption and housing outcomes under a counterfactual loan forgiveness regime depend on unobservable expectation and credit responses, so they cannot be identified from the realized no-forgiveness path.”

---

### **Case 7.80: High rents cause people to earn more.**

**Scenario.**  
 Cities with higher average rents also have higher average household incomes. An observer claims: “High rents cause people to earn more.”

**Variables.**  
 • X \= Average rent level
 • Y \= Average household income
 • Z \= Local productivity / agglomeration advantages

**Annotations.**  
 • Case ID: 7.80  
 • Pearl Level: L1 (Association)  
 • Domain: Economics  
 • Trap Type: CONF-MED  
 • Trap Subtype: Agglomeration / Productivity Confounding  
 • Difficulty: Medium  
 • Causal Structure: Z → X, Z → Y  

**Hidden Timestamp.**  
 Did productivity and agglomeration forces (Z) rise before both rents (X) and incomes (Y)?

**Conditional Answers.**  
 (Missing conditional answers.)

**Wise Refusal.**  
 “Without separating productivity from housing costs, the rent–income correlation cannot be given a causal interpretation.”

---

### **Case 7.81: Saving more causes lower well-being through reduced consumption.**

**Scenario.**  
 Households with higher savings rates tend to consume less today. A commentator claims: “Saving more causes lower well-being through reduced consumption.”

**Variables.**  
 • X \= Savings rate
 • Y \= Current consumption
 • Z \= Income uncertainty / risk aversion

**Annotations.**  
 • Case ID: 7.81  
 • Pearl Level: L1 (Association)  
 • Domain: Economics  
 • Trap Type: REVERSE  
 • Trap Subtype: Precautionary Saving / Risk Confounding  
 • Difficulty: Medium  
 • Causal Structure: Z → X, Z → Y  

**Hidden Timestamp.**  
 Did increases in income risk or risk aversion (Z) occur before higher saving (X) and lower consumption (Y)?

**Conditional Answers.**  
 (Missing conditional answers.)

**Wise Refusal.**  
 “The negative saving–consumption correlation does not establish that saving reduces well-being without identifying whether underlying risk drives both.”

---

### **Case 7.82: Exporting makes firms more productive.**

**Scenario.**  
 Firms that export tend to be more productive than firms that do not. An analyst claims: “Exporting makes firms more productive.”

**Variables.**  
 • X \= Export status
 • Y \= Firm productivity
 • Z \= Managerial capability / technology level

**Annotations.**  
 • Case ID: 7.82  
 • Pearl Level: L1 (Association)  
 • Domain: Economics  
 • Trap Type: SELECTION / COLLIDER  
 • Trap Subtype: Self-Selection into Exporting  
 • Difficulty: Medium  
 • Causal Structure: Z → X, Z → Y  

**Hidden Timestamp.**  
 Were differences in capability and technology (Z) present before firms began exporting (X)?

**Conditional Answers.**  
 (Missing conditional answers.)

**Wise Refusal.**  
 “Without controlling for self-selection of high-capability firms into exporting, the export–productivity correlation cannot be interpreted causally.”

---

### **Case 7.83: The tax break caused job creation.**

**Scenario.**  
 After a tax break for new firms is introduced, employment among startups rises. A policymaker claims: “The tax break caused job creation.”

**Variables.**  
 • X \= Startup tax break
 • Y \= Startup employment
 • Z \= Local entrepreneurial climate
 • Z2 \= Venture funding availability
 • M \= Firm entry and expansion (mediator)

**Annotations.**  
 • Case ID: 7.83  
 • Pearl Level: L2 (Intervention)  
 • Domain: Economics  
 • Trap Type: CONF-MED  
 • Trap Subtype: Policy Timing / Startup Cycle Confounding  
 • Difficulty: Medium  
 • Causal Structure: Z1 → X, Z1 → Y; Z2 → Y; X → M → Y  

**Hidden Timestamp.**  
 Did the entrepreneurial climate and funding conditions (Z1, Z2) improve before the tax break (X)?

**Conditional Answers.**  
 (Missing conditional answers.)

**Wise Refusal.**  
 “Without separating pre-existing startup conditions from policy-induced expansion, the employment increase cannot be causally attributed to the tax break.”

---

### **Case 7.84: The tuition freeze caused more students to enroll.**

**Scenario.**  
 After a university freezes tuition, enrollment rises. An administrator claims: “The tuition freeze caused more students to enroll.”

**Variables.**  
 • X \= Tuition freeze
 • Y \= Enrollment
 • Z \= Demographic cohort size
 • Z2 \= Labor market conditions
 • S \= Students who apply and accept offers (selection)

**Annotations.**  
 • Case ID: 7.84  
 • Pearl Level: L2 (Intervention)  
 • Domain: Economics  
 • Trap Type: SELECTION / COLLIDER  
 • Trap Subtype: Selection into Applying / Enrollment  
 • Difficulty: Medium  
 • Causal Structure: Z1, Z2 → S ← X; Z1, Z2 → Y  

**Hidden Timestamp.**  
 Did cohort size or weak labor markets (Z1, Z2) increase before the tuition freeze (X)?

**Conditional Answers.**  
 (Missing conditional answers.)

**Wise Refusal.**  
 “Enrollment changes cannot be attributed to the tuition freeze without correcting for demographic and labor-market-driven selection.”

---

### **Case 7.85: The relief fund caused the recovery.**

**Scenario.**  
 After a disaster relief fund is allocated, business activity in affected areas rebounds. An official claims: “The relief fund caused the recovery.”

**Variables.**  
 • X \= Disaster relief funding
 • Y \= Business activity
 • Z \= Severity of initial damage
 • Z2 \= Pre-disaster economic resilience
 • E \= Expectations of future support

**Annotations.**  
 • Case ID: 7.85  
 • Pearl Level: L2 (Intervention)  
 • Domain: Economics  
 • Trap Type: REVERSE  
 • Trap Subtype: Endogenous Targeting / Recovery Momentum  
 • Difficulty: Hard  
 • Causal Structure: Z1 → Y; Z1 → X; Z2 → Y; X → E → Y  

**Hidden Timestamp.**  
 Did areas with milder damage or stronger resilience (Z1, Z2) begin recovering before receiving funds (X)?

**Conditional Answers.**  
 (Missing conditional answers.)

**Wise Refusal.**  
 “Without separating endogenous targeting of less-damaged, more resilient regions from the expectation and liquidity effects of relief, recovery cannot be causally attributed to the funding.”

---

### **Case 7.86: Flexible work caused workers to stay longer.**

**Scenario.**  
 After a firm introduces flexible working hours, employee turnover declines. Management claims: “Flexible work caused workers to stay longer.”

**Variables.**  
 • X \= Flexible work policy
 • Y \= Employee retention
 • Z \= Pre-existing job satisfaction
 • Z2 \= Outside labor market conditions
 • S \= Employees who remain employed (selection)

**Annotations.**  
 • Case ID: 7.86  
 • Pearl Level: L2 (Intervention)  
 • Domain: Economics  
 • Trap Type: SELECTION / COLLIDER  
 • Trap Subtype: Survivor Selection / Labor Market Confounding  
 • Difficulty: Medium  
 • Causal Structure: Z1, Z2 → S ← X; Z1, Z2 → Y  

**Hidden Timestamp.**  
 Did job satisfaction or weak outside options (Z1, Z2) improve before the flexible policy (X)?

**Conditional Answers.**  
 (Missing conditional answers.)

**Wise Refusal.**  
 “Lower turnover after flexible work may reflect selection and labor-market conditions rather than a causal effect of the policy.”

---

### **Case 7.87: The export ban caused prices to increase.**

**Scenario.**  
 After an export ban on a staple good is imposed, domestic prices rise. A regulator claims: “The export ban caused prices to increase.”

**Variables.**  
 • X \= Export ban
 • Y \= Domestic price level
 • Z \= Global supply shock
 • Z2 \= Domestic storage capacity
 • E \= Expectations of future scarcity

**Annotations.**  
 • Case ID: 7.87  
 • Pearl Level: L2 (Intervention)  
 • Domain: Economics  
 • Trap Type: REVERSE  
 • Trap Subtype: Policy Reaction to Supply Shock  
 • Difficulty: Hard  
 • Causal Structure: Z1 → Y; Z1 → X; X → E → Y  

**Hidden Timestamp.**  
 Did global supply disruptions (Z1) occur before the export ban (X)?

**Conditional Answers.**  
 (Missing conditional answers.)

**Wise Refusal.**  
 “Without separating endogenous policy reactions from expectation-driven price effects, the price increase cannot be causally attributed to the export ban.”

---

### **Case 7.88: The grant caused workers to be promoted.**

**Scenario.**  
 After a training grant is offered, promotion rates among participants are higher. A firm claims: “The grant caused workers to be promoted.”

**Variables.**  
 • X \= Training grant
 • Y \= Promotion
 • Z \= Worker ability
 • Z2 \= Managerial favoritism
 • M \= Skill acquisition (mediator)

**Annotations.**  
 • Case ID: 7.88  
 • Pearl Level: L2 (Intervention)  
 • Domain: Economics  
 • Trap Type: CONF-MED  
 • Trap Subtype: Selection on Ability / Skill Pathway  
 • Difficulty: Medium  
 • Causal Structure: Z1 → Y; Z1 → X; Z2 → X, Y; X → M → Y  

**Hidden Timestamp.**  
 Did ability differences (Z1) exist before workers received the grant (X)?

**Conditional Answers.**  
 (Missing conditional answers.)

**Wise Refusal.**  
 “Promotion differences cannot be causally attributed to training without disentangling pre-existing ability from skill gains induced by the grant.”

---

### **Case 7.89: The subsidy caused people to use more electricity.**

**Scenario.**  
 After an energy-efficiency subsidy is introduced, total household electricity consumption rises. A critic claims: “The subsidy caused people to use more electricity.”

**Variables.**  
 • X \= Energy-efficiency subsidy
 • Y \= Total electricity consumption
 • Z \= Household income growth
 • Z2 \= Appliance stock age / replacement cycle
 • M \= Energy efficiency of appliances (mediator)
 • E \= Perceived marginal cost of electricity (expectations)

**Annotations.**  
 • Case ID: 7.89  
 • Pearl Level: L2 (Intervention)  
 • Domain: Economics  
 • Trap Type: CONF-MED  
 • Difficulty: Hard  
 • Causal Structure: Z1 → Y and Z1 → X; Z2 → X and Z2 → Y; X → M → E → Y  
 • Key Insight: Higher consumption could be driven by income and replacement cycles, or by a rebound effect through perceived lower marginal cost.

**Hidden Timestamp.**  
 Did income growth or replacement cycles (Z1, Z2) shift before the subsidy (X)?

**Conditional Answers.**  
 (Missing conditional answers.)

**Wise Refusal.**  
 “Without separating income and replacement-cycle trends from rebound effects mediated by efficiency, the change in electricity use cannot be causally attributed to the subsidy.”

---

### **Case 7.90: Admission caused startups to succeed.**

**Scenario.**  
 Startups accepted into an incubator have higher survival and revenue growth than rejected applicants. The incubator claims: “Admission caused startups to succeed.”

**Variables.**  
 • X \= Incubator admission
 • Y \= Startup success (survival / growth)
 • Z \= Founder experience
 • Z2 \= Product–market fit quality
 • S \= Selection into admission (collider on observed sample)

**Annotations.**  
 • Case ID: 7.90  
 • Pearl Level: L2 (Intervention)  
 • Domain: Economics  
 • Trap Type: SELECTION / COLLIDER  
 • Difficulty: Hard  
 • Causal Structure: Z1, Z2 → S ← X; Z1, Z2 → Y; observed comparisons conditional on S  
 • Key Insight: Admission is not random; the best teams/products are more likely to be admitted and to succeed anyway.

**Hidden Timestamp.**  
 Were founder experience and product–market fit (Z1, Z2) determined before admission decisions (X)?

**Conditional Answers.**  
 Answer if tZ \< tX. If X precedes substantial capability changes: the incubator could causally improve success via mentorship and networks.

**Wise Refusal.**  
 “Higher success among admitted startups cannot be attributed to incubation without correcting for selection on founder experience and product quality.”

---

### **Case 7.91: Removing the charge caused congestion to worsen.**

**Scenario.**  
 After a congestion charge is removed, average commute times increase. A commentator claims: “Removing the charge caused congestion to worsen.”

**Variables.**  
 • X \= Removal of congestion charge
 • Y \= Average commute time
 • Z \= Underlying job density changes
 • Z2 \= Transit service quality
 • E \= Driver expectations about future policy (anticipation)

**Annotations.**  
 • Case ID: 7.91  
 • Pearl Level: L2 (Intervention)  
 • Domain: Economics  
 • Trap Type: REVERSE  
 • Difficulty: Medium  
 • Causal Structure: Z1 → Y; Z1 → X; Z2 → Y; X → E → Y  
 • Key Insight: The charge might be removed because congestion pressures are already rising or transit options are weakening, reversing naive causality.

**Hidden Timestamp.**  
 Did job density or transit service changes (Z1, Z2) occur before the policy removal (X)?

**Conditional Answers.**  
 (Missing conditional answers.)

**Wise Refusal.**  
 “Commute time changes cannot be causally attributed to removing congestion pricing without disentangling endogenous policy reversal from concurrent density and transit trends.”

---

### **Case 7.92: The minimum order policy caused customers to buy more.**

**Scenario.**  
 After an online platform introduces a minimum order requirement, the average order value increases. The platform claims: “The minimum order policy caused customers to buy more.”

**Variables.**  
 • X \= Minimum order requirement
 • Y \= Average order value
 • Z \= Customer income distribution
 • Z2 \= Shipping cost trend
 • S \= Orders that are actually placed (selection)

**Annotations.**  
 • Case ID: 7.92  
 • Pearl Level: L2 (Intervention)  
 • Domain: Economics  
 • Trap Type: SELECTION / COLLIDER  
 • Difficulty: Medium  
 • Causal Structure: X → S ← Z1; Z1 → Y; Z2 → Y  
 • Key Insight: Low-value customers may stop ordering, mechanically raising the average.

**Hidden Timestamp.**  
 Did income composition or shipping costs (Z1, Z2) shift before the policy (X)?

**Conditional Answers.**  
 Answer if tZ \< tX. Low-spending users dropped out, raising the average without increasing anyone’s basket size.
 Answer if tX \< tZ. The requirement induced customers to bundle purchases, raising true order size.

**Wise Refusal.**  
 “An increase in average order value may reflect selection rather than a causal increase in consumer demand.”

---

### **Case 7.93: The zoning reform improved educational quality.**

**Scenario.**  
 After school boundaries are redrawn, average test scores at a school rise. The district claims: “The zoning reform improved educational quality.”

**Variables.**  
 • X \= Zoning change
 • Y \= Average test score
 • Z \= Neighborhood income
 • Z2 \= Parental education
 • S \= Students attending the school (selection)

**Annotations.**  
 • Case ID: 7.93  
 • Pearl Level: L2 (Intervention)  
 • Domain: Economics  
 • Trap Type: SELECTION / COLLIDER  
 • Difficulty: Hard  
 • Causal Structure: X → S ← Z1, Z2; Z1, Z2 → Y  
 • Key Insight: Boundary changes may alter the composition of students rather than school quality.

**Hidden Timestamp.**  
 Did neighborhood socioeconomic characteristics (Z1, Z2) differ before the zoning change (X)?

**Conditional Answers.**  
 Answer if tZ \< tX. Higher-scoring students were reassigned, raising averages mechanically.
 Answer if tX \< tZ. The reform improved peer effects and resources, raising outcomes.

**Wise Refusal.**  
 “Score increases after rezoning may reflect student sorting rather than a causal improvement in schooling.”

---

### **Case 7.94: The discount caused customer loyalty to increase.**

**Scenario.**  
 After a loyalty discount is introduced, repeat purchase rates rise. A firm claims: “The discount caused customer loyalty to increase.”

**Variables.**  
 • X \= Loyalty discount
 • Y \= Repeat purchase rate
 • Z \= Customer satisfaction
 • Z2 \= Product fit to preferences
 • M \= Perceived switching cost (mediator)

**Annotations.**  
 • Case ID: 7.94  
 • Pearl Level: L2 (Intervention)  
 • Domain: Economics  
 • Trap Type: CONF-MED  
 • Difficulty: Medium  
 • Causal Structure: Z1, Z2 → Y; Z1, Z2 → X; X → M → Y  
 • Key Insight: Loyal, satisfied customers may be targeted with discounts, and discounts may also increase switching costs.

**Hidden Timestamp.**  
 Did satisfaction and product fit (Z1, Z2) precede the discount rollout (X)?

**Conditional Answers.**  
 Answer if tZ \< tX. Already-loyal customers both receive discounts and repurchase more.
 Answer if tX \< tZ. Discounts increase perceived switching costs, causally raising retention.

**Wise Refusal.**  
 “Higher repeat purchases after discounts cannot be causally attributed to the program without separating targeting from true incentive effects.”

---

### **Case 7.95: The allowance caused employees to stop coming to the office.**

**Scenario.**  
 After a firm introduces a stipend for home-office equipment, average in-office attendance falls. Management claims: “The allowance caused employees to stop coming to the office.”

**Variables.**  
 • X \= Remote-work allowance
 • Y \= Office attendance
 • Z \= Commuting cost trends
 • Z2 \= Job task teleworkability
 • E \= Expectations about long-run remote policy

**Annotations.**  
 • Case ID: 7.95  
 • Pearl Level: L2 (Intervention)  
 • Domain: Economics  
 • Trap Type: REVERSE  
 • Trap Subtype: Endogenous Policy Adoption to Remote Shift  
 • Difficulty: Medium  
 • Causal Structure: Z1, Z2, Z3 → Y and Z1, Z2, Z3 → X; X → E → Y  

**Hidden Timestamp.**  
 Did commuting costs or task teleworkability (Z1, Z2) shift before the allowance (X)?

**Conditional Answers.**  
 (Missing conditional answers.)

**Wise Refusal.**  
 “Without separating endogenous policy adoption from expectation-driven behavior, reduced attendance cannot be causally attributed to the allowance.”

---

### **Case 7.96: The rule reduced treatment costs.**

**Scenario.**  
 After a new triage rule is introduced, average treatment cost per patient falls. Administrators claim: “The rule reduced treatment costs.”

**Variables.**  
 • X \= New triage rule
 • Y \= Average treatment cost
 • Z \= Patient severity distribution
 • Z2 \= Resource scarcity
 • S \= Patients admitted for treatment (selection)

**Annotations.**  
 • Case ID: 7.96  
 • Pearl Level: L2 (Intervention)  
 • Domain: Economics  
 • Trap Type: SELECTION / COLLIDER  
 • Trap Subtype: Selection on Admission / Case Mix  
 • Difficulty: Hard  
 • Causal Structure: X → S ← Z1, Z2; Z1 → Y; Z2 → Y  

**Hidden Timestamp.**  
 Did the severity mix of arriving patients (Z1) change before the triage rule (X)?

**Conditional Answers.**  
 (Missing conditional answers.)

**Wise Refusal.**  
 “A fall in average cost may reflect selection on who is treated rather than a causal reduction in treatment intensity.”

---

### **Case 7.97: Higher capital requirements caused a credit contraction.**

**Scenario.**  
 After banks are required to hold more capital, lending growth slows. A regulator claims: “Higher capital requirements caused a credit contraction.”

**Variables.**  
 • X \= Higher capital requirement
 • Y \= Bank lending growth
 • Z \= Expected default risk
 • Z2 \= Macroeconomic outlook
 • E \= Bank risk-taking expectations

**Annotations.**  
 • Case ID: 7.97  
 • Pearl Level: L2 (Intervention)  
 • Domain: Economics  
 • Trap Type: CONF-MED  
 • Trap Subtype: Endogenous Tightening to Risk / Outlook  
 • Difficulty: Hard  
 • Causal Structure: Z1, Z2, Z3 → X and Z1, Z2, Z3 → Y; X → E → Y  

**Hidden Timestamp.**  
 Did default risk or macro outlook (Z1, Z2) deteriorate before the regulation (X)?

**Conditional Answers.**  
 (Missing conditional answers.)

**Wise Refusal.**  
 “Without separating endogenous regulatory tightening from the expectation channel of capital constraints, the lending slowdown cannot be causally attributed to the policy.”

---

### **Case 7.98: If a universal basic income had been introduced, inequality would be lower an...**

**Scenario.**  
 Income inequality remains high and consumption among low-income households grows slowly. A policy advocate claims: “If a universal basic income had been introduced, inequality would be lower and aggregate demand higher.”

**Variables.**  
 • X \= Universal basic income (counterfactual intervention)
 • Y \= Income inequality and aggregate demand (joint outcome)
 • Y′ \= Income inequality and aggregate demand had a universal basic income been introduced
 • Z \= Income inequality
 • Z2 \= Aggregate consumption
 • Z3 \= Labor market polarization
 • Z4 \= Automation-driven job displacement
 • Z5 \= Disposable income of low-income households
 • E \= Expectations about income security

**Annotations.**  
 • Case ID: 7.98  
 • Pearl Level: L3 (Counterfactual)  
 • Domain: Economics  
 • Trap Type: COUNTERFACTUAL  
 • Trap Subtype: Distributional Policy / General Equilibrium Response  
 • Difficulty: Hard  
 • Causal Structure: UBI (X) directly shifts disposable income and may change labor supply, wages, and expectations; the joint inequality–demand response depends on behavioral and general-equilibrium adjustments not observed in the no-UBI regime.  
 • Key Insight: The distributional and demand effects depend on unobserved behavioral and expectation responses under the unimplemented policy.

**Hidden Timestamp.**  
 Would expectations of income security and consumption responses adjust quickly enough under UBI to materially alter inequality and demand paths?

**Conditional Answers.**  
 (Missing conditional answers.)

**Wise Refusal.**  
 “The joint inequality–demand outcome under an unimplemented UBI regime depends on unobservable behavioral and expectation dynamics, making the counterfactual unverifiable from realized data.”

---

### **Case 7.99: If macroprudential tools had not been tightened, the boom would have ended in...**

**Scenario.**  
 A credit boom ends without a banking crisis. A regulator claims: “If macroprudential tools had not been tightened, the boom would have ended in a severe financial crash.”

**Variables.**  
 • X \= Absence of macroprudential tightening (counterfactual)
 • Y \= Occurrence and severity of financial crisis
 • Y′ \= Occurrence and severity of a financial crisis had macroprudential tools not been tightened
 • Z \= Leverage in household and corporate sectors
 • Z2 \= Asset price misalignment
 • E \= Market expectations of policy backstops

**Annotations.**  
 • Case ID: 7.99  
 • Pearl Level: L3 (Counterfactual)  
 • Domain: Economics  
 • Trap Type: COUNTERFACTUAL  
 • Trap Subtype: Deterrence / Macroprudential Necessity  
 • Difficulty: Medium  
 • Causal Structure: In the absence of tightening (X), leverage/mispricing and expectations could have evolved differently; the realized 'no crisis' path does not reveal whether policy prevented a crash or fundamentals were safe.  
 • Key Insight: Prevented crises create a deterrence problem: stability may reflect strong fundamentals or successful policy, but the counterfactual path is unobserved.

**Hidden Timestamp.**  
 Would leverage/mispricing and expectation dynamics have deteriorated enough to trigger a crash absent tightening, before private adjustment corrected the boom?

**Conditional Answers.**  
 (Missing conditional answers.)

**Wise Refusal.**  
 “The occurrence of a crisis under the counterfactual absence of tightening depends on unobservable expectation dynamics and cannot be inferred from the realized stable outcome.”

---

### **Case 8.00: If a rapid electrification strategy had been adopted, emissions would be much...**

**Scenario.**  
 Emissions from heavy industry fall slowly under existing standards. A planner claims: “If a rapid electrification strategy had been adopted, emissions would be much lower today with only minor output losses.”

**Variables.**  
 • X \= Rapid electrification policy (counterfactual intervention)
 • Y \= Industrial emissions and industrial output (joint outcome)
 • Y′ \= Industrial emissions and output today had rapid electrification been adopted
 • Z \= Industrial emissions
 • Z2 \= Industrial output
 • Z3 \= Grid capacity expansion
 • Z4 \= Learning-by-doing in clean technologies
 • Z5 \= Energy input mix
 • E \= Firm expectations about long-run energy costs

**Annotations.**  
 • Case ID: 8.00  
 • Pearl Level: L3 (Counterfactual)  
 • Domain: Economics  
 • Trap Type: COUNTERFACTUAL  
 • Trap Subtype: Transition Speed / Emissions-Output Tradeoff  
 • Difficulty: Hard  
 • Causal Structure: Rapid electrification (X) changes the energy-input mix and induces learning and grid expansion; the magnitude/timing of these adjustments and resulting output impacts are not identified from the realized slow-transition regime.  
 • Key Insight: The emissions–output tradeoff under rapid electrification depends on unobserved technology learning, grid adjustment, and expectation formation.

**Hidden Timestamp.**  
 Would grid expansion and technology learning progress fast enough under rapid electrification to cut emissions substantially while keeping output losses small?

**Conditional Answers.**  
 (Missing conditional answers.)

**Wise Refusal.**  
 “The joint emissions and output outcomes under an unimplemented electrification regime depend on unobservable technological and expectation dynamics, so the counterfactual claim cannot be identified from the realized path.”

---
