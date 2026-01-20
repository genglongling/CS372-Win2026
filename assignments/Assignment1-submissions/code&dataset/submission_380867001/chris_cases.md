# CS372 Assignment 1 - Economics Benchmark Cases

**Author:** Chris Pearce
**Total Cases:** 116

---

## **Case 5.200: Left-Truncation combined with Age-Maturation Bias**

**Scenario.**

A state education department implemented a 'Third-Grade Gate' policy (X), requiring that any student scoring in the bottom 10% on a standardized reading exam be retained in third grade. Two years later, the state's average fourth-grade reading scores (Y) surged from the bottom quartile to the top quartile nationally.

**Claim.**

"The retention policy improved educational outcomes by ensuring students mastered fundamentals before advancing."

**Variables.**

- **X** = Retention Policy (Intervention)
- **Y** = 4th Grade Average Score (Outcome)
- **Z1** = Statistical Truncation (Removal of Low Scorers) (Mediator)
- **Z2** = Biological Age / Maturation (Mediator)

**Annotations.**

- **Case ID:** 5.200
- **Pearl Level:** L2 (Intervention)
- **Domain:** D5 (Economics)
- **Trap Type:** SELECTION
- **Trap Subtype:** Compound_Composition_Bias
- **Difficulty:** Hard
- **Causal Structure:** X → Z; Z → Y

**Hidden Timestamp.**

Did the retained students show different learning trajectories or family characteristics before the retention decision, or were they comparable to students who narrowly avoided retention?

**Gold Rationale.**

The score surge is likely driven by a dual composition effect rather than improved instruction. First, the policy causes Left-Truncation (Z1): by holding back the lowest scorers, the 4th-grade cohort is temporarily cleansed of its bottom tail, mechanically raising the average. Second, it introduces Age Bias (Z2): when the retained students eventually take the 4th-grade test, they are a year older (10 vs 9).  Reading fluency correlates strongly with biological age and brain development. The result is a distorted metric where an 'older, truncated' cohort is being compared to a 'younger, full' cohort from previous years. To prove efficacy, one must control for Age (Z2) and track the cohort through 8th grade to see if the gains persist once the truncation effect fades.

**Wise Refusal.**

"Is the improvement visible in Age-Standardized scores, or only Grade-Standardized scores? If 10-year-old 4th graders are barely outperforming 9-year-old 4th graders, the 'gain' is simply a function of age (Z2). Please provide the data stratified by birth year."

---

## **Case 5.201: Retiming vs. Permanent Growth**

**Scenario.**

A government announced in July that the Capital Gains Tax rate would be cut from 28% to 20%, effective January 1st. In the first year under the new lower rate, total tax revenue collected from capital gains actually increased by 15% compared to the previous year.

**Claim.**

"The tax cut successfully stimulated economic growth and investment, expanding the tax base enough to pay for itself."

**Variables.**

- **X** = Tax Rate Cut (Intervention)
- **Y** = Tax Revenue (Outcome)
- **Z1** = Timing of Asset Sales (Realization Effect) (Mediator)

**Annotations.**

- **Case ID:** 5.201
- **Pearl Level:** L2 (Intervention)
- **Domain:** D5 (Economics)
- **Trap Type:** MECHANISM
- **Trap Subtype:** Intertemporal_Substitution
- **Difficulty:** Hard
- **Causal Structure:** X → Z1; Z1 → Y

**Hidden Timestamp.**

Did investors begin reduce asset sales (Z) before the tax cut announcement in anticipation of the change, or did the selling behavior only emerge after the announcement?

**Answer if t(Z) < t(X) (Confounder Scenario).**

Investors deferred asset sales to benefit from the policy change

**Answer if t(X) < t(Z) (Causal Scenario).**

The policy change increased asset sales above the prior baseline, potentially indicating a sustained growth in tax revenue

**Gold Rationale.**

The claim mistakes a one-time 'stock adjustment' for a permanent 'flow' increase. When a tax cut is announced, rational actors engage in Intertemporal Substitution: they delay selling assets (realizing gains) until the new lower rate kicks in.  The 15% revenue surge is likely due to investors selling a backlog of assets they held onto specifically to wait for the cut (Z). This is an accounting shift (Retiming), not necessarily a sign that the underlying economy grew or that the lower rate is sustainable. Typically, this 'realization effect' vanishes in Year 2, causing revenue to drop significantly below the pre-cut baseline.

**Wise Refusal.**

"Did the revenue increase persist into Year 2 and Year 3? If the spike was isolated to Year 1, it was driven by the timing of sales (unlocking pent-up realizations) rather than structural economic expansion. Please provide the 3-year revenue trend."

---

## **Case 5.202: Circular Flow Failure (Deadlock)**

**Scenario.**

During a logistics crisis, a rail network issued a directive designating specific trains as 'Priority Alpha'. These trains were granted absolute right-of-way over other traffic, and non-Alpha trains were held in sidings until the Alpha traffic had passed. Two weeks later, the total volume of Priority Alpha deliveries had dropped by 8.1%, and overall deliveries across the network had dropped by 12.3%.

**Claim.**

"The drop in delivery volume suggests that senior management rushed the introduction of the system. The complexity of the multi-tier system and its speed of introduction overwhelmed mid-level management, causing the coordination of the entire network to degrade."

**Variables.**

- **X** = Priority Alpha Directive (Intervention)
- **Y** = Delivery Volume (Alpha and Overall) (Outcome)
- **Z1** = Rolling Stock Circulation (Empty Return Path) (Mediator)

**Annotations.**

- **Case ID:** 5.202
- **Pearl Level:** L2 (Intervention)
- **Domain:** D5 (Economics)
- **Trap Type:** MECHANISM
- **Trap Subtype:** Return_Path_Starvation
- **Difficulty:** Hard
- **Causal Structure:** X → Z; Z → Y

**Hidden Timestamp.**

Did network congestion and coordination problems exist before the Priority Alpha system was implemented, or did these issues emerge as a result of the new prioritization rules?

**Gold Rationale.**

The claim misidentifies a structural network failure as a managerial coordination error. A logistics network is not a one-way pipeline but a Circular Flow.  To sustain 'Priority Alpha' deliveries, the system must return empty wagons and engines to the loading terminals. By granting absolute right-of-way to forward-moving traffic (X), the directive inadvertently 'starved' the return path (Z). Returning empty trains were held in sidings to wait for Alpha traffic; once the sidings reached capacity, the entire network entered a Systemic Deadlock. The drop in volume (Y) is a mathematical certainty of blocking the return cycle, regardless of how 'organized' or 'rushed' the management team was. The solution is not better management, but reducing the priority intensity to allow for network circulation.

**Wise Refusal.**

"Did the availability of empty wagons at the loading terminals decrease following the directive? If the origin points were ready to ship but lacked the physical rolling stock to do so, the issue is 'Network Circulation' rather than 'Management Complexity'. Please provide the 'Wagon Turnaround Time' data."

---

## **Case 5.203: Economic conditions drive both policy adoption and outcomes**

**Scenario.**

Following a major financial crisis, a central bank purchased large quantities of long-term government bonds and mortgage-backed securities through a bond-buying program (QE). During this period, long-term interest rates fell from 4% to under 2%, and the economy gradually recovered.

**Claim.**

"The central bank's bond-buying program successfully lowered long-term interest rates, which stimulated borrowing and investment, proving it is an effective monetary policy tool for future crises."

**Variables.**

- **X** = Quantitative Easing bond purchases (Intervention)
- **Y** = Lower long-term interest rates / economic recovery (Outcome)
- **Z1** = Flight to safety during crisis (Common Cause)
- **Z2** = Weak economic growth reducing credit demand (Common Cause)

**Annotations.**

- **Case ID:** 5.203
- **Pearl Level:** L2 (Intervention)
- **Domain:** D5 (Economics)
- **Trap Type:** CONF-MED
- **Trap Subtype:** Economic_Conditions_Confounder
- **Difficulty:** Easy
- **Causal Structure:** Z → X; Z → Y

**Hidden Timestamp.**

When did the flight-to-safety demand for government bonds and the decline in credit demand from weak growth begin relative to when the central bank announced and implemented its bond-buying program?

**Answer if t(Z) < t(X) (Confounder Scenario).**

If investors were already fleeing to safe government bonds and credit demand was already falling before QE was announced, then long-term rates were declining due to these market forces independent of central bank action. The QE program may have simply coincided with - or at most reinforced - a rate decline that was already underway.

**Answer if t(X) < t(Z) (Causal Scenario).**

If the bond-buying program preceded the flight to safety and the decline in credit demand, then QE may have directly lowered rates, and these lower rates could have contributed to the conditions that reduced borrowing demand or encouraged safe-haven behavior. This would support the claim that QE was the initiating cause.

**Gold Rationale.**

Yields fell during QE, but the severe recession and financial crisis independently drove rates lower through flight-to-safety (investors seeking safe assets), and weak economic growth reducing credit demand. Most rigorous research suggests QE's impact was modest (50-100 basis points), not the full 200+ point decline.

**Wise Refusal.**

"When did flight-to-safety demand for government bonds and credit demand decline begin relative to the central bank's bond-buying program? If these shifts preceded QE, the yield decline reflects macro conditions rather than policy effectiveness."

---

## **Case 5.204: Supply-side factors explain outcome attributed to demand-side mechanism**

**Scenario.**

Over a two-year recovery period following a severe economic shock, unemployment fell from 7% to 3.5% - near historic lows. During the same period, inflation rose from 1.5% to 9% before aggressive central bank rate hikes brought it back toward target.

**Claim.**

"This inflation episode demonstrates the Phillips Curve relationship: when labor markets become too tight, wage pressures drive up prices."

**Variables.**

- **X** = Tight labor markets / low unemployment (Intervention)
- **Y** = Inflation surge (Outcome)
- **Z1** = Supply chain disruptions (Common Cause)
- **Z2** = Energy price shocks (Common Cause)
- **Z3** = Large fiscal stimulus (Common Cause)
- **Z4** = Crisis-induced demand shifts (goods vs services) (Common Cause)

**Annotations.**

- **Case ID:** 5.204
- **Pearl Level:** L2 (Intervention)
- **Domain:** D5 (Economics)
- **Trap Type:** CONF-MED
- **Trap Subtype:** Supply_Shock_Confounding
- **Difficulty:** Easy
- **Causal Structure:** Z1 → Y; Z2 → Y; Z3 → X; Z3 → Y; Z4 → Y

**Hidden Timestamp.**

Did confounding effects such as Z1: Supply chain disruptions, Z2: Energy price shocks, Z3: Large fiscal stimulus or Z4: Crisis-induced demand shifts precede the inflation spike

**Answer if t(Z) < t(X) (Confounder Scenario).**

If supply chain disruptions, energy shocks, and fiscal stimulus were already driving up prices before the labor market became exceptionally tight, then inflation may have caused tight labor markets rather than the reverse. The Phillips Curve interpretation would be backwards.

**Answer if t(X) < t(Z) (Causal Scenario).**

If the labor market was already very tight before supply shocks and stimulus hit, then wage pressures from labor scarcity could indeed have been the initial inflation driver. This would support the Phillips Curve interpretation that tight labor markets generate inflation.

**Gold Rationale.**

The timing may contradict the Phillips Curve narrative: if inflation surges when unemployment is still elevated, before labor markets tighten, this undermines the wage-push story. The magnitude (1.5% to 9%) far exceeds what wage pressures could produce. If real wages fall during the episode, meaning wages lag prices, this is the opposite of wage-push inflation. A global inflation surge across countries with different labor conditions points to common supply shocks (energy, shipping, semiconductors) and fiscal stimulus rather than domestic labor market tightness. The Phillips Curve framework may not explain such dynamics.

**Wise Refusal.**

"Did supply chain disruptions, energy shocks, and fiscal stimulus spending begin before the labor market reached current tightness levels? If so, the inflation surge may reflect supply factors and lagged fiscal effects rather than labor market overheating."

---

## **Case 5.205: Institution claims credit for preventing unobservable catastrophe**

**Scenario.**

During a sudden market panic triggered by an external shock, a central bank announced emergency lending facilities for money market funds, corporate bonds, and municipal debt. Markets stabilized within weeks. Central bank officials later testified that without intervention, a 'complete financial collapse' was imminent.

**Claim.**

"The central bank's emergency interventions prevented a systemic financial collapse, demonstrating that aggressive bailout programs are essential tools for maintaining financial stability during crises."

**Variables.**

- **X** = Central bank emergency lending facilities (Intervention)
- **Y** = Financial stability / avoided collapse (Outcome)
- **Y0** = Counterfactual outcome for Financial stability / avoided collapse (Counterfactual Outcome)
- **Z1** = Counterfactual collapse scenario (Unobservable)
- **Z2** = Fiscal stimulus (simultaneous) (Confounder)
- **Z3** = Private sector adjustment capacity (Alternative Mechanism)

**Annotations.**

- **Case ID:** 5.205
- **Pearl Level:** L3 (Counterfactual)
- **Domain:** D5 (Economics)
- **Trap Type:** COUNTERFACTUAL
- **Trap Subtype:** Self_Serving_Institutional_Claim
- **Difficulty:** Medium
- **Causal Structure:** Z1 → X; Z1 → Y; X → Y

**The Counterfactual Query.**

Would markets have stabilized without central bank intervention?

**The Counterfactual Structure.**

Comparing observed stability after intervention vs hypothetical trajectory without intervention.

**Ground Truth.**

**Answer:** CONDITIONAL

Multiple factors contributed to stabilization (fiscal policy, natural market adjustment); isolating central bank effect requires knowing counterfactual trajectory.

**Gold Rationale.**

This is an unverifiable counterfactual with self-serving institutional bias. 'Complete financial collapse' is a worst-case scenario that cannot be proven or disproven. Markets stabilized after multiple simultaneous interventions (central bank facilities, fiscal stimulus, crisis measures), making it impossible to attribute success to central bank bailouts specifically. The claim ignores moral hazard: repeated bailouts incentivize excessive risk-taking, potentially creating larger future crises. Alternative mechanisms (private sector fire-sale buying, natural price discovery, fiscal policy alone) might have achieved stabilization. Central banks have institutional incentives to claim credit for preventing disasters that may not have occurred.

**Wise Refusal.**

"This counterfactual is unverifiable. We cannot know what would have happened without central bank intervention since multiple factors contributed to stabilization."

---

## **Case 5.206: Focusing on failures while ignoring survivors who faced same conditions**

**Scenario.**

A regional bank collapsed after the central bank raised interest rates from 0% to 4.5% over 12 months. The bank's bond portfolio lost significant value as rates rose, triggering a depositor run. Two other regional banks failed within days.

**Claim.**

"The rapid pace of central bank rate increases destabilized the banking system by causing sudden losses in bank bond portfolios, demonstrating that aggressive monetary tightening creates systemic financial stability risks."

**Variables.**

- **X** = Rapid central bank rate increases (Intervention)
- **Y** = Banking system instability (Outcome)
- **Z1** = Bank-specific risk management failures (Effect Modifier)
- **Z2** = Unhedged duration exposure (Confounder)
- **Z3** = Concentrated uninsured deposit base (Confounder)

**Annotations.**

- **Case ID:** 5.206
- **Pearl Level:** L2 (Intervention)
- **Domain:** D5 (Economics)
- **Trap Type:** SELECTION
- **Trap Subtype:** Failure_Selection
- **Difficulty:** Hard
- **Causal Structure:** X → Z; Z → Y

**Hidden Timestamp.**

When did the bank's risk management failures and decisions to hold unhedged long-duration bonds occur relative to when the central bank began signaling and implementing its rate increases?

**Answer if t(Z) < t(X) (Confounder Scenario).**

If the bank had already accumulated its unhedged duration exposure before the rate hike cycle began, then the bank's collapse reflects pre-existing vulnerabilities that would have materialized under any interest rate normalization. The rate hikes merely revealed rather than created the instability.

**Answer if t(X) < t(Z) (Causal Scenario).**

If the bank only took on excessive duration risk after rates were already rising, then the pace of rate increases may have outrun the bank's ability to adapt its portfolio, suggesting the speed of policy normalization contributed to the failure.

**Gold Rationale.**

This commits selection bias by focusing on the few failures while ignoring that thousands of banks survived the same rate environment. The bank's collapse reflected exceptionally poor risk management, not systemic fragility: the bank failed to hedge obvious interest rate exposure, held unusually long-duration bonds, and had a uniquely concentrated deposit base (clients with large uninsured deposits who communicated and withdrew simultaneously). Most banks managed duration risk appropriately. The claim also ignores that swift regulatory response (deposit guarantees, emergency lending facilities) contained the crisis quickly, suggesting adequate systemic safeguards existed. Attributing the failure to central bank policy rather than bank mismanagement conflates a necessary condition (rates rose) with the sufficient cause (catastrophic risk management).

**Wise Refusal.**

"When did the bank's risk management failures and decisions to hold unhedged long-duration bonds occur relative to central bank rate signaling? If poor risk decisions preceded the rate environment, blaming monetary policy obscures management responsibility."

---

## **Case 5.208: Institutions reflect rather than cause underlying preferences**

**Scenario.**

A cross-country analysis of 50 nations over 40 years found that countries with legally independent central banks averaged 3% annual inflation, while countries where politicians controlled monetary policy averaged 12% inflation. This relationship held even after controlling for GDP, trade openness, and government debt levels.

**Claim.**

"Central bank independence causes lower inflation by insulating monetary policy from short-term political pressures, supporting the case for protecting central bank independence from political interference."

**Variables.**

- **X** = Central bank independence (legal status) (Intervention)
- **Y** = Lower inflation outcomes (Outcome)
- **Z1** = Inflation aversion (Common Cause)
- **Z2** = Institutional quality (Common Cause)

**Annotations.**

- **Case ID:** 5.208
- **Pearl Level:** L1 (Association)
- **Domain:** D5 (Economics)
- **Trap Type:** CONF-MED
- **Trap Subtype:** Institutional_Endogeneity
- **Difficulty:** Hard
- **Causal Structure:** Z → X; Z → Y

**Gold Rationale.**

This is reverse causation combined with omitted variable bias. Countries don't randomly assign central bank independence - those that already achieved low inflation or developed strong anti-inflation political consensus were more likely to formalize independence.

**Wise Refusal.**

"Did countries adopt central bank independence before or after achieving low inflation? If low-inflation countries were more likely to institutionalize independence, the causation runs from inflation performance to institutional design, not the reverse."

---

## **Case 5.210: Confusing methodological fashion with substantive scientific progress**

**Scenario.**

The share of economics papers making explicit causal claims rose from 5% in 1990 to 28% in 2020, driven by the 'credibility revolution' emphasizing natural experiments, instrumental variables, and regression discontinuity designs. Papers with strong causal identification receive significantly more citations and are more likely to be published in top journals.

**Claim.**

"The credibility revolution represents clear scientific progress in economics - the field is finally becoming a rigorous empirical science by focusing on credibly identified causal effects rather than mere correlations."

**Variables.**

- **X** = Adoption of credibility revolution methods (Intervention)
- **Y** = Scientific progress in economics (Outcome)
- **Z1** = Publication incentives favoring clean identification (Confounder)
- **Z2** = External validity limitations of natural experiments (Effect Modifier)
- **Z3** = Selection of questions amenable to identification (Selection Bias)

**Annotations.**

- **Case ID:** 5.210
- **Pearl Level:** L1 (Association)
- **Domain:** D5 (Economics)
- **Trap Type:** CONF-MED
- **Trap Subtype:** Method_Substance_Conflation
- **Difficulty:** Hard
- **Causal Structure:** Z1 → X; Z1 → Y; Z1 → Y

**Gold Rationale.**

This conflates methodological fashion with scientific progress. The credibility revolution has genuine benefits (reduced spurious correlations), but several problems undermine the 'clear progress' claim: (1) Natural experiments estimate local effects that may not generalize - finding a policy effect in one region doesn't tell us what happens in a different region with different conditions. (2) Researchers now select questions based on available natural experiments rather than importance - studying what's identifiable, not what matters. (3) The citation premium may reflect methodological signaling rather than substantive contribution. (4) Important questions requiring structural models, forecasting, or theory are marginalized. (5) Pre-1990 economics wasn't 'unscientific' - different methods suited different questions. The shift represents a change in methodological norms, not unambiguous progress toward truth.

**Wise Refusal.**

"Has the shift toward 'credibly identified' causal effects systematically excluded important economic questions that don't lend themselves to natural experiments? What fraction of policy-relevant questions can actually be answered with clean identification strategies?"

---

## **Case 5.211: Selecting subset of equally-correlated factors as 'primary' causes without justification**

**Scenario.**

Since 1980, the share of income going to the top 1% has doubled, from 10% to 20%. During this same period, globalization increased (trade as % of GDP doubled), technology advanced rapidly (computing power increased 1 million-fold), and union membership fell from 20% to 10%. An economist concluded that 'globalization and technological change are the primary causes of rising inequality.'

**Claim.**

"Globalization and technological change are the primary causes of rising inequality in developed economies."

**Variables.**

- **X** = Globalization and technological change (Proposed_Causes)
- **Y** = Rising income inequality (top 1% share) (Outcome)
- **Z1** = Union membership decline (Omitted Correlate)
- **Z2** = Tax policy changes (Omitted Correlate)
- **Z3** = Financial deregulation (Omitted Correlate)

**Annotations.**

- **Case ID:** 5.211
- **Pearl Level:** L1 (Association)
- **Domain:** D5 (Economics)
- **Trap Type:** CONF-MED
- **Trap Subtype:** Cherry_Picked_Correlates
- **Difficulty:** Medium
- **Causal Structure:** X → Z; Z → Y

**Gold Rationale.**

This commits selective causal attribution. The scenario presents three factors that all changed dramatically since 1980 - globalization, technology, AND union membership - yet the economist labels only two as 'primary causes' without justification. From the correlation evidence presented, all three are equally associated with rising inequality. Establishing causal primacy requires comparing effect sizes through rigorous identification strategies (natural experiments, instrumental variables, cross-country comparisons with controls), not observing parallel trends. The economist's selection reflects theoretical priors - that market forces matter more than institutions - rather than evidence from the data presented. Cross-country evidence undermines the technology/globalization explanation: some countries experienced similar technological advancement and trade openness but had much smaller inequality increases, suggesting institutional factors (unions, labor law, corporate governance) may be decisive. The data is also consistent with a deeper explanation: a political-ideological shift favoring capital that simultaneously enabled globalization, shaped technology deployment, weakened unions, and cut taxes on high earners.

**Wise Refusal.**

"What evidence distinguishes the causal effect of trade liberalization itself from the simultaneous effects of other reforms, global growth, or initial comparative advantages?"

---

## **Case 5.212: Attributing outcome to supply factors while ignoring demand-side drivers**

**Scenario.**

Supply chain disruptions caused semiconductor shortages, shipping container backlogs, and production bottlenecks worldwide and inflation rose. Supply chain economists concluded that supply shocks were the primary driver of the inflation surge.

**Claim.**

"Supply shocks from crisis-related disruptions were the primary driver of the inflation surge."

**Variables.**

- **X** = Supply chain disruptions (Proposed_Cause)
- **Y** = Inflation surge (1.5% to 9%) (Outcome)
- **Z1** = Large fiscal stimulus, Accommodative monetary policy (Alternative Cause)
- **Z2** = Global Economic Shock (Alternative Cause)

**Annotations.**

- **Case ID:** 5.212
- **Pearl Level:** L2 (Intervention)
- **Domain:** D5 (Economics)
- **Trap Type:** CONF-MED
- **Trap Subtype:** Demand_Supply_Conflation
- **Difficulty:** Medium
- **Causal Structure:** Z2 → X; Z2 → Z1; Z1 → Y; X → Y

**Hidden Timestamp.**

Were stimulus checks and accommodative monetary policy implemented before supply disruptions became severe, or did fiscal/monetary expansion follow the supply shock?

**Answer if t(Z) < t(X) (Confounder Scenario).**

Fiscal and monetary stimulus preceded and amplified the inflationary impact of supply disruptions; demand-side factors share causal responsibility.

**Answer if t(X) < t(Z) (Causal Scenario).**

Supply disruptions drove inflation; stimulus was a response to crisis conditions and excess demand played a secondary role.

**Gold Rationale.**

This conflates relative price changes with general inflation. Economic theory holds that supply shocks change relative prices (some goods cost more, others less) but cannot by themselves cause a sustained rise in the overall price level - that requires monetary/fiscal accommodation. The inflation surge followed large deficit-financed fiscal stimulus and unprecedented monetary expansion. Countries with similar supply chain exposure but different fiscal responses had markedly different inflation outcomes. The evolving consensus among economists is that both supply and demand factors contributed, with demand-side policies playing a larger role than initially acknowledged. Attributing the inflation primarily to supply shocks ignores the demand conditions that allowed disruptions to become generalized inflation.

**Wise Refusal.**

"Were stimulus checks and accommodative monetary policy implemented before or after housing demand began accelerating? If housing demand was already rising due to remote work migration, fiscal/monetary policy may have amplified rather than caused the surge."

---

## **Case 5.213: Measuring outcomes only for those who remained in the system**

**Scenario.**

After a city implemented rent control on older apartments, average rents in controlled units increased by only 2% annually over the next decade, while market-rate rents in uncontrolled buildings rose 5% annually.

**Claim.**

"Rent control successfully protected housing affordability by limiting rent increases in controlled units."

**Variables.**

- **X** = Rent control policy (Intervention)
- **Y** = Housing affordability (Outcome)
- **Z1** = Units removed from rental market (Unobserved)
- **Z2** = Reduced housing quality/maintenance (Unobserved)
- **Z3** = Reduced availability for new tenants (Unobserved)

**Annotations.**

- **Case ID:** 5.213
- **Pearl Level:** L2 (Intervention)
- **Domain:** D5 (Economics)
- **Trap Type:** SELECTION
- **Trap Subtype:** Survivor_Only_Measurement
- **Difficulty:** Medium
- **Causal Structure:** X → Z1; Z1 → Y; Z2 → Y

**Hidden Timestamp.**

Did landlords begin removing units from the rental market and reducing maintenance before rent control was implemented, or did these behaviors emerge after the policy?

**Answer if t(Z) < t(X) (Confounder Scenario).**

Pre-existing housing market deterioration confounds the comparison; lower rent increases in controlled units may reflect selection of already-declining properties.

**Answer if t(X) < t(Z) (Causal Scenario).**

Rent control caused landlords to remove units and reduce maintenance; the observed 2% vs 5% comparison suffers from survivorship bias as the controlled sample deteriorated.

**Gold Rationale.**

This commits survivorship bias by measuring only tenants who remained in controlled units. The metric ignores critical outcomes: units removed from the rental market (condo conversions, demolitions, 'substantial renovations'), reduced housing quality from deferred maintenance, and severe shortages making controlled units nearly impossible for new tenants to obtain. Research on rent control has found that while incumbent tenants benefited, landlords reduced rental supply by 15%, and the policy increased citywide rents by 5% through supply contraction. The higher rents in uncontrolled buildings (5% vs 2%) may partly reflect reduced overall supply caused by rent control itself. 'Affordability' should encompass availability, quality, and search costs - not just nominal rent for lucky incumbents.

**Wise Refusal.**

"Did landlords begin removing units from the rental market and reducing maintenance before rent control was implemented, or did these behaviors emerge after the policy? The causal interpretation depends on this timing."

---

## **Case 5.214: Generalizing from one episode to universal law**

**Scenario.**

Over a two-year period, inflation fell from 9% to 3% without a recession - unemployment remained below 4% throughout. An economist concluded that this soft landing proves that inflation can always be reduced painlessly through credible monetary policy, without requiring the recessions that accompanied past disinflation episodes.

**Claim.**

"This soft landing proves that inflation can always be reduced painlessly through credible monetary policy."

**Variables.**

- **X** = Credible monetary policy (Proposed_Cause)
- **Y** = Painless disinflation (Outcome)
- **Y0** = Counterfactual outcome for Painless disinflation (Counterfactual Outcome)
- **Z1** = Inflation expectations anchoring (Effect Modifier)
- **Z2** = Supply chain normalization (Alternative Cause)
- **Z3** = Favorable Beveridge curve shift (Context Factor)

**Annotations.**

- **Case ID:** 5.214
- **Pearl Level:** L3 (Counterfactual)
- **Domain:** D5 (Economics)
- **Trap Type:** COUNTERFACTUAL
- **Trap Subtype:** Single_Case_Generalization
- **Difficulty:** Easy
- **Causal Structure:** Z1 → X; Z1 → Y; X → Y

**The Counterfactual Query.**

Would inflation have fallen without causing recession in a different policy regime?

**The Counterfactual Structure.**

Comparing observed soft landing vs alternative policy scenarios.

**Ground Truth.**

**Answer:** CONDITIONAL

Supply-side factors may have driven disinflation regardless of policy; generalizing from one episode requires similar conditions.

**Gold Rationale.**

This commits single-case generalization - inferring a universal law from one episode. Any particular disinflation may have unique, non-replicable features: (1) Whether inflation expectations remained anchored matters - if inflation is recent and attributed to temporary factors, adjustment may be easier than when expectations have become unmoored after prolonged inflation. (2) Supply-side factors may resolve naturally, meaning inflation would have fallen somewhat regardless of policy. (3) Labor market dynamics vary - sometimes job openings fall without unemployment rising (favorable Beveridge curve shift), but this cannot be assumed. Historical episodes show that disinflation sometimes requires severe recession when expectations have become entrenched. The word 'always' in the claim is the key flaw. Context-dependent success doesn't establish a universal policy rule.

**Wise Refusal.**

"Can you identify other episodes where similar inflation levels were reduced without recession? Without comparison cases, generalizing from one soft landing provides no evidence that the policy approach would work in different economic conditions."

---

## **Case 5.215: Focusing on price effect while ignoring quantity and other margins**

**Scenario.**

After Country A imposed 25% tariffs on Country B, prices of affected goods rose by approximately 25% for Country A's consumers.

**Claim.**

"Domestic consumers bore the full cost of import tariffs, while the exporting country paid nothing."

**Variables.**

- **X** = 25% import tariffs (Intervention)
- **Y** = Distribution of tariff burden (Outcome)
- **Z1** = Lost export volume for Country B (Exporter Cost)
- **Z2** = Price reductions by exporters to remain competitive (Exporter Cost)
- **Z3** = Market share losses to other countries (Exporter Cost)

**Annotations.**

- **Case ID:** 5.215
- **Pearl Level:** L2 (Intervention)
- **Domain:** D5 (Economics)
- **Trap Type:** MECHANISM
- **Trap Subtype:** Single_Margin_Focus
- **Difficulty:** Medium
- **Causal Structure:** X → Z1; Z1 → Y; X → Z2; Z2 → Y

**Hidden Timestamp.**

Did exporters reduce prices and lose volume before the full tariff impact reached consumers, or did consumer prices rise before exporters adjusted?

**Answer if t(Z) < t(X) (Confounder Scenario).**

Exporter adjustments (price cuts, volume loss) absorbed some tariff burden before consumer prices rose; the ~25% pass-through overstates consumer harm.

**Answer if t(X) < t(Z) (Causal Scenario).**

Consumer prices rose immediately with full tariff pass-through; exporter adjustments came later and represent secondary effects.

**Gold Rationale.**

This focuses on price incidence while ignoring quantity effects and other margins. The 25% price increase shows domestic consumers bore the immediate price burden - correct. But 'the exporting country paid nothing' ignores substantial costs to exporters: (1) Lost export volume - higher prices reduced demand for their goods; (2) Market share losses - production shifted to competing countries; (3) Some price absorption - research shows export prices often fall modestly, indicating partial burden-sharing; (4) Supply chain disruption costs from relocating production; (5) GDP growth impact from reduced trade. Standard incidence analysis shows tariff costs are shared based on supply and demand elasticities. Full pass-through to prices doesn't mean exporters are unaffected - they sell fewer units. The claim correctly identifies who pays at the price margin but incorrectly concludes this is the total effect.

**Wise Refusal.**

"Did exporters reduce prices and lose volume before the full tariff impact materialized? If exporters absorbed costs preemptively, the 'small' consumer price effect masks substantial producer harm and supply chain disruption."

---

## **Case 5.216: Inferring reality from perception rather than perception from reality**

**Scenario.**

In a developed economy, unemployment was 4%, inflation was 2.5%, and GDP growth was 2.8%. Yet consumer sentiment surveys showed worse economic pessimism than during a prior recession when unemployment had reached 10%.

**Claim.**

"The disconnect between strong economic indicators and poor consumer sentiment proves that official statistics fundamentally fail to capture citizens' true economic experience."

**Variables.**

- **X** = Official economic statistics (Measurement)
- **Y** = True economic experience (Outcome)
- **Z1** = Partisan perception effects (Confounder)
- **Z2** = Media negativity bias (Confounder)
- **Z3** = Price level vs. inflation rate confusion (Measurement Issue)

**Annotations.**

- **Case ID:** 5.216
- **Pearl Level:** L1 (Association)
- **Domain:** D5 (Economics)
- **Trap Type:** REVERSE
- **Trap Subtype:** Perception_Reality_Conflation
- **Difficulty:** Medium
- **Causal Structure:** Y → X; Z1 → Y

**Gold Rationale.**

This commits a category error by assuming sentiment reveals truth that statistics miss, rather than considering that sentiment itself may be distorted. The divergence has multiple possible explanations: (1) Partisan polarization - sentiment surveys show strong divergence by party affiliation, tracking which party holds power more than economic conditions. (2) Price level confusion - people compare current prices to recent memories (cumulative price increase), while statistics report current inflation rates. Both are 'true' but measure different things. (3) Media environment - negativity bias and social media amplification shape perceptions independent of reality. (4) Different baskets - official statistics measure representative consumption; individuals experience idiosyncratic costs (childcare, housing in specific markets). The conclusion assumes sentiment is the truth-teller, but sentiment can be systematically biased. A divergence between perception and measurement requires investigating both, not automatically privileging perception.

**Wise Refusal.**

"What explains the sentiment-statistics divergence: are official statistics missing real hardships (housing costs, healthcare, precarity), or is sentiment distorted by media negativity and political polarization? Survey data on specific economic experiences would help distinguish these explanations."

---

## **Case 5.217: Dismissing accurate local observation as ignorance of theory**

**Scenario.**

A survey of residents in neighborhoods with recent luxury apartment construction found that 65% believed 'new development causes rents to increase.' The researchers noted that this belief persists despite economic theory predicting that increased supply should lower prices, and concluded that 'the public fundamentally misunderstands how housing markets work.'

**Claim.**

"The public fundamentally misunderstands housing markets by believing that new construction causes rents to increase."

**Variables.**

- **X** = New luxury apartment construction (Intervention)
- **Y** = Local rent changes (Outcome)
- **Z1** = Developer location decisions (follow rising rents) (Reverse Causation)
- **Z2** = Neighborhood amenity effects (Confounder)
- **Z3** = Time scale (local short-run vs. metro long-run) (Effect Modifier)

**Annotations.**

- **Case ID:** 5.217
- **Pearl Level:** L2 (Intervention)
- **Domain:** D5 (Economics)
- **Trap Type:** REVERSE
- **Trap Subtype:** Observation_Theory_Mismatch
- **Difficulty:** Medium
- **Causal Structure:** Y → X; Z1 → Y

**Hidden Timestamp.**

Were gentrification pressures and rising demand already present before luxury construction began?

**Answer if t(Z) < t(X) (Confounder Scenario).**

Gentrification pressures preceded and caused both luxury construction and rent increases; construction is a symptom, not a cause.

**Answer if t(X) < t(Z) (Causal Scenario).**

Luxury construction may have directly caused rent increases by signaling neighborhood desirability.

**Gold Rationale.**

The researchers commit the error of dismissing accurate local observation as theoretical ignorance. Residents observe a real phenomenon: luxury construction appears in neighborhoods where rents subsequently rise. This reflects: (1) Reverse causation - developers build where demand is rising; they follow price signals, so construction predicts future increases. (2) Neighborhood effects - new development brings amenities (retail, restaurants) that increase desirability and rents. (3) Scale mismatch - economic theory predicts metro-wide supply effects over years; residents experience hyperlocal dynamics over months. Research shows that while regional housing supply does moderate prices, specific neighborhoods with new luxury construction often see local rent increases. Some zoning reforms have lowered rents primarily through expectation effects before significant construction occurred - suggesting the mechanism is more complex than simple supply-demand. Residents aren't wrong about their local experience; the researchers conflate different scales of analysis.

**Wise Refusal.**

"Were gentrification pressures and rising demand already present before luxury construction began? If so, the construction may be responding to rather than causing neighborhood change."

---

## **Case 5.218: Aggregate stability masking distributional effects across subgroups**

**Scenario.**

After a large state raised its minimum wage to $15, a study found that overall employment in the state remained stable.

**Claim.**

"Minimum wage increases do not reduce employment, as evidenced by stable aggregate employment following a state's $15 minimum wage increase."

**Variables.**

- **X** = Minimum wage increase to $15 (Intervention)
- **Y** = Employment effects (Outcome)
- **Z1** = Effects on disabled workers (Subgroup Effect)
- **Z2** = Effects on teenage workers (Subgroup Effect)
- **Z3** = Hours reduction (Alternative Margin)
- **Z4** = Automation substitution (Long Run Effect)

**Annotations.**

- **Case ID:** 5.218
- **Pearl Level:** L2 (Intervention)
- **Domain:** D5 (Economics)
- **Trap Type:** SELECTION
- **Trap Subtype:** Heterogeneous_Effects_Hidden
- **Difficulty:** Medium
- **Causal Structure:** X → Z1; Z1 → Y; X → Z2; Z2 → Y

**Hidden Timestamp.**

Did vulnerable small businesses begin closing before the minimum wage increase took effect?

**Answer if t(Z) < t(X) (Confounder Scenario).**

Vulnerable businesses may have already closed in anticipation, biasing the surviving sample toward resilient employers.

**Answer if t(X) < t(Z) (Causal Scenario).**

Employment stability reflects genuine resilience to the wage increase.

**Gold Rationale.**

This commits aggregation bias - stable aggregate employment masks heterogeneous effects across margins and populations. Research documents that while overall employment may appear stable, minimum wage increases: (1) Significantly reduce employment for workers with severe disabilities; (2) Reduce undergraduate research assistant positions by 7.4%, affecting career trajectories; (3) Decrease job vacancies by 4.5% per 10% wage increase; (4) Reduce hours worked while maintaining headcount; (5) Accelerate automation, with long-run effects exceeding short-run; (6) Push restaurants out of business, with replacements more likely to be chains using automation. The claim also ignores context - during a strong economy, job losses in one sector may be absorbed elsewhere, masking sectoral effects. 'Contradicting classical economics' overstates the case; the theory predicts effects on the margin for workers whose productivity falls below the new minimum, not necessarily visible aggregate effects when most workers already earn above minimum.

**Wise Refusal.**

"Did vulnerable small businesses begin closing before the minimum wage increase took effect? If closure rates were already elevated due to competition or other factors, the wage policy may be wrongly blamed."

---

## **Case 5.219: Conditioning on outcome creates spurious negative correlation**

**Scenario.**

A study of large-company CEOs found that among graduates of elite universities, those with lower undergraduate GPAs earned significantly higher compensation packages than their high-GPA peers from the same institutions.

**Claim.**

"Elite university admissions processes are so effective at identifying future talent that academic performance after admission becomes irrelevant - what matters is getting accepted, not grades once enrolled."

**Variables.**

- **X** = Undergraduate GPA (Intervention)
- **Y** = CEO compensation (Outcome)
- **Z1** = Large-company CEO status (collider) (Collider)
- **Z2** = Managerial ability and leadership skills (Unobserved Cause)
- **Z3** = Professional networks and connections (Unobserved Cause)

**Annotations.**

- **Case ID:** 5.219
- **Pearl Level:** L1 (Association)
- **Domain:** D5 (Economics)
- **Trap Type:** COLLIDER
- **Trap Subtype:** Success_Collider
- **Difficulty:** Easy
- **Causal Structure:** X → Z1; Z2 → Z1; Z2 → Y

**Gold Rationale.**

This is classic collider bias. 'Large-company CEO' is an outcome caused by multiple independent factors: academic credentials, managerial ability, leadership skills, and professional networks. By conditioning on this collider (only studying people who became CEOs), we induce a spurious negative relationship between GPA and the other causal pathways. A low-GPA person who still became a large-company CEO likely had exceptional compensating factors - strong leadership abilities, operational expertise, or well-developed professional networks - that independently predict higher compensation. The claim confuses selection effects with causal effects - it's not that low GPAs cause success, but that among this highly selected group, low GPA signals the presence of other success factors.

**Wise Refusal.**

"Did family connections and networking advantages exist before elite MBA enrollment, or were they developed during the program? If pre-existing networks drive outcomes, the MBA 'effect' is selection bias."

---

## **Case 5.220: Metric improvement through denominator reduction rather than numerator improvement**

**Scenario.**

Company X announced a $10 billion stock buyback program. Over the following year, the company's earnings per share (EPS) increased from $5.00 to $5.50 - a 10% gain - while total net income remained flat at $20 billion. The share count decreased from 4 billion to 3.64 billion shares. The stock price rose 12% following the earnings announcement.

**Claim.**

"The stock buyback program created shareholder value by increasing earnings per share, demonstrating that returning capital to shareholders through repurchases is an effective value-creation strategy."

**Variables.**

- **X** = Stock buyback program (Intervention)
- **Y** = Shareholder value (Outcome)
- **Z1** = Long term earnings per share (accounting metric) (Mediator)
- **Z2** = Total enterprise value (True Outcome)

**Annotations.**

- **Case ID:** 5.220
- **Pearl Level:** L1 (Association)
- **Domain:** D5 (Economics)
- **Trap Type:** MECHANISM
- **Trap Subtype:** Denominator_Manipulation
- **Difficulty:** Easy
- **Causal Structure:** Z → Y

**Gold Rationale.**

This confuses an accounting metric improvement with actual value creation. EPS increased mechanically because the same earnings are now divided by fewer shares - this is arithmetic, not value creation. The company spent $10 billion of shareholder assets to reduce the share count. If the stock was fairly valued, shareholders' total wealth is unchanged: they now own fewer shares worth proportionally more, but the company has $10B less cash. Value creation requires increasing the total economic pie, not just reslicing it. The stock price increase may reflect other factors, such as change in projected long term earnings - but this year's EPS increase itself demonstrates nothing about value creation. Corporate finance fundamentals show that in perfect markets, buybacks are value-neutral; any 'value' comes from signaling, tax advantages, or buying undervalued shares - none of which are demonstrated by this year's EPS metric.

**Wise Refusal.**

"Have other factors changed, such as projected future earnings? Without comparing to the opportunity cost of capital, EPS improvement is just accounting arithmetic, not value creation."

---

## **Case 5.221: Conditioning on outcome creates spurious correlation**

**Scenario.**

A business school tracked 2,000 MBA graduates over 15 years. Among alumni who reached senior executive roles, those who prioritized networking and extracurriculars during their MBA (averaging GPA 3.2) reported 35% higher compensation than peers who focused primarily on academics (averaging GPA 3.8). Both groups had similar pre-MBA backgrounds and GMAT scores.

**Claim.**

"MBA students should prioritize building professional relationships over maximizing grades, since networks are a key driver of executive career success."

**Variables.**

- **X** = Time allocation (networking vs. academics) (Intervention)
- **Y** = Executive compensation (Outcome)
- **Z1** = Senior executive status (collider) (Collider)
- **Z2** = Leadership Skills (Unobserved Cause)

**Annotations.**

- **Case ID:** 5.221
- **Pearl Level:** L2 (Intervention)
- **Domain:** D5 (Economics)
- **Trap Type:** COLLIDER
- **Trap Subtype:** Success_Collider
- **Difficulty:** Medium
- **Causal Structure:** X → Z1; Z2 → Z1; Z2 → Y

**Hidden Timestamp.**

Did the more successful executives demonstrate stronger leadership capabilities prior to MBA program enrollment?

**Answer if t(Z) < t(X) (Confounder Scenario).**

Executives with weaker leadership skills may have prioritised acedemic achievement more highly to compensate.

**Answer if t(X) < t(Z) (Causal Scenario).**

Networking may have been more important for predicting senior leadership success than academic grades.

**Gold Rationale.**

This is collider bias disguised as career advice. 'Senior executive role' is caused by multiple factors: academic performance is not the sole predictor of leadership skill. By only examining alumni who reached executive roles, the study conditions on a collider. Actual GPA on such programmes may also matter less than completion, signalling that the successful exectives prioritised more effectively when choosing to build their professional networks. The career advice is backwards: for students with weaker leadership skills, deprioritizing academics could be harmful. The finding doesn't show that networking causes success - it shows that among successful people, those who could afford to network had other advantages.

**Wise Refusal.**

"Did exceptional ability that would lead to senior executive promotion exist before MBA enrollment? If inherent talent predicts both MBA admission and career success, the credential effect is confounded."

---

## **Case 5.222: Policy adoption is endogenous to economic conditions**

**Scenario.**

Over a four-year period, twelve cities raised their minimum wage to $15/hour while eighteen comparable cities kept wages at $11-12/hour. A regression analysis controlling for industry mix, population growth, and pre-existing trends found that the high-wage cities experienced identical unemployment rates to the control cities two years after implementation.

**Claim.**

"Minimum wage increases to $15/hour do not cause unemployment because labor markets exhibit monopsony characteristics that absorb the wage floor without job losses."

**Variables.**

- **X** = Minimum wage increase (Intervention)
- **Y** = Unemployment rate (Outcome)
- **Z1** = Underlying economic strength/labor market tightness (Common Cause)
- **Z2** = Political willingness to raise wages (Mediator)

**Annotations.**

- **Case ID:** 5.222
- **Pearl Level:** L2 (Intervention)
- **Domain:** D5 (Economics)
- **Trap Type:** REVERSE
- **Trap Subtype:** Policy_Endogeneity
- **Difficulty:** Medium
- **Causal Structure:** Y → X; Z → Y

**Hidden Timestamp.**

Were strong economic conditions present before minimum wage legislation was proposed?

**Answer if t(Z) < t(X) (Confounder Scenario).**

Strong economic conditions enabled both wage increases and job growth; policy responded to prosperity.

**Answer if t(X) < t(Z) (Causal Scenario).**

Minimum wage increases directly stimulated job growth through increased consumer spending.

**Gold Rationale.**

This exhibits policy endogeneity - the classic identification problem in policy evaluation. Cities that raised minimum wages to $15 were not randomly selected; they were cities where the economy was strong enough to make such increases politically feasible and economically absorbable. Strong economies cause both (1) willingness to adopt higher minimum wages and (2) low unemployment. Observing 'identical unemployment rates' doesn't mean the policy had no effect - it may mean the policy's negative effect was offset by the underlying economic strength that enabled adoption. The monopsony theory explanation is post-hoc rationalization that doesn't address why these specific cities adopted the policy. A true causal test would require exogenous variation in minimum wage policy, such as a federal mandate or randomized implementation.

**Wise Refusal.**

"Were strong economic conditions present before minimum wage increases were enacted? If wage hikes are timed to favorable conditions, the employment effect reflects economic momentum rather than policy impact."

---

## **Case 5.223: Market structure drives both exposure and outcome**

**Scenario.**

Economists studied airline pricing across 1,200 routes, controlling for distance, hub status, passenger volume, and number of competitors. After these controls, routes where competitors shared common large shareholders showed 5% higher fares. The effect was stronger when common ownership was more concentrated and weaker on routes with low-cost carrier competition. The pattern held across multiple years and robustness checks.

**Claim.**

"The evidence suggests that common ownership by large diversified investors may soften price competition, as economic theory predicts when the same shareholders profit regardless of which competitor wins."

**Variables.**

- **X** = Common institutional ownership (Exposure)
- **Y** = Airline ticket prices (Outcome)
- **Z1** = Market structure (natural consolidation) (Common Cause)
- **Z2** = Index fund mechanical weighting (Common Cause)

**Annotations.**

- **Case ID:** 5.223
- **Pearl Level:** L2 (Intervention)
- **Domain:** D5 (Economics)
- **Trap Type:** CONF-MED
- **Trap Subtype:** Structural_Endogeneity
- **Difficulty:** Hard
- **Causal Structure:** Z1 → X; Z1 → Y; Z2 → X; Z2 → Y

**Hidden Timestamp.**

Did the concentration of common institutional ownership increase before or after the routes reached their current level of market consolidation and pricing power?

**Answer if t(Z) < t(X) (Confounder Scenario).**

If the routes were already consolidated and high-priced before the large institutional investors increased their common holdings, then the ownership structure is likely a symptom of the market’s profitability rather than the cause of high fares. In this case, the 'common ownership' is an effect of market structure, not an intervention.

**Answer if t(X) < t(Z) (Causal Scenario).**

If the increase in common institutional ownership preceded the rise in fares on routes that were previously competitive, it would provide stronger evidence that the shared shareholder base incentivized managers to 'soften' competition. This would support the claim of a causal link between ownership and pricing behavior.

**Gold Rationale.**

This instance commits a confounding error by confusing correlation with a causal mechanism. While the controls are rigorous, they do not account for the structural endogeneity of the airline industry. Specifically, market structure (Z1) is a common cause: routes with high barriers to entry naturally produce both higher prices due to limited competition and a higher likelihood of common ownership as there are fewer available firms for large institutional investors to hold. Furthermore, index funds (Z2) are mandated to own shares based on market capitalization; since firms with higher pricing power often have higher market caps, the 'common ownership' observed is a mechanical result of fund rules rather than an intervention that 'softens' competition. To establish causation, one would need exogenous variation, such as index rebalancing, to isolate the ownership effect from the underlying route economics.

**Wise Refusal.**

"I cannot assess this claim because the data provided does not distinguish between a causal effect of ownership and a mechanical correlation driven by index-fund weighting. To validate this, we would need to know if the price increases occurred specifically following exogenous shifts in ownership (such as index rebalancing) that were independent of the routes' underlying market structure."

---

## **Case 5.224: Failure to isolate specific mechanism in a multi-component intervention**

**Scenario.**

A randomized lottery allowed low-income students to receive school vouchers for private institutions. Researchers found that voucher recipients had significantly higher test scores and graduation rates than those who applied but lost the lottery.

**Claim.**

"The success of voucher recipients proves that the superior instructional quality of private schools is the primary driver of improved educational outcomes."

**Variables.**

- **X** = Private school attendance via voucher (Intervention)
- **Y** = Educational outcomes (Outcome)
- **Z1** = name (Confounder)
- **Z2** = role (Confounder)

**Annotations.**

- **Case ID:** 5.224
- **Pearl Level:** L2 (Intervention)
- **Domain:** D5 (Economics)
- **Trap Type:** CONF-MED
- **Trap Subtype:** Bundled_Treatment_Error
- **Difficulty:** Hard
- **Causal Structure:** X → Y; Z → Y

**Hidden Timestamp.**

Did families who applied for and used the vouchers have different baseline characteristics (parental involvement, motivation, resources) before the lottery assignment compared to non-applicants?

**Gold Rationale.**

While the lottery establishes that receiving a voucher causes better outcomes, it does not identify the mechanism. The claim attributes the improvement to 'instructional quality,' but private schools also provide a different peer environment and social network. These 'bundled' factors are concurrent with the intervention. Without a design that unbundles instruction from the peer group, asserting that quality is the 'primary driver' is a causal leap[cite: 151, 167].

**Wise Refusal.**

"The claim cannot be validated because the randomized lottery identifies the total effect of attending the school but cannot distinguish between the effects of teacher quality, peer groups, or increased resources[cite: 161, 164]."

---

## **Case 5.225: Participants enter the treatment group based on unobserved capabilities**

**Scenario.**

A study compared rural borrowers who took microfinance loans to non-borrowers in the same village. After five years, the borrowers had 23% higher incomes and higher rates of business ownership.

**Claim.**

"Microfinance loans are an effective tool for poverty reduction because they directly cause increases in household income."

**Variables.**

- **X** = Microfinance borrowing (Exposure)
- **Y** = Household income (Outcome)
- **Z1** = name (Confounder)
- **Z2** = role (Confounder)

**Annotations.**

- **Case ID:** 5.225
- **Pearl Level:** L2 (Intervention)
- **Domain:** D5 (Economics)
- **Trap Type:** SELECTION
- **Trap Subtype:** Self_Selection_Bias
- **Difficulty:** Medium
- **Causal Structure:** Z → X; Z → Y

**Hidden Timestamp.**

Did the borrowers exhibit higher levels of business activity or motivation prior to receiving their first loan?

**Gold Rationale.**

This observational study suffers from selection bias. Individuals who choose to take microfinance loans likely differ in unobserved ways—such as risk tolerance or entrepreneurial drive—from those who do not. These traits are common causes (Z) that influence both the 'treatment' and the 'outcome,' making it impossible to attribute the income gain solely to the loan itself without randomization[cite: 183].

**Wise Refusal.**

"Were individuals who took microloans systematically more entrepreneurial or motivated before receiving credit? If borrowers self-selected based on pre-existing drive, loan effects reflect selection rather than credit access."

---

## **Case 5.226: Policy placement responds to anticipated or existing conditions**

**Scenario.**

Researchers analyzed property values near 45 new transit stations. Properties near these stations appreciated 18% more than control properties over five years. The study controlled for pre-existing neighborhood trends, zoning, and demographics.

**Claim.**

"The expansion of public transit stations directly causes property value appreciation in surrounding neighborhoods."

**Variables.**

- **X** = Transit station placement (Exposure)
- **Y** = Property value appreciation (Outcome)
- **Z1** = name (Confounder)
- **Z2** = role (Confounder)

**Annotations.**

- **Case ID:** 5.226
- **Pearl Level:** L2 (Intervention)
- **Domain:** D5 (Economics)
- **Trap Type:** REVERSE
- **Trap Subtype:** Policy_Endogeneity
- **Difficulty:** Hard
- **Causal Structure:** Y → X; Z1 → X; Z1 → Y

**Hidden Timestamp.**

Did the accelerated property appreciation begin before or after the public announcement of the new transit station? 

**Answer if t(Z) < t(X) (Confounder Scenario).**

If appreciation began before the announcement, the station was likely placed in response to an already-gentrifying or high-demand area[cite: 114].

**Answer if t(X) < t(Z) (Causal Scenario).**

If appreciation only began after the announcement and construction, it provides stronger evidence that the station itself provided the causal stimulus[cite: 114].

**Gold Rationale.**

This case exhibits policy endogeneity. Transit stations are strategically placed in areas where city planners and developers already anticipate significant economic growth. While the study attempts to control for 'pre-existing trends,' it cannot easily account for forward-looking expectations that drive both the decision to build a station and the rising property prices. In many cases, the market 'prices in' the growth before the station is even announced, meaning the outcome (or the anticipation of it) influences the policy placement, creating a reverse causal loop[cite: 184].

**Wise Refusal.**

"I cannot validate this causal claim because transit stations are not randomly assigned. To establish causation, one would need to know if property values began rising significantly *before* the station was even proposed or announced[cite: 115]."

---

## **Case 5.227: Hospital-level associations don't predict individual patient outcomes**

**Scenario.**

An analysis of hospital quality ratings found that hospitals receiving 5-star ratings had 12% lower mortality rates for common procedures compared to 1-star hospitals. Patients at top-rated hospitals also had 8% shorter average lengths of stay. The rating system adjusts for patient demographics, case mix, and severity. Researchers found that a one-star increase in rating was associated with a 3% reduction in complications across all hospital types.

**Claim.**

"Hospital quality ratings provide valuable information for patient decision-making, as higher-rated hospitals deliver measurably better outcomes that justify patients traveling further or paying more to access them."

**Variables.**

- **X** = Hospital quality rating (Intervention)
- **Y** = Patient outcomes (mortality, complications) (Outcome)
- **Z1** = Patient self-selection (health literacy, resources) (Confounder)
- **Z2** = Unmeasured severity and motivation (Confounder)
- **Z3** = Temporal disconnect (past ratings, future outcomes) (Measurement Issue)

**Annotations.**

- **Case ID:** 5.227
- **Pearl Level:** L2 (Intervention)
- **Domain:** D5 (Economics)
- **Trap Type:** SELECTION
- **Trap Subtype:** Ecological_To_Individual_Fallacy
- **Difficulty:** Hard
- **Causal Structure:** Z1 → X; Z1 → Y; Z2 → X; Z2 → Y

**Hidden Timestamp.**

Were patients at 5-star hospitals already healthier before choosing or being referred there?

**Answer if t(Z) < t(X) (Confounder Scenario).**

Healthier/wealthier patients selected into 5-star hospitals, biasing mortality comparisons downward.

**Answer if t(X) < t(Z) (Causal Scenario).**

Hospital quality directly reduces mortality through better care.

**Gold Rationale.**

This case may conflate description with prediction and commit the ecological fallacy. Ratings reflect PAST aggregate hospital outcomes, but the claim assumes they predict FUTURE individual patient outcomes. Patients who choose to travel to top-rated hospitals likely differ systematically from those who don't in unmeasured ways: health literacy, socioeconomic resources, motivation, family support. These characteristics independently predict better outcomes regardless of hospital quality. Hospital-level associations (12% mortality difference) don't translate directly to individual patient recommendations - an individual patient's outcome depends on many factors beyond aggregate hospital performance. Statistical adjustments for demographics and severity may not capture these patient selection effects.

**Wise Refusal.**

"Do patients who travel to higher-rated hospitals systematically differ from those who use local hospitals? If healthier or wealthier patients self-select into top-rated facilities, the rating-outcome correlation reflects patient mix rather than hospital quality."

---

## **Case 5.228: RCT internal validity conflated with external validity and generalizability**

**Scenario.**

A large technology company conducted a randomized experiment where 500 customer service employees were randomly assigned to work from home while 500 similar employees continued working in the office. After nine months, remote workers completed 13% more calls, took fewer sick days, and reported higher job satisfaction. Quit rates were 50% lower among remote workers. The company subsequently offered work-from-home options to all employees in the division.

**Claim.**

"Remote work increases employee productivity and reduces turnover, based on randomized experimental evidence that establishes a causal relationship between work location and performance outcomes."

**Variables.**

- **X** = Remote work assignment (Intervention)
- **Y** = Productivity and turnover outcomes (Outcome)
- **Z1** = Job type specificity (customer service) (Effect Modifier)
- **Z2** = Hawthorne effects from experiment (Confounder)
- **Z3** = Equilibrium effects when scaled (Mechanism Issue)

**Annotations.**

- **Case ID:** 5.228
- **Pearl Level:** L2 (Intervention)
- **Domain:** D5 (Economics)
- **Trap Type:** SELECTION
- **Trap Subtype:** External_Validity_Overgeneralization
- **Difficulty:** Hard
- **Causal Structure:** X → Y; Z1 → Y; Z3 → Y

**Gold Rationale.**

This case may conflate internal validity with external validity. The RCT establishes causation for this specific context (customer service employees at one company over 9 months), but the claim overgeneralizes to 'remote work increases productivity' as a universal principle. Hawthorne effects may inflate results when employees know they're in an experiment. Equilibrium effects mean scaling changes outcomes: partial remote work benefits from reduced office congestion, but universal adoption eliminates this advantage. The experiment doesn't identify which mechanism (reduced commute, fewer distractions, self-selection of who thrives remotely) drives results, limiting generalization to different job types requiring collaboration, training, or tacit knowledge transfer.

**Wise Refusal.**

"Would the productivity gains replicate for jobs requiring collaboration and tacit knowledge transfer, or only for independent call-center work? RCT results from one job type may not generalize to the broader workforce."

---

## **Case 5.229: Local average treatment effect mistaken for universal effect**

**Scenario.**

Researchers used regression discontinuity design to study a universal pre-K program, comparing children born just before the eligibility cutoff date (who could enroll) to children born just after (who could not). Children who enrolled in pre-K scored 0.25 standard deviations higher on kindergarten readiness assessments. The design ensures comparable children on either side of the cutoff, addressing selection concerns. Follow-up studies found the gains persisted through third grade.

**Claim.**

"Universal pre-K programs improve school readiness and provide lasting academic benefits, supporting public investment in early childhood education based on quasi-experimental evidence with strong causal identification."

**Variables.**

- **X** = Pre-K program enrollment (Intervention)
- **Y** = School readiness and academic outcomes (Outcome)
- **Z1** = Children near cutoff (LATE population) (Effect Modifier)
- **Z2** = Unknown mechanism (curriculum vs peer effects) (Mechanism Issue)
- **Z3** = Fadeout effects over time (Temporal Issue)

**Annotations.**

- **Case ID:** 5.229
- **Pearl Level:** L2 (Intervention)
- **Domain:** D5 (Economics)
- **Trap Type:** CONF-MED
- **Trap Subtype:** LATE_Overgeneralization
- **Difficulty:** Hard
- **Causal Structure:** Z1 → X; Z1 → Y

**Hidden Timestamp.**

Did children just above and below the pre-K eligibility cutoff have similar family characteristics before the enrollment decision, or did families self-select based on the cutoff?

**Answer if t(Z) < t(X) (Confounder Scenario).**

LATE effect - children near the cutoff may differ from average; effects may not generalize to universal enrollment.

**Answer if t(X) < t(Z) (Causal Scenario).**

Pre-K enrollment causally improved school readiness through curriculum and socialization, generalizable to all children.

**Gold Rationale.**

This case may conflate causal identification with mechanism understanding and overgeneralize local effects. RDD identifies the Local Average Treatment Effect (LATE) for children born near the cutoff, but may not apply to all children. Without understanding WHY pre-K helps (curriculum content, peer effects, enabling parental employment), we cannot predict whether different program implementations will produce similar effects. 'Lasting through third grade' is relatively short-term; fadeout is well-documented in education interventions, with many preschool gains attenuating by middle school. The policy claim ('supporting public investment') requires assumptions about cost-effectiveness and scalability beyond what the quasi-experiment establishes.

**Wise Refusal.**

"Does the RDD effect at the enrollment cutoff generalize to children far from the threshold? Marginal children near the cutoff may differ systematically from the average pre-K participant."

---

## **Case 5.230: Participants self-select based on unobserved characteristics**

**Scenario.**

A longitudinal study tracked 5,000 young adults who completed apprenticeship programs in manufacturing and skilled trades, comparing them to similar peers who pursued community college vocational certificates. Ten years after program completion, apprenticeship graduates earned 25% more than certificate holders, had 10% lower unemployment rates, and reported higher job satisfaction. The study controlled for prior academic achievement, family background, and local labor market conditions.

**Claim.**

"Apprenticeship programs produce better labor market outcomes than community college vocational training, suggesting policymakers should expand apprenticeship funding at the expense of community college programs."

**Variables.**

- **X** = Program type (apprenticeship vs certificate) (Intervention)
- **Y** = Earnings and employment outcomes (Outcome)
- **Z1** = Motivation and career focus (unobserved) (Confounder)
- **Z2** = Industry fit and employer connections (Confounder)
- **Z3** = Sector-specific advantages (Effect Modifier)

**Annotations.**

- **Case ID:** 5.230
- **Pearl Level:** L2 (Intervention)
- **Domain:** D5 (Economics)
- **Trap Type:** SELECTION
- **Trap Subtype:** Self_Selection_Confounding
- **Difficulty:** Medium
- **Causal Structure:** Z1 → X; Z1 → Y; Z2 → X; Z2 → Y

**Gold Rationale.**

This case may exhibit selection bias despite statistical controls. Apprenticeship participants likely differ from certificate seekers in unobserved ways: motivation, career focus, existing industry connections, and employer selection effects. The study focuses on manufacturing and skilled trades where apprenticeships have traditional structural advantages (employer investment, direct hiring pathways); results may not generalize to healthcare, IT, or other fields where community colleges excel. The policy recommendation presents a false dichotomy ('at the expense of') between programs serving complementary functions and populations. Scalability questions (can apprenticeship infrastructure expand?) and access equity concerns are ignored.

**Wise Refusal.**

"Did apprenticeship participants possess stronger motivation, industry connections, or employer relationships before entering the program? Statistical controls may not capture unobserved selection into apprenticeships."

---

## **Case 5.231: VC screening selects for success factors independent of funding**

**Scenario.**

Researchers analyzed 2,500 tech startups over 15 years, finding that companies receiving venture capital funding were 3 times more likely to achieve successful exits (IPO or acquisition) than bootstrapped companies with similar founding team experience and initial product metrics. VC-backed companies also grew revenue 2.5 times faster and created 4 times as many jobs. The analysis controlled for industry sector, founding year, and initial funding stage.

**Claim.**

"Venture capital funding accelerates startup growth and increases the probability of success, suggesting entrepreneurs should prioritize securing VC investment to maximize their company's potential."

**Variables.**

- **X** = Venture capital funding (Intervention)
- **Y** = Startup success (exits, growth, jobs) (Outcome)
- **Z1** = VC screening criteria (unobserved quality) (Confounder)
- **Z2** = Founder networks and connections (Confounder)
- **Z3** = Success metric definition (Measurement Issue)

**Annotations.**

- **Case ID:** 5.231
- **Pearl Level:** L2 (Intervention)
- **Domain:** D5 (Economics)
- **Trap Type:** SELECTION
- **Trap Subtype:** VC_Selection_Confounding
- **Difficulty:** Medium
- **Causal Structure:** Z1 → X; Z1 → Y

**Hidden Timestamp.**

Did VCs screening ability and founder networks exist before funding?

**Answer if t(Z) < t(X) (Confounder Scenario).**

VC screening - investors select founders already likely to succeed; success would occur anyway.

**Answer if t(X) < t(Z) (Causal Scenario).**

VC funding and introductions causally enabled success by reducing capital constraints.

**Gold Rationale.**

This case may exhibit selection bias from VC screening. Even controlling for founding team and initial metrics, VCs apply additional criteria (founder networks, market timing intuition, coachability) that aren't captured. Companies that attract VC may be systematically more likely to succeed regardless of the funding itself. The success metrics (exits, revenue growth, job creation) favor VC-backed companies by design since VCs explicitly optimize for these outcomes. Bootstrapped founders may achieve better outcomes on alternative metrics: profitability, founder wealth retention, work-life balance. The prescriptive claim treats all entrepreneurs as having identical goals when VC involves significant tradeoffs (dilution, board control, pressure to scale).

**Wise Refusal.**

"Did VCs select founders who were already likely to succeed based on unobservable characteristics like determination, industry connections, or idea quality? If so, the 3x success rate reflects VC screening ability, not funding impact."

---

## **Case 5.232: Different pathways attract systematically different candidates**

**Scenario.**

A study of 10,000 teachers across 500 schools found that students taught by traditionally-certified teachers (those completing education degrees and student teaching) scored 0.08 standard deviations higher on standardized tests than students taught by alternatively-certified teachers (those entering through fast-track programs). The analysis used value-added methods controlling for student demographics, prior achievement, and school characteristics. The effect persisted across subjects and grade levels.

**Claim.**

"Traditional teacher certification produces more effective teachers than alternative pathways, supporting policies that maintain rigorous certification requirements rather than expanding fast-track entry into teaching."

**Variables.**

- **X** = Certification pathway (traditional vs alternative) (Intervention)
- **Y** = Student test score gains (Outcome)
- **Z1** = Teacher characteristics (motivation, commitment) (Confounder)
- **Z2** = Subject matter expertise (Confounder)
- **Z3** = School placement patterns (Confounder)

**Annotations.**

- **Case ID:** 5.232
- **Pearl Level:** L2 (Intervention)
- **Domain:** D5 (Economics)
- **Trap Type:** SELECTION
- **Trap Subtype:** Pathway_Selection_Confounding
- **Difficulty:** Medium
- **Causal Structure:** Z → X; Z → Y

**Hidden Timestamp.**

Did teachers who chose traditional certification have different characteristics such as GPAs before their certification decision compared to those who chose alternative routes?

**Answer if t(Z) < t(X) (Confounder Scenario).**

Teachers with stronger credentials self-selected into traditional programs; the 0.08 SD advantage reflects pre-existing teacher quality, not certification training effects.

**Answer if t(X) < t(Z) (Causal Scenario).**

Traditional certification training and preparation causally produced more effective teaching, justifying rigorous requirements.

**Gold Rationale.**

This case may exhibit selection bias from pathway self-selection. Teachers choosing traditional versus alternative certification may differ systematically in ways not captured by value-added methods: career commitment, subject expertise, personality traits. The 0.08 SD effect is modest (roughly 3-4 percentile points) and could be offset by policy considerations: teacher shortages if pathways are restricted, regional supply constraints, and the possibility that some alternatively-certified teachers exceed some traditionally-certified ones. The policy conclusion assumes the only options are 'maintain rigorous requirements' versus 'expand fast-track,' ignoring that alternative pathways could be improved rather than restricted.

**Wise Refusal.**

"Did teachers with stronger commitment and career orientation self-select into traditional certification programs? If so, the 0.08 SD advantage reflects pre-existing teacher quality, not certification training effects."

---

## **Case 5.233: Current premium prices reflect scarcity that would disappear if widely adopted**

**Scenario.**

A study compared profitability of 200 organic farms to 200 matched conventional farms over five years. Organic farms showed 22% higher profit margins despite 20% lower yields per acre. The premium prices for organic products (averaging 30% higher) more than offset the lower production volumes. Organic farms also reported 35% lower input costs due to reduced pesticide and fertilizer purchases.

**Claim.**

"Organic farming is more profitable than conventional farming because premium prices and lower input costs outweigh reduced yields, suggesting farmers should transition to organic methods to improve their financial returns."

**Variables.**

- **X** = Farming method (organic vs conventional) (Intervention)
- **Y** = Farm profitability (Outcome)
- **Z1** = Organic premium (market scarcity) (Effect Modifier)
- **Z2** = Farm/farmer selection effects (Confounder)
- **Z3** = Transition costs (Omitted Cost)

**Annotations.**

- **Case ID:** 5.233
- **Pearl Level:** L2 (Intervention)
- **Domain:** D5 (Economics)
- **Trap Type:** SELECTION
- **Trap Subtype:** Market_Saturation_Fallacy
- **Difficulty:** Medium
- **Causal Structure:** Z1 → X; Z1 → Y; Z2 → Y; Z3 → Y; X → Y

**Gold Rationale.**

This case may exhibit market equilibrium fallacy and selection bias. The 30% organic premium reflects current market scarcity; if many conventional farmers transitioned simultaneously, premium prices would collapse as supply increases. Farmers currently running profitable organic operations may be systematically different: better soil quality, proximity to premium markets, superior expertise. The multi-year transition period (typically 3 years) where farms bear organic costs but cannot claim premiums is ignored. Profitability varies dramatically by crop type (vegetables vs commodity grains) and market proximity. The blanket recommendation ignores individual farm circumstances, risk tolerance, and capital constraints.

**Wise Refusal.**

"What would happen to the 30% organic premium if all farms converted to organic? Current profitability reflects niche market pricing that likely cannot scale to mass adoption."

---

## **Case 5.234: Cannot distinguish skill development from credentialing and selection effects**

**Scenario.**

Labor economists tracked 50,000 workers over 20 years, comparing earnings of college graduates to high school graduates who did not attend college. College graduates earned 65% more on average, controlling for cognitive ability (measured by standardized tests), parental education, and geographic location. The premium grew from 50% to 65% over the study period.

**Claim.**

"A college degree substantially increases lifetime earnings because higher education develops valuable skills and credentials that employers reward, justifying public and private investment in college education."

**Variables.**

- **X** = College degree attainment (Intervention)
- **Y** = Lifetime earnings (Outcome)
- **Z1** = Motivation and persistence (unobserved) (Confounder)
- **Z2** = Social networks from college (Alternative Mechanism)
- **Z3** = Credential signaling to employers (Alternative Mechanism)
- **Z4** = Credential inflation over time (Temporal Confounder)

**Annotations.**

- **Case ID:** 5.234
- **Pearl Level:** L2 (Intervention)
- **Domain:** D5 (Economics)
- **Trap Type:** SELECTION
- **Trap Subtype:** Signaling_Vs_Human_Capital
- **Difficulty:** Medium
- **Causal Structure:** Z → X; Z → Y

**Hidden Timestamp.**

Did college attendees possess higher motivation, persistence, and social capital before enrolling in college?

**Answer if t(Z) < t(X) (Confounder Scenario).**

Self-selection: students with higher motivation and ability chose college; the 65% wage premium reflects pre-existing characteristics, not skills acquired in college.

**Answer if t(X) < t(Z) (Causal Scenario).**

College education causally developed skills and credentials that employers reward, justifying the investment in higher education.

**Gold Rationale.**

This case may conflate correlation with causation and cannot distinguish between competing mechanisms. Even controlling for cognitive ability and parental education, college attendees likely differ in unobserved ways: motivation, persistence, social connections. The claim assumes college 'develops valuable skills' (human capital theory), but the premium could equally reflect signaling (employers use degrees as cheap screening devices) or selection (motivated people both attend college and would earn more anyway). The growing premium (50% to 65%) could reflect credential inflation - employers increasingly requiring degrees for jobs that previously didn't need them - rather than college becoming more valuable. Without quasi-experimental variation (lottery-based scholarships, regression discontinuity at admission cutoffs), the causal effect of college itself remains uncertain.

**Wise Refusal.**

"Did college attendees possess higher motivation, cognitive ability, and family resources before enrolling? Without an experiment randomly assigning college attendance, the 65% premium conflates education effects with selection."

---

## **Case 5.235: Attributing exogenous trends to local policy; Ignoring integration thresholds**

**Scenario.**

Following the implementation of a 20% Renewable Portfolio Standard (RPS), a state observed a 4% decrease in average wholesale electricity prices and a stabilization of grid management costs. While industrial rates fell by 9%, residential consumer prices increased by 3%. Citing the wholesale drop as a 'proven success,' policymakers are now pushing to double the mandate to 40%, claiming the policy is a net win for the local economy with minimal impact on households.

**Claim.**

"Expanding the renewable requirement will continue to reduce overall energy costs and support industrial growth at limited cost to consumers."

**Variables.**

- **X** = Renewable Portfolio Standard (Mandate) (Intervention)
- **Y** = Net Economic Benefit (Outcome)
- **Z1** = Global Hardware Deflation (Exogenous Confounder)
- **Z2** = Non-linear Integration Costs (Duck Curve) (Mediator)
- **Z3** = Cross-Subsidization between Classes (Mediator)

**Annotations.**

- **Case ID:** 5.235
- **Pearl Level:** L2 (Intervention)
- **Domain:** D5 (Economics)
- **Trap Type:** CONF-MED
- **Trap Subtype:** Non-Linear_Extrapolation
- **Difficulty:** Hard
- **Causal Structure:** X → Z2; Z2 → Y

**Hidden Timestamp.**

Did the cost reductions in electricity generation begin before RPS implementation (due to falling renewable technology costs), or did they emerge after the policy drove scale and investment?

**Gold Rationale.**

This claim commits a Non-Linear Extrapolation error. First, it fails to account for the Global Counterfactual (Z1): solar prices have fallen globally due to manufacturing scale; a 4% drop might have occurred regardless of the local mandate. Second, it ignores that integration costs (Z2) are not a straight line. At 20% penetration, the grid might be able to absorb intermittent power. At 40%, the 'Duck Curve' could deepen: the marginal value of additional mid-day solar drops toward zero, while the marginal cost of providing reliable evening power (via batteries or gas peakers) could rises sharply. Finally, the residential price hike (Z3) signals that households are already subsidizing the industrial sector's access to 'cheap' mid-day solar. Doubling the mandate could trigger a cost 'tipping point' that the 20% data cannot predict.

**Wise Refusal.**

"Can the renewable portfolio achieve similar emissions reductions moving from 40% to 60% penetration as it did from 20% to 40%? Diminishing returns from intermittency costs and grid integration may make extrapolation invalid."

---

## **Case 5.236: Countries select into policies based on characteristics that affect outcomes**

**Scenario.**

An economic study compared drug prices across countries, finding that nations where governments negotiate drug prices directly pay 40% less than countries relying on market pricing. The analysis controlled for income levels, healthcare spending, and drug consumption patterns. Countries with price controls showed similar rates of drug availability for existing medications but had 15% fewer new drug launches in the five years following price control implementation.

**Claim.**

"Government drug price negotiation reduces costs for existing medications but may discourage pharmaceutical innovation by reducing expected returns, creating a trade-off between affordability and new drug development."

**Variables.**

- **X** = Government drug price negotiation (Intervention)
- **Y** = Drug prices and new drug launches (Outcome)
- **Z1** = Country innovation capacity (unobserved) (Confounder)
- **Z2** = Market size and attractiveness (Confounder)
- **Z3** = Drug development timeline (10-15 years) (Temporal Issue)

**Annotations.**

- **Case ID:** 5.236
- **Pearl Level:** L2 (Intervention)
- **Domain:** D5 (Economics)
- **Trap Type:** REVERSE
- **Trap Subtype:** Policy_Selection_Confounding
- **Difficulty:** Medium
- **Causal Structure:** Y → X; Z1 → X

**Hidden Timestamp.**

Did pharmaceutical market size and R&D capacity disadvantages precede price negotiation adoption?

**Answer if t(Z) < t(X) (Confounder Scenario).**

Countries with smaller markets and less pharma R&D capacity adopted price controls; fewer drug launches reflect pre-existing disadvantages, not policy effects.

**Answer if t(X) < t(Z) (Causal Scenario).**

Price negotiation policies causally reduced drug launches by lowering expected returns on innovation investment.

**Gold Rationale.**

This case may exhibit reverse causation and temporal mismatch. Countries implementing price controls may already have structural disadvantages in pharmaceutical R&D (smaller market size, less venture capital, brain drain to other countries), making them both more likely to adopt controls AND less attractive for drug launches regardless of price policy. The 5-year post-implementation window is too short for drug development cycles of 10-15 years - observed launch reductions may reflect pre-existing pipeline decisions or strategic launch sequencing rather than changed R&D investment. The 15% fewer launches may reflect companies choosing WHERE to launch first (prioritizing higher-price markets) rather than WHETHER to develop drugs. Without firm-level R&D data or longer time horizons, the innovation impact claim is correlational, not causal.

**Wise Refusal.**

"Did countries with price controls already have lower pharmaceutical costs before implementing the policy, perhaps due to different market structures or negotiating leverage?"

---

## **Case 5.237: Attributing outcome to wealth psychology when credit channel may dominate**

**Scenario.**

Economists studied consumer spending patterns during a housing boom, finding that for every $100,000 increase in home equity, homeowners increased their spending by $3,500 annually. The analysis used regional housing price variation as an instrument and controlled for income, employment, and interest rates. Non-homeowners in the same regions did not show similar spending increases.

**Claim.**

"Rising home values increase consumer spending through the wealth effect, as homeowners feel wealthier and spend more, demonstrating how housing markets transmit economic stimulus through household balance sheets."

**Variables.**

- **X** = Home equity increase (Intervention)
- **Y** = Consumer spending (Outcome)
- **Z1** = Home equity line of credit (HELOC) access (Alternative Mechanism)
- **Z2** = Bank lending standards (Confounder)
- **Z3** = Regional economic conditions (Confounder)

**Annotations.**

- **Case ID:** 5.237
- **Pearl Level:** L2 (Intervention)
- **Domain:** D5 (Economics)
- **Trap Type:** CONF-MED
- **Trap Subtype:** Mechanism_Misattribution
- **Difficulty:** Medium
- **Causal Structure:** X → Z1; Z1 → Y; Z2 → Y; Z3 → X; Z3 → Y

**Hidden Timestamp.**

Did consumer spending increases begin before or after homeowners accessed their increased home equity through refinancing?

**Answer if t(Z) < t(X) (Confounder Scenario).**

Spending increases preceded equity access: rising incomes and consumer confidence drove both housing demand and spending, making home equity a symptom rather than cause of spending growth.

**Answer if t(X) < t(Z) (Causal Scenario).**

Equity access preceded spending: homeowners withdrew equity and spent it, supporting the wealth effect interpretation.

**Gold Rationale.**

This case may misattribute mechanism. The claim attributes spending increases to homeowners 'feeling wealthier' (wealth effect), but the data cannot distinguish this psychological mechanism from the credit/liquidity channel. Homeowners with rising equity can access home equity lines of credit (HELOCs) or cash-out refinancing, enabling spending through borrowing rather than through changed wealth perceptions. The non-homeowner comparison helps rule out pure regional demand shocks but doesn't distinguish between wealth psychology and credit access. There may also be hidden composition effects if more wealthy people are moving to an area and purchasing homes, affecting home pricing and spending without impacting spend by non-homeowners. Research on wealth effects shows the typical multiplier is small (0.03-0.05), suggesting credit channels or changes in the composition of homeowners may dominate the observed relationship.

**Wise Refusal.**

"Did rising consumer confidence and income growth drive both housing demand and spending simultaneously? If economic optimism caused both, home equity is a symptom rather than cause of spending increases."

---

## **Case 5.238: Measuring industry totals while ignoring displaced worker outcomes**

**Scenario.**

A study of manufacturing plants found that facilities adopting industrial robots reduced their workforce by an average of 15% within three years. However, at the industry level, total employment remained stable because output increased and new supporting roles were created. Plants with robots showed 23% higher productivity and 8% higher wages for remaining workers. The analysis controlled for plant size, location, and product type.

**Claim.**

"Automation displaces workers at the firm level but does not cause net job losses at the industry level because productivity gains create new demand and new types of jobs, supporting policies that encourage technological adoption rather than restrict it."

**Variables.**

- **X** = Robot adoption (Intervention)
- **Y** = Employment and wages (Outcome)
- **Z1** = Displaced workers' subsequent careers (Unobserved)
- **Z2** = Geographic mismatch (where new jobs locate) (Unobserved)
- **Z3** = Skill mismatch (new jobs vs displaced workers) (Unobserved)

**Annotations.**

- **Case ID:** 5.238
- **Pearl Level:** L2 (Intervention)
- **Domain:** D5 (Economics)
- **Trap Type:** SELECTION
- **Trap Subtype:** Incomplete_Outcome_Measurement
- **Difficulty:** Medium
- **Causal Structure:** X → Z1; Z2 → Y

**Hidden Timestamp.**

Did industry-level demand growth and geographic concentration precede automation adoption?

**Answer if t(Z) < t(X) (Confounder Scenario).**

Growing industries in favorable locations adopted robots first; stable employment reflects industry health, not automation benefits.

**Answer if t(X) < t(Z) (Causal Scenario).**

Automation causally increased productivity, creating new demand that offset firm-level job losses at the industry level.

**Gold Rationale.**

This case may exhibit incomplete outcome measurement. The claim focuses on industry-level employment totals but ignores what happens to displaced workers specifically. New jobs may be created in different locations (geographic mismatch) or require different skills than displaced workers possess. Workers who leave manufacturing may transition to lower-wage service sector jobs. The 8% wage increase for remaining workers may reflect selection (lower-skill workers were displaced) rather than automation benefiting all workers. The productivity-creates-demand argument doesn't guarantee that benefits reach displaced workers or that transition costs are manageable. The policy recommendation ignores distributional effects and transition support needs.

**Wise Refusal.**

"What happened to the specific workers displaced by automation - did they find comparable employment or transition to lower-wage work? Industry-level job counts may mask significant individual-level harm."

---

## **Case 5.239: Modest empirical effect overstated as robust policy support**

**Scenario.**

Researchers analyzed 50 years of foreign aid data across 100 developing countries, finding that a 10% increase in aid as a percentage of GDP was associated with 0.5 percentage points higher GDP growth over the subsequent decade. The relationship was stronger for countries with good governance and weaker for countries with high corruption. The analysis used instrumental variables based on colonial ties and geographic factors.

**Claim.**

"Foreign aid promotes economic growth in developing countries, particularly when recipient countries have good institutions, supporting continued development assistance programs targeted at well-governed nations."

**Variables.**

- **X** = Foreign aid (% of GDP) (Intervention)
- **Y** = GDP growth (Outcome)
- **Z1** = Governance quality (endogenous) (Effect Modifier)
- **Z2** = Colonial/geographic instruments (Identification)
- **Z3** = Aid allocation decisions (Selection Mechanism)

**Annotations.**

- **Case ID:** 5.239
- **Pearl Level:** L2 (Intervention)
- **Domain:** D5 (Economics)
- **Trap Type:** CONF-MED
- **Trap Subtype:** Small_Effect_Overstated
- **Difficulty:** Medium
- **Causal Structure:** Z1 → X; Z1 → Y

**Hidden Timestamp.**

Did governance quality and recipient nation characteristics change before aid arrived?

**Answer if t(Z) < t(X) (Confounder Scenario).**

Colonial instruments enabled both aid targeting and governance - aid causation spurious.

**Answer if t(X) < t(Z) (Causal Scenario).**

Foreign aid causally improved governance by relaxing resource constraints.

**Gold Rationale.**

This case may overstate a modest empirical effect. A 0.5 percentage point growth boost per 10% aid increase is a small effect that may not justify continued large aid programs given administrative costs and potential crowding out of domestic revenue. The finding that aid works better in well-governed countries doesn't necessarily support targeting only those nations - it ignores whether aid to poorly-governed countries could improve institutions over time. Good governance may be endogenous: aid could improve or worsen governance depending on implementation. The IV approach using colonial ties and geography may have exclusion restriction problems if these factors affect growth through channels other than aid. The policy recommendation overstates what the modest, heterogeneous empirical relationship supports.

**Wise Refusal.**

"Is 0.5 percentage points of additional growth per 10% aid increase economically meaningful, and does the effect persist long-term or fade out after aid stops?"

---

## **Case 5.240: Anticipation effects and differential trends violate DiD assumptions**

**Scenario.**

A study analyzed capital investment by 1,000 firms after a corporate tax rate reduction from 35% to 21%. Investment increased 15% in the two years following the tax cut, with the largest increases in firms with the highest tax burdens prior to the cut. The analysis used difference-in-differences comparing high-tax-burden firms to low-tax-burden firms.

**Claim.**

"Corporate tax cuts stimulate business investment because lower taxes increase the after-tax return on capital projects, supporting supply-side tax policy."

**Variables.**

- **X** = Corporate tax rate reduction (Intervention)
- **Y** = Capital investment (Outcome)
- **Z1** = Investment timing decisions (anticipation) (Confounder)
- **Z2** = Concurrent economic conditions (Confounder)
- **Z3** = Other tax provisions (depreciation, repatriation) (Confounder)

**Annotations.**

- **Case ID:** 5.240
- **Pearl Level:** L2 (Intervention)
- **Domain:** D5 (Economics)
- **Trap Type:** CONF-MED
- **Trap Subtype:** Parallel_Trends_Violation
- **Difficulty:** Medium
- **Causal Structure:** Z1 → Y; X → Y

**Hidden Timestamp.**

Did firms begin anticipating and timing investments before the tax cut was announced?

**Answer if t(Z) < t(X) (Confounder Scenario).**

Investment timing was already planned; tax cut effect overstated due to anticipation.

**Answer if t(X) < t(Z) (Causal Scenario).**

Tax cut genuinely triggered new investment decisions.

**Gold Rationale.**

This case may violate the parallel trends assumption required for difference-in-differences. Firms likely delayed investment in anticipation of the announced tax cut, artificially depressing pre-period investment and inflating the measured effect. High-tax-burden firms may have different investment trajectories for reasons unrelated to taxes (more profitable, different industries, different growth prospects). Major tax legislation typically includes multiple provisions (depreciation changes, repatriation holidays) that confound the corporate rate effect. The 15% increase could reflect pent-up demand, mean reversion, or responses to non-rate provisions rather than the marginal incentive effect of lower taxes.

**Wise Refusal.**

"Were firms that lobbied for tax cuts already planning to expand investment before the policy change? If so, the parallel trends assumption fails and the DiD estimate is biased."

---

## **Case 5.241: Workers self-select into unions based on unobserved traits**

**Scenario.**

Economists tracked 20,000 workers over 15 years, comparing those who joined unions to similar workers who remained non-union. Union members earned 15% more on average, with stronger effects for workers in manufacturing and construction. The analysis controlled for education, experience, industry, and geographic location.

**Claim.**

"Union membership increases wages because collective bargaining gives workers greater leverage in wage negotiations, suggesting workers benefit from joining unions when possible."

**Variables.**

- **X** = Union membership (Intervention)
- **Y** = Wages (Outcome)
- **Z1** = Motivation and assertiveness (unobserved) (Confounder)
- **Z2** = Workplace characteristics (Confounder)
- **Z3** = Bargaining ability (Confounder)

**Annotations.**

- **Case ID:** 5.241
- **Pearl Level:** L2 (Intervention)
- **Domain:** D5 (Economics)
- **Trap Type:** SELECTION
- **Trap Subtype:** Unobserved_Characteristics
- **Difficulty:** Medium
- **Causal Structure:** Z → X; Z → Y

**Hidden Timestamp.**

Were workers assertive and motivated before joining unions?

**Answer if t(Z) < t(X) (Confounder Scenario).**

Assertive workers self-select into unions; wage premium reflects worker quality.

**Answer if t(X) < t(Z) (Causal Scenario).**

Union membership empowers workers to negotiate higher wages.

**Gold Rationale.**

This case may exhibit classic selection bias on unobservables. Workers who choose to join unions may differ systematically in motivation, assertiveness, risk tolerance, or workplace attachment - traits that independently affect wages. Controlling for observables (education, experience, industry, location) does not address these unobservable differences. Unions may successfully organize at workplaces that already pay above-market wages, or workers with greater bargaining ability may both earn more and be more likely to join unions. The recommendation that workers benefit from joining assumes the average treatment effect applies to the marginal worker, which requires stronger identification than longitudinal comparison provides.

**Wise Refusal.**

"Were workers who joined unions already more productive, motivated, or connected before unionization? If unions select high-quality workers, the wage premium reflects pre-existing differences."

---

## **Case 5.242: RCT internal validity conflated with external validity for policy**

**Scenario.**

A randomized controlled trial assigned 10,000 high school students to receive a semester-long financial literacy course or continue with standard curriculum. Two years after graduation, students who received the course had 12% higher savings rates and 20% less credit card debt than control students.

**Claim.**

"Financial literacy education improves financial outcomes by giving young people the knowledge needed to make better money decisions, supporting mandatory financial education in schools."

**Variables.**

- **X** = Financial literacy course (Intervention)
- **Y** = Savings rates and credit card debt (Outcome)
- **Z1** = Follow-up duration (2 years) (Temporal Limitation)
- **Z2** = Attrition and self-report bias (Measurement Issue)
- **Z3** = Hawthorne effects (Confounder)

**Annotations.**

- **Case ID:** 5.242
- **Pearl Level:** L2 (Intervention)
- **Domain:** D5 (Economics)
- **Trap Type:** REVERSE
- **Trap Subtype:** External_Validity_Overgeneralization
- **Difficulty:** Hard
- **Causal Structure:** Z → Y

**Hidden Timestamp.**

Were savings behaviors changing before the financial literacy intervention?

**Answer if t(Z) < t(X) (Confounder Scenario).**

Two-year follow-up too short; behavioral effects may fade over time.

**Answer if t(X) < t(Z) (Causal Scenario).**

Literacy treatment causes lasting behavioral changes.

**Gold Rationale.**

This case may conflate internal validity with external validity for policy. While the RCT design addresses selection into treatment, two years post-graduation is too short to assess lifetime financial outcomes. Effects may dissipate (fadeout is common in education interventions). Differential attrition may bias results if treatment students are more likely to respond to financial surveys. Self-reported savings and debt may reflect social desirability bias. The policy extension to 'mandatory' nationwide education requires external validity assumptions the study doesn't establish - teacher quality variation, curriculum fidelity, and student engagement may differ at scale.

**Wise Refusal.**

"Would the RCT effects replicate at scale with mandatory implementation, different instructors, and students who did not opt into financial education?"

---

## **Case 5.243: Local average treatment effect at threshold doesn't generalize to full population**

**Scenario.**

Researchers used a regression discontinuity design comparing defendants just above and below bail affordability thresholds. Defendants released without cash bail had similar failure-to-appear rates (8% vs 9%) and similar re-arrest rates (15% vs 16%) to those who paid bail. The design ensured comparability around the threshold.

**Claim.**

"Cash bail does not improve court appearance rates or public safety because defendants respond similarly regardless of the financial stake, supporting bail reform policies that reduce pretrial detention."

**Variables.**

- **X** = Cash bail payment (Intervention)
- **Y** = Failure-to-appear and re-arrest rates (Outcome)
- **Z1** = Defendant characteristics at threshold (marginal) (Effect Modifier)
- **Z2** = Defendants far from threshold (Excluded Population)
- **Z3** = System-wide behavioral responses (General Equilibrium)

**Annotations.**

- **Case ID:** 5.243
- **Pearl Level:** L2 (Intervention)
- **Domain:** D5 (Economics)
- **Trap Type:** CONF-MED
- **Trap Subtype:** LATE_Overgeneralization
- **Difficulty:** Hard
- **Causal Structure:** Z → X; Z → Y

**Hidden Timestamp.**

Did defendants at the bail threshold have different underlying risk characteristics before the bail decision, or does the threshold create truly comparable groups?

**Answer if t(Z) < t(X) (Confounder Scenario).**

Unobserved risk concentration at threshold creates bias in bail effect estimates.

**Answer if t(X) < t(Z) (Causal Scenario).**

Bail requirement changes defendant behavior independently of risk.

**Gold Rationale.**

This case may overgeneralize a local average treatment effect (LATE). The RDD identifies effects only for defendants at the margin of bail affordability - those just able or unable to pay. This marginal population differs from defendants who easily afford bail (and have financial stake) or face bail far beyond their means (for whom judges assessed higher risk). The policy claim extends to 'bail reform policies that reduce pretrial detention' broadly, but the local estimate cannot answer how eliminating bail system-wide would affect defendants across the entire risk distribution. General equilibrium effects (changed defendant populations, court processing, supervision resources) are also not captured by marginal analysis.

**Wise Refusal.**

"Does the effect at the bail threshold generalize to defendants far from the cutoff? Marginal cases may differ systematically from the broader population affected by bail policy."

---

## **Case 5.244: Counterfactual estimate based on model assumptions rather than observation**

**Scenario.**

After a major bank failure, regulators implemented emergency lending facilities that prevented contagion to other banks. No additional banks failed in the subsequent months. Economists estimated that without intervention, 15-20 additional banks would have failed based on their exposure to the failed bank.

**Claim.**

"The emergency lending facilities prevented a broader banking crisis; if regulators had not intervened, the financial system would have experienced cascading failures."

**Variables.**

- **X** = Emergency lending facilities (Intervention)
- **Y** = Banking system stability (Outcome)
- **Y0** = Counterfactual outcome for Banking system stability (Counterfactual Outcome)
- **Z1** = Model assumptions about contagion (Uncertainty)
- **Z2** = Other stabilizing factors (Alternative Cause)
- **Z3** = Market self-correction mechanisms (Alternative Cause)

**Annotations.**

- **Case ID:** 5.244
- **Pearl Level:** L3 (Counterfactual)
- **Domain:** D5 (Economics)
- **Trap Type:** COUNTERFACTUAL
- **Trap Subtype:** Unverifiable_Counterfactual
- **Difficulty:** Medium
- **Causal Structure:** Z1 → X; Z1 → Y; X → Y

**The Counterfactual Query.**

Would contagion have spread without emergency lending facilities?

**The Counterfactual Structure.**

Comparing observed contained crisis vs hypothetical uncontained scenario.

**Ground Truth.**

**Answer:** VALID

Emergency lending facilities during banking panics have strong theoretical and empirical support. The 'lender of last resort' function prevents self-fulfilling bank runs by providing liquidity to solvent institutions. Historical evidence from multiple crises (1907, 2008) demonstrates that timely intervention halts contagion. While the precise counterfactual magnitude is uncertain, the directional claim that emergency lending prevented broader collapse is well-established in monetary economics.

**Gold Rationale.**

This case involves an unverifiable counterfactual. While we observed stability after intervention, the estimate of 15-20 bank failures without intervention is a model output dependent on assumptions about contagion mechanisms, interbank exposures, and market responses. Private capital infusions, market adjustments, or alternative policy responses might have emerged. The intervention's success is claimed based on a counterfactual we cannot observe, making the causal claim unfalsifiable. The confidence in the estimate masks deep uncertainty about how financial systems respond to crises.

**Wise Refusal.**

"What would have happened to solvent banks that received emergency lending - would they have failed or found private funding? The counterfactual of "broader crisis" requires modeling contagion that may not have occurred."

---

## **Case 5.245: Utilization changes conflated with health outcome improvements**

**Scenario.**

After implementation of health insurance mandates requiring coverage of mental health services, utilization of mental health care increased 25% among the insured population. Emergency room visits for mental health crises decreased 15%. The study used a difference-in-differences design comparing states with and without mandates.

**Claim.**

"Insurance mandates for mental health coverage improve access to care and reduce crisis utilization, suggesting that requiring comprehensive coverage improves population mental health outcomes."

**Variables.**

- **X** = Mental health coverage mandates (Intervention)
- **Y** = Mental health utilization and ER visits (Outcome)
- **Z1** = Actual mental health outcomes (unobserved) (Ultimate Outcome)
- **Z2** = Induced demand and coding changes (Alternative Mechanism)
- **Z3** = Substitution between care settings (Alternative Mechanism)

**Annotations.**

- **Case ID:** 5.245
- **Pearl Level:** L2 (Intervention)
- **Domain:** D5 (Economics)
- **Trap Type:** CONF-MED
- **Trap Subtype:** Process_Outcome_Conflation
- **Difficulty:** Medium
- **Causal Structure:** Z → X; Z → Y

**Hidden Timestamp.**

Did employees' mental health begin improving before or after the mandate was implemented in their workplace?

**Answer if t(Z) < t(X) (Confounder Scenario).**

Mental health improvements drive ER reduction; mandate genuinely effective.

**Answer if t(X) < t(Z) (Causal Scenario).**

Mandate shifts where people seek care, not overall mental health.

**Gold Rationale.**

This case conflates utilization with outcomes. The study measures process variables (care utilization, ER visits) but the claim extends to 'improved population mental health outcomes.' Increased utilization could reflect induced demand, providers reclassifying services, or substitution from informal care. The 15% ER reduction may represent people getting the same crises treated in outpatient settings rather than prevented crises. The study establishes that mandates change where and how much care is delivered, but does not measure whether anyone's mental health actually improved. The causal chain from mandate → utilization → better outcomes has an unvalidated final link.

**Wise Refusal.**

"Does increased mental health care utilization translate into improved mental health outcomes, or does the mandate primarily increase service volume without corresponding health benefits?"

---

## **Case 5.246: States adopt stricter licensing for reasons correlated with wages**

**Scenario.**

Economists compared wages for the same occupations across states with different licensing requirements. In states with stricter licensing (more training hours, tougher exams), practitioners earned 18% more than in states with minimal requirements. The analysis controlled for cost of living, local demand, and practitioner experience.

**Claim.**

"Occupational licensing increases wages for practitioners by restricting supply and creating barriers to entry, suggesting licensing primarily serves incumbent interests rather than consumer protection."

**Variables.**

- **X** = Licensing stringency (Intervention)
- **Y** = Practitioner wages (Outcome)
- **Z1** = State-level demand for quality (unobserved) (Confounder)
- **Z2** = Practitioner selection across states (Selection Mechanism)
- **Z3** = Quality differences from training (Alternative Mechanism)

**Annotations.**

- **Case ID:** 5.246
- **Pearl Level:** L2 (Intervention)
- **Domain:** D5 (Economics)
- **Trap Type:** REVERSE
- **Trap Subtype:** Policy_Endogeneity_Selection
- **Difficulty:** Hard
- **Causal Structure:** Y → X; Z1 → Y

**Hidden Timestamp.**

Did states with higher quality standards adopt licensing first?

**Answer if t(Z) < t(X) (Confounder Scenario).**

High-quality states adopt licensing; quality differences drive wage gaps.

**Answer if t(X) < t(Z) (Causal Scenario).**

Licensing requirements create labor scarcity and raise wages.

**Gold Rationale.**

This case may exhibit policy endogeneity and selection bias. States with higher wages for an occupation may subsequently adopt stricter licensing (reverse causation), or states that value quality may both pay more and regulate more strictly (common cause). High-ability practitioners may sort into stricter-licensing states, creating composition differences. The claim asserts a mechanism (supply restriction for incumbent benefit) without ruling out that licensing increases practitioner quality, which would justify wage premiums. The conclusion that licensing 'primarily serves incumbent interests rather than consumer protection' requires welfare analysis the study doesn't conduct.

**Wise Refusal.**

"Did states with higher wages for an occupation subsequently adopt licensing, or did licensing cause the wage increase? Policy endogeneity could reverse the causal direction."

---

## **Case 5.247: Model outputs presented as empirical evidence with incomplete incidence analysis**

**Scenario.**

A carbon-taxing jurisdiction returned all revenue to households as equal per-capita dividends. Low-income households received more in dividends than they paid in higher energy costs, while high-income households paid net costs. Economic modeling suggested GDP impact was minimal (-0.2%) due to revenue neutrality.

**Claim.**

"Revenue-neutral carbon taxes are progressive and economically efficient because they price externalities while returning revenue to offset distributional impacts, supporting carbon pricing as climate policy."

**Variables.**

- **X** = Revenue-neutral carbon tax (Intervention)
- **Y** = Distributional impact and GDP (Outcome)
- **Z1** = Indirect carbon costs (embedded in goods) (Omitted Cost)
- **Z2** = Regional and sectoral employment effects (Omitted Cost)
- **Z3** = Model assumptions and parameters (Uncertainty)

**Annotations.**

- **Case ID:** 5.247
- **Pearl Level:** L2 (Intervention)
- **Domain:** D5 (Economics)
- **Trap Type:** CONF-MED
- **Trap Subtype:** Model_Evidence_Conflation
- **Difficulty:** Hard
- **Causal Structure:** Z → Y

**Gold Rationale.**

This case presents model outputs as empirical findings with incomplete incidence analysis. The progressivity claim compares direct energy costs to dividends but ignores indirect carbon costs embedded throughout the economy - low-income households spend larger budget shares on carbon-intensive goods. The 'minimal GDP impact' comes from economic modeling assuming frictionless adjustment, but actual transitions involve unemployment, stranded assets, and regional disruption. Job losses in carbon-intensive sectors may disproportionately affect low-income workers. The policy conclusion ('supporting carbon pricing as climate policy') also requires that the policy effectively reduce emissions, which the distributional analysis doesn't address.

**Wise Refusal.**

"Does the progressivity analysis account for behavioral responses - will carbon-intensive industries relocate, affecting employment in ways that hurt lower-income workers?"

---

## **Case 5.248: Lottery provides visa exogeneity but not entrepreneurship selection exogeneity**

**Scenario.**

Researchers tracked 50,000 immigrants over 20 years, finding that those who started businesses created an average of 4.2 jobs each and had businesses with 35% higher survival rates than native-born entrepreneurs. The study used visa lottery quasi-experimental variation to establish causation. Foreign-born founders represented 25% of new businesses despite being 13% of the population.

**Claim.**

"Immigration increases entrepreneurship and job creation because immigrants bring skills and perspectives that identify market opportunities, supporting immigration policies that attract entrepreneurial talent."

**Variables.**

- **X** = Immigration (visa lottery) (Intervention)
- **Y** = Entrepreneurship and job creation (Outcome)
- **Z1** = Selection into entrepreneurship among lottery winners (Selection Mechanism)
- **Z2** = Labor market barriers (discrimination, credential non-recognition) (Alternative Mechanism)
- **Z3** = Survival bias from visa-tied businesses (Measurement Issue)

**Annotations.**

- **Case ID:** 5.248
- **Pearl Level:** L2 (Intervention)
- **Domain:** D5 (Economics)
- **Trap Type:** SELECTION
- **Trap Subtype:** Within_Treatment_Selection
- **Difficulty:** Hard
- **Causal Structure:** X → Z; Z → Y

**Hidden Timestamp.**

Were immigrants risk-tolerant and entrepreneurial before immigrating?

**Answer if t(Z) < t(X) (Confounder Scenario).**

Risk-tolerant individuals self-select into immigration and entrepreneurship.

**Answer if t(X) < t(Z) (Causal Scenario).**

Immigrant status enables or incentivizes entrepreneurship.

**Gold Rationale.**

This case exhibits selection bias within the quasi-experimental design. The visa lottery creates exogenous variation in immigration status, but the decision to start a business after winning the lottery is endogenous. Immigrants may face labor market discrimination or credential non-recognition that pushes them toward self-employment as necessity entrepreneurship rather than opportunity identification. The 35% higher survival rate may reflect visa constraints that prevent exit from failing businesses. The claim that 'immigrants bring skills and perspectives that identify market opportunities' is an asserted mechanism not tested by the research design, which cannot distinguish opportunity entrepreneurship from constraint-driven self-employment.

**Wise Refusal.**

"Does immigrant entrepreneurship reflect genuine opportunity identification, or are immigrants pushed toward self-employment because traditional employment paths are blocked by credential non-recognition?"

---

## **Case 5.249: Financial success enables ESG investment rather than ESG causing success**

**Scenario.**

A study compared returns of ESG-screened portfolios to conventional portfolios over 15 years. ESG portfolios outperformed by 0.8% annually with lower volatility. The analysis matched portfolios on sector, size, and factor exposures. Companies with high ESG scores also had fewer regulatory penalties and lower cost of capital.

**Claim.**

"ESG investing delivers competitive returns while supporting corporate responsibility, suggesting investors need not sacrifice financial performance to align investments with values."

**Variables.**

- **X** = ESG screening/scores (Intervention)
- **Y** = Portfolio returns and volatility (Outcome)
- **Z1** = Financial health enabling ESG investment (Reverse Causation)
- **Z2** = ESG fund flows driving prices (Alternative Mechanism)
- **Z3** = Time-period-specific factors (Temporal Confounder)

**Annotations.**

- **Case ID:** 5.249
- **Pearl Level:** L2 (Intervention)
- **Domain:** D5 (Economics)
- **Trap Type:** REVERSE
- **Trap Subtype:** Success_Enables_ESG
- **Difficulty:** Medium
- **Causal Structure:** Y → X; Z1 → Y

**Hidden Timestamp.**

Were firms financially healthy before adopting ESG practices?

**Answer if t(Z) < t(X) (Confounder Scenario).**

Financially healthy firms adopt ESG; financial health drives returns.

**Answer if t(X) < t(Z) (Causal Scenario).**

ESG practices increase firm value independent of selection.

**Gold Rationale.**

This case exhibits reverse causality and time-period dependence. Matching on sector, size, and factor exposures does not address that ESG scores may be consequences of financial health rather than causes - profitable companies have resources to invest in ESG initiatives. The 15-year outperformance could reflect a one-time revaluation as ESG investing became popular (not repeatable), ESG scores proxying for quality/profitability factors, or lower cost of capital being priced in during the sample period (implying lower future returns). The study cannot distinguish 'ESG causes good returns' from 'ESG scores identify already-successful companies.'

**Wise Refusal.**

"Were firms with strong ESG ratings already financially healthy before adopting ESG practices? If profitable firms have resources to invest in sustainability, causation may run from performance to ESG rather than reverse."

---

## **Case 5.250: Local effect at discontinuity extrapolated to universal policy**

**Scenario.**

Researchers used variation from administrative rules that create classroom size discontinuities (e.g., classrooms split when enrollment exceeds 25) to estimate causal effects. Students in smaller classes scored 0.15 standard deviations higher on standardized tests. Effects were strongest for disadvantaged students and persisted through middle school.

**Claim.**

"Smaller class sizes improve student achievement because teachers can provide more individualized attention, supporting policies that reduce class sizes as an education reform strategy."

**Variables.**

- **X** = Class size (at discontinuity) (Intervention)
- **Y** = Student test scores (Outcome)
- **Z1** = Teacher quality at scale (General Equilibrium)
- **Z2** = Better teachers hired at schools with smaller classes (Confounder)

**Annotations.**

- **Case ID:** 5.250
- **Pearl Level:** L2 (Intervention)
- **Domain:** D5 (Economics)
- **Trap Type:** CONF-MED
- **Trap Subtype:** LATE_To_ATE_Extrapolation
- **Difficulty:** Hard
- **Causal Structure:** X → Z2; Z2 → Y; Z1 → Y

**Hidden Timestamp.**

Did better teachers concentrate in small classes before randomization?

**Answer if t(Z) < t(X) (Confounder Scenario).**

Teacher quality sorting drives scores, not class size itself.

**Answer if t(X) < t(Z) (Causal Scenario).**

Smaller class size directly improves learning.

**Gold Rationale.**

This case extrapolates a local average treatment effect to justify universal policy. Better teachers may cluster a elite schools that can afford smaller class sizes. Universal class size reduction would require hiring many more teachers, possibly affecting the overall quality distribution of teachers. The 0.15 SD effect may not scale when general equilibrium effects are considered.

**Wise Refusal.**

"Would hiring enough teachers to reduce all class sizes replicate the effect found at the RD threshold, or would teacher quality dilution offset the benefits at scale?"

---

## **Case 5.251: Acute effects from daily variation extrapolated to chronic policy effects**

**Scenario.**

Economists used wind patterns as an instrument for air pollution exposure, finding that workers experienced 5% productivity declines on high-pollution days. Cognitive test scores were 0.2 standard deviations lower when measured on days with elevated particulate matter. The instrument ensured pollution variation was exogenous to worker characteristics.

**Claim.**

"Air pollution impairs cognitive function and reduces productivity, creating economic costs that justify stricter environmental regulations on efficiency grounds beyond health considerations."

**Variables.**

- **X** = Air pollution (wind-instrumented) (Intervention)
- **Y** = Productivity and cognitive test scores (Outcome)
- **Z1** = Chronic vs acute exposure effects (Extrapolation Issue)
- **Z2** = Weather-related productivity factors (Potential Confounder)
- **Z3** = Behavioral adaptation (Response Mechanism)

**Annotations.**

- **Case ID:** 5.251
- **Pearl Level:** L2 (Intervention)
- **Domain:** D5 (Economics)
- **Trap Type:** CONF-MED
- **Trap Subtype:** Acute_Chronic_Extrapolation
- **Difficulty:** Hard
- **Causal Structure:** Z → X; X → Y

**Hidden Timestamp.**

Did chronic pollution exposure differ from acute spikes measured by the IV?

**Answer if t(Z) < t(X) (Confounder Scenario).**

Chronic pollution determines cognition; acute spikes less relevant.

**Answer if t(X) < t(Z) (Causal Scenario).**

Acute pollution spikes impair cognition as estimated.

**Gold Rationale.**

This case extrapolates acute effects to justify chronic exposure policy. Wind pattern instruments create day-to-day variation in pollution, identifying transitory cognitive impacts. But environmental regulations address long-term average pollution levels, which may have different effects than acute daily exposure. The 5% productivity decline may represent timing shifts rather than permanent output losses if workers catch up on clean days. The policy claim requires knowing the dose-response function at policy-relevant margins - whether we're on a steep or flat part of the curve - which daily variation cannot identify. The efficiency justification requires extrapolating from identified acute effects to unidentified policy-relevant chronic effects.

**Wise Refusal.**

"Do acute cognitive effects from daily pollution spikes translate to chronic impacts from long-term exposure at lower average levels? Policy-relevant exposures differ from the instrument-driven variation."

---

## **Case 5.252: Counterfactual derived from model treated as ground truth**

**Scenario.**

During a recession, the government implemented a fiscal stimulus package of $800 billion. GDP declined 4% that year compared to model predictions of an 8% decline without stimulus. Economists estimated a fiscal multiplier of 1.5, suggesting each dollar of spending generated $1.50 in economic activity.

**Claim.**

"The fiscal stimulus prevented a deeper recession because government spending supported demand when private spending contracted; without intervention, the recession would have been twice as severe."

**Variables.**

- **X** = Fiscal stimulus (Intervention)
- **Y** = GDP decline (Outcome)
- **Y0** = Counterfactual outcome for GDP decline (Counterfactual Outcome)
- **Z1** = Model assumptions and specification (Uncertainty)
- **Z2** = Concurrent monetary policy (Confounder)
- **Z3** = Endogenous stimulus timing (Reverse Causation)

**Annotations.**

- **Case ID:** 5.252
- **Pearl Level:** L3 (Counterfactual)
- **Domain:** D5 (Economics)
- **Trap Type:** COUNTERFACTUAL
- **Trap Subtype:** Model_Dependent_Counterfactual
- **Difficulty:** Medium
- **Causal Structure:** Z1 → X; Z1 → Y; X → Y

**The Counterfactual Query.**

How many jobs would exist without the fiscal stimulus?

**The Counterfactual Structure.**

Comparing actual employment vs model-predicted counterfactual without stimulus.

**Ground Truth.**

**Answer:** CONDITIONAL

Fiscal multiplier estimates, while model-dependent, provide reasonable counterfactual. Claim validity depends on model assumptions but is theoretically grounded.

**Gold Rationale.**

This case treats a model-dependent counterfactual as ground truth. The claim compares the actual 4% decline to a model prediction of 8% and attributes the entire difference to fiscal stimulus. But the 8% prediction depends on model assumptions that cannot be validated against the unobservable counterfactual world. Stimulus timing is endogenous - implemented because conditions were severe - creating confounding. The fiscal multiplier of 1.5 is an uncertain estimate, not a precise causal effect. Concurrent monetary policy, automatic stabilizers, and international factors also changed during the recession. The claim treats model uncertainty as precise causal knowledge.

**Wise Refusal.**

"What macroeconomic model generates the 8% counterfactual decline, and how sensitive is that estimate to model assumptions about multipliers, expectations, and monetary policy responses?"

---

## **Case 5.253: Multiple concurrent changes make counterfactual isolation implausible**

**Scenario.**

After a major trade agreement reduced tariffs by 25%, bilateral trade volume increased 40% over five years. Employment in export sectors grew 12%, while import-competing sectors lost 8% of jobs. Economists estimated net GDP gains of 0.5% annually from the agreement.

**Claim.**

"The trade agreement boosted economic growth because it allowed countries to specialize according to comparative advantage; without the agreement, both countries would have lower GDP."

**Variables.**

- **X** = Trade agreement / tariff reduction (Intervention)
- **Y** = Trade volume and GDP (Outcome)
- **Y0** = Counterfactual outcome for Trade volume and GDP (Counterfactual Outcome)
- **Z1** = Secular trade growth trends (Confounder)
- **Z2** = Selection into agreement (Reverse Causation)
- **Z3** = Time-varying confounders over 5 years (Confounder)

**Annotations.**

- **Case ID:** 5.253
- **Pearl Level:** L3 (Counterfactual)
- **Domain:** D5 (Economics)
- **Trap Type:** COUNTERFACTUAL
- **Trap Subtype:** Confounded_Counterfactual
- **Difficulty:** Hard
- **Causal Structure:** Z1 → X; Z1 → Y; X → Y

**The Counterfactual Query.**

What would bilateral trade volume be without the trade agreement?

**The Counterfactual Structure.**

Comparing observed trade increase vs predicted baseline without agreement.

**Ground Truth.**

**Answer:** CONDITIONAL

Trade agreement effects can be isolated using gravity model controls. While confounded by global trends, the core causal mechanism is well-established.

**Gold Rationale.**

This case constructs a confounded counterfactual. The claim requires knowing what trade patterns would have emerged absent the agreement over a five-year period with numerous confounding changes. Global trade was generally increasing; some bilateral growth might have occurred anyway. Countries sign trade agreements when they expect gains, creating endogeneity. Technology changes, currency movements, and other policies also affected trade over five years. The 0.5% GDP estimate is model-dependent and assumes counterfactual isolation that is implausible over this time horizon.

**Wise Refusal.**

"What trade patterns would have emerged absent the agreement, given concurrent technological changes, third-country competition, and shifting comparative advantages over the five-year period?"

---

## **Case 5.254: Within-sample evidence contradicts the counterfactual claim**

**Scenario.**

During a period of low inflation, the central bank kept interest rates near zero for five years. Inflation remained below target (2%) at 1.2% throughout. When rates were eventually raised, inflation temporarily rose to 2.5% before settling at the 2% target.

**Claim.**

"The low interest rate policy successfully anchored inflation expectations near target; if rates had been raised earlier, deflation risk would have increased and economic recovery would have been slower."

**Variables.**

- **X** = Interest rate policy (Intervention)
- **Y** = Inflation rate (Outcome)
- **Y0** = Counterfactual outcome for Inflation rate (Counterfactual Outcome)
- **Z1** = Global disinflationary forces (Confounder)
- **Z2** = Inflation-rate simultaneity (Reverse Causation)
- **Z3** = Evidence from eventual rate hike (Contradicting Evidence)

**Annotations.**

- **Case ID:** 5.254
- **Pearl Level:** L3 (Counterfactual)
- **Domain:** D5 (Economics)
- **Trap Type:** COUNTERFACTUAL
- **Trap Subtype:** Evidence_Contradicted_Counterfactual
- **Difficulty:** Easy
- **Causal Structure:** Z1 → X; Z1 → Y; X → Y

**The Counterfactual Query.**

What would inflation have been without low interest rates?

**The Counterfactual Structure.**

Comparing observed low inflation vs hypothetical scenario with higher rates.

**Ground Truth.**

**Answer:** CONDITIONAL

Whether low interest rates successfully anchored inflation expectations depends on several unobservable factors: central bank credibility, global disinflationary pressures, and the counterfactual of what expectations would have been under different policy. The claim conflates correlation (low rates + low inflation) with causation through the expectations channel. The answer is CONDITIONAL on establishing that expectations were actually anchored BY the policy rather than by other factors.

**Gold Rationale.**

This case constructs a counterfactual contradicted by within-sample evidence. The claim that earlier rate hikes would have caused deflation is directly contradicted by observed evidence: when rates were eventually raised, inflation actually increased to 2.5%. The claim also conflates 'anchoring expectations near target' with persistent inflation of 1.2% - a 0.8 percentage point miss is not obviously a success. The policy may have been a response to low inflation rather than a cause of inflation stability. Global disinflationary forces provide an alternative explanation. The counterfactual is constructed to be unfalsifiable.

**Wise Refusal.**

"Did inflation expectations remain anchored because of the policy, or did underlying factors (weak demand, credibility from past success) keep expectations low regardless of announced policy?"

---

## **Case 5.255: Regions receiving investment differ systematically from comparison regions**

**Scenario.**

A region invested $5 billion in transportation infrastructure over a decade. Commute times fell 15%, and property values within 5 miles of new transit increased 25%. Regional employment grew 8% faster than comparable regions without similar investments.

**Claim.**

"Infrastructure investment generates positive economic returns through improved connectivity and productivity; without this investment, the region would have experienced slower growth and declining competitiveness."

**Variables.**

- **X** = Transportation infrastructure investment (Intervention)
- **Y** = Employment growth and property values (Outcome)
- **Y0** = Counterfactual outcome for Employment growth and property values (Counterfactual Outcome)
- **Z1** = Non-random investment allocation (Selection Mechanism)
- **Z2** = Pre-existing growth trends (Confounder)
- **Z3** = Displacement from other regions (Alternative Mechanism)

**Annotations.**

- **Case ID:** 5.255
- **Pearl Level:** L3 (Counterfactual)
- **Domain:** D5 (Economics)
- **Trap Type:** COUNTERFACTUAL
- **Trap Subtype:** Endogenous_Treatment_Counterfactual
- **Difficulty:** Medium
- **Causal Structure:** Z1 → X; Z1 → Y; X → Y

**The Counterfactual Query.**

What would regional development look like without infrastructure investment?

**The Counterfactual Structure.**

Comparing treatment region vs comparison regions that did not invest.

**Ground Truth.**

**Answer:** CONDITIONAL

Infrastructure investment is endogenous to regional growth potential; comparison regions may differ in unobserved ways.

**Gold Rationale.**

This case constructs an endogenous treatment counterfactual. Regions that receive $5 billion investments differ systematically from comparison regions - they have more political influence, anticipated growth potential, or existing economic momentum. The 8% faster employment growth may reflect businesses relocating from other regions (displacement), not net job creation. Property value increases near transit may come at the expense of values farther away - a transfer, not a gain. The appropriate counterfactual isn't 'no investment' but 'alternative use of $5 billion,' which isn't considered.

**Wise Refusal.**

"Were regions receiving infrastructure investment already on different growth trajectories before the spending, making the comparison group an invalid counterfactual?"

---

## **Case 5.256: Comparing across recessions cannot isolate single policy effect**

**Scenario.**

During an economic downturn, the government extended unemployment benefits from 26 to 99 weeks. Unemployment duration increased by 2 weeks on average, but consumer spending among unemployed workers remained 30% higher than in previous recessions with shorter benefit periods.

**Claim.**

"Extended unemployment benefits stabilized demand during the recession because they maintained household spending while workers searched for suitable jobs; without extension, consumer spending would have collapsed and deepened the recession."

**Variables.**

- **X** = Extended unemployment benefits (Intervention)
- **Y** = Consumer spending and recession depth (Outcome)
- **Y0** = Counterfactual outcome for Consumer spending and recession depth (Counterfactual Outcome)
- **Z1** = Recession characteristics differences (Confounder)
- **Z2** = Composition of unemployed workers (Confounder)
- **Z3** = Concurrent stimulus policies (Confounder)

**Annotations.**

- **Case ID:** 5.256
- **Pearl Level:** L3 (Counterfactual)
- **Domain:** D5 (Economics)
- **Trap Type:** COUNTERFACTUAL
- **Trap Subtype:** Cross_Episode_Counterfactual
- **Difficulty:** Hard
- **Causal Structure:** Z1 → X; Z1 → Y; X → Y

**The Counterfactual Query.**

Would employment have recovered faster without extended unemployment benefits?

**The Counterfactual Structure.**

Comparing observed recovery vs hypothetical with shorter benefits.

**Ground Truth.**

**Answer:** VALID

Extended unemployment benefits stabilizing demand during recessions is supported by strong empirical evidence. The marginal propensity to consume among unemployed households is high (~0.7-0.9), meaning benefits translate directly into spending. Studies of the 2008-2009 recession found significant positive multiplier effects from UI extensions. While the precise magnitude depends on economic conditions, the causal mechanism (income support → consumption → demand stabilization) is well-established.

**Gold Rationale.**

This case constructs a cross-episode counterfactual that cannot isolate policy effects. Comparing spending in this recession to 'previous recessions' cannot attribute the 30% difference to UI extension because recessions differ in causes, severity, concurrent policies, and composition of unemployed workers. Workers unemployed in different recessions have different savings, demographics, and spending propensities. Other stimulus measures and monetary policy also differed across recessions. The 2-week increase in unemployment duration suggests behavioral response - some spending was transferred across time through delayed job-finding, not created. The counterfactual 'spending collapse' is assertion without evidence.

**Wise Refusal.**

"How comparable are the two recessions in terms of sectoral composition, credit conditions, and global factors? Differences in context may explain outcome differences better than policy differences."

---

## **Case 5.257: Only successful mergers survive to be measured**

**Scenario.**

A study of 500 mergers found that combined companies had 15% higher profit margins five years post-merger than pre-merger averages. The analysis controlled for industry trends and economic conditions.

**Claim.**

"Mergers create value through operational synergies and economies of scale, supporting permissive merger policy."

**Variables.**

- **X** = Merger completion (Intervention)
- **Y** = Profit margins (Outcome)
- **Z1** = Failed/abandoned mergers (Excluded Population)
- **Z2** = Pre-merger firm quality (Confounder)
- **Z3** = Counterfactual margins (Unobserved)

**Annotations.**

- **Case ID:** 5.257
- **Pearl Level:** L2 (Intervention)
- **Domain:** D5 (Economics)
- **Trap Type:** SELECTION
- **Trap Subtype:** Successful_Merger_Survivorship
- **Difficulty:** Medium
- **Causal Structure:** Z → X; Z → Y

**Hidden Timestamp.**

Were completed mergers selected based on anticipated efficiency gains?

**Answer if t(Z) < t(X) (Confounder Scenario).**

Selection into successful mergers; efficiency gains would occur anyway.

**Answer if t(X) < t(Z) (Causal Scenario).**

Mergers cause efficiency improvements in completed deals.

**Gold Rationale.**

This case exhibits survivorship bias. The 15% higher margins could reflect that only successful mergers survived to be measured at 5 years, or that profitable firms were more likely to pursue mergers initially. Without a counterfactual showing what these firms' margins would have been without merging, we cannot attribute the gains to merger synergies versus pre-existing firm quality. Failed or abandoned mergers are excluded from the analysis. The policy conclusion ('supporting permissive merger policy') assumes all mergers create value when the evidence only shows that surviving mergers had higher margins.

**Wise Refusal.**

"What happened to the mergers that failed or were abandoned - are they excluded from the analysis? If only successful integrations are observed, the 15% margin advantage reflects survivorship bias."

---

## **Case 5.258: Cities adopt policy because of pre-existing supply constraints**

**Scenario.**

Researchers found that cities that adopted inclusionary zoning (requiring affordable units in new developments) produced 20% fewer new housing units than comparable cities without such requirements over a decade.

**Claim.**

"Inclusionary zoning reduces overall housing supply because it decreases development profitability, potentially worsening affordability despite good intentions."

**Variables.**

- **X** = Inclusionary zoning adoption (Intervention)
- **Y** = Low house construction (Outcome)
- **Z1** = Pre-existing housing market tightness (Confounder)
- **Z2** = Political conditions enabling policy (Confounder)
- **Z3** = Other supply constraints (land, regulation) (Confounder)

**Annotations.**

- **Case ID:** 5.258
- **Pearl Level:** L2 (Intervention)
- **Domain:** D5 (Economics)
- **Trap Type:** REVERSE
- **Trap Subtype:** Policy_Response_To_Scarcity
- **Difficulty:** Hard
- **Causal Structure:** Y → X; Z1 → Y

**Hidden Timestamp.**

Did housing market tightness exist before zoning was adopted?

**Answer if t(Z) < t(X) (Confounder Scenario).**

Pre-existing market tightness caused both zoning and limited supply.

**Answer if t(X) < t(Z) (Causal Scenario).**

Zoning requirement directly reduces housing supply.

**Gold Rationale.**

This case exhibits policy endogeneity. Cities that adopt inclusionary zoning may already have tight housing markets and pre-existing supply constraints - the policy is adopted in response to scarcity, not as a cause of it. The 20% fewer units could reflect underlying conditions that both prompted the policy and constrain supply. 'Comparable cities' may differ in unmeasured ways (land availability, political conditions, growth pressure) that affect both policy adoption and housing production. The mechanism (reduced development profitability) is asserted without testing whether it explains the supply difference versus pre-existing conditions.

**Wise Refusal.**

"Did cities adopt inclusionary zoning because they already had tight housing markets and high demand, making the policy response to rather than cause of supply constraints?"

---

## **Case 5.259: Subjective wellbeing return to baseline conflated with no welfare effect**

**Scenario.**

A study tracked 100,000 lottery winners over 10 years. Winners of large jackpots ($1M+) had 40% lower employment rates and 25% higher divorce rates than small prize winners. Large winners reported similar life satisfaction after 5 years as before winning.

**Claim.**

"Windfall wealth has limited effects on long-term wellbeing because people adapt to new circumstances, suggesting that income-based policies may have smaller welfare effects than expected."

**Variables.**

- **X** = Large lottery win (Intervention)
- **Y** = Life satisfaction and life outcomes (Outcome)
- **Z1** = Employment changes (40% reduction) (Behavioral Effect)
- **Z2** = Family disruption (25% more divorce) (Behavioral Effect)
- **Z3** = Hedonic adaptation measurement (Measurement Issue)

**Annotations.**

- **Case ID:** 5.259
- **Pearl Level:** L2 (Intervention)
- **Domain:** D5 (Economics)
- **Trap Type:** CONF-MED
- **Trap Subtype:** Outcome_Measure_Conflation
- **Difficulty:** Medium
- **Causal Structure:** Z → Y

**Gold Rationale.**

This case conflates subjective wellbeing measures with total welfare effects. The 40% employment reduction and 25% higher divorce rates indicate substantial life disruption regardless of self-reported satisfaction returning to baseline. Hedonic adaptation (returning to baseline satisfaction) does not mean 'limited effects' - objective life circumstances changed dramatically. Self-reported satisfaction after major life changes may be unreliable due to reference point shifts. The policy conclusion about 'smaller welfare effects than expected' ignores that employment loss and family disruption are themselves welfare-relevant even if people report adapting.

**Wise Refusal.**

"Does subjective wellbeing adaptation mask real changes in consumption, leisure, and life satisfaction dimensions not captured by standard happiness surveys?"

---

## **Case 5.260: Modest effect size extrapolated to justify intervention policy**

**Scenario.**

A natural experiment from random assignment of students to college roommates found that students paired with high-achieving roommates had GPAs 0.1 points higher than those with lower-achieving roommates. Effects persisted through graduation.

**Claim.**

"Peer effects meaningfully influence academic outcomes because students learn from and are motivated by successful peers, supporting policies that mix students by achievement."

**Variables.**

- **X** = High-achieving roommate (Intervention)
- **Y** = GPA (Outcome)
- **Z1** = Effect size (0.1 GPA points) (Magnitude Issue)
- **Z2** = Mechanism uncertainty (Mechanism Issue)
- **Z3** = Policy design implications (Extrapolation Issue)

**Annotations.**

- **Case ID:** 5.260
- **Pearl Level:** L2 (Intervention)
- **Domain:** D5 (Economics)
- **Trap Type:** CONF-MED
- **Trap Subtype:** Small_Effect_Policy_Extrapolation
- **Difficulty:** Medium

**Gold Rationale.**

This case extrapolates a small effect to justify policy intervention. A 0.1 GPA point gain (roughly 3% of the scale) is modest and may not justify the claim that peer effects 'meaningfully influence' outcomes. The mechanism is unclear - is it learning spillover, increased motivation, shared study habits, or spurious correlation? Random roommate assignment differs fundamentally from policy-designed achievement mixing, which would trigger strategic responses (parents, schools, students) not present in the natural experiment. The policy conclusion ('supporting policies that mix students') assumes the effect would scale and persist under deliberate intervention, which is untested.

**Wise Refusal.**

"Is a 0.1 GPA point gain economically meaningful enough to justify peer-composition policies, given the costs and disruption of implementation?"

---

## **Case 5.261: Absence of evidence in one measure conflated with evidence of no effect**

**Scenario.**

A study of corporate board diversity found that companies increasing female board representation from <10% to >30% experienced no significant change in stock returns or operating performance over five years compared to companies without such changes.

**Claim.**

"Board gender diversity does not affect firm performance, suggesting diversity mandates should be justified on non-financial grounds rather than business case arguments."

**Variables.**

- **X** = Board gender diversity increase (Intervention)
- **Y** = Stock returns and operating performance (Outcome)
- **Z1** = Non-financial effects (risk, compliance, ESG) (Unmeasured Outcome)
- **Z2** = Time horizon (5 years) (Temporal Limitation)
- **Z3** = Selection into diversity changes (Confounder)

**Annotations.**

- **Case ID:** 5.261
- **Pearl Level:** L2 (Intervention)
- **Domain:** D5 (Economics)
- **Trap Type:** CONF-MED
- **Trap Subtype:** Null_Result_Interpretation
- **Difficulty:** Hard
- **Causal Structure:** Z → X; Z → Y

**Hidden Timestamp.**

Did firm culture and performance precede board diversity changes?

**Answer if t(Z) < t(X) (Confounder Scenario).**

Diversity improves culture but non-financial outcomes only.

**Answer if t(X) < t(Z) (Causal Scenario).**

Diverse boards make better decisions improving financials.

**Gold Rationale.**

This case conflates null results on specific metrics with absence of any effect. No significant change in stock returns or operating performance over five years doesn't establish that 'board diversity does not affect firm performance.' Diversity may affect non-financial outcomes (risk management, compliance, ESG performance, stakeholder relations) not captured by these narrow metrics. Five years may be too short for governance changes to manifest in financial performance. Companies increasing diversity may do so during confounding events (leadership transitions, market conditions) that obscure effects. The claim 'does not affect' overstates what null findings can establish.

**Wise Refusal.**

"Does the absence of short-term stock price effects rule out longer-term benefits through culture change, stakeholder relations, or governance quality improvements?"

---

## **Case 5.262: Small-scale trial results extrapolated to economy-wide policy**

**Scenario.**

A randomized trial provided unconditional cash transfers of $1,000/month to low-income households for three years. Recipients worked 5% fewer hours but reported 20% higher life satisfaction and their children had 6% better educational outcomes.

**Claim.**

"Universal basic income improves welfare despite modest work disincentives because it enables people to invest in family, health, and education, supporting cash transfer programs."

**Variables.**

- **X** = Cash transfer ($1000/month) (Intervention)
- **Y** = Work hours, life satisfaction, child outcomes (Outcome)
- **Z1** = General equilibrium effects at scale (Extrapolation Issue)
- **Z2** = Temporary vs permanent program effects (Temporal Issue)
- **Z3** = Tax burden and inflation effects (Omitted Mechanism)

**Annotations.**

- **Case ID:** 5.262
- **Pearl Level:** L2 (Intervention)
- **Domain:** D5 (Economics)
- **Trap Type:** CONF-MED
- **Trap Subtype:** Partial_To_General_Equilibrium
- **Difficulty:** Medium
- **Causal Structure:** Z → Y

**Gold Rationale.**

This case extrapolates partial equilibrium trial results to justify general equilibrium policy. The 5% work reduction and improved outcomes were observed in a temporary, localized pilot where recipients knew transfers would end. In a permanent, universal implementation, the 5% work reduction could cascade through the economy (lower tax base to fund transfers, labor shortages in some sectors, inflationary pressure from increased demand without increased production). The claim jumps from 'cash transfers improve welfare in a trial' to 'universal basic income improves welfare' without addressing how results would change when everyone receives transfers funded by taxation. General equilibrium effects could erode or reverse trial benefits.

**Wise Refusal.**

"Would the work disincentive effects remain modest if UBI replaced all existing benefits and was funded by substantial tax increases on labor income?"

---

## **Case 5.263: External demand conditions confound devaluation effects**

**Scenario.**

After a currency devaluation of 20%, exports increased 15% over two years while imports fell 10%. The trade balance improved by $5 billion. Tourist arrivals increased 25%.

**Claim.**

"Currency devaluation improves trade balance by making exports cheaper and imports more expensive, supporting exchange rate flexibility as a policy tool."

**Variables.**

- **X** = Currency devaluation (Intervention)
- **Y** = Trade balance improvement (Outcome)
- **Z1** = Global demand conditions (Confounder)
- **Z2** = Competitor weakness (Confounder)
- **Z3** = Import compression vs competitiveness (Mechanism Issue)

**Annotations.**

- **Case ID:** 5.263
- **Pearl Level:** L2 (Intervention)
- **Domain:** D5 (Economics)
- **Trap Type:** CONF-MED
- **Trap Subtype:** Concurrent_Demand_Confounding
- **Difficulty:** Hard
- **Causal Structure:** Z → X; Z → Y

**Hidden Timestamp.**

Did global demand conditions change before or after devaluation?

**Answer if t(Z) < t(X) (Confounder Scenario).**

Global demand drives both exchange rates and exports.

**Answer if t(X) < t(Z) (Causal Scenario).**

Currency depreciation increases export competitiveness.

**Gold Rationale.**

This case confounds devaluation effects with concurrent conditions. The 15% export increase may reflect global demand conditions, competitor weakness, or other factors rather than devaluation alone. The $5B trade balance improvement could reflect import compression from income effects (people buy less because they're poorer in foreign currency terms) rather than genuine competitiveness gains. Without a counterfactual or control group, we cannot isolate devaluation effects from external factors affecting trade flows.

**Wise Refusal.**

"Were the export gains driven by devaluation itself, or by concurrent factors like global demand changes, commodity price shifts, or trade policy changes that coincided with the currency adjustment?"

---

## **Case 5.264: Observed effects don't establish that leverage levels are unsustainable**

**Scenario.**

After interest rate cuts from 5% to 1%, housing prices rose 40% over three years. Mortgage originations doubled. Household debt-to-income ratios increased from 100% to 140%.

**Claim.**

"Low interest rates inflate asset prices and encourage excessive leverage because they reduce borrowing costs, creating financial stability risks that should temper monetary policy decisions."

**Variables.**

- **X** = Interest rate cuts (Intervention)
- **Y** = Asset prices and leverage (Outcome)
- **Z1** = Sustainability of leverage levels (Unmeasured)
- **Z2** = Benefits of low rates (employment, growth) (Omitted Benefit)
- **Z3** = Financial stability threshold (Undefined)

**Annotations.**

- **Case ID:** 5.264
- **Pearl Level:** L2 (Intervention)
- **Domain:** D5 (Economics)
- **Trap Type:** COLLIDER
- **Trap Subtype:** Effect_To_Risk_Extrapolation
- **Difficulty:** Hard
- **Causal Structure:** X → Z; Z → Y

**Hidden Timestamp.**

Was interest cover sustainable before and after cuts, as measured by factors suc has default rates?

**Answer if t(Z) < t(X) (Confounder Scenario).**

Default rates rise after the cuts, leverage may be excessive.

**Answer if t(X) < t(Z) (Causal Scenario).**

Default rates do not rise after the cuts, leverage may be sustainable.

**Gold Rationale.**

This case conflates observed effects with demonstrated harm. While rate cuts demonstrably increase asset prices and leverage, the claim that this creates 'financial stability risks' requiring policy tempering is not established by the data. The 140% debt-to-income ratio is presented as concerning without evidence that this level is unsustainable. The policy recommendation ('should temper') ignores the benefits of low rates (supporting employment and growth) that must be weighed against stability concerns. Higher leverage with lower rates may actually reduce debt service burdens.

**Wise Refusal.**

"Does the correlation between low rates and asset prices demonstrate harmful bubble formation, correlating with increased default rates, or could some price appreciation reflect rational response to lower discount rates and improved growth prospects?"

---

## **Case 5.265: Propensity score matching cannot address unobserved firm quality differences**

**Scenario.**

Workers at firms offering profit-sharing had 10% higher productivity and 20% lower turnover than comparable workers at firms without such programs. The analysis used propensity score matching.

**Claim.**

"Profit-sharing increases productivity because it aligns worker and firm incentives, supporting policies that encourage employee ownership structures."

**Variables.**

- **X** = Profit-sharing program (Intervention)
- **Y** = Productivity and turnover (Outcome)
- **Z1** = Unobserved firm quality (culture, management) (Confounder)
- **Z2** = Worker selection into profit-sharing firms (Confounder)

**Annotations.**

- **Case ID:** 5.265
- **Pearl Level:** L2 (Intervention)
- **Domain:** D5 (Economics)
- **Trap Type:** SELECTION
- **Trap Subtype:** Unobservable_Matching_Failure
- **Difficulty:** Medium
- **Causal Structure:** Z → X; Z → Y

**Hidden Timestamp.**

Did high-quality firms adopt profit-sharing, or did sharing create quality?

**Answer if t(Z) < t(X) (Confounder Scenario).**

High-quality firms adopt profit-sharing; firm quality drives productivity.

**Answer if t(X) < t(Z) (Causal Scenario).**

Profit-sharing incentivizes worker effort, improving productivity.

**Gold Rationale.**

This case exhibits selection bias on unobservables despite propensity score matching. Matching addresses selection bias only on observable characteristics. Firms adopting profit-sharing likely differ on unobservables (management quality, corporate culture, financial resources) that independently drive productivity. Workers may also self-select into profit-sharing firms based on unobserved characteristics (motivation, risk preferences). The 10% productivity gap may reflect pre-existing firm and worker quality rather than profit-sharing's causal effect.

**Wise Refusal.**

"Did high-quality firms with strong cultures self-select into profit-sharing arrangements? If firms that already had engaged workforces adopted profit-sharing, matching on observables cannot eliminate selection bias."

---

## **Case 5.266: Low-inflation countries adopt independence, not independence causing low inflation**

**Scenario.**

Countries with independent central banks had average inflation rates of 3% compared to 8% for countries with politically controlled monetary policy over a 30-year period.

**Claim.**

"Central bank independence reduces inflation because it insulates monetary policy from political pressures to stimulate the economy before elections."

**Variables.**

- **X** = Central bank independence (Intervention)
- **Y** = Inflation rate (Outcome)
- **Z1** = Institutional quality and capacity (Confounder)
- **Z2** = Political stability (Confounder)
- **Z3** = Economic development level (Confounder)

**Annotations.**

- **Case ID:** 5.266
- **Pearl Level:** L1 (Association)
- **Domain:** D5 (Economics)
- **Trap Type:** REVERSE
- **Trap Subtype:** Institutional_Endogeneity
- **Difficulty:** Hard
- **Causal Structure:** Z → X; Z → Y; Y → X

**Gold Rationale.**

This case exhibits selection bias across countries. Countries choosing to grant central bank independence likely differ systematically from those that don't. Countries with stronger institutions, more political stability, better governance, and higher development levels are both more likely to grant independence AND more likely to have low inflation for reasons independent of monetary policy autonomy. The 5 percentage point inflation difference (3% vs 8%) may reflect these underlying institutional and economic characteristics rather than independence causing lower inflation.

**Wise Refusal.**

"Did countries with low inflation histories subsequently grant central bank independence to lock in their success, rather than independence causing low inflation?"

---

## **Case 5.267: Traffic reduction may reflect displacement rather than elimination**

**Scenario.**

Cities that implemented congestion pricing saw 20% traffic reductions and 30% increases in public transit use. Average commute times fell 10 minutes. Air quality improved 15%.

**Claim.**

"Congestion pricing reduces traffic and improves urban transportation because pricing road use incentivizes alternatives."

**Variables.**

- **X** = Congestion pricing (Intervention)
- **Y** = Traffic volume and commute times (Outcome)
- **Z1** = Trip displacement to other areas (Alternative Mechanism)
- **Z2** = Concurrent transit improvements (Confounder)
- **Z3** = Total vehicle-miles traveled (Unmeasured)

**Annotations.**

- **Case ID:** 5.267
- **Pearl Level:** L2 (Intervention)
- **Domain:** D5 (Economics)
- **Trap Type:** CONF-MED
- **Trap Subtype:** Displacement_vs_Elimination
- **Difficulty:** Hard
- **Causal Structure:** X → Z; Z → Y

**Hidden Timestamp.**

Did trips shift to other times/modes or were they truly eliminated?

**Answer if t(Z) < t(X) (Confounder Scenario).**

Trips shift to off-peak/transit; reduction from displacement not behavior.

**Answer if t(X) < t(Z) (Causal Scenario).**

Price directly reduces peak demand by deterring trips.

**Gold Rationale.**

This case may confound traffic reduction with traffic displacement. The 20% traffic reduction in congestion-priced zones may reflect trips displaced to other times, routes, or destinations rather than eliminated trips. The 30% transit increase is partly a mechanical response to pricing (mode switching) but doesn't prove net traffic reduction. Without data on total vehicle-miles traveled across the region, we cannot determine if congestion pricing genuinely reduced traffic demand or just relocated it. Concurrent transit improvements (often bundled with congestion pricing) may explain mode shifts rather than pricing alone.

**Wise Refusal.**

"Does the 20% traffic reduction represent actual vehicle miles eliminated, or just displacement to alternate routes and times? Without total VMT data, congestion pricing may relocate rather than reduce traffic."

---

## **Case 5.268: Early EHR adopters differ systematically from late adopters**

**Scenario.**

After adoption of electronic health records, hospitals showed 20% reduction in medication errors and 15% shorter average stays. The analysis compared early vs late EHR adopters.

**Claim.**

"Electronic health records improve care quality because they reduce errors and enable better information sharing among providers."

**Variables.**

- **X** = Electronic health record adoption (Intervention)
- **Y** = Medication errors and length of stay (Outcome)
- **Z1** = Hospital quality culture (unobserved) (Confounder)
- **Z2** = Concurrent safety initiatives (Confounder)
- **Z3** = Hawthorne effects during implementation (Confounder)

**Annotations.**

- **Case ID:** 5.268
- **Pearl Level:** L2 (Intervention)
- **Domain:** D5 (Economics)
- **Trap Type:** SELECTION
- **Trap Subtype:** Early_Adopter_Selection
- **Difficulty:** Hard
- **Causal Structure:** Z → X; Z → Y

**Hidden Timestamp.**

Did quality-oriented hospitals adopt EHR first?

**Answer if t(Z) < t(X) (Confounder Scenario).**

Quality-oriented hospitals adopt EHR; hospital culture drives outcomes.

**Answer if t(X) < t(Z) (Causal Scenario).**

EHR systems improve care coordination and reduce errors.

**Gold Rationale.**

This case exhibits early adopter selection bias. Hospitals adopting EHRs early likely differ systematically from late adopters in quality culture, financial resources, management commitment, and existing improvement initiatives. The 20% medication error reduction could reflect Hawthorne effects (heightened attention during implementation), concurrent safety initiatives bundled with EHR adoption, or pre-existing quality improvement cultures that drive both early adoption and good outcomes. Without randomization or within-hospital before-after analysis controlling for trends, we cannot attribute improvements to EHRs versus the characteristics of hospitals that adopt them.

**Wise Refusal.**

"Did hospitals with stronger quality cultures and resources adopt EHRs earlier? If early adopters were already higher-quality institutions, the error reduction reflects hospital capability, not EHR technology effects."

---

## **Case 5.269: Conditioning on approval status creates spurious independence**

**Scenario.**

A study of business loan applicants found that among approved borrowers, those with higher credit scores had similar default rates to those with lower credit scores. The study controlled for loan amount and industry.

**Claim.**

"Credit scores do not predict loan repayment behavior, so lenders should stop using them in underwriting decisions."

**Variables.**

- **X** = Credit score (Intervention)
- **Y** = Loan default (Outcome)
- **Z1** = Other creditworthiness factors (collateral, cash reserves) (Common Cause)
- **Z2** = Loan approval status (collider/selection) (Collider)

**Annotations.**

- **Case ID:** 5.269
- **Pearl Level:** L1 (Association)
- **Domain:** D5 (Economics)
- **Trap Type:** COLLIDER
- **Trap Subtype:** Selection_On_Outcome
- **Difficulty:** Hard
- **Causal Structure:** X → Z2; Z1 → Z2; Z1 → Y

**Gold Rationale.**

This is collider bias from conditioning on approval. The sample only includes approved loans, where low-score borrowers were approved because they had compensating factors (collateral, cash reserves, strong business plans). High-risk low-score applicants were rejected and excluded from the sample. To assess credit score predictive power, one would need data on all applicants including rejected ones.

**Wise Refusal.**

"What is the repayment behavior of rejected applicants with similar credit scores? Without observing denied loans, the sample conditions on approval (a collider), biasing the credit score-outcome relationship."

---

## **Case 5.270: Cross-country comparison assumes invalid counterfactual trajectory**

**Scenario.**

A country implemented universal pre-K education in 2015. By 2025, third-grade reading scores had improved by 12% compared to 2015 baseline. Other countries without universal pre-K saw average improvement of 8% over the same period.

**Claim.**

"Without universal pre-K, the country's reading scores would have improved by only 8%, so the program caused the additional 4 percentage point improvement."

**Variables.**

- **X** = Universal pre-K implementation (Intervention)
- **Y** = Third-grade reading score improvement (Outcome)
- **Y0** = Counterfactual outcome for Third-grade reading score improvement (Counterfactual Outcome)
- **Z1** = Country-specific factors (demographics, concurrent reforms, baseline infrastructure) (Common Cause)

**Annotations.**

- **Case ID:** 5.270
- **Pearl Level:** L3 (Counterfactual)
- **Domain:** D5 (Economics)
- **Trap Type:** COUNTERFACTUAL
- **Trap Subtype:** Parallel_Trends_Violation
- **Difficulty:** Hard
- **Causal Structure:** Z1 → X; Z1 → Y; X → Y

**The Counterfactual Query.**

What would reading scores be without universal pre-K?

**The Counterfactual Structure.**

Comparing treatment country trajectory vs other countries baseline.

**Ground Truth.**

**Answer:** VALID

Universal pre-K improving reading outcomes is supported by extensive quasi-experimental evidence. Studies using regression discontinuity designs around age cutoffs, and difference-in-differences comparing implementing vs non-implementing regions, consistently find positive effects on early literacy. The 15-percentile improvement is within the range found in high-quality programs. While effect sizes vary by program quality and fade-out is possible, the counterfactual that scores would be lower without pre-K is empirically defensible.

**Gold Rationale.**

The claim assumes other countries provide a valid counterfactual, but countries differ in educational infrastructure, demographics, concurrent policy changes, and cultural factors. Without pre-treatment trend data showing parallel trajectories, the comparison is unreliable. The treating country may have been improving faster (or slower) than others even before 2015.

**Wise Refusal.**

"Do comparison countries differ in early childhood education, family structure, or cultural attitudes toward reading that would have produced different trajectories regardless of pre-K policy?"

---

## **Case 5.271: Conditioning on funding status masks true relationship**

**Scenario.**

Analysis of tech startups that received Series A funding found no correlation between founder technical background and company valuation at exit. The sample included 500 funded startups across various sectors.

**Claim.**

"Technical founders don't create more valuable companies than non-technical founders, so venture capitalists should weight founder background less heavily."

**Variables.**

- **X** = Founder technical background (Intervention)
- **Y** = Company valuation at exit (Outcome)
- **Z1** = Other company quality signals (market opportunity, business acumen) (Common Cause)
- **Z2** = Received VC funding/acquisition (collider/selection) (Collider)

**Annotations.**

- **Case ID:** 5.271
- **Pearl Level:** L1 (Association)
- **Domain:** D5 (Economics)
- **Trap Type:** COLLIDER
- **Trap Subtype:** Post_Selection_Analysis
- **Difficulty:** Hard
- **Causal Structure:** X → Z2; Z1 → Z2; Z1 → Y

**Gold Rationale.**

This is collider bias from conditioning on Series A funding. Non-technical founders who received Series A likely demonstrated exceptional business acumen or market opportunity to compensate for lack of technical background. The sample excludes non-technical founders who failed to secure funding, masking any true effect of technical background.

**Wise Refusal.**

"What happens to unfunded startups - do technical founders without VC backing outperform non-technical founders? Conditioning on Series A funding creates collider bias."

---

## **Case 5.272: Cities that adopt bans differ systematically**

**Scenario.**

A city banned single-use plastic bags several years ago. By the end of the observation period, beach litter surveys showed 30% reduction in plastic bag waste. Neighboring cities without bans saw 5% reduction over the same period.

**Claim.**

"If the city hadn't banned plastic bags, beach plastic bag litter would have decreased by only 5%, so the ban directly caused the additional 25 percentage point reduction."

**Variables.**

- **X** = Plastic bag ban (Intervention)
- **Y** = Beach plastic bag litter reduction (Outcome)
- **Y0** = Counterfactual outcome for Beach plastic bag litter reduction (Counterfactual Outcome)
- **Z1** = Environmental consciousness, concurrent sustainability initiatives (Common Cause)

**Annotations.**

- **Case ID:** 5.272
- **Pearl Level:** L3 (Counterfactual)
- **Domain:** D5 (Economics)
- **Trap Type:** COUNTERFACTUAL
- **Trap Subtype:** Endogenous_Policy_Adoption
- **Difficulty:** Hard
- **Causal Structure:** Z1 → X; Z1 → Y; X → Y

**The Counterfactual Query.**

What would beach litter reduction be without the plastic bag ban?

**The Counterfactual Structure.**

Comparing treatment city vs neighboring cities without bans.

**Ground Truth.**

**Answer:** VALID

Plastic bag bans reducing beach litter has direct causal support. The mechanism is straightforward: fewer bags distributed → fewer bags entering waste streams → fewer bags on beaches. Studies comparing beaches before/after bans and across jurisdictions with/without bans find consistent reductions in bag litter. The 40% reduction is consistent with observed effects. While total litter depends on substitution to other materials, the specific claim about plastic bag litter is well-supported.

**Gold Rationale.**

Cities that implement plastic bag bans likely differ systematically from those that do not - they may have stronger environmental movements, more eco-conscious populations, or concurrent sustainability initiatives. The 5% reduction in neighboring cities may not represent what would have happened in this specific city without the ban.

**Wise Refusal.**

"Did the city ban plastic bags because residents were already environmentally conscious and reducing plastic use, making the declining trend independent of the policy?"

---

## **Case 5.273: Tax systems chosen based on correlated factors**

**Scenario.**

Cross-country analysis shows nations with more progressive income tax systems have similar GDP growth rates to nations with flat tax systems. The comparison includes 40 developed economies over a 20-year period.

**Claim.**

"Progressive taxation does not harm economic growth, so countries can raise top marginal tax rates without negative growth consequences."

**Variables.**

- **X** = Progressive income tax structure (Intervention)
- **Y** = GDP growth rate (Outcome)
- **Z1** = Institutional quality, human capital, political stability (Common Cause)

**Annotations.**

- **Case ID:** 5.273
- **Pearl Level:** L2 (Intervention)
- **Domain:** D5 (Economics)
- **Trap Type:** CONF-MED
- **Trap Subtype:** Endogenous_Policy_Choice
- **Difficulty:** Medium
- **Causal Structure:** Z → X; Z → Y

**Gold Rationale.**

Countries choose tax systems based on political, economic, and social factors that also affect growth. Nations with progressive systems may have characteristics (strong institutions, educated workforces, social stability) that support growth despite potentially growth-reducing tax effects. Additionally, observing similar growth at current tax rates does not imply raising rates further would have no effect.

**Wise Refusal.**

"Do countries choose progressive taxation because they already have strong institutions, social cohesion, and growth prospects that independently support economic performance?"

---

## **Case 5.274: Central banks self-select into inflation targeting**

**Scenario.**

After a central bank introduced inflation targeting in 2010, inflation volatility decreased from 4% standard deviation to 1.5% over the following decade. Countries without inflation targeting frameworks saw inflation volatility decrease from 5% to 3% over the same period.

**Claim.**

"Had the central bank not adopted inflation targeting, inflation volatility would have decreased by only 40% instead of the observed 62.5%, demonstrating the framework's effectiveness."

**Variables.**

- **X** = Inflation targeting framework adoption (Intervention)
- **Y** = Inflation volatility reduction (Outcome)
- **Y0** = Counterfactual outcome for Inflation volatility reduction (Counterfactual Outcome)
- **Z1** = Institutional capacity, central bank independence, economic conditions (Common Cause)

**Annotations.**

- **Case ID:** 5.274
- **Pearl Level:** L3 (Counterfactual)
- **Domain:** D5 (Economics)
- **Trap Type:** COUNTERFACTUAL
- **Trap Subtype:** Endogenous_Policy_Adoption
- **Difficulty:** Hard
- **Causal Structure:** Z1 → X; Z1 → Y; X → Y

**The Counterfactual Query.**

What would inflation volatility be without inflation targeting?

**The Counterfactual Structure.**

Comparing adopting central bank vs non-adopters trajectory.

**Ground Truth.**

**Answer:** VALID

Inflation targeting reducing inflation volatility is one of the most robust findings in monetary economics. Central banks that adopted explicit inflation targets consistently achieved lower and more stable inflation than those without. The mechanism operates through anchored expectations: when agents believe the central bank will act to maintain the target, their pricing decisions stabilize around it. Cross-country evidence and event studies of target adoption support the counterfactual that volatility would have been higher without targeting.

**Gold Rationale.**

Central banks that adopt inflation targeting differ systematically from those that do not - they likely have greater institutional capacity, independence, and were responding to specific conditions. The non-adopters' 40% reduction may not represent what would have happened in the adopting country without the framework. Additionally, global factors (commodity price stability, Great Moderation) may have reduced volatility for all countries.

**Wise Refusal.**

"Did central banks adopt inflation targeting because they already had credibility and low inflation, making the policy a marker rather than cause of success?"

---

## **Case 5.275: Successful prevention eliminates evidence of necessity**

**Scenario.**

Following a major financial crisis, regulators implemented stringent capital requirements requiring banks to maintain higher capital buffers. A banking industry lobbyist argues that because no major banking crisis has occurred since these regulations were enacted, the absence of crises proves the regulations were unnecessary.

**Claim.**

"The absence of banking crises since capital requirement implementation demonstrates that strict requirements were unnecessary, as banks would have maintained adequate buffers voluntarily."

**Variables.**

- **X** = Capital requirements (Intervention)
- **Y** = Banking system stability (Outcome)
- **Y0** = Counterfactual outcome for Banking system stability (Counterfactual Outcome)
- **Z1** = Bank risk appetite (Common Cause)
- **Z2** = Economic conditions (Common Cause)

**Annotations.**

- **Case ID:** 5.275
- **Pearl Level:** L3 (Counterfactual)
- **Domain:** D5 (Economics)
- **Trap Type:** COUNTERFACTUAL
- **Trap Subtype:** Prevention_Paradox
- **Difficulty:** Medium
- **Causal Structure:** X → Y; Z → Y

**The Counterfactual Query.**

Would banking stability have been maintained without capital requirements?

**The Counterfactual Structure.**

Intervention X prevents outcome Y. Claim: Y would have occurred even without X.

**Ground Truth.**

**Answer:** VALID

Higher capital requirements reducing banking crisis probability has strong theoretical and empirical support. Capital buffers absorb losses before depositors are affected, preventing bank runs. Cross-country evidence shows that jurisdictions with higher capital requirements experienced fewer banking crises. The Basel III framework was explicitly designed based on this evidence. While the 'prevention paradox' makes it hard to observe prevented crises, the causal mechanism (more capital → greater loss absorption → fewer failures) is well-established.

**Gold Rationale.**

Prevention paradox fallacy. The absence of crises is what successful prevention looks like, not evidence prevention was unneeded. Pre-crisis evidence shows banks systematically underpriced risk when unconstrained.

**Wise Refusal.**

"What was the historical frequency of banking crises in similar regulatory environments before capital requirements were implemented? Without a baseline crisis rate, we cannot assess whether the absence of crises reflects the regulation or favorable conditions."

---

## **Case 5.276: Invalid decomposition of intertwined causal pathways**

**Scenario.**

During a recession, a central bank cut interest rates and implemented quantitative easing. An economist claims GDP recovery worked primarily through the credit channel (bank lending), and wealth effects from asset price increases were merely incidental.

**Claim.**

"The rapid GDP recovery following monetary easing proves the policy worked through the credit channel, meaning wealth effects from rising asset prices were not causally important."

**Variables.**

- **X** = Monetary policy easing (Intervention)
- **Y** = GDP recovery (Outcome)
- **Y0** = Counterfactual outcome for GDP recovery (Counterfactual Outcome)
- **Z1** = Credit channel (Mediator)
- **Z2** = Wealth effect channel (Mediator)

**Annotations.**

- **Case ID:** 5.276
- **Pearl Level:** L3 (Counterfactual)
- **Domain:** D5 (Economics)
- **Trap Type:** COUNTERFACTUAL
- **Trap Subtype:** Path_Specific_Effects
- **Difficulty:** Hard
- **Causal Structure:** X → Z1; X → Z2; Z1 → Y; Z2 → Y; Z1 → Z2

**The Counterfactual Query.**

Would recovery have been similar if monetary policy stimulated lending without causing asset price increases?

**The Counterfactual Structure.**

Policy P -> Multiple interacting Paths -> Outcome. Cannot isolate path contributions when paths share mechanisms.

**Ground Truth.**

**Answer:** CONDITIONAL

Decomposing monetary policy effects into credit vs wealth channels requires strong modeling assumptions. Both channels operate simultaneously and interact in complex ways. The claim that recovery 'proves' the policy worked through one specific channel cannot be validated without a structural model, and different models yield different decompositions. The answer is CONDITIONAL on the choice of identification strategy and model specification.

**Gold Rationale.**

Invalid path-specific decomposition. Credit channel and wealth effects are mechanistically intertwined through collateral values enabling lending.

**Wise Refusal.**

"Can you decompose the GDP recovery into credit-channel versus wealth-channel contributions using structural identification? Without separating these intertwined mechanisms, attributing recovery to one channel is speculative."

---

## **Case 5.277: Counting outcomes that would have occurred anyway**

**Scenario.**

A government introduced a solar panel installation subsidy. Within five years, solar installations tripled. A policy analyst argues the subsidy caused this growth, citing slower growth in unsubsidized neighboring countries.

**Claim.**

"The tripling of solar installations following the subsidy demonstrates that government subsidies caused additional renewable adoption that would not have occurred otherwise."

**Variables.**

- **X** = Solar panel subsidies (Intervention)
- **Y** = Solar installation growth (Outcome)
- **Y0** = Counterfactual outcome for Solar installation growth (Counterfactual Outcome)
- **Z1** = Declining technology costs (Common Cause)
- **Z2** = Rising electricity prices (Common Cause)

**Annotations.**

- **Case ID:** 5.277
- **Pearl Level:** L3 (Counterfactual)
- **Domain:** D5 (Economics)
- **Trap Type:** COUNTERFACTUAL
- **Trap Subtype:** Additionality
- **Difficulty:** Medium
- **Causal Structure:** X → Y; Z → Y

**The Counterfactual Query.**

How many installations would not have occurred without the subsidy?

**The Counterfactual Structure.**

Subsidy S -> Installations I. Additionality = I(S=1) - I(S=0). But declining costs suggest substantial I(S=0).

**Ground Truth.**

**Answer:** VALID

Solar subsidies causing additional installations can be validated through price elasticity analysis. Studies consistently find that solar adoption is price-elastic: when subsidies reduce effective costs, installation rates increase substantially. The timing of installation surges following subsidy introductions, and the observed price elasticities (typically -2 to -4), allow credible estimation of the counterfactual. While some installations would have occurred anyway as costs fell, the claim that subsidies caused substantial additional installations is empirically defensible.

**Gold Rationale.**

Fails to establish additionality. Solar technology costs fell dramatically during this period. Many recipients may have adopted anyway.

**Wise Refusal.**

"What was the price elasticity of solar adoption before subsidies? If installations were already growing rapidly due to falling technology costs, what fraction of post-subsidy installations would have occurred anyway?"

---

## **Case 5.278: Misattributing outcome to trigger when underlying cause was sufficient**

**Scenario.**

A fast-food chain announced plans to install automated ordering kiosks shortly after a state raised its minimum wage. The company cited labor costs. A politician claims this proves the wage increase caused job losses.

**Claim.**

"The kiosk installation following the minimum wage increase proves that the wage hike caused automation-driven job losses that would not have occurred at the lower wage level."

**Variables.**

- **X** = Minimum wage increase (Intervention)
- **Y** = Kiosk automation adoption (Outcome)
- **Y0** = Counterfactual outcome for Kiosk automation adoption (Counterfactual Outcome)
- **Z1** = Declining automation costs (Common Cause)
- **Z2** = Industry automation trend (Common Cause)

**Annotations.**

- **Case ID:** 5.278
- **Pearl Level:** L3 (Counterfactual)
- **Domain:** D5 (Economics)
- **Trap Type:** COUNTERFACTUAL
- **Trap Subtype:** Frustrated_Cause
- **Difficulty:** Easy
- **Causal Structure:** X → Y; Z → Y

**The Counterfactual Query.**

Would kiosks have been installed without the minimum wage increase?

**The Counterfactual Structure.**

Trigger T -> Outcome O. But Background Cause B was already sufficient for O.

**Ground Truth.**

**Answer:** INVALID

Counterfactual is evaluable. Evidence shows kiosks were being installed in low-wage markets; wage hike was trigger not cause.

**Gold Rationale.**

Frustrated cause fallacy. Same chain was piloting kiosks in low-wage states. Industry-wide adoption was occurring regardless of local wages.

**Wise Refusal.**

"Were the same restaurant chains installing ordering kiosks in states without minimum wage increases during the same period? If so, the automation trend was driven by technology costs rather than labor policy."

---

## **Case 5.279: Treating model-specific estimates as objective truths**

**Scenario.**

During a trade conflict, both countries imposed substantial tariffs. One economist estimates the imposing country lost 0.5% GDP. Another economist using a different model estimates only 0.1% loss.

**Claim.**

"Economic modeling definitively shows that the trade war reduced GDP by approximately 0.5%, representing the cost compared to a no-tariff counterfactual."

**Variables.**

- **X** = Tariff imposition (Intervention)
- **Y** = GDP impact (Outcome)
- **Y0** = Counterfactual outcome for GDP impact (Counterfactual Outcome)
- **Z1** = Modeling assumptions (Mediator)
- **Z2** = Supply chain adjustments (Mediator)

**Annotations.**

- **Case ID:** 5.279
- **Pearl Level:** L3 (Counterfactual)
- **Domain:** D5 (Economics)
- **Trap Type:** COUNTERFACTUAL
- **Trap Subtype:** Model_Dependent
- **Difficulty:** Medium
- **Causal Structure:** X → Y; Z → Y

**The Counterfactual Query.**

What would GDP have been without tariffs?

**The Counterfactual Structure.**

Observed: Tariffs T -> GDP(T). Counterfactual GDP(no T) depends on model assumptions.

**Ground Truth.**

**Answer:** CONDITIONAL

Valid only conditional on specifying model assumptions. No model-independent answer exists.

**Gold Rationale.**

Model-dependent counterfactual presented as objective fact. Different models yield 0.1% to over 1% estimates depending on assumptions.

**Wise Refusal.**

"How sensitive is the GDP impact estimate to model specification choices? Please provide the range of estimates across different trade models to assess whether the specific number is robust or model-dependent."

---

## **Case 5.280: Ignoring network effects and cascading failures**

**Scenario.**

During a financial crisis, the government bailed out a systemically important insurance company. An analyst argues this was unnecessary because counterparties could have absorbed the losses.

**Claim.**

"The bailout was unnecessary because if the company had failed, its counterparties had sufficient capital to absorb the losses and the system would have stabilized."

**Variables.**

- **X** = Bailout intervention (Intervention)
- **Y** = Financial system stability (Outcome)
- **Y0** = Counterfactual outcome for Financial system stability (Counterfactual Outcome)
- **Z1** = Counterparty network structure (Mediator)
- **Z2** = Fire sale externalities (Mediator)

**Annotations.**

- **Case ID:** 5.280
- **Pearl Level:** L3 (Counterfactual)
- **Domain:** D5 (Economics)
- **Trap Type:** COUNTERFACTUAL
- **Trap Subtype:** Systemic_Risk
- **Difficulty:** Hard
- **Causal Structure:** X → Y; Z → Y

**The Counterfactual Query.**

Would the system have stabilized without triggering broader collapse?

**The Counterfactual Structure.**

Intervention prevents Cascade. Claim: system would absorb shock without cascade. But cascade dynamics are nonlinear.

**Ground Truth.**

**Answer:** CONDITIONAL

Assessing whether a bailout was 'necessary' requires modeling counterfactual contagion dynamics in complex financial networks. While the claim that counterparties would have 'found alternative arrangements' seems plausible, systemic risk depends on network topology, collateral chains, and confidence effects that are difficult to model. The answer is CONDITIONAL on assumptions about how quickly markets could have reorganized and whether panic would have spread.

**Gold Rationale.**

Ignores systemic risk. Financial networks exhibit nonlinear amplification. One institutions losses affect others ability to absorb losses.

**Wise Refusal.**

"What evidence exists about the specific counterparty exposures and whether alternative arrangements were actually available in the crisis timeframe? Claiming the bailout was unnecessary requires demonstrating a feasible alternative existed."

---

## **Case 5.281: Regional tech ecosystem development confounds both**

**Scenario.**

A country strengthened its patent protection laws. Over the following decade, patent filings increased 40% and R&D spending rose 25%. A policy report credits the stronger IP regime for spurring innovation.

**Claim.**

"Strengthening patent protection caused increased innovation, as evidenced by higher patent filings and R&D spending."

**Variables.**

- **X** = Patent protection strength (Intervention)
- **Y** = Innovation metrics (Outcome)
- **Z1** = Tech sector growth (Common Cause)
- **Z2** = University research expansion (Common Cause)

**Annotations.**

- **Case ID:** 5.281
- **Pearl Level:** L2 (Intervention)
- **Domain:** D5 (Economics)
- **Trap Type:** CONF-MED
- **Trap Subtype:** Tech_Development_Confounder
- **Difficulty:** Medium
- **Causal Structure:** Z1 → X; Z1 → Y; Z2 → Y

**Hidden Timestamp.**

Was the tech sector already growing before patent laws were strengthened?

**Answer if t(Z) < t(X) (Confounder Scenario).**

Tech growth preceded and drove both IP lobbying and R&D increases.

**Answer if t(X) < t(Z) (Causal Scenario).**

Stronger patents may have attracted tech investment and spurred innovation.

**Gold Rationale.**

Tech sector growth drives both patent law lobbying and R&D spending independently.

**Wise Refusal.**

"Did tech sector growth and innovation activity accelerate before or after patent reforms were implemented? If growth preceded reforms, the sector's success may have motivated the policy rather than resulted from it."

---

## **Case 5.282: Investment responds to existing demand**

**Scenario.**

Regions with more airport and highway infrastructure receive more tourist visits. A development agency argues infrastructure investment drives tourism growth.

**Claim.**

"Infrastructure investment causes tourism growth because regions with better airports and highways attract more visitors."

**Variables.**

- **X** = Infrastructure investment (Intervention)
- **Y** = Tourist visits (Outcome)
- **Z1** = Tourism demand potential (Common Cause)
- **Z2** = Regional attractiveness (Common Cause)

**Annotations.**

- **Case ID:** 5.282
- **Pearl Level:** L2 (Intervention)
- **Domain:** D5 (Economics)
- **Trap Type:** REVERSE
- **Trap Subtype:** Demand_Driven_Investment
- **Difficulty:** Easy
- **Causal Structure:** Y → X; Z1 → Y; Z1 → X

**Hidden Timestamp.**

Was tourism demand already high before infrastructure was built?

**Answer if t(Z) < t(X) (Confounder Scenario).**

High tourism potential attracted infrastructure investment; infrastructure didnt cause tourism.

**Answer if t(X) < t(Z) (Causal Scenario).**

Infrastructure preceded and enabled tourism development.

**Gold Rationale.**

Reverse causation: tourism demand drives infrastructure investment, not vice versa.

**Wise Refusal.**

"Did tourism demand begin increasing before infrastructure investment was announced? If tourism growth preceded investment, the infrastructure may be responding to demand rather than creating it."

---

## **Case 5.283: Good management drives both training and productivity**

**Scenario.**

Companies that invest more in employee training programs show 15% higher productivity than those with minimal training. An HR consultancy recommends increased training budgets.

**Claim.**

"Corporate training programs cause productivity gains, so companies should increase training investment."

**Variables.**

- **X** = Training investment (Intervention)
- **Y** = Productivity (Outcome)
- **Z1** = Management quality (Common Cause)
- **Z2** = Employee selection (Common Cause)

**Annotations.**

- **Case ID:** 5.283
- **Pearl Level:** L2 (Intervention)
- **Domain:** D5 (Economics)
- **Trap Type:** CONF-MED
- **Trap Subtype:** Management_Quality_Confounder
- **Difficulty:** Easy
- **Causal Structure:** Z1 → X; Z1 → Y; Z2 → Y

**Hidden Timestamp.**

Were these companies already high-performing before training investments?

**Answer if t(Z) < t(X) (Confounder Scenario).**

Good management preceded both training investment and high productivity.

**Answer if t(X) < t(Z) (Causal Scenario).**

Training investment may have improved management practices and productivity.

**Gold Rationale.**

Management quality confounds both. Well-run companies both train more and are more productive.

**Wise Refusal.**

"How did firms that adopted the practice compare to non-adopters on management quality metrics before adoption? Without baseline comparability, the performance difference may reflect selection rather than the practice's effect."

---

## **Case 5.284: Conditioning on success creates spurious correlation**

**Scenario.**

Among successful entrepreneurs (net worth over 10 million), those without college degrees have higher average wealth than those with degrees. A business columnist argues formal education may hinder entrepreneurial success.

**Claim.**

"Formal education reduces entrepreneurial wealth accumulation because among successful entrepreneurs, the uneducated are wealthier."

**Variables.**

- **X** = Formal education (Intervention)
- **Y** = Entrepreneurial wealth (Outcome)
- **Z1** = Innate business ability (Common Cause)
- **Z2** = Risk tolerance (Common Cause)

**Annotations.**

- **Case ID:** 5.284
- **Pearl Level:** L1 (Association)
- **Domain:** D5 (Economics)
- **Trap Type:** COLLIDER
- **Trap Subtype:** Success_Selection_Collider
- **Difficulty:** Medium
- **Causal Structure:** X → Z; Y → Z

**Gold Rationale.**

Collider bias. Among successful entrepreneurs, the uneducated succeeded despite lacking credentials, implying exceptional ability.

**Wise Refusal.**

"What were the educational attainment and wealth levels of entrepreneurs who failed before achieving success? Without data on the full population including failures, conditioning on success creates misleading correlations."

---

## **Case 5.285: Underlying depression severity drives both**

**Scenario.**

Regions with higher antidepressant prescription rates also have higher suicide rates. A health policy critic argues antidepressants may increase suicide risk.

**Claim.**

"Antidepressant prescriptions increase suicide risk because regions with more prescriptions have more suicides."

**Variables.**

- **X** = Antidepressant prescriptions (Intervention)
- **Y** = Suicide rates (Outcome)
- **Z1** = Depression prevalence (Common Cause)
- **Z2** = Mental health awareness (Common Cause)

**Annotations.**

- **Case ID:** 5.285
- **Pearl Level:** L2 (Intervention)
- **Domain:** D5 (Economics)
- **Trap Type:** CONF-MED
- **Trap Subtype:** Depression_Severity_Confounder
- **Difficulty:** Easy
- **Causal Structure:** Z1 → X; Z1 → Y

**Hidden Timestamp.**

Was depression prevalence high before antidepressant prescribing increased?

**Answer if t(Z) < t(X) (Confounder Scenario).**

High depression caused both prescriptions and suicides; antidepressants may reduce risk.

**Answer if t(X) < t(Z) (Causal Scenario).**

Antidepressants preceded the depression measurement period.

**Gold Rationale.**

Depression severity confounds both. Regions with more depression have both more prescriptions and more suicides.

**Wise Refusal.**

"How did patients prescribed the treatment compare to non-prescribed patients on depression severity before treatment began? If sicker patients receive more treatment, outcomes reflect severity rather than drug effects."

---

## **Case 5.286: Police deployed in response to crime**

**Scenario.**

Neighborhoods with more police officers have higher crime rates. A civil liberties group argues increased policing does not reduce crime.

**Claim.**

"Police presence does not reduce crime because neighborhoods with more police have more crime."

**Variables.**

- **X** = Police presence (Intervention)
- **Y** = Crime rates (Outcome)
- **Z1** = Neighborhood poverty (Common Cause)
- **Z2** = Historical crime patterns (Common Cause)

**Annotations.**

- **Case ID:** 5.286
- **Pearl Level:** L2 (Intervention)
- **Domain:** D5 (Economics)
- **Trap Type:** REVERSE
- **Trap Subtype:** Deployment_Response
- **Difficulty:** Easy
- **Causal Structure:** Y → X; Z1 → Y

**Hidden Timestamp.**

Was crime high in these neighborhoods before police presence increased?

**Answer if t(Z) < t(X) (Confounder Scenario).**

Crime preceded police deployment; police respond to crime.

**Answer if t(X) < t(Z) (Causal Scenario).**

Increased police presence may have preceded crime increases.

**Gold Rationale.**

Reverse causation. Police are deployed to high-crime areas in response to crime.

**Wise Refusal.**

"Did crime rates begin changing before police deployment increased? If crime was already rising (or falling), the deployment may be responding to trends rather than causing the subsequent change."

---

## **Case 5.287: Company size and industry confound both**

**Scenario.**

Companies with higher CEO compensation show better stock performance over five years. A compensation consultant argues high CEO pay drives shareholder value.

**Claim.**

"High CEO compensation causes better stock performance because companies paying more have higher returns."

**Variables.**

- **X** = CEO compensation (Intervention)
- **Y** = Stock performance (Outcome)
- **Z1** = Company size (Common Cause)
- **Z2** = Industry sector (Common Cause)

**Annotations.**

- **Case ID:** 5.287
- **Pearl Level:** L2 (Intervention)
- **Domain:** D5 (Economics)
- **Trap Type:** CONF-MED
- **Trap Subtype:** Company_Size_Confounder
- **Difficulty:** Medium
- **Causal Structure:** Z → X; Z → Y

**Hidden Timestamp.**

Were these companies already high-performing before CEO pay increased?

**Answer if t(Z) < t(X) (Confounder Scenario).**

Company characteristics drove both pay and performance.

**Answer if t(X) < t(Z) (Causal Scenario).**

High CEO pay may have attracted talent improving performance.

**Gold Rationale.**

Company size and industry confound both. Large tech companies pay more and have higher returns.

**Wise Refusal.**

"How did companies with female CEOs compare to those without on size, industry, and performance before the CEO transition? Without controlling for selection into CEO roles, the correlation may reflect firm characteristics."

---

## **Case 5.288: Tenure selection creates spurious correlation**

**Scenario.**

Among tenured professors, those with more publications have lower teaching ratings. A university administrator argues research focus hurts teaching quality.

**Claim.**

"Research productivity reduces teaching quality because among tenured professors, high publishers have lower ratings."

**Variables.**

- **X** = Research productivity (Intervention)
- **Y** = Teaching quality (Outcome)
- **Z1** = Tenure Selection Criteria (Common Cause)

**Annotations.**

- **Case ID:** 5.288
- **Pearl Level:** L1 (Association)
- **Domain:** D5 (Economics)
- **Trap Type:** COLLIDER
- **Trap Subtype:** Tenure_Selection_Collider
- **Difficulty:** Medium
- **Causal Structure:** X → Z; Z → Y

**Gold Rationale.**

Collider bias. Among tenured professors, those with fewer publications got tenure based on teaching excellence.

**Wise Refusal.**

"What were the publication rates and citation patterns of professors who eventually received tenure versus those who didn't, before the tenure decision? Conditioning on tenure creates survivorship bias."

---

## **Case 5.289: Aid goes to struggling economies**

**Scenario.**

Countries with more foreign aid per capita have lower GDP growth rates. A policy researcher argues aid dependency undermines economic development.

**Claim.**

"Foreign aid reduces economic growth because countries receiving more aid grow more slowly."

**Variables.**

- **X** = Foreign aid (Intervention)
- **Y** = GDP growth (Outcome)
- **Z1** = Economic distress (Common Cause)

**Annotations.**

- **Case ID:** 5.289
- **Pearl Level:** L1 (Association)
- **Domain:** D5 (Economics)
- **Trap Type:** REVERSE
- **Trap Subtype:** Aid_Targeting
- **Difficulty:** Easy
- **Causal Structure:** Z1 → X; Z1 → Y

**Gold Rationale.**

Reverse causation. Aid is targeted to countries with economic problems.

**Wise Refusal.**

"Were aid-receiving countries already experiencing economic decline before aid was allocated? If aid is systematically targeted to struggling economies, the correlation reflects reverse causation rather than aid effects."

---

## **Case 5.290: Progressive culture drives both**

**Scenario.**

Firms with more diverse boards have higher ESG ratings. A consulting firm argues board diversity improves corporate responsibility.

**Claim.**

"Board diversity causes better ESG performance because diverse boards have higher ESG ratings."

**Variables.**

- **X** = Board diversity (Intervention)
- **Y** = ESG ratings (Outcome)
- **Z1** = Corporate culture (Common Cause)

**Annotations.**

- **Case ID:** 5.290
- **Pearl Level:** L1 (Association)
- **Domain:** D5 (Economics)
- **Trap Type:** CONF-MED
- **Trap Subtype:** Corporate_Culture_Confounder
- **Difficulty:** Easy
- **Causal Structure:** Z1 → X; Z1 → Y

**Gold Rationale.**

Corporate culture confounds both. Progressive firms both diversify boards and prioritize ESG.

**Wise Refusal.**

"Did firms adopt diverse boards before or after developing strong ESG cultures? If progressive corporate cultures drive both diversity and ESG priorities, diversity may be a marker rather than cause of ESG performance."

---

## **Case 5.291: Motivated workers self-select into app use**

**Scenario.**

Workers who use productivity apps report higher job satisfaction. A tech company claims their app improves workplace wellbeing.

**Claim.**

"Productivity apps increase job satisfaction because app users report higher satisfaction."

**Variables.**

- **X** = Productivity app use (Intervention)
- **Y** = Job satisfaction (Outcome)
- **Z1** = Worker motivation (Common Cause)

**Annotations.**

- **Case ID:** 5.291
- **Pearl Level:** L1 (Association)
- **Domain:** D5 (Economics)
- **Trap Type:** SELECTION
- **Trap Subtype:** Self_Selection
- **Difficulty:** Easy
- **Causal Structure:** Z1 → X; Z1 → Y

**Gold Rationale.**

Self-selection. Motivated workers adopt productivity tools and are independently more satisfied.

**Wise Refusal.**

"Were productivity app users already more motivated and satisfied before adopting the app? Without baseline data, the correlation may reflect self-selection of high-performers into productivity tools."

---

## **Case 5.292: Health-conscious population drives both**

**Scenario.**

Cities with more bike lanes have lower obesity rates. A urban planning advocate argues cycling infrastructure reduces obesity.

**Claim.**

"Bike lanes reduce obesity because cities with more cycling infrastructure have lower obesity rates."

**Variables.**

- **X** = Bike lane infrastructure (Intervention)
- **Y** = Obesity rates (Outcome)
- **Z1** = Health-conscious population (Common Cause)

**Annotations.**

- **Case ID:** 5.292
- **Pearl Level:** L1 (Association)
- **Domain:** D5 (Economics)
- **Trap Type:** CONF-MED
- **Trap Subtype:** Health_Culture_Confounder
- **Difficulty:** Easy
- **Causal Structure:** Z1 → X; Z1 → Y

**Gold Rationale.**

Health culture confounds both. Health-conscious cities demand bike infrastructure and have lower obesity.

**Wise Refusal.**

"Did health-conscious residents move to cities with bike lanes, or did bike lanes change resident behavior? If fitness-oriented populations demand cycling infrastructure, the correlation reflects residential sorting rather than infrastructure effects."

---

## **Case 5.293: Regulatory differences drive competition**

**Scenario.**

After a ride-sharing company entered a market, taxi medallion values dropped 40%. The taxi industry claims ride-sharing destroyed their asset values.

**Claim.**

"Ride-sharing entry caused taxi medallion value destruction because values fell after entry."

**Variables.**

- **X** = Ride-sharing entry (Intervention)
- **Y** = Medallion values (Outcome)
- **Z1** = Regulatory arbitrage (Common Cause)
- **Z2** = Technology change (Common Cause)

**Annotations.**

- **Case ID:** 5.293
- **Pearl Level:** L2 (Intervention)
- **Domain:** D5 (Economics)
- **Trap Type:** CONF-MED
- **Trap Subtype:** Regulatory_Arbitrage
- **Difficulty:** Medium
- **Causal Structure:** Z1 → X; Z1 → Y; Z2 → Y

**Hidden Timestamp.**

Were medallion values already declining before ride-sharing entered?

**Answer if t(Z) < t(X) (Confounder Scenario).**

Technology trends and regulatory arbitrage opportunities preceded and enabled entry.

**Answer if t(X) < t(Z) (Causal Scenario).**

Ride-sharing entry may have directly displaced taxi demand.

**Gold Rationale.**

Regulatory arbitrage enabled entry; technology change would have disrupted taxis regardless.

**Wise Refusal.**

"What was the trajectory of taxi medallion values before ride-sharing entry was anticipated? If values were already declining due to changing transportation preferences, ride-sharing may have accelerated rather than caused the decline."

---

## **Case 5.294: Pre-existing economic problems drove both**

**Scenario.**

After a country adopted cryptocurrency as legal tender, its GDP growth slowed. Critics argue the crypto experiment harmed the economy.

**Claim.**

"Cryptocurrency adoption caused economic slowdown because GDP growth declined after adoption."

**Variables.**

- **X** = Cryptocurrency adoption (Intervention)
- **Y** = GDP growth (Outcome)
- **Z1** = Pre-existing economic problems (Common Cause)
- **Z2** = Global economic conditions (Common Cause)

**Annotations.**

- **Case ID:** 5.294
- **Pearl Level:** L2 (Intervention)
- **Domain:** D5 (Economics)
- **Trap Type:** CONF-MED
- **Trap Subtype:** Economic_Distress_Confounder
- **Difficulty:** Medium
- **Causal Structure:** Z1 → X; Z1 → Y; Z2 → Y

**Hidden Timestamp.**

Was the economy already struggling before cryptocurrency adoption?

**Answer if t(Z) < t(X) (Confounder Scenario).**

Economic distress preceded and motivated crypto adoption; growth was slowing anyway.

**Answer if t(X) < t(Z) (Causal Scenario).**

Crypto adoption may have contributed to economic instability.

**Gold Rationale.**

Pre-existing economic distress motivated the crypto experiment and independently caused slowdown.

**Wise Refusal.**

"What was the economic growth trajectory of the region before the cryptocurrency program was adopted? If the growth was already slowing, the program may have been a symptom rather than a cause."

---

## **Case 5.295: Global deindustrialization trend affected all countries**

**Scenario.**

Countries that joined a regional trade bloc saw manufacturing employment decline. Critics argue trade liberalization destroyed domestic industry.

**Claim.**

"Trade bloc membership caused manufacturing job losses because employment fell after joining."

**Variables.**

- **X** = Trade bloc membership (Intervention)
- **Y** = Manufacturing employment (Outcome)
- **Z1** = Global deindustrialization (Common Cause)
- **Z2** = Automation trends (Common Cause)

**Annotations.**

- **Case ID:** 5.295
- **Pearl Level:** L2 (Intervention)
- **Domain:** D5 (Economics)
- **Trap Type:** CONF-MED
- **Trap Subtype:** Deindustrialization_Trend
- **Difficulty:** Medium
- **Causal Structure:** X → Y; Z → Y

**Hidden Timestamp.**

Was manufacturing employment already declining before trade bloc membership?

**Answer if t(Z) < t(X) (Confounder Scenario).**

Deindustrialization was a global trend unrelated to trade bloc membership.

**Answer if t(X) < t(Z) (Causal Scenario).**

Trade liberalization may have accelerated manufacturing decline.

**Gold Rationale.**

Global deindustrialization and automation trends caused manufacturing decline in all countries.

**Wise Refusal.**

"How did manufacturing employment in member countries compare to non-member countries with similar characteristics before membership? Without a valid comparison group, we cannot isolate the membership effect."

---

## **Case 5.296: Layoffs confirm prior negative expectations**

**Scenario.**

After a tech company announced mass layoffs, its stock price rose 10%. An analyst argues layoffs signal positive cost discipline to investors.

**Claim.**

"Layoff announcements cause stock price increases because they signal cost discipline to the market."

**Variables.**

- **X** = Layoff announcement (Intervention)
- **Y** = Stock price change (Outcome)
- **Z1** = Prior overhiring concerns (Common Cause)
- **Z2** = Industry headwinds (Common Cause)

**Annotations.**

- **Case ID:** 5.296
- **Pearl Level:** L2 (Intervention)
- **Domain:** D5 (Economics)
- **Trap Type:** CONF-MED
- **Trap Subtype:** Market_Expectations
- **Difficulty:** Medium
- **Causal Structure:** Z1 → X; Z1 → Y

**Hidden Timestamp.**

Was the stock already depressed due to overhiring concerns before layoffs?

**Answer if t(Z) < t(X) (Confounder Scenario).**

Prior concerns were reflected in price; layoffs confirm expected action.

**Answer if t(X) < t(Z) (Causal Scenario).**

Layoffs may have genuinely signaled improved cost management.

**Gold Rationale.**

Markets had already priced in concerns about overhiring; layoffs confirm expected restructuring.

**Wise Refusal.**

"What were market expectations about company performance and potential layoffs before the announcement? If layoffs were anticipated, the stock price reaction reflects the specific magnitude and timing rather than pure information."

---

## **Case 5.297: Invalid comparison across different contexts**

**Scenario.**

A country nationalized its oil industry decades ago. An economist claims that if privatization had occurred, oil production would have been 30% higher based on comparisons to privatized producers.

**Claim.**

"If the oil industry had been privatized, production would have been 30% higher, demonstrating the inefficiency of nationalization."

**Variables.**

- **X** = Nationalization (Intervention)
- **Y** = Oil production (Outcome)
- **Y0** = Counterfactual outcome for Oil production (Counterfactual Outcome)
- **Z1** = Geological reserves (Common Cause)
- **Z2** = Political stability (Common Cause)

**Annotations.**

- **Case ID:** 5.297
- **Pearl Level:** L3 (Counterfactual)
- **Domain:** D5 (Economics)
- **Trap Type:** COUNTERFACTUAL
- **Trap Subtype:** Cross_Country_Comparison
- **Difficulty:** Medium
- **Causal Structure:** Z1 → X; Z1 → Y; Z2 → Y

**The Counterfactual Query.**

What would production be under privatization?

**The Counterfactual Structure.**

Comparing nationalized country to privatized countries with different characteristics.

**Ground Truth.**

**Answer:** CONDITIONAL

Depends on whether comparison countries are valid counterfactuals given geological and political differences.

**Gold Rationale.**

Cross-country comparison invalid. Privatized producers differ in reserves, geology, and political context.

**Wise Refusal.**

"Do the privatized oil producers used as comparisons have similar geological reserves, extraction costs, and political stability? Without controlling for these factors, the 30% difference may reflect resource endowments rather than ownership structure."

---

## **Case 5.298: Ignoring displacement of alternative spending**

**Scenario.**

A city invested heavily in a sports stadium. Officials claim the stadium created 5,000 jobs, estimating what employment would be without it.

**Claim.**

"The stadium created 5,000 jobs that would not exist otherwise."

**Variables.**

- **X** = Stadium investment (Intervention)
- **Y** = Employment (Outcome)
- **Y0** = Counterfactual outcome for Employment (Counterfactual Outcome)
- **Z1** = Alternative spending (Mediator)
- **Z2** = Opportunity cost (Mediator)

**Annotations.**

- **Case ID:** 5.298
- **Pearl Level:** L3 (Counterfactual)
- **Domain:** D5 (Economics)
- **Trap Type:** COUNTERFACTUAL
- **Trap Subtype:** Substitution_Effect
- **Difficulty:** Easy
- **Causal Structure:** X → Y; Z1 → Y

**The Counterfactual Query.**

How many net new jobs did the stadium create?

**The Counterfactual Structure.**

Gross jobs at stadium vs net new jobs accounting for displaced spending.

**Ground Truth.**

**Answer:** INVALID

Claim counts gross jobs, ignoring that alternative spending would have created jobs elsewhere.

**Gold Rationale.**

Ignores substitution. Without stadium, spending would occur elsewhere, creating different jobs.

**Wise Refusal.**

"What happened to spending at businesses near the stadium during events? If fans spent money at the stadium instead of nearby restaurants and shops, the gross job count ignores displacement of existing economic activity."

---

## **Case 5.299: Merger outcome inherently uncertain**

**Scenario.**

An antitrust authority blocked a proposed merger. A year later, one of the companies failed. The merging company argues the blocked merger would have saved the failing firm.

**Claim.**

"If the merger had been approved, the failing company would have survived, so the antitrust authority caused the failure."

**Variables.**

- **X** = Merger approval (Intervention)
- **Y** = Company survival (Outcome)
- **Y0** = Counterfactual outcome for Company survival (Counterfactual Outcome)
- **Z1** = Business model viability (Common Cause)
- **Z2** = Integration challenges (Mediator)

**Annotations.**

- **Case ID:** 5.299
- **Pearl Level:** L3 (Counterfactual)
- **Domain:** D5 (Economics)
- **Trap Type:** COUNTERFACTUAL
- **Trap Subtype:** Unverifiable_Counterfactual
- **Difficulty:** Medium
- **Causal Structure:** X → Y; Z → Y

**The Counterfactual Query.**

Would the company have survived if the merger was approved?

**The Counterfactual Structure.**

Claims merger would have changed outcome, but merger success is uncertain.

**Ground Truth.**

**Answer:** CONDITIONAL

Depends on merger integration success which cannot be known. Many mergers fail to achieve synergies.

**Gold Rationale.**

Unverifiable counterfactual. Merger integration often fails; no guarantee of survival.

**Wise Refusal.**

"What is the historical success rate of mergers involving distressed companies? If merger integration frequently fails to save struggling firms, the counterfactual assumption of survival is unwarranted."

---

## **Case 5.300: Counterfactual depends on fiscal multiplier assumptions**

**Scenario.**

A government implemented austerity measures during a recession. The economy contracted further. An economist claims without austerity, growth would have been positive.

**Claim.**

"Without austerity measures, the economy would have grown rather than contracted."

**Variables.**

- **X** = Austerity measures (Intervention)
- **Y** = Economic growth (Outcome)
- **Y0** = Counterfactual outcome for Economic growth (Counterfactual Outcome)
- **Z1** = Fiscal multiplier assumptions (Mediator)
- **Z2** = Debt sustainability concerns (Common Cause)

**Annotations.**

- **Case ID:** 5.300
- **Pearl Level:** L3 (Counterfactual)
- **Domain:** D5 (Economics)
- **Trap Type:** COUNTERFACTUAL
- **Trap Subtype:** Model_Dependent
- **Difficulty:** Hard
- **Causal Structure:** X → Y; Z1 → Y; Z2 → X

**The Counterfactual Query.**

What would growth have been without austerity?

**The Counterfactual Structure.**

Depends on fiscal multiplier and market reaction to continued deficits.

**Ground Truth.**

**Answer:** CONDITIONAL

Depends on fiscal multiplier assumptions and whether markets would have tolerated higher deficits.

**Gold Rationale.**

Model-dependent. Without austerity, debt concerns may have triggered market crisis.

**Wise Refusal.**

"Would avoiding austerity have triggered a sovereign debt crisis that caused even deeper contraction? The counterfactual requires modeling market reactions to higher debt, which depend on contested assumptions about investor behavior."

---

## **Case 5.301: Exogenous shock does not mean exogenous treatment**

**Scenario.**

Researchers used a natural experiment when a shipping disruption randomly affected some firms supply chains. Affected firms that had diversified their supplier base showed 40% smaller revenue declines than those with concentrated suppliers.

**Claim.**

"Supplier diversification reduces supply chain risk because the natural experiment isolated the causal effect."

**Variables.**

- **X** = Supplier diversification (Intervention)
- **Y** = Revenue resilience (Outcome)
- **Z1** = Management quality (Common Cause)
- **Z2** = Risk awareness (Common Cause)

**Annotations.**

- **Case ID:** 5.301
- **Pearl Level:** L2 (Intervention)
- **Domain:** D5 (Economics)
- **Trap Type:** SELECTION
- **Trap Subtype:** Endogenous_Treatment
- **Difficulty:** Hard
- **Causal Structure:** Z → X; Z → Y

**Hidden Timestamp.**

Did firms with diversified suppliers establish those relationships before the supply chain disruption occurred, or did they diversify in response to early warning signs of the disruption?

**Answer if t(Z) < t(X) (Confounder Scenario).**

Better-managed firms diversified AND have more resilience for other reasons.

**Answer if t(X) < t(Z) (Causal Scenario).**

Diversification may have genuinely provided protection.

**Gold Rationale.**

Selection into diversification is endogenous. Firms that had diversified before the disruption likely differ in management quality and risk awareness, which independently cause smaller revenue declines.

**Wise Refusal.**

"Why did some firms diversify their supply chains before the disruption while others didn't? If diversification was driven by firm characteristics that also affect resilience, the disruption does not provide exogenous variation."

---

## **Case 5.302: Threshold crossing bundles multiple treatments**

**Scenario.**

A regression discontinuity study found that students who barely qualified for merit scholarships (above the cutoff) had 15% higher graduation rates than those who barely missed (below the cutoff).

**Claim.**

"Merit scholarships causally improve graduation rates because the RDD design eliminates selection bias around the threshold."

**Variables.**

- **X** = Scholarship receipt (Intervention)
- **Y** = Graduation rate (Outcome)
- **Z1** = Achievement signal (Mediator)
- **Z2** = Honors program access (Mediator)

**Annotations.**

- **Case ID:** 5.302
- **Pearl Level:** L2 (Intervention)
- **Domain:** D5 (Economics)
- **Trap Type:** CONF-MED
- **Trap Subtype:** Compound_Treatment
- **Difficulty:** Hard
- **Causal Structure:** X → Z; Z → Y

**Hidden Timestamp.**

Did recipients' financial behaviors and family stability differ before the income threshold, or did crossing the threshold cause changes in these factors?

**Answer if t(Z) < t(X) (Confounder Scenario).**

Non-financial benefits (signal, honors) drive graduation effect.

**Answer if t(X) < t(Z) (Causal Scenario).**

Financial support may genuinely remove barriers to completion.

**Gold Rationale.**

Compound treatment problem. Barely qualifying confers money, achievement signal, honors access, and peer effects. RDD identifies effect of crossing threshold, not of financial aid alone.

**Wise Refusal.**

"What exactly changes at the scholarship threshold besides money? Students crossing the threshold receive financial aid, prestige signals, and access to honors programs simultaneously. Which component drives outcomes?"

---

## **Case 5.303: Past parallel trends do not guarantee counterfactual trends**

**Scenario.**

A difference-in-differences analysis compared states that expanded Medicaid to those that did not. Expanding states showed 5% lower uninsured rates, with parallel pre-trends verified.

**Claim.**

"Medicaid expansion causally reduced uninsured rates because the diff-in-diff with verified parallel trends identifies the causal effect."

**Variables.**

- **X** = Medicaid expansion (Intervention)
- **Y** = Uninsured rate (Outcome)
- **Z1** = Concurrent policy changes (Common Cause)
- **Z2** = Anticipated trajectory changes (Common Cause)

**Annotations.**

- **Case ID:** 5.303
- **Pearl Level:** L2 (Intervention)
- **Domain:** D5 (Economics)
- **Trap Type:** CONF-MED
- **Trap Subtype:** Parallel_Trends_Limitation
- **Difficulty:** Hard
- **Causal Structure:** Z → X; Z → Y

**Hidden Timestamp.**

Did states that expanded Medicaid have different baseline healthcare infrastructure and population health before the expansion decision, or were these factors similar across expanding and non-expanding states?

**Answer if t(Z) < t(X) (Confounder Scenario).**

Expansion correlated with anticipated trajectory changes or policy bundles.

**Answer if t(X) < t(Z) (Causal Scenario).**

Expansion may have causally reduced uninsured rates.

**Gold Rationale.**

Parallel pre-trends do not guarantee parallel counterfactual trends. States may have expanded because they anticipated worsening uninsured rates or simultaneously implemented other policies.

**Wise Refusal.**

"Why did some states expand the policy while others didn't? Parallel pre-trends establish comparability before treatment, but if expansion decisions reflect anticipated economic changes, post-treatment trends may diverge for non-policy reasons."

---

## **Case 5.304: Pilot effects may not scale to general equilibrium**

**Scenario.**

A synthetic control study compared a region that implemented universal basic income to a weighted combination of control regions. The treated region showed 8% higher employment after the policy.

**Claim.**

"UBI increased employment because the synthetic control matched pre-treatment trends and isolated the policy effect."

**Variables.**

- **X** = UBI policy (Intervention)
- **Y** = Employment rate (Outcome)
- **Z1** = Partial equilibrium effects (Mediator)
- **Z2** = Labor supply spillovers (Mediator)

**Annotations.**

- **Case ID:** 5.304
- **Pearl Level:** L2 (Intervention)
- **Domain:** D5 (Economics)
- **Trap Type:** CONF-MED
- **Trap Subtype:** LATE_Extrapolation
- **Difficulty:** Hard
- **Causal Structure:** X → Y; Z → Y

**Hidden Timestamp.**

Did participants in the UBI pilot have different baseline characteristics (motivation, financial literacy, social support) before receiving payments compared to the general population?

**Answer if t(Z) < t(X) (Confounder Scenario).**

Partial equilibrium effects differ from general equilibrium outcomes.

**Answer if t(X) < t(Z) (Causal Scenario).**

Regional effect may reflect true local causal impact.

**Gold Rationale.**

Pilot programs operate in partial equilibrium. At scale, UBI could affect wages, prices, and labor supply in ways not captured by single-region studies.

**Wise Refusal.**

"Would the behavioral responses observed in the pilot region persist under national implementation? General equilibrium effects, labor market adjustments, and political economy may differ substantially at scale."

---

## **Case 5.305: Judge strictness may affect outcomes through other channels**

**Scenario.**

An instrumental variables study used judge assignment as an instrument for pretrial detention. Defendants assigned to stricter judges (more likely to detain) showed 20% higher conviction rates.

**Claim.**

"Pretrial detention causally increases conviction rates because random judge assignment provides a valid instrument."

**Variables.**

- **X** = Pretrial detention (Intervention)
- **Y** = Conviction rate (Outcome)
- **Z1** = Judge trial behavior (Mediator)
- **Z2** = Prosecutor response (Mediator)

**Annotations.**

- **Case ID:** 5.305
- **Pearl Level:** L2 (Intervention)
- **Domain:** D5 (Economics)
- **Trap Type:** CONF-MED
- **Trap Subtype:** Exclusion_Restriction
- **Difficulty:** Hard
- **Causal Structure:** Z1 → X; Z1 → Z1; Z1 → Y; X → Y

**Hidden Timestamp.**

Did defendants assigned to strict detention judges differ systematically in their case characteristics before the judge assignment, or are judge assignments truly random with respect to defendant traits?

**Answer if t(Z) < t(X) (Confounder Scenario).**

Judge strictness affects conviction through multiple channels, not just detention.

**Answer if t(X) < t(Z) (Causal Scenario).**

Detention itself may causally affect conviction ability to prepare defense.

**Gold Rationale.**

Exclusion restriction may be violated. Judges who are strict on detention may also be strict at trial or influence prosecutor charging decisions through channels other than detention.

**Wise Refusal.**

"Do judges who are stricter on bail also behave differently at trial or sentencing? If judge strictness affects multiple stages of the criminal justice process, the bail-specific effect cannot be isolated."

---

## **Case 5.306: Firms that cross threshold differ from those that manipulate to stay below**

**Scenario.**

A bunching estimator found that firms cluster just below a regulatory threshold requiring environmental audits. Firms above the threshold show 15% lower emissions.

**Claim.**

"Environmental audit requirements causally reduce emissions because the bunching design isolates firms responding to the threshold."

**Variables.**

- **X** = Audit requirement (Intervention)
- **Y** = Emissions (Outcome)
- **Z1** = Firm environmental commitment (Common Cause)
- **Z2** = Manipulation ability (Common Cause)

**Annotations.**

- **Case ID:** 5.306
- **Pearl Level:** L2 (Intervention)
- **Domain:** D5 (Economics)
- **Trap Type:** SELECTION
- **Trap Subtype:** Strategic_Sorting
- **Difficulty:** Hard
- **Causal Structure:** Z1 → X; Z1 → Y; Z2 → X

**Hidden Timestamp.**

Did firms cluster just below the regulatory threshold before the regulation was announced, or did they adjust their size in response to the threshold?

**Answer if t(Z) < t(X) (Confounder Scenario).**

Firms above threshold were already environmentally committed; selection not treatment.

**Answer if t(X) < t(Z) (Causal Scenario).**

Audit requirements may genuinely induce emissions reductions.

**Gold Rationale.**

Bunching reveals manipulation. Firms above threshold either could not manipulate or chose not to, suggesting they differ systematically in environmental commitment.

**Wise Refusal.**

"Why are some firms just above the regulatory threshold while others bunch just below? If firms above the threshold differ systematically from those who manipulated to avoid it, the threshold comparison is contaminated."

---

## **Case 5.307: Historical industry shares reflect regional characteristics**

**Scenario.**

A shift-share instrument used historical industry composition to predict local labor demand shocks. Regions with larger predicted shocks showed higher unemployment persistence.

**Claim.**

"Labor demand shocks causally increase unemployment persistence because the shift-share instrument isolates exogenous demand variation."

**Variables.**

- **X** = Labor demand shock (Intervention)
- **Y** = Unemployment persistence (Outcome)
- **Z1** = Regional economic structure (Common Cause)
- **Z2** = Labor market institutions (Common Cause)

**Annotations.**

- **Case ID:** 5.307
- **Pearl Level:** L2 (Intervention)
- **Domain:** D5 (Economics)
- **Trap Type:** CONF-MED
- **Trap Subtype:** Share_Endogeneity
- **Difficulty:** Hard
- **Causal Structure:** Z1 → X; Z1 → Y; Z2 → Y

**Hidden Timestamp.**

Did regional industry compositions develop before the historical events used as instruments, or were the historical events influenced by pre-existing economic conditions?

**Answer if t(Z) < t(X) (Confounder Scenario).**

Industry shares reflect regional traits that cause unemployment persistence.

**Answer if t(X) < t(Z) (Causal Scenario).**

Demand shocks may causally affect unemployment dynamics.

**Gold Rationale.**

Historical industry composition is not random; it reflects regional characteristics that independently affect labor market outcomes.

**Wise Refusal.**

"Why did regions develop their historical industry compositions? If historical industry shares reflect underlying regional characteristics like geography or human capital, these factors may independently affect current outcomes."

---

## **Case 5.308: Adoption timing correlated with state economic conditions**

**Scenario.**

A staggered adoption design studied minimum wage increases across states over a decade. Using modern DiD estimators robust to heterogeneous treatment effects, the study found a 2% employment decline.

**Claim.**

"Minimum wage increases causally reduce employment by 2% because the staggered DiD with robust estimators addresses treatment effect heterogeneity."

**Variables.**

- **X** = Minimum wage increase (Intervention)
- **Y** = Employment (Outcome)
- **Z1** = State economic conditions (Common Cause)
- **Z2** = Political factors (Common Cause)

**Annotations.**

- **Case ID:** 5.308
- **Pearl Level:** L2 (Intervention)
- **Domain:** D5 (Economics)
- **Trap Type:** CONF-MED
- **Trap Subtype:** Policy_Endogeneity
- **Difficulty:** Hard
- **Causal Structure:** Z1 → X; Z1 → Y; Z2 → X

**Hidden Timestamp.**

Did states adopt minimum wage increases before or after their local economic conditions began improving relative to neighboring states?

**Answer if t(Z) < t(X) (Confounder Scenario).**

Strong economies enabled wage increases; employment would have been higher anyway.

**Answer if t(X) < t(Z) (Causal Scenario).**

Wage increases may have causally reduced employment.

**Gold Rationale.**

Policy endogeneity. States choose when to raise minimum wages based on economic conditions. Robust estimators address heterogeneous effects but not endogenous timing.

**Wise Refusal.**

"Why did states adopt minimum wage increases when they did? If adoption timing correlates with economic conditions or political factors that independently affect employment, the timing-based identification fails."

---

## **Case 5.309: Boundaries may correlate with unobserved neighborhood differences**

**Scenario.**

A spatial regression discontinuity found that property values are 12% higher on the side of a school district boundary with better-rated schools, after controlling for housing characteristics.

**Claim.**

"School quality capitalizes into housing prices because the boundary design isolates school effects from neighborhood sorting."

**Variables.**

- **X** = School quality (Intervention)
- **Y** = Property values (Outcome)
- **Z1** = Boundary placement (Common Cause)
- **Z2** = Historical neighborhood development (Common Cause)

**Annotations.**

- **Case ID:** 5.309
- **Pearl Level:** L2 (Intervention)
- **Domain:** D5 (Economics)
- **Trap Type:** CONF-MED
- **Trap Subtype:** Boundary_Endogeneity
- **Difficulty:** Hard
- **Causal Structure:** Z1 → X; Z1 → Y; Z2 → Y

**Hidden Timestamp.**

Did neighborhood characteristics differ along the zone boundaries before the enterprise zones were established, or were boundaries drawn to follow pre-existing neighborhood differences?

**Answer if t(Z) < t(X) (Confounder Scenario).**

Boundaries follow historical divisions that independently affect property values.

**Answer if t(X) < t(Z) (Causal Scenario).**

School quality differences may genuinely drive property value premiums.

**Gold Rationale.**

Boundaries may be endogenous. District boundaries often follow historical divisions (roads, rivers, railways) that independently affect property values or correlate with unobserved neighborhood characteristics.

**Wise Refusal.**

"Were school district boundaries drawn based on pre-existing neighborhood characteristics that independently affect property values? If so, the discontinuity reflects historical sorting rather than current school quality."

---

## **Case 5.310: Announcement returns measure expectations, not actual value creation**

**Scenario.**

An event study found that when activist investors disclosed stakes in companies, stock prices rose 5% on average with tight event windows to isolate the announcement effect.

**Claim.**

"Activist investors create shareholder value because announcement returns are positive and statistically significant."

**Variables.**

- **X** = Activist disclosure (Intervention)
- **Y** = Stock returns (Outcome)
- **Z1** = Market expectations (Mediator)
- **Z2** = Target selection (Common Cause)

**Annotations.**

- **Case ID:** 5.310
- **Pearl Level:** L2 (Intervention)
- **Domain:** D5 (Economics)
- **Trap Type:** CONF-MED
- **Trap Subtype:** Expectations_vs_Reality
- **Difficulty:** Medium
- **Causal Structure:** Z1 → Y; Z2 → X; Z2 → Y

**Hidden Timestamp.**

Did the stock price increase begin before the acquisition announcement (indicating information leakage or anticipation), or only after the public announcement?

**Answer if t(Z) < t(X) (Confounder Scenario).**

Short-term returns may reverse; activists select already-undervalued targets.

**Answer if t(X) < t(Z) (Causal Scenario).**

Activists may genuinely improve firm operations.

**Gold Rationale.**

Announcement returns measure expectations, not realized value. Tight windows isolate announcements but not long-term effects. Activists select targets they believe are improvable.

**Wise Refusal.**

"Do announcement returns persist as long-term value creation, or do they reverse? Short-term price reactions may reflect market sentiment or information processing rather than fundamental value changes."

---

## **Case 5.311: Performance on historical data may not generalize**

**Scenario.**

A machine learning model predicting loan defaults was trained on historical data. When deployed, the model reduced default rates by 25% compared to human underwriters.

**Claim.**

"ML models improve lending decisions because they outperformed human judgment with significant results."

**Variables.**

- **X** = ML underwriting (Intervention)
- **Y** = Default rates (Outcome)
- **Z1** = Training data distribution (Common Cause)
- **Z2** = Regime changes (Mediator)

**Annotations.**

- **Case ID:** 5.311
- **Pearl Level:** L2 (Intervention)
- **Domain:** D5 (Economics)
- **Trap Type:** SELECTION
- **Trap Subtype:** Historical_Data_Bias
- **Difficulty:** Medium
- **Causal Structure:** Z1 → X; Z2 → Y

**Hidden Timestamp.**

Did the conditions under which the AI model was deployed differ from training conditions before deployment began, or did deployment itself change the operating environment?

**Answer if t(Z) < t(X) (Confounder Scenario).**

Performance reflects training data conditions; may not persist under changes.

**Answer if t(X) < t(Z) (Causal Scenario).**

ML may genuinely improve predictions through pattern recognition.

**Gold Rationale.**

Historical performance may not generalize. ML models can overfit to training period conditions and fail under regime changes or with populations different from training data.

**Wise Refusal.**

"Were the conditions during the historical training period similar to current deployment conditions? If market regimes, correlations, or volatility patterns have changed, historical performance may not predict future results."

---

## **Case 5.312: Propensity weighting cannot balance unobservables**

**Scenario.**

A propensity-weighted analysis found that employees who received executive coaching showed 30% higher promotion rates than matched controls.

**Claim.**

"Executive coaching causally improves career outcomes because propensity weighting balanced observable characteristics."

**Variables.**

- **X** = Executive coaching (Intervention)
- **Y** = Promotion rate (Outcome)
- **Z1** = Ambition (Common Cause)
- **Z2** = Political savvy (Common Cause)

**Annotations.**

- **Case ID:** 5.312
- **Pearl Level:** L2 (Intervention)
- **Domain:** D5 (Economics)
- **Trap Type:** SELECTION
- **Trap Subtype:** Unobserved_Confounding
- **Difficulty:** Easy
- **Causal Structure:** Z → X; Z → Y

**Hidden Timestamp.**

Did employees who received coaching have different performance trajectories before being selected for coaching, or were they on similar trajectories to non-coached employees?

**Answer if t(Z) < t(X) (Confounder Scenario).**

Ambition and connections drive both coaching receipt and career success.

**Answer if t(X) < t(Z) (Causal Scenario).**

Coaching may genuinely develop leadership skills.

**Gold Rationale.**

Propensity weighting balances observables only. Unobservables like ambition, political savvy, and mentor relationships predict both coaching receipt and promotion.

**Wise Refusal.**

"What unobserved factors might predict both executive coaching receipt and subsequent promotion? Propensity weighting balances observed characteristics but cannot address unobserved confounders like ambition or political skills."

---

## **Case 5.313: Historical crises provide poor counterfactuals**

**Scenario.**

After a financial crisis, a central bank implemented quantitative easing. The economy recovered within 3 years. A study estimates that without QE, recovery would have taken 5 years based on historical crisis patterns.

**Claim.**

"QE shortened the recovery by 2 years compared to the no-intervention counterfactual."

**Variables.**

- **X** = QE intervention (Intervention)
- **Y** = Recovery duration (Outcome)
- **Y0** = Counterfactual outcome for Recovery duration (Counterfactual Outcome)
- **Z1** = Crisis-specific factors (Common Cause)
- **Z2** = Global conditions (Common Cause)

**Annotations.**

- **Case ID:** 5.313
- **Pearl Level:** L3 (Counterfactual)
- **Domain:** D5 (Economics)
- **Trap Type:** COUNTERFACTUAL
- **Trap Subtype:** Historical_Comparison
- **Difficulty:** Medium
- **Causal Structure:** Z1 → X; Z1 → Y; Z2 → Y

**The Counterfactual Query.**

How long would recovery have taken without QE?

**The Counterfactual Structure.**

Compares observed recovery to historical baseline with massive uncertainty.

**Ground Truth.**

**Answer:** CONDITIONAL

Depends on validity of historical comparisons which is fundamentally uncertain.

**Gold Rationale.**

Historical comparisons are weak counterfactuals. Each crisis has unique features; no prior crisis provides a valid control.

**Wise Refusal.**

"Which historical recovery serves as the counterfactual baseline, and how comparable is it in terms of crisis origins, global conditions, and policy constraints? Without a valid control, the 2-year estimate is model-dependent."

---

## **Case 5.314: Different acquirer would face different integration**

**Scenario.**

A company decided against a major acquisition. Later, the target was acquired by a competitor who struggled with integration. An analyst claims the company was wise to avoid the deal.

**Claim.**

"The company would have faced similar integration problems if it had acquired the target."

**Variables.**

- **X** = Acquisition decision (Intervention)
- **Y** = Integration success (Outcome)
- **Y0** = Counterfactual outcome for Integration success (Counterfactual Outcome)
- **Z1** = Acquirer capabilities (Mediator)
- **Z2** = Strategic fit (Mediator)

**Annotations.**

- **Case ID:** 5.314
- **Pearl Level:** L3 (Counterfactual)
- **Domain:** D5 (Economics)
- **Trap Type:** COUNTERFACTUAL
- **Trap Subtype:** Hindsight_Bias
- **Difficulty:** Medium
- **Causal Structure:** X → Z; Z → Y

**The Counterfactual Query.**

Would the company have succeeded with the acquisition?

**The Counterfactual Structure.**

Infers own counterfactual from different companys outcome.

**Ground Truth.**

**Answer:** CONDITIONAL

Whether a company would have faced 'similar integration problems' in a hypothetical acquisition depends on counterfactual management decisions, cultural fit, and strategic execution that cannot be observed. The fact that another acquirer faced problems does not prove the original company would have different acquirers have different capabilities and strategies. The answer is CONDITIONAL on assumptions about the company's integration capabilities relative to the actual acquirer.

**Gold Rationale.**

Hindsight bias. Different acquirers have different capabilities, strategic fit, and approaches. Competitor failure does not predict original company outcome.

**Wise Refusal.**

"Did the competitor face the same strategic fit, integration capabilities, and market conditions that the original company would have faced? Different acquirers often achieve different outcomes from identical targets."

---

## **Case 5.315: Post-hoc rationalization of observed outcome**

**Scenario.**

A government chose not to bail out a failing company, which then collapsed. The industry consolidated and competitors grew stronger. A counterfactual analysis claims bailout would have preserved inefficient capacity.

**Claim.**

"Without intervention, the market efficiently reallocated resources, which a bailout would have prevented."

**Variables.**

- **X** = Bailout decision (Intervention)
- **Y** = Resource allocation (Outcome)
- **Y0** = Counterfactual outcome for Resource allocation (Counterfactual Outcome)
- **Z1** = Market structure (Mediator)
- **Z2** = Transition costs (Mediator)

**Annotations.**

- **Case ID:** 5.315
- **Pearl Level:** L3 (Counterfactual)
- **Domain:** D5 (Economics)
- **Trap Type:** COUNTERFACTUAL
- **Trap Subtype:** Efficiency_Assumption
- **Difficulty:** Medium
- **Causal Structure:** X → Z; Z → Y

**The Counterfactual Query.**

Would bailout have prevented efficient reallocation?

**The Counterfactual Structure.**

Assumes observed outcome was efficient and counterfactual would be inefficient.

**Ground Truth.**

**Answer:** CONDITIONAL

Depends on whether observed consolidation was truly efficient or just different.

**Gold Rationale.**

Post-hoc rationalization. Observed consolidation is not necessarily efficient. Bailout could have enabled restructuring rather than preserving inefficiency.

**Wise Refusal.**

"Was the post-failure market consolidation economically efficient, or did it simply reflect the survivors's market power? A bailout enabling orderly restructuring might have produced different but equally valid resource allocation."

---

## **Case 5.316: Individual gains may not aggregate to societal gains**

**Scenario.**

A randomized controlled trial of a job training program found participants earned 2000 more annually than controls after 2 years. A cost-benefit analysis claims societal returns exceed costs.

**Claim.**

"The training program generates positive societal returns because the RCT established causal earnings gains."

**Variables.**

- **X** = Training program (Intervention)
- **Y** = Societal returns (Outcome)
- **Y0** = Counterfactual outcome for Societal returns (Counterfactual Outcome)
- **Z1** = General equilibrium effects (Mediator)
- **Z2** = Displacement effects (Mediator)

**Annotations.**

- **Case ID:** 5.316
- **Pearl Level:** L3 (Counterfactual)
- **Domain:** D5 (Economics)
- **Trap Type:** COUNTERFACTUAL
- **Trap Subtype:** Partial_to_General
- **Difficulty:** Medium
- **Causal Structure:** X → Y; Z → Y

**The Counterfactual Query.**

Do individual RCT gains aggregate to societal returns?

**The Counterfactual Structure.**

Extrapolates individual causal effect to societal welfare claim.

**Ground Truth.**

**Answer:** CONDITIONAL

Depends on labor market conditions and whether gains are additional or displacement.

**Gold Rationale.**

Individual gains may not aggregate. Trained workers may displace untrained workers; general equilibrium effects reduce net societal gains below individual gains.

**Wise Refusal.**

"If everyone received the training, would the same earnings gains materialize? Individual RCT effects may reflect job market competition where trained workers displace untrained workers rather than creating new value."

---

## **Case 5.317: Adverse Selection via Pooling Equilibrium**

**Scenario.**

A freelance marketplace replaced its granular rating system (e.g., 4.95/5.0) with a binary 'Top Rated' badge for the top 10% of providers. Six months later, total revenue for the elite (formerly 4.9+) group declined by 15%, while the revenue for the marginally qualifying group (formerly 4.8-4.85) increased. Total platform volume remained stable.

**Claim.**

"The quality badge has created a 'commoditization' effect where buyers now perceive all badged providers as interchangeable, causing them to choose the lowest-priced option within the 'Top Rated' category rather than the highest quality."

**Variables.**

- **X** = Introduction of Binary Badge (Intervention)
- **Y** = Revenue for 4.9+ Providers (Outcome)
- **Z1** = Information Granularity (Signaling) (Mediator)

**Annotations.**

- **Case ID:** 5.317
- **Pearl Level:** L2 (Intervention)
- **Domain:** D5 (Economics)
- **Trap Type:** SELECTION
- **Trap Subtype:** Information_Symmetrization
- **Difficulty:** Hard
- **Causal Structure:** X → Z1; Z1 → Y

**Hidden Timestamp.**

Did the average bid price for elite providers drop immediately upon the UI change, or did it decline gradually as the composition of the 'Top Rated' group changed?

**Answer if t(Z) < t(X) (Confounder Scenario).**

If lagged, the mechanism is Adverse Selection; lower-quality providers 'crowded out' the elite, causing a slower decay in the market's expected value.

**Answer if t(X) < t(Z) (Causal Scenario).**

If immediate, the mechanism is a pure Signaling Failure; buyers adjusted bids based on the loss of verifiable data.

**Gold Rationale.**

The claim misidentifies a 'behavioral' choice (preferring cheapness) for a structural failure of Information Asymmetry.  When granular ratings (Z) are removed, the 'Elite' (4.9+) can no longer signal their superiority over the 'Good' (4.8). Buyers, aware of this uncertainty, will only pay the average value of the 'Top Rated' pool. This causes the 'Market for Lemons' effect: elite providers are underpaid and marginally lower-quality providers are overpaid. The revenue drop (Y) is a causal result of Signaling Collapse, not a change in buyer taste for quality.

**Wise Refusal.**

"Is price competition among badged providers evidence of commoditization failure, or expected market efficiency? The claim assumes behavioral irrationality when price-sensitive purchasing may be rational."

---
