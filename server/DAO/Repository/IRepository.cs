using Model.BoardRoom;
using System.Collections.Generic;
using System.Threading.Tasks;

namespace DAO.Repository
{
    public interface IRepository
    {
        Task<List<Proposal>> GetProposals();
        Task<List<Protocol>> GetProtocols();
        Task<List<Vote>> GetVotes();
        Task<Proposal> PostProposal(Proposal proposal);
        Task<Protocol> PostProtocols(Protocol protocol);
        Task<Vote> PostVote(Vote vote);
    }
}