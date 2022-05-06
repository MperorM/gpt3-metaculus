# Achieves worse results much worse results than the shorter prompt, is also significantly more expensive to run
gpt_prompt = '''A superintelligent AI is helping people make better predictions, and arrives at the following likelihoods for each event occuring.

Possible event:
The FAA has for several years been developing a set of regulations governing the use of unmanned aeriel systems (UASs, or "drones"), but has repeatedly missed deadlines to finalize those rules. Current regulations allow consumer use of "model aircraft" under certain conditions, and it was recently announced that one of those conditions would be registration of the drone.

Current FAA rules do not allow commercial operation of UASs except by special license. Comprehensive regulation specifying conditions under which commerical UASs can operate beyond line-of-sight of their operators (or autonomously) would open a host of industry uses of UAVs in aerial reconnaisance, delivery, etc.

Will such regulation be finalized by the FAA by June 15, 2016?

Likelihood of event occuring:
20%


Possible event:
In early December 2021, Russia has significantly increased the number of troops stationed on its border with Ukraine to nearly 100,000, according to the New York Times. In 2014 Russia invaded and annexed the Ukrainian-held Crimean peninsula, and skirmishes between Ukrainian forces and Russian-backed separatists have continued in the Donbas region of Ukraine ever since, for which Russia has denied involvement. In December 2021 US President Joe Biden warned Russian President Vladmir Putin that If Ukraine were invaded, the US would respond with economic sanctions.

Will Russia invade Ukrainian territory in 2022?

This question resolves positively if, between December 11, 2021 and January 1, 2023, representatives of the Government of the Russian Federation announce or acknowledge that Russia has invaded Ukraine, or if any two Permanent Members of the United Nations Security Council announce or acknowledge that the Russian Federation has invaded Ukraine. These announcements must be describing events which took place (at least in part) during the same period, from December 11, 2021 to January 1, 2023. Areas of Ukraine already occupied (officially or de facto) by Russia as of December 11, 2021, will not trigger resolution.

Likelihood of event occuring:
64%


Possible event:
The Joint Comprehensive Plan of Action (JCPOA) agreed between Iran and the P5+1 nations (China, France, Germany, Russia, United Kingdom and the United States) in 2015 limited the scope and scale of Iran's nuclear program.The USA unilaterally withdrew from the agreement in May 2018 and began reimposing economic sanctions against the country. Since then Iran has enriched uranium above limits agreed by the JCPOA, according to the latest assessment from IAEA. Negotiations resumed in Vienna in December 2021 between Iran and the P5+1 to agree on another deal.

Will the US rejoin the Iran Nuclear Deal before 2023?

This question resolves positively if the United States lifts or waives sanctions previously mandated by the JCPOA, before January 1, 2023, 00:00 UTC. The order must go into effect before 2023, a conditional announcement or promise does not suffice. The question will resolve regardless of whether Iran agrees to any terms or reduces its nuclear production capacity. the question will resolve on the basis of official statements by the US or Iranian governments, or credible media reports.

Likelihood of event occuring:
55%


Possible Event:
'''

short_gpt_prompt = '''A very knowledgable and epistemically modest analyst gives the following events a likelihood of occuring:

Event: Will the cost of sequencing a human genome fall below $500 by mid 2016? 
Likelihood: 43%

Event: Will Russia invade Ukrainian territory in 2022?
Likelihood: 64%

Event: Will the US rejoin the Iran Nuclear Deal before 2023?
Likelihood: 55%

Event: '''