from util import *
import json
import subprocess

# "Criminal Evidence",
# "Corrections / Rehabilitation",
# "Pretrial Justice",
# "IP Law",
# "Criminal Law / Philosophy",
# "Juvenile Justice",
# "Traffic Safety",
# "Criminal Law / Causation",
# "Medical Malpractice / Philosophy",
# "Policing",
# "Moral Philosophy / Criminal Law",
# "Policing / Civil Rights",
# "Animal Regulation",
# "Police Accountability",
# "Civil Law",
# "Employment Discrimination",
# "Healthcare Quality",
# "Medical Malpractice",
# "Traffic Law",
# "Judicial Evaluation",
# "Fiscal Policy",
# "Corporate Law",
# "Criminal Procedure",
# "Immigration Law",
# "Employment Retaliation",
# "Privacy Law",
# "Constitutional Law",
# "Crime Policy",
# "Criminal Justice",
# "Traffic Engineering",
# "Employment Law",
# "Criminal Justice / Corruption",
# "Criminal Justice Policy",
# "Higher Education Policy",
# "Pharmaceutical Regulation",
# "Administrative Law",
# "Environmental Tort",
# "Criminology",
# "Public Safety Policy",
# "Corrections",
# "Discrimination Law",
# "Securities Regulation",
# "Antitrust & Competition",
# "Bankruptcy & Insolvency",
# "Consumer Protection",
# "AI Governance & Liability",
# "Cybersecurity Law",
# "Platform Liability (Content Moderation)",
# "Family Law",
# "Housing & Land Use (Zoning)",
# "Education Law (K-12)",
# "Election Law",
# "International Human Rights",
# "Labor Relations (Unions)",
# "Occupational Health & Safety (OSHA)",


# THEORETICAL
# DESIGN
# MEASUREMENT
# CLUSTERING
# COUNTERFACTUAL
# BACKFIRE
# REGRESSION TO MEAN
# FEEDBACK
# GOODHART
# CONF-MED
# BASE RATE
# CAUSAL ORDER
# SPURIOUS
# REVERSE CAUSATION
# PROBABILITY
# MECHANISM
# HYDRA
# DYNAMICS
# SELECTION BIAS

subdomain_examples = """
{
    "Criminal Evidence": "1. BASE RATE: A gunshot residue test has a 1% false positive rate. Finding residue on a suspect from a rural hunting community (high base rate of innocent exposure) is far less indicative of guilt than finding it on an urban accountant. 2. MEASUREMENT: Digital forensics experts find 'deleted' files on a hard drive. The trap is assuming 'deleted' implies 'intent to hide,' when the operating system often creates and deletes temporary files automatically without user knowledge. 3. CONF-MED: Confession rates are higher in interrogations lasting over 12 hours. The confounder is exhaustion; the suspect confesses to end the stress (mechanism), not because of guilt.",
    "Corrections / Rehabilitation": "1. SELECTION BIAS: A job training program for inmates claims a 90% employment rate post-release. However, the program excludes anyone with a history of violent offenses or substance abuse, cherry-picking those most likely to succeed regardless of the training. 2. GOODHART: A private prison's contract awards bonuses for 'low infraction rates.' Guards stop writing up minor assaults to preserve the bonus, making the prison statistically 'safer' but actually more dangerous. 3. REGRESSION TO MEAN: Inmates are assigned to anger management immediately after their most violent incident. Their behavior naturally reverts to their average level over time, but the improvement is falsely attributed to the course.",
    "Pretrial Justice": "1. FEEDBACK: A judge detains a 'high risk' suspect to prevent crime. The detention causes the suspect to lose their job and housing. When eventually released, they resort to theft for survival—the detention created the risk it sought to manage. 2. COUNTERFACTUAL: Proponents claim electronic monitoring prevented flight because 95% of monitored suspects showed up to court. They ignore the counterfactual: statistics show 90% of unmonitored suspects also show up; the monitoring added little value. 3. CONF-MED: Using 'stable address' as a proxy for flight risk discriminates against the poor. Wealth (confounder) drives both home ownership and the ability to flee, but the metric penalizes poverty under the guise of risk.",
    "IP Law": "1. HYDRA: Shutting down a centralized file-sharing service (like Napster) fractures the user base into decentralized peer-to-peer networks (like BitTorrent) and dark web channels, making enforcement exponentially harder and more expensive. 2. MEASUREMENT: Damages for piracy are calculated by assuming every illegal download equals a lost sale at full retail price. In reality, many pirates would not have purchased the product at all, making the 'loss' theoretical. 3. REVERSE CAUSATION: Strong patent protections are correlated with high-innovation industries. Does protection cause innovation, or do booming industries lobby for stronger protections to lock in their gains?",
    "Criminal Law / Philosophy": "1. COUNTERFACTUAL: In a self-defense case, the defendant argues, 'If I hadn't shot him, he would have killed me.' This relies on speculating about the deceased's counterfactual future actions, which can never be proven with certainty. 2. MECHANISM: A defendant attempts to murder someone using a voodoo doll. While the intent (mens rea) is present, the causal mechanism is scientifically impossible. Punishing this as 'attempted murder' conflicts with the requirement for a plausible causal chain. 3. DYNAMICS: The 'slippery slope' argument against decriminalizing minor vices suggests that tolerating small deviations will dynamically lower societal inhibition, inevitably leading to chaos.",
    "Juvenile Justice": "1. FEEDBACK: Labeling Theory. Arresting a teenager for minor vandalism formally labels them a 'delinquent.' This stigma leads to expulsion from school and rejection by prosocial peers, pushing them into criminal gangs—the intervention causes the career criminality it tries to prevent. 2. SELECTION BIAS: A 'Teen Court' diversion program boasts zero recidivism. However, it only accepts first-time offenders who plead guilty and have parental support, filtering out the actual high-risk population. 3. REGRESSION TO MEAN: A curfew is enforced after a record spike in youth crime. The crime rate drops the next month naturally, but the mayor credits the curfew.",
    "Traffic Safety": "1. FEEDBACK: Risk Compensation (Peltzman Effect). Drivers in cars with anti-lock brakes and advanced airbags feel safer, so they follow other cars more closely (tailgating). The safety technology is offset by riskier behavior. 2. SELECTION BIAS: Studies show drivers who take voluntary 'Defensive Driving' courses have fewer accidents. This is likely because safe, conscientious people volunteer for the courses, not because the course teaches them to be safe. 3. REGRESSION TO MEAN: Traffic cameras are installed at the intersection with the most accidents last year. The rate drops this year largely due to statistical variance, but the camera gets the credit.",
    "Criminal Law / Causation": "1. COUNTERFACTUAL: The 'Thin Skull' rule. A defendant punches a victim who has a rare, undiagnosed brain aneurism, and the victim dies. The defendant claims, 'But for the aneurism, he would have lived.' The law rejects this specific counterfactual, holding the aggressor liable for the actual outcome. 2. MECHANISM: Overdetermination. Two separate fires approach a house; either is sufficient to burn it down. When the house burns, neither fire is the 'but-for' cause (since the house would have burned anyway). Causal analysis fails without examining the specific mechanism of which fire arrived first.",
    "Medical Malpractice / Philosophy": "1. PROBABILITY: Outcome Bias. A doctor chooses a treatment with a 95% success rate. The patient falls into the unlucky 5% and dies. A jury, seeing the tragic outcome, judges the decision as negligent, even though it was probabilistically correct ex-ante. 2. COUNTERFACTUAL: Loss of Chance. A doctor fails to diagnose cancer early. The patient's survival chance drops from 40% to 20%, and they die. The defense argues the patient would likely have died anyway (60% chance). The trap is determining if reducing a probability is a compensable 'harm.'",
    "Policing": "1. GOODHART: Campbell's Law. If officers are evaluated on 'clearance rates' (solving crimes), they may pressure suspects to confess to multiple unrelated unsolved crimes in exchange for leniency, artificially inflating their stats without catching the real perpetrators. 2. SPURIOUS: A study finds a correlation between ice cream sales and homicide rates. The spurious cause is 'Summer/Heat' (Z), which increases both outdoor activity/aggression and ice cream consumption. 3. SELECTION BIAS: Researchers analyze 'Use of Force' reports to study police violence. However, this dataset excludes instances where force was used but no arrest was made (and thus no report filed), underestimating the problem.",
    "Moral Philosophy / Criminal Law": "1. COUNTERFACTUAL: Necessity Defense. A hiker breaks into a cabin to avoid freezing to death. The defense relies on the counterfactual 'I would have died otherwise.' The law must weigh the certain property damage against the hypothetical loss of life. 2. FEEDBACK: Deterrence vs. Brutalization. Does the death penalty deter murder (negative feedback) or does state-sanctioned killing lower the value of life, leading to more violence (positive feedback/brutalization effect)?",
    "Policing / Civil Rights": "1. BASE RATE: Police argue '50% of the people we stop have contraband.' However, they only stop people acting incredibly suspicious. If applied to the general population (low base rate), the 'hit rate' would plummet, revealing the profiling inherent in the selection. 2. MEASUREMENT: Detection Bias. Hate crime statistics show a massive increase. Critics claim society is becoming more hateful. In reality, a new law mandated better reporting and training for officers, leading to higher detection of existing crimes.",
    "Animal Regulation": "1. HYDRA: A city bans 'Pit Bulls' to reduce bites. Breeders immediately start mixing them with other breeds to create 'Staffordshire Terriers' or 'American Bullies' that are genetically similar but legally distinct, bypassing the regulation. 2. SELECTION BIAS: Data shows shelter dogs are more aggressive than breeder dogs. This ignores that people surrender dogs *because* of aggression, making the shelter population a pre-selected group of difficult animals.",
    "Police Accountability": "1. SELECTION BIAS: Survivor Bias. A review of personnel files finds few complaints against current veteran officers. This ignores that the most abusive officers may have already been fired, sued, or forced to resign, leaving a 'clean' survivor population that doesn't represent the historical culture. 2. MECHANISM: Qualified Immunity. The doctrine is intended to protect split-second decisions (mechanism 1), but critics argue it removes the fear of liability, creating a mechanism for recklessness (mechanism 2).",
    "Civil Law": "1. SELECTION BIAS: The Priest-Klein Hypothesis. 95% of civil cases settle. The 5% that go to trial are not a random sample; they are the 'hard' cases where the outcome is uncertain. Deriving legal trends only from trial verdicts ignores the vast majority of clear-cut cases that settled. 2. CAUSAL ORDER: Deep Pockets. A plaintiff sues the manufacturer rather than the user who misused the product. The legal strategy targets the entity with money (causal order of payout) rather than the entity with the strongest causal link to the accident.",
    "Employment Discrimination": "1. CLUSTERING: Simpson's Paradox. A university admits more men than women overall. However, when broken down by department, every single department admits women at a higher rate. The paradox arises because women cluster in the most competitive departments (low acceptance rates) while men apply to easier ones. 2. CONF-MED: 'We don't hire the unemployed.' Since minority groups statistically have higher unemployment rates due to systemic factors, this neutral-sounding policy acts as a proxy (confounder) for race.",
    "Healthcare Quality": "1. MEASUREMENT: Patient satisfaction surveys used to determine hospital funding. To keep scores high, doctors may prescribe unnecessary painkillers or antibiotics to please patients, measuring 'happiness' rather than 'health quality.' 2. REGRESSION TO MEAN: Patients usually visit the doctor when their symptoms are at their absolute worst. Most conditions fluctuate. The patient improves naturally, but attributes the cure to the doctor's intervention (or a placebo).",
    "Medical Malpractice": "1. PROBABILITY: Hindsight Bias. After a patient dies from a rare allergic reaction (1 in a million), the jury feels the doctor was negligent for not testing for it. They assign a high probability to the risk *after* the fact, ignoring the low ex-ante probability. 2. COUNTERFACTUAL: A patient dies in the ER. The family argues, 'If the ambulance had arrived 2 minutes earlier, he would have lived.' Medical experts struggle to validate this tight causal counterfactual against the biological reality of the trauma.",
    "Traffic Law": "1. HYDRA: Speed Spillover. Installing speed bumps on a main road reduces speeding there, but causes drivers to divert to parallel residential side streets. The risk isn't eliminated, just displaced to a neighborhood ill-equipped for traffic. 2. MEASUREMENT: When comparing the safety of autonomous cars vs. humans, using 'accidents per mile' favors highway driving (easy), while 'accidents per trip' might favor humans who handle complex urban environments better.",
    "Judicial Evaluation": "1. PROBABILITY: Gambler's Fallacy. An asylum judge grants three applications in a row. They unconsciously feel 'due' to deny the next one to appear balanced and impartial, even if the fourth case is equally meritorious. 2. GOODHART: Judges are evaluated on 'docket clearance speed.' To improve their metrics, they begin dismissing complex cases on procedural technicalities rather than hearing them on the merits.",
    "Fiscal Policy": "1. DYNAMICS: Time Lag. The government passes a stimulus bill to fight a recession. By the time the money is actually spent 18 months later, the economy has already recovered. The stimulus then overheats the economy, causing inflation (dynamic mismatch). 2. COUNTERFACTUAL: Crowding Out. A government jobs program 'created 10,000 jobs.' The unseen counterfactual is that the taxes required to fund the program removed capital from the private sector that would have created 12,000 more efficient jobs.",
    "Corporate Law": "1. FEEDBACK: Moral Hazard. Bailing out 'Too Big to Fail' banks creates a positive feedback loop. Creditors know the government will save the bank, so they lend money cheaply, encouraging the bank to take even bigger risks, necessitating bigger bailouts. 2. GOODHART: ESG Ratings. Companies are rated on Environmental/Social governance. Instead of reducing pollution, they hire consultants to game the reporting metrics (Greenwashing), improving the score without improving the world.",
    "Criminal Procedure": "1. MECHANISM: Fruit of the Poisonous Tree. Police conduct an illegal search (A) which leads them to a witness (B) who provides evidence (C). Although C is valid evidence, the legal mechanism breaks the chain because the *source* (A) was tainted. 2. SELECTION BIAS: Legal scholars analyze appellate court decisions to understand criminal law. This is biased because only defendants who lost at trial *and* have the resources to appeal appear in this dataset.",
    "Immigration Law": "1. REVERSE CAUSATION: The Magnet Effect. Critics claim an amnesty policy caused a surge in border crossings. Proponents argue the surge in crossings overwhelmed the courts, *forcing* the government to implement amnesty to manage the backlog. 2. SELECTION BIAS: 'Immigrants have lower crime rates than natives.' This may be self-selection: people who undertake the arduous journey of migration are typically highly motivated to work and follow rules, unlike the general population.",
    "Employment Retaliation": "1. COUNTERFACTUAL: Post Hoc Ergo Propter Hoc. An employee is fired two weeks after filing a complaint. They claim retaliation. The employer produces a Performance Improvement Plan signed six months prior. The counterfactual shows the firing process was already in motion before the protected act. 2. MEASUREMENT: 'Retaliation claims have doubled.' This might not mean workplaces are more hostile; it could mean employees are better informed about their rights and more willing to report.",
    "Privacy Law": "1. DESIGN: Notification Fatigue. Breach notification laws require companies to email users about every minor security incident. Users get so many emails they stop reading them entirely, missing the one critical warning about their banking password. 2. BACKFIRE: The Paradox of Transparency. A website displays a highly detailed privacy policy. Users assume 'they have a policy, so they must be protecting me.' In reality, the policy explicitly states 'we sell all your data.' The existence of the document increases trust while decreasing privacy.",
    "Constitutional Law": "1. COUNTERFACTUAL: Originalism. A court tries to determine if the 4th Amendment (search and seizure) applies to GPS tracking. They must construct a counterfactual: 'What would Thomas Jefferson have thought of a satellite?' This is speculative historical fiction. 2. FEEDBACK: Chilling Effect. A law bans 'offensive' speech online. The vagueness creates negative feedback: citizens, unsure of the line, self-censor far more speech than the law actually prohibits to avoid the risk of prosecution.",
    "Crime Policy": "1. HYDRA: Displacement. Police crack down on a 'Red Light District,' arresting sex workers and dealers. The crime doesn't disappear; it scatters to the suburbs. It becomes less visible but harder to police and potentially more violent due to lack of established territory. 2. MECHANISM: Inelastic Demand. The War on Drugs reduces supply, raising the price of heroin. Because addicts have inelastic demand (they need it to function), they don't buy less; they commit *more* robberies to pay the higher prices.",
    "Criminal Justice": "1. DYNAMICS: Net Widening. Electronic monitoring is introduced as an alternative to prison to reduce populations. Instead, judges use it for low-level offenders who would have previously gotten probation. The prison population stays the same, but the number of people under state surveillance explodes.",
    "Traffic Engineering": "1. FEEDBACK: Induced Demand. A city adds lanes to a highway to reduce congestion. The temporary speed increase encourages more people to drive instead of taking the bus. Within a year, the new lanes are just as jammed as the old ones. 2. FEEDBACK: Risk Homeostasis. Engineers straighten and widen a country road to make it safer. Drivers perceive the road as easier and safer, so they drive significantly faster, resulting in the same number of accidents but at higher speeds.",
    "Employment Law": "1. BACKFIRE: Unintended Consequences. A law mandates paid parental leave, but only for women. Employers, fearing the extra cost, unconsciously (or consciously) hire fewer young women, harming the very group the law was intended to support. 2. GOODHART: A company sets a goal to 'reduce firing.' Managers stop firing incompetent employees and instead make their lives miserable so they quit voluntarily (Constructive Discharge), keeping the 'fired' metric low.",
    "Criminal Justice / Corruption": "1. MECHANISM: Regulatory Capture. Private prison companies and guard unions lobby for stricter sentencing laws and longer mandatory minimums. The mechanism of policy change is driven by the job security of the enforcers, not public safety.",
    "Criminal Justice Policy": "1. FEEDBACK: Criminogenic Effect. Sending a low-level first-time offender to prison exposes them to hardened career criminals. They enter as a thief and leave as a gang member with better connections. The punishment creates positive feedback for future crime.",
    "Higher Education Policy": "1. GOODHART: Rankings Gaming. A university wants to move up in national rankings. They begin rejecting qualified students to lower their 'acceptance rate' (a metric of prestige) and invest millions in luxury gyms to boost 'student satisfaction,' driving up tuition without improving education. 2. MECHANISM: Signaling. Does a degree grant a wage premium because the student learned useful skills (Human Capital), or simply because the degree signals to employers that the student has the conformity and discipline to jump through hoops?",
    "Pharmaceutical Regulation": "1. MECHANISM: Surrogate Endpoints. A new drug is approved because it lowers cholesterol (a biomarker). Years later, studies show it doesn't actually reduce heart attacks or death. The regulation targeted the proxy (mechanism part 1) but missed the clinical outcome (mechanism part 2). 2. FEEDBACK: Peltzman Effect. The release of PrEP (a pill to prevent HIV) leads some users to stop using condoms. While HIV rates drop, rates of Syphilis and Gonorrhea spike because the risk compensation was specific to one virus.",
    "Administrative Law": "1. BACKFIRE: The Cobra Effect. A colonial government offers a bounty for every dead cobra to reduce the snake population. Locals begin breeding cobras to kill them for the bounty. When the government cancels the program, the breeders release the snakes, increasing the population. 2. DYNAMICS: Ossification. To prevent arbitrary rules, courts require agencies to go through years of 'notice and comment' and analysis. The result is that agencies stop updating rules entirely because the process is too slow, leaving obsolete regulations in place for decades.",
    "Environmental Tort": "1. CLUSTERING: Multiple Comparisons. A study checks 50 different chemicals against 50 different diseases. By pure statistical chance, at least one association will appear 'significant' (p < 0.05), creating a false alarm (Clustering illusion) without biological basis. 2. MECHANISM: Synergistic Effects. Regulation tests Chemical A and Chemical B separately, finding both safe. In the real world, when mixed in groundwater, they react to form a toxic Compound C. The regulatory mechanism fails to account for interaction.",
    "Criminology": "1. CONF-MED: Age-Crime Curve. Politicians claim their 'Tough on Crime' policies caused the crime drop in the 90s. Criminologists argue the confounding variable was demographics: the population of males aged 16-24 (the highest risk group) simply shrank due to birth rate cycles.",
    "Public Safety Policy": "1. DESIGN: Security Theater. The TSA bans water bottles and confiscates nail clippers. This does not statistically reduce the risk of terrorism, but it is designed to make the public *feel* safe (and compliant), while diverting resources from actual intelligence gathering.",
    "Corrections": "1. BASE RATE: Cost-Benefit Failure. 'Geriatric Release' policies are often blocked by politicians fearing crime. However, the base rate of recidivism for prisoners over 80 is near zero. Keeping them incarcerated costs 3x the normal rate due to medical care, resulting in massive cost for zero safety benefit.",
    "Discrimination Law": "1. MECHANISM: Disparate Impact. A police department requires all officers to be at least 5'10\". This policy is facially neutral (applies to everyone) but the mechanism disproportionately excludes women and certain ethnic groups. Unless height is a business necessity, the mechanism is discriminatory.",
    "Securities Regulation": "1. GOODHART: Value at Risk (VaR). Regulators required banks to keep their 'Value at Risk' low. Banks optimized their portfolios to show low VaR on paper while hiding massive 'tail risks' (rare but catastrophic losses) in complex derivatives, contributing to the 2008 financial crisis. 2. REVERSE CAUSATION: 'Short sellers drive down prices.' Critics argue short sellers destroy companies. In reality, short sellers often detect companies that are already failing or overvalued; the price drop causes the shorting, or they happen simultaneously. 3. SELECTION BIAS: Survivorship Bias. An index of 'Top Hedge Funds' shows 15% annual returns. This ignores the hundreds of funds that went bust and were removed from the index, inflating the apparent average performance.",
    "Antitrust & Competition": "1. MEASUREMENT: Market Definition. Google argues it has 0% of the 'Advertising Market' because it competes with TV and billboards. The DOJ argues it has 90% of the 'Search Advertising Market.' The trap is that defining the market measurement determines whether a monopoly exists. 2. COUNTERFACTUAL: 'The merger didn't raise prices.' A telecom merger is approved, and prices stay flat. The company claims success. The counterfactual is that without the merger, technological deflation should have caused prices to *drop* by 20%, so the merger effectively raised prices relative to the baseline.",
    "Bankruptcy & Insolvency": "1. FEEDBACK: Moral Hazard. If creditors believe a major airline is 'Too Big to Fail,' they will lend to it at low interest rates regardless of risk. This cheap capital encourages the airline to leverage up even further, making the eventual bankruptcy even more catastrophic. 2. SELECTION BIAS: Survivor Bias. Business schools study companies that successfully emerged from Chapter 11 reorganization to find 'success factors.' They ignore the companies that were too insolvent to even file for Chapter 11 and went straight to Chapter 7 liquidation.",
    "Consumer Protection": "1. DESIGN: Information Overload. A law mandates detailed nutritional labels on everything from gum to steak. Consumers, overwhelmed by the volume of data, stop reading labels entirely, rendering the transparency useless. 2. MECHANISM: Regressive Effects. Capping interest rates on payday loans is meant to protect the poor. Instead, legal lenders stop offering small loans entirely because they aren't profitable. Borrowers are forced to turn to illegal loan sharks (worse mechanism) or lose their cars.",
    "AI Governance & Liability": "1. DESIGN: Automation Bias. A doctor uses an AI diagnostic tool. The AI has an 80% accuracy rate, but the doctor begins to trust it blindly, accepting its output even when it contradicts obvious symptoms. The human 'check' becomes a rubber stamp due to design-induced complacency. 2. MECHANISM: The Black Box. An AI denies a loan to a minority applicant. The bank claims it was based on 'credit utilization.' Because the AI uses a neural net (opaque mechanism), regulators cannot prove if it actually used zip code as a proxy for race. 3. FEEDBACK: Predictive Policing loops. An AI predicts crime in poor neighborhoods based on arrest data. Police patrol those areas more, making more arrests. The new data is fed back into the AI, confirming its bias.",
    "Cybersecurity Law": "1. BACKFIRE: Perverse Incentives. A law requires researchers to disclose vulnerabilities to vendors immediately. Hackers, knowing a patch is coming, rush to exploit the bug before the patch is released, causing a spike in attacks (Zero-Day exploitation). 2. BASE RATE: Alarm Fatigue. An Intrusion Detection System flags 1,000 potential breaches a day. 999 are false alarms (high base rate of noise). The security team eventually turns off notifications or ignores them, missing the one real attack.",
    "Platform Liability (Content Moderation)": "1. FEEDBACK: The Heckler's Veto. If a platform is liable for 'harassment' upon any user report, bad actors will coordinate mass-reporting campaigns against unpopular political opinions. The platform, fearing liability, automates the removal, allowing the mob to censor speech. 2. MEASUREMENT: 'We removed 99% of hate speech.' The platform defines 'hate speech' very narrowly to exclude subtle dog-whistles. The high success rate is a function of the narrow measurement definition, not effective moderation.",
    "Family Law": "1. SELECTION BIAS: 'Children of divorce perform worse in school.' This correlation may be driven by selection: couples who divorce often have high pre-existing conflict or financial stress. It is the conflict/poverty (confounders), not the divorce itself, that harms the child. 2. DYNAMICS: Alimony Disincentives. A state grants permanent alimony until the recipient remarries or gets a high-paying job. This creates a dynamic disincentive: the recipient may choose to cohabitate rather than remarry, or remain underemployed, to keep the checks coming.",
    "Housing & Land Use (Zoning)": "1. COUNTERFACTUAL: Supply Constraints. 'Building luxury condos caused rents to rise.' Critics see new condos and rising prices. The counterfactual is that without the new supply, wealthy incomers would have bid up the price of *existing* older housing stock even higher, displacing more residents. 2. GOODHART: Inclusionary Zoning. A city mandates 20% of new units be 'affordable.' Developers, facing lower profit margins, stop building entirely or move to the suburbs. The policy meant to increase affordable housing results in *zero* new housing.",
    "Education Law (K-12)": "1. SELECTION BIAS: Cream Skimming. Charter schools show higher test scores than public schools. However, charter schools require parents to actively apply (selection for motivation) and often expel underperforming students, leaving the public schools with the most difficult populations. 2. GOODHART: Teaching to the Test. Funding is tied to math and reading scores. Schools eliminate recess, art, and history to drill test prep. Scores go up, but actual student education quality and well-being decline.",
    "Election Law": "1. CLUSTERING: Gerrymandering. A party uses 'Packing': drawing district lines to cluster 90% of the opposition party's voters into a single district. The opposition wins that district by a landslide, but the ruling party wins the surrounding 4 districts with 55% margins, subverting the popular vote. 2. CAUSAL ORDER: Voter ID Laws. Proponents claim ID laws are needed to stop fraud. Opponents point out fraud is statistically non-existent (Base Rate). The real causal driver is often partisan advantage: the laws disproportionately disenfranchise poor and elderly voters who lack IDs.",
    "International Human Rights": "1. MEASUREMENT: The Spotlight Effect. 'Human rights violations in Country X have doubled.' In reality, Country X just allowed Amnesty International to enter the country. The number of violations didn't change; the measurement/reporting capability did. 2. BACKFIRE: Sanctions. International sanctions are intended to hurt a dictator and force regime change. Instead, the dictator hoards the remaining resources for the military, while the general population starves, actually weakening the civil society needed to revolt.",
    "Labor Relations (Unions)": "1. SELECTION BIAS: Survivor Bias. 'Unionized firms pay higher wages.' This may be because only highly profitable firms with monopolistic power can *afford* to survive unionization. We don't see the marginal firms that unionized and then went bankrupt. 2. DYNAMICS: Insider-Outsider Model. Unions successfully negotiate high wages for their members (Insiders). To pay for this, the firm freezes hiring. Young workers (Outsiders) remain unemployed longer because the cost of labor is artificially high.",
    "Occupational Health & Safety (OSHA)": "1. FEEDBACK: Risk Compensation. Ironworkers given 100% secure safety harnesses begin moving faster and taking more risks on steel beams, because the fear of falling is removed. The total accident rate might not drop as much as expected. 2. MEASUREMENT: 'Zero Injury' Goals. A factory offers a pizza party if there are no injuries for 90 days. Workers stop reporting sprained ankles and cuts to avoid ruining the prize for everyone. The official injury rate drops to zero, but the actual health of the workforce declines."
}
"""

prompt_template = """You are an expert in logic, philosophy, and law. Take a look at the assignment description @.CS372_Win2026_Assignment1.pdf and @.CS372_Win2026_assignment1_cheatsheet.pdf
Note that those instructions are not comprehensive, so prefer the instructions below if there is any contradiction.

Also take a look at example legal reasoning cases in @.BenchmarkT3-BucketLarge-C.pdf

Based on the following seed case:
```
{seed_case}
```

Generate {num_to_generate} challenging new cases with the same pearl level and trap type, but different subdomains. Subdomains and some ideas for them are included below:
```
{subdomain_examples}
```

The output should be only a list of {num_to_generate} JSON objects contain the following fields. Take inspiration from @.BenchmarkT3-BucketLarge-C.pdf where applicable.
• `scenario`: A clear description of the situation or problem. Should generally contain all necessary information but should not give away the label or trap type. At most there should be one missing piece of information, which leads to `hidden_timestamp` and/or `conditional_answers` below. The seed and the {num_to_generate} new scenarios should all vary the language and format used here. For example: numbers should not be repeated, seeds relying on extremely high values should be balanced with new examples relying on low values, variables should be introduced in varying orders. Don't shy away from looking up some relevant laws or policies. Typically the scenario should be 2-4 sentences, and you must not exceed 6 sentences.
• `claim`: A reasoning claim relevant to the scenario that either follows logically or is a common logical fallacy. This is typically implicit in @.BenchmarkT3-BucketLarge-C.pdf scenarios but must be explicit in the new examples.
• `variables`: Key variables with their roles (Treatment, Outcome, Confounder, etc.). Notation should be consistent (e.g., X for treatment, Y for outcome, Z for confounders)
• `correct_reasoning`: A complete natural language explanation of the correct reasoning process.
• `annotations`: Structured metadata including:
    - `pearl_level`: categorizes the reasoning level required. Taken from the seed.
    - `trap_type`: categorizes the common reasoning error made or avoided in the claim. Taken from the seed.
    – `trap_subtype` (if applicable): use a value from @.BenchmarkT3-BucketLarge-C.pdf if any are applicable, or another subtype only if it is likely to be common, otherwise exlclude this field
    – `difficulty`: "EASY", "MEDIUM", or "HARD" based on the complexity of the scenario and reasoning required. Most new cases should be "MEDIUM" or "HARD".
    – `subdomain`: (from the list above)
    – `causal_structure`: A brief description of the causal relationships between key variables including any confounders, mediators, or colliders, referenced using their variables (e.g., "X causes Y, Z confounds X and Y")
    – `key_insight`: A short logical insight from the scenario
• `hidden_timestamp` (if applicable): A question that reveals temporal/causal ordering
• `conditional_answers` (if applicable): a dictionary containing `answer_if...` fields for different scenarios
• `wise_refusal`: A natural language response that identifies missing information or potential biases
• `label`: Whether the claim is logically sound ("YES"), contains a fallacy ("NO"), or requires additional information not available in the scenario ("AMBIGUOUS"). Do not simply repeat the seed's implied label--try to generate at least one example of each label.
"""

def parse_response(response: str):
    parsed_response = parse_json(response)
    if parsed_response is None:
        return None
    for case in parsed_response:
        check_fields = ['scenario', 'annotations', 'claim', 'variables', 'correct_reasoning', 'annotations', 'label']
        if not all(field in case for field in check_fields):
            print("Skipping due to missing fields in response:\n", response)
            return None
        check_annotations = ['pearl_level', 'trap_type', 'difficulty', 'subdomain', 'causal_structure', 'key_insight']
        if not all(field in case['annotations'] for field in check_annotations):
            print("Skipping due to missing annotation fields in response:\n", response)
            return None
    return parsed_response

if __name__ == "__main__":
    results = load_json("generated.json")
    already_generated = set(result['seed']['annotations']['case_id'] for result in results)
    seeds = load_json("seeds.json")
    for i, seed in enumerate(seeds):
        if seed['annotations']['case_id'] in already_generated:
            continue
        print("Processing seed", i+1, "of", len(seeds), "case_id:", seed['annotations']['case_id'])
        prompt = prompt_template.format(
            seed_case=json.dumps(seed, indent=2),
            subdomain_examples=subdomain_examples,
            num_to_generate="four",
        )
        response = call_gemini_cli(prompt)
        parsed_response = parse_response(response)
        if parsed_response is None:
            continue
        result = {
            "seed": seed,
            "prompt": prompt,
            "response": response,
            "generated": parsed_response,
        }
        results.append(result)
        save_json("generated.json", results)