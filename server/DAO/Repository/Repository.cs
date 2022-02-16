using Microsoft.Azure.Cosmos;
using Microsoft.Azure.Cosmos.Linq;
using Model;
using Model.BoardRoom;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace DAO.Repository
{
    public class Repository : IRepository
    {
        private readonly Container _container;
        public Repository(string databaseId, string containerId, string connectionString)
        {
            _container = new CosmosClient(connectionString).GetContainer(databaseId, containerId);
        }

        public async Task<List<Protocol>> GetProtocols()
        {
            List<Protocol> protocols = new List<Protocol>();
            FeedIterator<Protocol> feedIterator = _container.GetItemLinqQueryable<Protocol>(false).Where(p => p.DocumentType == DocumentType.Protocol).ToFeedIterator();
            while (feedIterator.HasMoreResults)
            {
                foreach (Protocol protocol in await feedIterator.ReadNextAsync())
                    protocols.Add(protocol);
            }
            return protocols;
        }

        public async Task<Protocol> PostProtocols(Protocol protocol)
        {
            protocol.id = protocol.Name;
            return await _container.CreateItemAsync<Protocol>(protocol);
        }

        public async Task<List<Proposal>> GetProposals()
        {
            List<Proposal> proposals = new List<Proposal>();
            FeedIterator<Proposal> feedIterator = _container.GetItemLinqQueryable<Proposal>(false, requestOptions: new QueryRequestOptions { PartitionKey = new PartitionKey(DocumentType.Proposal.ToString()) }).ToFeedIterator();
            while (feedIterator.HasMoreResults)
            {
                foreach (Proposal proposal in await feedIterator.ReadNextAsync())
                    proposals.Add(proposal);
            }
            return proposals;
        }

        public async Task<Proposal> PostProposal(Proposal proposal)
        {
            proposal.id = Guid.NewGuid().ToString();
            return await _container.CreateItemAsync<Proposal>(proposal);
        }

        public async Task<List<Vote>> GetVotes()
        {
            List<Vote> votes = new List<Vote>();
            FeedIterator<Vote> feedIterator = _container.GetItemLinqQueryable<Vote>(false, requestOptions: new QueryRequestOptions { PartitionKey = new PartitionKey(DocumentType.Vote.ToString()) }).ToFeedIterator();
            while (feedIterator.HasMoreResults)
            {
                foreach (Vote vote in await feedIterator.ReadNextAsync())
                    votes.Add(vote);
            }
            return votes;
        }

        public async Task<Vote> PostVote(Vote vote)
        {
            vote.id = Guid.NewGuid().ToString();
            return await _container.CreateItemAsync<Vote>(vote);
        }
    }
}
