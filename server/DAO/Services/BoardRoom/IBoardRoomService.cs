using Model.BoardRoom;
using System.Collections.Generic;
using System.Threading.Tasks;

namespace DAO.Services.BoardRoom
{
    public interface IBoardRoomService
    {
        Task<List<Protocol>> GetProtocols();
        Task<List<Proposal>> GetProposals(string protocolName);
        Task<List<Vote>> GetVotesOnProposals(string refId);
    }
}