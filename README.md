# daochem
**DAOchem** is a solution in which on- and off-chain governance data sources react to produce a holistic view of DAO governance. We integrate data on **smart contract parameters**, **voting activity**, **Twitter activity**, and **contributor sentiment** to help DAO creators and contributors understand the governance landscape.

## Overarching questions driving our work
Are (on-chain) DAOs working right now? Are they achieving their stated goals, and how do members feel about their experience in the DAO?
- What governance systems are DAO members choosing to implement, with what "laws"?
- In what ways are DAO members participating (in measureable ways)? Does DAO member activity relate to the chosen systems?
- How satisfied are DAO members with their own experiences in the DAO and with the health/success of the DAO overall? How do these experiences relate to the chosen systems?

## Where are we getting the data?
### New datasets
#### Governance-related smart contract parameters
DAOs that have an on-chain component to their governance process often deploy their smart contracts through a platform like Arargon or DAOHaus. In these cases, the contract is created by the platform's factory contract. We are accessing the entire transaction history of these factory contracts using [TrueBlocks](https://trueblocks.io/) and an archive node (generously provided by [ArchiveNode.io](https://archivenode.io/), to pull out the parameters set at the time of deployment for each set of DAO governance smart contracts.
#### Twitter engagement with governance-related tweets
Twitter is a common way for a DAO to engage with its membership. We are using the Twitter API to acquire the follower counts and the contents and engagement of up to the 200 most recent tweets for DAOs with Twitter accounts. From these, we select those related to governance (based on keyword searchs) to guage how frequently the DAO communicates about its governance process and how engaged the DAO's followers are with these.
#### Contributor sentiment survey
Quantitative data on DAO governance is useful, but ignores an important component of a DAO's operations: its contributors. Similar to how GlassDoor provides some context about what it's like to actually work at a company, we are deploying a short survey to understand how DAO contributors feel about, for example, whether the governance process is legitimate, or whether their contribution is valued.
### Sourced datasets
#### DeepDAO
[DeepDAO](https://archivenode.io/) generously provided us with a mapping of DAOs to their governance-related addresses, which we are using for data linking.
#### Boardroom
Through the [Boardroom](https://www.boardroom.info/) API, we obtained the proposal creation and voting activity of DAOs that used an on-chain voting mechanism or Snapshot. We also used this to assign categories to DAOs.
#### DAOHQ
We referenced [DAOHQ](https://www.daohq.co/) to assign categories to DAOs.

## #BUIDLWeek deliverable
We are collecting new on- and off-chain data on DAO governance (contextualized with some existing datasets) to build a website displaying:
- For each DAO, 
  - Smart contract parameter values chosen
  - Quantitative governanceactivity information
  - Qualitative member experience information
- On aggregate,
  - Distribution of smart contract parameter values chosen across all DAOs, within frameworks
  - Distribution of quantitative activity metrics across select DAOs, within frameworks
  - Conclusions drawn from qualitative member experiences across select DAOs, within framework
  - Select relations between the above, within frameworks
  - Comparison across frameworks for select concepts
