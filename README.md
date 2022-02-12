# ethdenver-buidl (name to be updated :) )
## Logistics
- Sunday 02/20 @ 7am: project submission on [DoraHacks](https://hackerlink.io/hackathon/ethdenver22/) is due!
- Sunday 02/20 @ 9:30am-1pm: project presentation
- Sunday 02/20 @ 2pm: TBD!

## Overarching questions driving our work
Are (on-chain) DAOs working right now? Are they achieving their stated goals, and are members enjoying the experience?
- What governance systems are DAO members choosing to implement?
- In what ways are DAO members participating (in measureable ways)? Does DAO member activity relate to the chosen systems?
- How satisfied are DAO members with their own experiences in the DAO and with the health/success of the DAO overall? How do these experiences relate to the chosen systems?

## #BUIDLWeek deliverable
We will collect a new dataset of on- and off-chain data on DAO governance (contextualized with some existing datasets) to build a website displaying:
- For each DAO, 
  - Smart contract parameter values chosen
  - Quantitative activity information
  - Qualitative member experience information
  - Select relations between the above
- On aggregate,
  - Distribution of smart contract parameter values chosen across all DAOs, within frameworks
  - Distribution of quantitative activity metrics across select DAOs, within frameworks
  - Conclusions drawn from qualitative member experiences across select DAOs, within framework
  - Select relations between the above, within frameworks
  - Comparison across frameworks for select concepts
## Components
### Data source selection
### Blockchain data collection: **Lucia**
- [ ] Which contract blockchain addresses are we querying?
- [ ] What TrueBlocks commands + Python post-processing will get (1) smart contract content and (2) contract-creation transaction history?
- [ ] How can we automate the process so that the data can be readily updated at a later date?
### Contextual quantitative data collection: **Fabio**
- [ ] What kind of contextual information are we collecting, and from what sources (e.g., Snapshot proposal counts, from boardroom.info's API)? 
- [ ] Which specific DAOs are we getting contextual quantitative information for?
### Contextual qualitative data collection: **Sage**
- [ ] What kind of contextual information are we collecting, and how (e.g., survey, what kinds of questions)? 
- [ ] Which specific DAOs are we seeking contextual qualitative information for (e.g., member experiences via survey)?
- [ ] How are we reaching out to DAOs to get this?
### Blockchain data analysis: **Son + Lucia**
- [ ] What view of the data do we display for each DAO?
- [ ] What aggregate stats/conclusions can we find and display?
### Contextual quantitative data analysis: **Fabio + Son**
- [ ] What view of the data do we display for each DAO?
- [ ] What aggregate stats/conclusions can we find and display?
### Contextual qualitative data analysis: **Sage + Son**
- [ ] What view of the data do we display for each DAO?
- [ ] What aggregate stats/conclusions
### Aggregate data analysis: **Son + Lucia ( + all)**
- [ ] Can we identify any interesting relationships between the data sources within individual DAO? (to display for each DAO)
- [ ] Can we find any trends/relationships between the data sources across DAOs in aggregate? (to display in the aggregate data)
### Database setup: **Fabio**
- [ ] Store all the above data
### Front-end setup: **Fabio ( + all)**
- [ ] Display data neatly for each DAO
- [ ] Display aggregate analysis data
### Preparation for hackathon final presentation: **all**
- [ ] Write short bit describing our work for "about" page
- [ ] Draft elevator pitch

## References
- [ETHDenver #BUIDL guide](https://www.ethdenver.com/buidl)
- [ETHDenver judging info](https://www.ethdenver.com/judging)
- Existing DAO/DAO tooling aggregators:
  - [Coopatroopah blog post](https://coopahtroopa.mirror.xyz/_EDyn4cs9tDoOxNGZLfKL7JjLo5rGkkEfRa_a-6VEWw): Listing of big DAOs (by assets). Note that we should also find big DAOS by membership where we can, since these may not necessarily have large treasuris! (E.g., service DAOs, impact DAOs, social DAOs)
  - [DeepDAO](https://deepdao.io/): Ranking of DAOs by assets, some governance metrics
  - [DAOHQ](https://www.daohq.co/): Listing of off-chain locations of DAO communities
  - [Boardroom](https://www.boardroom.info/): Snapshot and other governance metrics
  - [DAOMasters](https://www.daomasters.xyz/): Listing of DAO tools/frameworks
